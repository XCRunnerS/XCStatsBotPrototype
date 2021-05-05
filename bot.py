# this is the central bot file
import os
import discord
from discord.ext import commands
import hypixel
import asyncio
from urllib.request import urlopen
import json
bot = commands.Bot(command_prefix='.')
API_KEY = os.environ.get('HYPIXEL_API')
DISCORD = os.environ.get('DISCORD_KEY')

"""
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")


for extension in os.listdir("cogs"):
    if extension.endswith('.py'):
            bot.load_extension("cogs." + extension[:-3])
"""
"""
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

"""

for extension in os.listdir('./cogs'):
    if extension.endswith('.py'):
        bot.load_extension("cogs." + extension[:-3])


#prints bot message
@bot.event
async def on_ready():
    print('Bot Ready')

"""#check's bot is online
@bot.command()
async def ping(ctx):
    await ctx.send(f'pong {round(((bot.latency)*1000),0)} ms')
#   bot's ping"""

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('command does not exist, type `.help` for a list of commands!')


#testing context (not in use) also all these use client not bot
"""@client.command()
async def igncmd(ctx, ign):
    ign = ign
    await ctx.send(ign)"""

#Tests embed (not in use)
"""@client.command()
async def embedtests(ctx):
    embed = discord.Embed(title="[MVP+]XCRunnerS",
                          color=discord.Color.blue())
    embed.set_author(name="XCStatsBot", url="https://twitter.com/RealDrewData",
                     icon_url="https://crafatar.com/avatars/cffe420233a448289719f62ffcde53e4.png")
    embed.set_thumbnail(url="https://crafatar.com/avatars/cffe420233a448289719f62ffcde53e4.png")

    embed.add_field(name="Skywars Stats", value="Overall",
                    inline=False)
    embed.add_field(name="Wins", value="`1000`", inline=True)
    embed.add_field(name="Losses", value="`502`", inline=True)
    embed.add_field(name="Wins/Losses", value="`1.99`", inline=True)

    embed.add_field(name="Kills", value="`7082`", inline=True)
    embed.add_field(name="Deaths", value="`502`", inline=True)
    embed.add_field(name="Kills/Deaths", value="`14.14`", inline=True)

    embed.set_footer(text="This is the footer.")
    embed.set_image(url="https://crafatar.com/renders/body/cffe420233a448289719f62ffcde53e4.png")
    await ctx.send(embed=embed)"""

#VERSION 1 SW COMMAND (not in use)
"""@client.command()
async def stats(ctx, ign):
    uuidurl = json.loads(urlopen(f"https://api.mojang.com/users/profiles/minecraft/{ign}").read().decode("utf-8"))
    uuid = uuidurl["id"]


    jsonurl = f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}"
    jsondump = json.loads(urlopen(jsonurl).read().decode("utf-8"))


    embed = discord.Embed(title="Default Title",
                          color=discord.Color.blue())
    embed.set_author(name="XStats Bot", url="https://github.com/XCRunnerS",
                     icon_url=f"https://crafatar.com/avatars/{uuid}.png")
    embed.set_thumbnail(url=f"https://crafatar.com/avatars/{uuid}.png")

    embed.add_field(name="Skywars Stats", value="Overall",inline=False)
    embed.add_field(name="Wins", value=round((jsondump['player']['stats']['SkyWars']['wins']),2), inline=True)
    embed.add_field(name="Losses", value=round((jsondump['player']['stats']['SkyWars']['losses']),2), inline=True)
    embed.add_field(name="Wins/Losses", value=round(((jsondump['player']['stats']['SkyWars']['wins'])/(jsondump['player']['stats']['SkyWars']['losses'])),2), inline=True)

    embed.add_field(name="Kills", value=round((jsondump['player']['stats']['SkyWars']['kills']),2), inline=True)
    embed.add_field(name="Deaths", value=round((jsondump['player']['stats']['SkyWars']['deaths']),2), inline=True)
    embed.add_field(name="Kills/Deaths",value=round(((jsondump['player']['stats']['SkyWars']['kills'])/(jsondump['player']['stats']['SkyWars']['deaths'])),2), inline=True)

    embed.set_footer(text="This is the footer.")
    embed.set_image(url=f"https://crafatar.com/renders/body/{uuid}.png")
    await ctx.send(embed=embed)
# dont ask how long the line above took..."""

#VERSION 2 SW COMMAND (cleaner code to read, check ./cogs/skywars.py)
"""@bot.command(name="skywars", aliases=["skywar", "skw", "sw"])
async def skywars(ctx, ign):

    #I skipped ign listing, gotten from command
    #get UUID from official mojang api to bypass ignlimits
    uuidurl = json.loads(urlopen(f"https://api.mojang.com/users/profiles/minecraft/{ign}").read().decode("utf-8"))
    uuid = uuidurl["id"]
    #sets uuid

    jsonurl = f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}"
    jsondump = json.loads(urlopen(jsonurl).read().decode("utf-8"))

    #get the wins/losses here
    sw_wins =  (jsondump['player']['stats']['SkyWars']['wins'])
    sw_losses =  (jsondump['player']['stats']['SkyWars']['losses'])
    float(sw_wins) #makes it so I can make the nums clean with ,s
    float(sw_losses)
    round_sw_wl = format((sw_wins/sw_losses), ',.2f')
    #get the kills/deaths here
    sw_kills = (jsondump['player']['stats']['SkyWars']['kills'])
    sw_deaths = (jsondump['player']['stats']['SkyWars']['deaths'])
    float(sw_kills)
    float(sw_deaths)
    round_sw_kd = format((sw_kills/sw_deaths), ',.2f')

    #build embed
    embed = discord.Embed(title=f"IGN: {jsondump['player']['displayname']}",
                          color=discord.Color.blue())
    embed.set_author(name="XStats Bot", url="https://github.com/XCRunnerS",
                     icon_url=f"https://crafatar.com/avatars/{uuid}.png") #this is the same method as the mojang api but just the url
    embed.set_thumbnail(url=f"https://crafatar.com/avatars/{uuid}.png")

    embed.add_field(name="Skywars Stats", value="Overall",inline=False)
    embed.add_field(name="Wins", value=f"`{format(sw_wins, ',')}`", inline=True)
    embed.add_field(name="Losses", value=f"`{format(sw_losses, ',')}`", inline=True)
    embed.add_field(name="Wins/Losses", value=f"`{round_sw_wl}`", inline=True)

    embed.add_field(name="Kills", value=f"`{format(sw_kills, ',')}`", inline=True)
    embed.add_field(name="Deaths", value=f"`{format(sw_deaths, ',')}`", inline=True)
    embed.add_field(name="Kills/Deaths",value=f"`{round_sw_kd}`", inline=True)

   # embed.set_footer(text="This is the footer.") #I should put a thing here but I dont want to rn
    embed.set_image(url=f"https://crafatar.com/renders/body/{uuid}.png") #full body render instead of just head
    await ctx.send(embed=embed) #sends embed
"""

bot.run(f'{DISCORD}')
