from discord.ext import commands
# Restarter default prefix
bot = commands.Bot(command_prefix='r.')
# About command, with all the aliases that Restarter recognizes
@bot.command(name='about', aliases=['information', 'info', 'support', 'botinfo', 'botinformation'])
async def about_message(ctx):
    await ctx.send("Hello")

bot.run('token')
