import os
import random
import json
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='.', intents=intents)
# create instance of client to connect to discord. Also apply the intents test
# client = discord.Client(intents = intents)

# read json speed data
speed_json_file = open('resources/speed_data.json', 'r')
speed_json_data = speed_json_file.read()

# parse json data
speed_data = json.loads(speed_json_data)

# according to the documentation, overriding the on_message event will disable commands. Instead, use a listerner like this
@bot.listen('on_message')
async def message_listener(message):
# called when message is received. 
  # however we don't want it to work when the message is from the bot itself
  if message.author == bot.user:
    return
  if message.content.startswith('.hello'):
    await message.channel.send('Hey there')

@bot.event
# called when bot is ready/logged in
async def on_ready():
  print("Bot logged in as {0.user}".format(bot))

# use this to process commands to prevent them from not working
@bot.event
async def on_message(message): 
  await bot.process_commands(message)

# event when new user joins
@bot.event
async def on_member_join(member):
  # get the member's mention
  mention = member.mention
  greetings = [f"Welcome to our discord server {mention}! Please change your nickname to your e7 name so everyone knows who you are! Feel free to chat about anything", f"Do you hear the approaching ruin {mention}? Just kidding! Welcome to the server and please change your nickname to your e7 name so we know who you are!", f"Glad you made it {mention}!  Please change your nickname to your e7 name so we know who you are!"]
  # generate random intenger from 0 to 4
  random_greeting = random.choice(greetings)
  # rand_greeting = random.randrange(0, 5)
  channel = discord.utils.get(member.guild.text_channels, name="hello")
  await channel.send(random_greeting)


@bot.command(name="test")
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command(name="speed")
async def speed(ctx, *, arg):
  try:
    base_speed = speed_data[arg]["base"]
    set_bonus = speed_data[arg]["set_bonus"]
    await ctx.send("Name: {} | Base speed: {} | With speed set bonus: {}".format(arg, base_speed, set_bonus))
  except KeyError:
    await ctx.send("Sorry, couldn't find that unit's speed. Please make sure you type in the **full** name in **lowercase**.")
  
# lastly, run the bot
# token = os.environ['TOKEN']
# bot.run(token)
bot.run('NDgyMDM0MTMwODc2MzY2ODQ5.Dl_EIg.TKMT95vUe4q3fU9q74T_4Y4S408')