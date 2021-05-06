import os
import discord
from discord.ext import commands
import hypixel
import asyncio
from urllib.request import urlopen
import json
API_KEY = os.environ.get('HYPIXEL_API')
DISCORD = os.environ.get('DISCORD_KEY')
# this is fixed

class Misc(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

    # check's bot is online
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong {round(((bot.latency) * 1000), 0)} ms')
    #   bot's ping

    #donation info
    @commands.command(name="donate", aliases=["dono", "donation", "donations",'donates','support','fund','d'])
    async def donate(self,ctx):
        await ctx.send('donate via https://ko-fi.com/xcrunners to keep me running :)')

    #info info
    @commands.command(name="info", aliases=["information", "i", "about",'credits','more','inform'])
    async def info(self,ctx):
        embed = discord.Embed(title=f"Info",
                              color=discord.Color.purple())
        embed.set_author(name="XStats Bot", url="https://github.com/XCRunnerS",
                         icon_url=f"https://raw.githubusercontent.com/XCRunnerS/XCStatsBotPrototype/main/512xnewhypixel.png")  # pink

        embed.add_field(name="Developer:", value="@XCRunnerS#7188", inline=False)
        embed.add_field(name="Github:", value="code availible on github: https://github.com/XCRunnerS", inline=False)
        embed.add_field(name="Donation link:", value="donate via https://ko-fi.com/xcrunners to keep me running :)", inline=False)

        # embed.set_footer(text="This is the footer.") #I should put a thing here but I dont want to rn
        await ctx.send(embed=embed)  # sends embed



    @commands.command(name="helpplus", aliases=["hp", "hlp",'helps','help2','help+','help_plus','h'])
    async def helpplus(self,ctx):
        await ctx.send('for a list of commands type `!help`')
        await ctx.send('list of prefixes: `.`  `h!`')
        await ctx.send('help server: `not availible atm`') #I gotta do a thing dont I oof


def setup(bot):
    bot.add_cog(Misc(bot))