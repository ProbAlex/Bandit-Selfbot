from discord.ext import commands
from urllib.parse import quote

class Youtube(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def youtube(self, ctx, *, query):
        safequery = quote(query)
        await ctx.send(f"https://www.youtube.com/results?search_query={safequery}")


def setup(bot):
    bot.add_cog(Youtube(bot))