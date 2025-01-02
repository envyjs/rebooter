from discord.ext import commands

bot = commands.Bot(command_prefix='r.')
    
@bot.command(name='about', aliases=['information', 'info', 'support', 'botinfo', 'botinformation'])
async def about_message(ctx):
    await ctx.send("Hello")

bot.run('token')
