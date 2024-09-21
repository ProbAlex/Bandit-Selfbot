from discord.ext import commands


class OnMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author != self.bot.user:
            return

        if message.content.startswith('>'):
        
            print(f"Command: {message.content}")
            message.content = "!" + message.content[1:]
            await message.delete()

        await self.bot.process_commands(message)


def setup(bot):
    bot.add_cog(OnMessage(bot))
