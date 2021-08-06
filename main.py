import os
import random
import json
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=".", intents=intents)
# create instance of client to connect to discord. Also apply the intents test
# client = discord.Client(intents = intents)

# read json speed data
speed_json_file = open('resources/speed_data.json', 'r')
speed_json_data = speed_json_file.read()

# parse json data
speed_data = json.loads(speed_json_data)

@bot.command(name="test")
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def speed(ctx, arg):
  print("received speed command")
  name = str(speed_data['Schuri'])
  base_speed = str(speed_data['speed'][0])
  set_bonus = str(speed_data['speed'][1])
  await ctx.send("i am speed. have some speed data bitch - Name: ", name, " Base speed: ", base_speed, " Set bonus: ", set_bonus)

# create client event decorator to register an event
@bot.event
# called when bot is ready
async def on_ready():
  print("Bot logged in as {0.user}".format(bot))

# main listening function for commands
@bot.event
async def on_message(message): # called when message is received. 
  # however we don't want it to work when the message is from the bot itself
  if message.author == bot.user:
    return
  if message.content.startswith('.hello'):
    await message.channel.send('Hey there')

# event when new user joins
@bot.event
async def on_member_join(member):
  # get the member's mention
  mention = member.mention
  greetings = [f"Welcome to our discord server {mention}! Please change your nickname to your e7 name so everyone knows who you are! Feel free to chat about anything", f"Do you hear the approaching ruin {mention}? Just kidding! Welcome to the server and please change your nickname to your e7 name so we know who you are!", f"Glad you made it {mention}!  Please change your nickname to your e7 name so we know who you are!", f"Hello and welcome to the discord {mention}! Please change your nickname to your e7 name so we know who you are!"]
  # generate random intenger from 0 to 4
  random_greeting = random.choice(greetings)
  # rand_greeting = random.randrange(0, 5)
  channel = discord.utils.get(member.guild.text_channels, name="hello")
  await channel.send(random_greeting)


# lastly, run the bot
token = os.environ['TOKEN']
bot.run(token)