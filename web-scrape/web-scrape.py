import bs4
import re
import json
from urllib.request import urlopen as uReq
from urllib.request import Request
from bs4 import BeautifulSoup as soup

# preliminary variables for saving the json file
path = './'
fileName = 'speed_data'
def writeToJSON(path, fileName, data):
    filePath = '../' + "resources" + '/' + fileName + '.json'
    with open(filePath, 'w') as fp:
        json.dump(data, fp)

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
speed_containers = page_soup.findAll("h4", {"class": "mt-20"}) # span containers that has the speed set stats
group_name_containers = page_soup.findAll("div", {"class": "pure-g"}) #divs that contain all names in a row
name_containers = page_soup.findAll("div", {"class": "f-12 mt-20 lh-15"})

character_data = {}
speed = {}

# for some reason there's a bunch of white space and newlines when reading the names, so I use regex to filter them
pattern = '\w'

# nested for loop that iterates through each row of speed, then iterates through each column name
# ie: each row of speed can contain more than one name, so this adheres to it
for speed_iterator in range(len(speed_containers)):
    speed_values = speed_containers[speed_iterator].text.split()    # get the speed from the div

    base_speed = speed_values[0].strip().replace(" ", "")   # base speed is index 0
    set_bonus = speed_values[1].strip("()").replace(" ", "") # set bonus speed is index 1, but contains brackets so I'l remove them 

    group_name = group_name_containers[speed_iterator+2].text

    # I split the lines to iterate through each line individually
    # then I check via regex which lines contain a character, so I use those as the names
    for line in group_name.splitlines():
        if re.match(pattern, line):
            name = line.lower()

            speed = {"base": base_speed, "set_bonus": set_bonus}
            character_data[name] = speed

# finally I'll write this to the designated file (and directory)
writeToJSON(path, fileName, character_data)
