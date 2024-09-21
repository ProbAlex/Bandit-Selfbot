from discord.ext import commands
import random

class DiceRoll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def diceroll(self, ctx, message=1):
        diceOut = 0
        for x in range(0, message):
            diceOut += random.randint(1,6)
        await ctx.send(f"You rolled a {diceOut}!")


def setup(bot):
    bot.add_cog(DiceRoll(bot))
