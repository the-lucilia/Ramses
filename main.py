"""
Ramses II is the code name for SCARAB 2.0

SCARAB - Systematic Coordination of Automated Regional Assault Bot

SCARAB is a discord bot to trigger tag runs on its own, built for the Sekhmet Legion.
"""

import discord
import os
from discord.ext import commands


intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)


# This runs when bot is ready, we have it load all of our cogs
@bot.event
async def on_ready():
    # print("Ready to go!")
    await bot.change_presence(activity=discord.Game(name="in the sand"))

    # When we are ready we want to load all cogs from the cogs directory
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'Loaded {filename[:-3]}')
            except Exception as e:
                print(f'Failed to load {filename[:-3]}\tError {e}')
    print("Ready to rock'n'roll!")


# This is reading out our token from token.txt and running the bot with it
token = open('token.txt', 'r')
token = str(token.read())
bot.run(token)
