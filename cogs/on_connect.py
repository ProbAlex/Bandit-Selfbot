from discord.ext import commands



class OnConnect(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self):
        print("Alex is gay.")


def setup(bot):
    bot.add_cog(OnConnect(bot))
