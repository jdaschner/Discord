import discord
import asyncio
from datetime import datetime, timedelta

class WelcomeRoleBot(discord.Client):
    def __init__(self, role_id, token, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.role_id = role_id
        self.token = token

    async def on_member_join(self, member):
        role = discord.utils.get(member.guild.roles, id=self.role_id)
        await member.add_roles(role)

    async def on_ready(self):
        print('Logged in as {0.user}'.format(self))
        await self.check_roles()

    async def check_roles(self):
        await self.wait_until_ready()
        while not self.is_closed():
            for guild in self.guilds:
                for member in guild.members:
                    role = discord.utils.get(member.guild.roles, id=self.role_id)
                    if role in member.roles:
                        join_date = member.joined_at.astimezone()
                        if datetime.now().astimezone() - join_date > timedelta(days=7):
                            await member.remove_roles(role)
            await asyncio.sleep(60)


