import os
import discord
from discord.ext import commands
import hypixel
import asyncio
from urllib.request import urlopen
import json
from minecraftfunctionality import hypixelstats
from bot import API_KEY, DISCORD
# this is fixed

class Misc(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

    # check's bot is online
    @commands.command()
    async def ping(self, ctx):
    #   await ctx.send(f'pong {round(((bot.latency) * 1000), 0)} ms')
    #   bot's ping
        await ctx.send('pong') # will fix l8r

    #donation info
    @commands.command(name="donate", aliases=["dono", "donation", "donations",'donates','support','fund','d'])
    async def donate(self,ctx):
        await ctx.send('donate via https://ko-fi.com/xcrunners to help keep me running!')

    #info info
    @commands.command(name="info", aliases=["information", "i", "about",'credits','more','inform'])
    async def info(self,ctx):
        embed = discord.Embed(title=f"Info",
                              color=discord.Color.purple())
        embed.set_author(name="XStats Bot", url="https://github.com/XCRunnerS",
                         icon_url=f"https://raw.githubusercontent.com/XCRunnerS/XCStatsBotPrototype/main/512xnewhypixel.png")  # pink

        embed.add_field(name="Developer:", value="@XCRunnerS#7188", inline=False)
        embed.add_field(name="Github:", value="code availible on github: https://github.com/XCRunnerS", inline=False)
        embed.add_field(name="Donation link:", value="donate at https://ko-fi.com/xcrunners to keep me running", inline=False)
        embed.add_field(name="Mojang api:", value="https://api.mojang.com/",inline=False)
        embed.add_field(name="Hypixel api:", value="https://api.hypixel.net/", inline=False)
        embed.add_field(name="discord.py docs:", value="https://discordpy.readthedocs.io/en/latest/", inline=False)
        embed.add_field(name="discord.py code:",value="https://github.com/Rapptz/discord.py",inline=False)
        embed.add_field(name="python docs:", value="https://www.python.org/doc/", inline=False)
        # embed.set_footer(text="This is the footer.") #I should put a thing here but I dont want to rn
        await ctx.send(embed=embed)  # sends embed



    @commands.command(name="helpplus", aliases=["hp", "hlp",'helps','help2','help+','help_plus','h'])
    async def helpplus(self,ctx):
        await ctx.send('for a list of commands type `!help` (its way frickin easier than me making one manually or generating one) \nlist of prefixes: `.`  `h!`\nhelp server: `not availible atm`')
        #await ctx.send('list of prefixes: `.`  `h!`')
        #await ctx.send('help server: `not availible atm`') #I gotta do a thing dont I oof


def setup(bot):
    bot.add_cog(Misc(bot))