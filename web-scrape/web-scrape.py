# libraries for parsing html into stuff
import bs4
import itertools
# from urllib.request import urllib
from urllib.request import urlopen as uReq
from urllib.request import Request
from bs4 import BeautifulSoup as soup

# we'll read the speed cheat sheet

# generate the request  using url and headers
speed_sheet_url = 'https://epic7x.com/speed-cheat-sheet/'
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = Request(speed_sheet_url, headers=hdr)
# call urllib to open the url

uClient = uReq(req)
page_html = uClient.read()
uClient.close() # be sure to close the connection when done

# parse the html using soup
page_soup = soup(page_html, "html.parser")

# find all divs that contain the thing in the second parameter
name_containers = page_soup.findAll("div", {"class": "pure-u-1-4 pure-u-md-1-8 text-center"}) # div containers that has the names
speed_containers = page_soup.findAll("h4", {"class": "mt-20"}) # span containers that has the speed set stats
name_parent_containers = page_soup.findAll("div", {"class": "pure-g"})
# speed_set_values = page_soup.findAll("span", {"class": "awakening-stat"}) # span containers that has the speed set stats
print("Name container length: ", len(name_containers))
print("Speed container length: ", len(speed_containers))
print("Pure g container length: ", len(name_parent_containers))

# speed_values = speed_containers[0].text.split()
# print("kayron base speed: ", speed_values[0].strip().replace(" ", ""))
# print("kayron with speed set: ", speed_values[1].strip("()").replace(" ", ""))

previous_speed = ""
speed_iterator = 0
# iterate through each container and retrieve values from their bodies
for name_iterator in range(len(name_containers)):
    # grab the name from its div
    name = name_containers[name_iterator].div.text

    # filter the speed values since they come in an array
    # print("DEBUG: ", speed_containers[speed_iterator].text.split())
    speed_values = speed_containers[speed_iterator].text.split()

    if previous_speed != speed_values:
        previous_speed = speed_values
        speed_iterator += 1
    base_speed = speed_values[0].strip().replace(" ", "")
    speed_set = speed_values[1].strip("()").replace(" ", "")

    print("Name: ", name)
    print("Base speed: ", base_speed)
    print("speed set: ", speed_set)

    # print("Name: {}, Base speed: {}, With speed set: {}".format(name, base_speed, speed_set))
    # print(name_containers[name_container].div.text)
