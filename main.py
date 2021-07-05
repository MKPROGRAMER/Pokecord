import os
import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True


client = commands.Bot(command_prefix="p!")

client.load_extension("commands")

my BOT_TOKEN = os.environ['BOT_TOKEN']

client.run("BOT_TOKEN")

