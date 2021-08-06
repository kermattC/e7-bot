# e7-bot
A discord bot I made for my friend's server for a mobile game

Features:
- automatic greeting that mentions new user upon joining server
- speed lookup
  - uses web scraping to grab data from a website. the data is the corresponding speed for each character in the game. the data is then parsed into a JSON file inside of the resources folder
  - url for reference: https://epic7x.com/speed-cheat-sheet/
  - in main.py, upon receiving the command the second argument will be the key in the dictionary - which the bot will use to retrieve the details for the specified character
  - example of use:
  -   .speed schuri   -> Name: schuri | Base speed: 110 | With speed set bonus: 138
