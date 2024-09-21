import discord
from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await ctx.guild.ban(member, reason=reason)
        await ctx.send(f"{member.mention} has been banned for {reason}")

def setup(bot):
    bot.add_cog(Ban(bot))