from discord.ext import commands
from urllib.parse import quote

class Lmgt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lmgt(self, ctx, *, query):
        safequery = quote(query)
        await ctx.send(f"https://www.letmegooglethat.com/?q={safequery.replace('%20', '+')}")


def setup(bot):
    bot.add_cog(Lmgt(bot))