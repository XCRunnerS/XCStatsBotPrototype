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

    @commands.command(name="donate", aliases=["dono", "donation", "donations",'donates','support','fund','d'])
    async def donate(self,ctx):
        await ctx.send('donate via https://ko-fi.com/xcrunners to keep me running :)')

    @commands.command(name="info", aliases=["information", "i", "about",'credits','more','inform'])
    async def info(self,ctx):
        embed = discord.Embed(title=f"Info",
                              color=discord.Color.purple())
        embed.set_author(name="XStats Bot", url="https://github.com/XCRunnerS",
                         icon_url=f"https://imgur.com/OXhzVTf.png")  # pink
        #embed.set_thumbnail(url=f"https://imgur.com/BJS8r5H.png")

        embed.add_field(name="Developer:", value="@XCRunnerS#7188", inline=False)
        embed.add_field(name="Github:", value="code availible on github: https://github.com/XCRunnerS", inline=False)
        embed.add_field(name="Donation link:", value="donate via https://ko-fi.com/xcrunners to keep me running :)", inline=False)

        # embed.set_footer(text="This is the footer.") #I should put a thing here but I dont want to rn
        # embed.set_image(url=f"https://crafatar.com/renders/body/{uuid}.png")  # full body render instead of just head
        await ctx.send(embed=embed)  # sends embed



def setup(bot):
    bot.add_cog(Misc(bot))