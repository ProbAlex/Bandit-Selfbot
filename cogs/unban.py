import discord
from discord.ext import commands

class Unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member: discord.User):
        await ctx.guild.unban(member)
        await ctx.send(f"{member.mention} has been unbanned")

def setup(bot):
    bot.add_cog(Unban(bot))