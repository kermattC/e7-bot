import os
import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
# bot=commands.Bot(command_prefix='.',intents=intents)
# create instance of client to connect to discord. Also apply the intents test
client = discord.Client(intents = intents)

# create client event decorator to register an event
@client.event
# called when bot is ready
async def on_ready():
  print("Bot logged in as {0.user}".format(client))

# main listening function for commands
@client.event
async def on_message(message): # called when message is received. 
  # however we don't want it to work when the message is from the bot itself
  if message.author == client.user:
    return
  if message.content.startswith('.hello'):
    await message.channel.send('Hey there')

# event when new user joins
@client.event
async def on_member_join(member):
  # get the member's mention
  mention = member.mention
  greetings = [f"Welcome to our discord server {mention}! Please change your nickname to your e7 name so everyone knows who you are! Feel free to chat about anything", f"Do you hear the approaching ruin {mention}? Just kidding! Welcome to the server and please change your nickname to your e7 name so we know who you are!", f"Glad you made it {mention}!  Please change your nickname to your e7 name so we know who you are!", f"Hello and welcome to the discord {mention}! Please change your nickname to your e7 name so we know who you are!"]
  # generate random intenger from 0 to 4
  random_greeting = random.choice(greetings)
  # rand_greeting = random.randrange(0, 5)
  channel = discord.utils.get(member.guild.text_channels, name="hello")
  await channel.send(random_greetings)


  # no switch case here so we resort to if/else if
  # if rand_greeting == 0:
  #   await channel.send(f"Welcome to our discord server {mention}! Please change your nickname to your e7 name so everyone knows who you are! Feel free to chat about anything")
  # elif rand_greeting == 1:
  #   await channel.send(f"Do you hear the approaching ruin {mention}? Just kidding! Welcome to the server and please change your nickname to your e7 name so we know who you are!")
  # elif rand_greeting == 2:
  #   await channel.send(f"Glad you made it {mention}!  Please change your nickname to your e7 name so we know who you are!")
  # elif rand_greeting == 3:
  #   await channel.send(f"Hello and welcome to the discord {mention}! Please change your nickname to your e7 name so we know who you are!")

# lastly, run the bot
token = os.environ['TOKEN']
client.run(token)