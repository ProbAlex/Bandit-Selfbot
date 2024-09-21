from discord.ext import commands
from blockgamebot.api import Scammers
import json
with open("config.json", "r") as config_file:
    config = json.load(config_file)
scammerlistkey = config['scammer_list']
scammers = Scammers(scammerlistkey)

class Lookup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lookup(self, ctx, *, query):
        scammer = await scammers.lookup(query)
        if scammer["found"]:
            await ctx.send(f' # {query} is a scammer. Results are below.')
            for x in range(scammer["amount"]):
                results = scammer["results"][x]
                await ctx.send(f'''
**Tag**: {results["tag"]}
**ID**: {results["id"]}
**Method**: {results["method"]}
**Amount**: {results["amount"]}
**Search Similarity**: 100%
''')
        else:
            await ctx.send(f' # {query} is NOT a scammer. Results are below.')
            for x in range(scammer["amount"]):
                results = scammer["results"][x]
                await ctx.send(f'''
**Tag**: {results["tag"]}
**ID**: {results["id"]}
**Method**: {results["method"]}
**Amount**: {results["amount"]}
**Search Similarity**: {int(float(results["similarity"])*100)}%
''')



def setup(bot):
    bot.add_cog(Lookup(bot))