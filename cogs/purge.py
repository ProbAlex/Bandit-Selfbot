import discord
from discord.ext import commands
import asyncio

class Purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        botMessage = await ctx.send(f"**{limit}** messages were successfully purged!")
        await asyncio.sleep(5)
        await botMessage.delete()

def setup(bot):
    bot.add_cog(Purge(bot))