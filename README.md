# e7-bot
A discord bot I made for my friend's server for a mobile game. The token is not uploaded here of course, but you can use your own token to create your own bot with these features

Features:
- automatic greeting that mentions new user upon joining server
- speed lookup
  - uses beautiful soup and urllib to grab html from website (url for reference: https://epic7x.com/speed-cheat-sheet/)
  - the data is the corresponding speed for each character in the game. the data is then parsed into a JSON file inside of the resources folder
  - in main.py, the bot reads the file and upon receiving the command the second argument will be the key in the dictionary - which the bot will use to retrieve the details for the specified character
  - example of use:
  - type in .speed schuri   
    - which the bot will return: Name: schuri | Base speed: 110 | With speed set bonus: 138
