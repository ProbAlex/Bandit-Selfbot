from discord.ext import commands
from urllib.parse import quote

class Google(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def google(self, ctx, *, query):
        safequery = quote(query)
        await ctx.send(f"https://www.google.com/search?q={safequery}")


def setup(bot):
    bot.add_cog(Google(bot))