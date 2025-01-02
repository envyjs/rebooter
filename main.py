print("Starting Envy Rebooter")
from discord.ext import commands

# Create an instance of the bot
intents = discord.Intents.default()
intents.messages = True
# Restarter default prefix
bot = commands.Bot(command_prefix='r.', intents=intents)

# When the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# About command, with all the aliases that Restarter recognizes
@bot.command(name='about', aliases=['information', 'info', 'support', 'botinfo', 'botinformation'])
async def about_message(ctx):
    await ctx.send("Hello")

bot.run('token')
