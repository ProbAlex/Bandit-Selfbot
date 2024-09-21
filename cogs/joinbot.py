from discord.ext import commands
import asyncio


class JoinBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(
        name="joinbot",
        aliases=["jb"],
        invoke_without_command=True
    )
    async def joinbot(self, ctx, *, message):
        while True:
            if self.bot.pingSwitch:
                await ctx.send(message)
                await asyncio.sleep(120)
            else:
                await ctx.send("Joinbot disabled, use `>joinbot t` to enable")
                break

    @joinbot.command(
        name="toggle",
        aliases=["t"]
    )
    async def toggle(self, ctx):
        self.bot.pingSwitch = not self.bot.pingSwitch
        await ctx.send(f"Joiner enabled: {not self.bot.pingSwitch} -> {self.bot.pingSwitch}")


def setup(bot):
    bot.add_cog(JoinBot(bot))