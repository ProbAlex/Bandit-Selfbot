import random
from discord.ext import commands

class CoinFlip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def coinflip(self, ctx):
        if random.randint(1,2) == 1:
            await ctx.send(f" # You got head! {self.bot.invisible} https://images-ext-1.discordapp.net/external/OK46gCwJMG5XlB6wvYRMFQI5tNwxg-bsgt9i4mghgT0/https/s3-us-west-2.amazonaws.com/s.cdpn.io/4273/spiritedaway-head.png?width=330&height=372")
        else:
            await ctx.send(f" # You didn't get head (tails)! {self.bot.invisible} https://images-ext-1.discordapp.net/external/RP5rDW2jl8MFPL3c5raE3tMbtJMA7cAa0h4m8DfQ1nc/%3Fcb%3D20220427053256%26path-prefix%3Dprotagonist/https/static.wikia.nocookie.net/p__/images/b/bf/TailsSO.png/revision/latest?width=869&height=674")


def setup(bot):
    bot.add_cog(CoinFlip(bot))
