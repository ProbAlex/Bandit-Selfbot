import discord
from discord.ext import commands
import requests

class Blowjob(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def blowjob(self, ctx):
        hentaiPayload = requests.get("https://waifu.pics/api/nsfw/blowjob")
        hentaiJSON = hentaiPayload.json()
        justhentai = hentaiJSON["url"]
        await ctx.send(f"{self.bot.invisible}{justhentai}")

def setup(bot):
    bot.add_cog(Blowjob(bot))
    