import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run('MTE0MjI5NzA3NjM3NDQzNzg4OQ.G5yep6.DGGTmUKSNR9BhhMlFq8_8LuUzm3B6UWTQw4Jno')