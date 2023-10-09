import os
import discord

from welcome_roles import WelcomeRoleBot

welcome_role = int(os.environ['WELCOME_ROLE'])
token = os.environ['BOT_TOKEN']

intents = discord.Intents.default()
intents.members = True

bot = WelcomeRoleBot(role_id=welcome_role, token=token, intents=intents)
bot.run(bot.token)