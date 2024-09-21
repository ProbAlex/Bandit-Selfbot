import discord
from discord.ext import commands
import asyncio
from blockgamebot.api import Scammers
import json
import time
import requests

with open("config.json", "r") as config_file:
    config = json.load(config_file)
scammerlistkey = config['scammer_list']
whitelist = config['Whitelist']
webhook_url = config['webhook']
scammers = Scammers(scammerlistkey)


class Antiscam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def antiscam(self, ctx):
        start_time = time.time()
        botMessage = await ctx.send(f"`Started scammer autoban`")
        banned_users = [ban_entry.user.id for ban_entry in await ctx.guild.bans()]
        all_scammers = await scammers.get_all()
        for x in range(len(all_scammers)):
            scammer_id = all_scammers[x]["id"]
            if scammer_id in whitelist:
                print("Continued due to scammer favoritism")
                continue
            elif scammer_id in banned_users:
                print("Continued due to previously banned member.")
                continue
            else:
                try:
                    scammer = await self.bot.fetch_user(scammer_id)
                    if scammer is not None:
                        await asyncio.sleep(0.5)
                        await ctx.guild.ban(scammer, reason="scammer autoban")
                        print(f"Banned {scammer}")
                except:
                    continue
        end_time = time.time()
        elapsed = end_time - start_time
        await botMessage.delete()
        finish = {
  "content": " ",
  "embeds": [
    {
      "title": "Antiscam Function Finished",
      "description": f"**Banned all scammers in {int(elapsed)} seconds**",
      "color": 711618,
      "author": {
        "name": "Bandit Selfbot!"
      }
    }
  ],
  "username": "SelfBot",
  "avatar_url": "https://cdn-icons-png.flaticon.com/512/4712/4712035.png",
  "attachments": []
}
        requests.post(webhook_url, json = finish)

def setup(bot):
    bot.add_cog(Antiscam(bot))