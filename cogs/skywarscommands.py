import os
import discord
from discord.ext import commands
import hypixel
import asyncio
from urllib.request import urlopen
import json
API_KEY = os.environ.get('HYPIXEL_API')
DISCORD = os.environ.get('DISCORD_KEY')
# this is decent

class Skywarscommands(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="skywars", aliases=["skywar", "skw", "sw"])
    async def skywars(self, ctx, ign):
            # I skipped ign listing, gotten from command
            # get UUID from official mojang api to bypass ignlimits
            uuidurl = json.loads(urlopen(f"https://api.mojang.com/users/profiles/minecraft/{ign}").read().decode("utf-8"))
            uuid = uuidurl["id"]
            # sets uuid

            jsonurl = f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}"
            jsondump = json.loads(urlopen(jsonurl).read().decode("utf-8"))

            # get the wins/losses here
            sw_wins = (jsondump['player']['stats']['SkyWars']['wins'])
            sw_losses = (jsondump['player']['stats']['SkyWars']['losses'])
            float(sw_wins)  # makes it so I can make the nums clean with ,s
            float(sw_losses)
            round_sw_wl = format((sw_wins / sw_losses), ',.2f')
            # get the kills/deaths here
            sw_kills = (jsondump['player']['stats']['SkyWars']['kills'])
            sw_deaths = (jsondump['player']['stats']['SkyWars']['deaths'])
            float(sw_kills)
            float(sw_deaths)
            round_sw_kd = format((sw_kills / sw_deaths), ',.2f')

            # build embed
            embed = discord.Embed(title=f"IGN: {jsondump['player']['displayname']}",
                                  color=discord.Color.blue())
            embed.set_author(name="XStats Bot", url="https://github.com/XCRunnerS",
                             icon_url=f"https://imgur.com/BJS8r5H.png")  # this is the same method as the mojang api but just the url
            embed.set_thumbnail(url=f"https://imgur.com/BJS8r5H.png")

            embed.add_field(name="Skywars Stats", value="Overall", inline=False)
            embed.add_field(name="Wins", value=f"`{format(sw_wins, ',')}`", inline=True)
            embed.add_field(name="Losses", value=f"`{format(sw_losses, ',')}`", inline=True)
            embed.add_field(name="W/L", value=f"`{round_sw_wl}`", inline=True)

            embed.add_field(name="Kills", value=f"`{format(sw_kills, ',')}`", inline=True)
            embed.add_field(name="Deaths", value=f"`{format(sw_deaths, ',')}`", inline=True)
            embed.add_field(name="K/D", value=f"`{round_sw_kd}`", inline=True)

            # embed.set_footer(text="This is the footer.") #I should put a thing here but I dont want to rn
            embed.set_image(url=f"https://crafatar.com/renders/body/{uuid}.png")  # full body render instead of just head
            await ctx.send(embed=embed)  # sends embed
    @skywars.error
    async def skywar_serror(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('missing arguments! please follow this context:')
            await ctx.send('`!skywars ign`')


    @commands.command(name="rating", aliases=["rsw", "rs", "ranked","badgame"])
    async def rating(self, ctx, ign):
        await ctx.send('WIP')

def setup(bot):
    bot.add_cog(Skywarscommands(bot))
