from discord.ext import commands
from urllib.parse import quote

class Github(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def github(self, ctx, *, query):
        safequery = quote(query)
        await ctx.send(f"https://github.com/search?q={safequery}&type=repositories")


def setup(bot):
    bot.add_cog(Github(bot))