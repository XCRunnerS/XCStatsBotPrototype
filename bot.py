# this is the central bot file
import os
import discord
from discord.ext import commands
import hypixel
import asyncio
from urllib.request import urlopen
import json

bot = commands.Bot(command_prefix=['.','h!'])
API_KEY = os.environ.get('HYPIXEL_API')
DISCORD = os.environ.get('DISCORD_KEY')


for extension in os.listdir('./cogs'):
    if extension.endswith('.py'):
        bot.load_extension("cogs." + extension[:-3])
#all my commands are in ./cogs/filename.py :) [prefix]help will show you in discord

#prints bot message in console
@bot.event
async def on_ready():
    print('Bot Ready')

#non-existing commands
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('command does not exist, type `.help` for a list of commands!')

bot.run(f'{DISCORD}')
