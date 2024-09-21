import discord
from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await ctx.guild.kick(member)
        await ctx.send(f"{member.mention} has been kicked for {reason}")

def setup(bot):
    bot.add_cog(Kick(bot))