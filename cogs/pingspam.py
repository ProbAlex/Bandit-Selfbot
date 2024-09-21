from discord.ext import commands
import asyncio


class PingSpam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(
        name="pingspam",
        aliases=["ps"],
        invoke_without_command=True
    )
    async def pingspam(self, ctx, *, message):
        while True:
            if self.bot.pingSwitch:
                await ctx.send(message)
                await asyncio.sleep(1)
            else:
                await ctx.send("Pingspam disabled, use `>pingspam t` to enable")
                break

    @pingspam.command(
        name="toggle",
        aliases=["t"]
    )
    async def toggle(self, ctx):
        self.bot.pingSwitch = not self.bot.pingSwitch
        await ctx.send(f"Pingspam enabled: {not self.bot.pingSwitch} -> {self.bot.pingSwitch}")


def setup(bot):
    bot.add_cog(PingSpam(bot))