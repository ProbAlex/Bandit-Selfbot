import discord
from discord.ext import commands

class RoleObject:
    def __init__(self, name, id, color, position, permissions, mentionable, hoist, managed, is_bot_managed, is_premium_subscriber):
        self.name = name
        self.id = id
        self.color = color
        self.position = position
        self.permissions = permissions
        self.mentionable = mentionable
        self.hoist = hoist
        self.managed = managed  
        self.is_bot_managed = is_bot_managed
        self.is_premium_subscriber = is_premium_subscriber

class ChannelObject:
    def __init__(self, name, id, type, position, category, overwrites):
        self.name = name
        self.id = id
        self.type = type[0]
        self.position = position
        self.category = category
        self.overwrites = overwrites

async def copy_roles(context, roles):
    for role in context.guild.roles:
        try:
            await role.delete()
        except:
            pass
        
    for r in reversed(roles):
        for role, data in r.items():
            role = RoleObject(role, **data)
            if role.is_bot_managed or role.is_premium_subscriber or role.managed:
                continue
          
            if role.name == "@everyone":
                continue
            
            await context.guild.create_role(
                name=role.name,
                color=discord.Colour(role.color),
                permissions=discord.Permissions(role.permissions),
                mentionable=role.mentionable,
                hoist=role.hoist,
                
            )

async def copy_channels(context, channels):
    for channel in context.guild.channels:
        try:
            await channel.delete()
        except:
            pass
      
    _channels = []
    categories = []

    for c in channels:
        for channel, data in c.items():
            if data["type"][0] == "category":
                categories.append(ChannelObject(channel, **data))
            else:
              _channels.append(ChannelObject(channel, **data))


    for channel in categories:
            try:
                overwrites = {
                    context.guild.default_role: discord.PermissionOverwrite.from_pair(deny=discord.Permissions(channel.overwrites["@everyone"][1]), allow=discord.Permissions(channel.overwrites["@everyone"][0])),

                }
            except:
                overwrites = {
                    context.guild.default_role: discord.PermissionOverwrite.from_pair(deny=discord.Permissions(0), allow=discord.Permissions(0)),

                }
                
            for role, perms in channel.overwrites.items():
                if role == "@everyone":
                    continue
                
                try:
                    role = discord.utils.get(context.guild.roles, name=role)
                    if role is None:
                        continue
                    overwrites[role] = discord.PermissionOverwrite.from_pair(deny=discord.Permissions(perms[1]), allow=discord.Permissions(perms[0]))
                except:
                    pass

            await context.guild.create_category(
                name=channel.name,
                overwrites=overwrites,
                position=channel.position
            )


    for channel in _channels:
        if channel.type == "text":
            try:
                overwrites = {
                    context.guild.default_role: discord.PermissionOverwrite.from_pair(deny=discord.Permissions(channel.overwrites["@everyone"][1]), allow=discord.Permissions(channel.overwrites["@everyone"][0])),

                }
            except:
                overwrites = {
                    context.guild.default_role: discord.PermissionOverwrite.from_pair(deny=discord.Permissions(0), allow=discord.Permissions(0)),

                }
            for role, perms in channel.overwrites.items():
                if role == "@everyone":
                    continue
                
                try:
                    role = discord.utils.get(context.guild.roles, name=role)
                    if role is None:
                        continue
                    overwrites[role] = discord.PermissionOverwrite.from_pair(deny=discord.Permissions(perms[1]), allow=discord.Permissions(perms[0]))
                except:
                    pass

            category = discord.utils.get(context.guild.categories, name=channel.category)
            await context.guild.create_text_channel(
                name=channel.name,
                overwrites=overwrites,
                category=category,
                position=channel.position
            )

        elif channel.type == "voice":
            try:
                overwrites = {
                    context.guild.default_role: discord.PermissionOverwrite.from_pair(deny=discord.Permissions(channel.overwrites["@everyone"][1]), allow=discord.Permissions(channel.overwrites["@everyone"][0])),

                }
            except:
                overwrites = {
                    context.guild.default_role: discord.PermissionOverwrite.from_pair(deny=discord.Permissions(0), allow=discord.Permissions(0)),

                }
            for role, perms in channel.overwrites.items():
                if role == "@everyone":
                    continue
                
                try:
                    role = discord.utils.get(context.guild.roles, name=role)
                    if role is None:
                        continue
                    overwrites[role] = discord.PermissionOverwrite.from_pair(deny=discord.Permissions(perms[1]), allow=discord.Permissions(perms[0]))
                except:
                    pass

            category = discord.utils.get(context.guild.categories, name=channel.category)
            await context.guild.create_voice_channel(
                name=channel.name,
            
                overwrites=overwrites,
                category=category,
                position=channel.position
            )

class Copy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="copy",
        description="Copy a fucking server LMAO"
    )
    async def copyroles(self, ctx, serverid):
        guild = self.bot.get_guild(int(serverid))
        await ctx.send("Process started.")
        gdata = {
            "name": guild.name, 
            "channels": [{channel.name: {
                "type": channel.type,
                "id": channel.id, 
                "position": channel.position, 
                "category": channel.category.name if channel.category else None,
                "overwrites": {overwrite.name: [value.value for value in channel.overwrites[overwrite].pair()] for overwrite in channel.overwrites}
                    }
                } for channel in guild.channels], 

            "roles": [{role.name: {
                "id": role.id,
                "color": role.color.value,
                "position": role.position,
                "permissions": role.permissions.value,
                "mentionable": role.mentionable,
                "hoist": role.hoist,
                "managed": role.managed,
                "is_bot_managed": role.is_bot_managed(),
                "is_premium_subscriber": role.is_premium_subscriber()}} for role in guild.roles]}
        

        roles = gdata["roles"]
        channels = gdata["channels"]
        await copy_roles(ctx, roles)
        await copy_channels(ctx, channels)
        
def setup(bot):
    bot.add_cog(Copy(bot))
