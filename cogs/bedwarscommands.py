import os
import discord
from discord.ext import commands
import hypixel
import asyncio
from urllib.request import urlopen
import json
API_KEY = os.environ.get('HYPIXEL_API')
DISCORD = os.environ.get('DISCORD_KEY')
# this is ok for apis


class Bedwarscommands(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    # check's bot is online
    @commands.command(name="bedwars", aliases=["bedwar", "bws", "bw"])
    async def bedwars(self, ctx, ign):
        # I skipped ign listing, gotten from command
        # get UUID from official mojang api to bypass ignlimits
        uuidurl = json.loads(urlopen(f"https://api.mojang.com/users/profiles/minecraft/{ign}").read().decode("utf-8"))
        uuid = uuidurl["id"]
        # sets uuid

        jsonurl = f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}"
        jsondump = json.loads(urlopen(jsonurl).read().decode("utf-8"))

        # get the wins/losses here
        bw_wins = (jsondump['player']['stats']['Bedwars']['wins_bedwars'])
        bw_losses = (jsondump['player']['stats']['Bedwars']['losses_bedwars'])
        float(bw_wins)  # makes it so I can make the nums clean with ,s
        float(bw_losses)
        round_bw_wl = format((bw_wins / bw_losses), ',.2f')
        # get the kills/deaths here
        bw_kills = (jsondump['player']['stats']['Bedwars']['final_kills_bedwars'])
        bw_deaths = (jsondump['player']['stats']['Bedwars']['final_deaths_bedwars'])
        float(bw_kills)
        float(bw_deaths)
        round_bw_fkdr = format((bw_kills / bw_deaths), ',.2f')

        # build embed
        embed = discord.Embed(title=f"IGN: {jsondump['player']['displayname']}",
                              color=discord.Color.red())
        embed.set_author(name="XStats Bot", url="https://github.com/XCRunnerS",
                         icon_url=f"https://imgur.com/ZbDcW34.png")  # this is the same method as the mojang api but just the url
        embed.set_thumbnail(url=f"https://imgur.com/ZbDcW34.png") #game logo (for embedding)

        embed.add_field(name="Bedwars Stats", value="Overall", inline=False)
        embed.add_field(name="Wins", value=f"`{format(bw_wins, ',')}`", inline=True)
        embed.add_field(name="Losses", value=f"`{format(bw_losses, ',')}`", inline=True)
        embed.add_field(name="W/L", value=f"`{round_bw_wl}`", inline=True)

        embed.add_field(name="Final Kills", value=f"`{format(bw_kills, ',')}`", inline=True)
        embed.add_field(name="Final Deaths", value=f"`{format(bw_deaths, ',')}`", inline=True)
        embed.add_field(name="FKDR", value=f"`{round_bw_fkdr}`", inline=True)

        # embed.set_footer(text="This is the footer.") #I should put a thing here but I dont want to rn
        embed.set_image(url=f"https://crafatar.com/renders/body/{uuid}.png")  # full body render instead of just head
        await ctx.send(embed=embed)  # sends embed

    @bedwars.error
    async def bedwars_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('missing arguments! please follow this context:')
            await ctx.send('`!bedwars ign`')
        else:
            await ctx.send('something went wrong in the API (this could be an invalid player or they havent played this game!)')



def setup(bot):
    bot.add_cog(Bedwarscommands(bot))