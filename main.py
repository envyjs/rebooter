print("Starting Envy Rebooter")
import discord
from discord.ext import commands
from datetime import datetime, timedelta
# Create an instance of the bot
intents = discord.Intents.default()
intents.message_content = True
# Restarter default prefix
bot = commands.Bot(command_prefix='r.', intents=intents)
# Start counting uptime
start_time = None

# When the bot is ready
@bot.event
async def on_ready():
    global start_time
    start_time = datetime.utcnow()
    print(f'Logged in as {bot.user}')

# About command, with all the aliases that Restarter recognizes
@bot.command(name='about', aliases=['information', 'info', 'support', 'botinfo', 'botinformation'])
async def about_message(ctx):
    embed = discord.Embed(
        title="📋 Information",
        description="To get the invite link for this bot, please use `r.invite`.",
        color=0x2ECC71  # Green color
    )
    embed.add_field(name="Author", value="Envy Rebooter is made by Envy, a global community.", inline=False)
    embed.add_field(
        name="Support",
        value="Join the support server for general discussion about the bot, bug reporting, and for help: [Support Server](https://discord.gg/eNs4HBZF)",
        inline=False
    )
    embed.set_footer(
        text="Envy Rebooter | https://envy.ink/rebooter",
        icon_url="https://example.com/path_to_logo.png"  # Replace with actual logo URL sometime
    )
    await ctx.send(embed=embed)

# Invite command, with all the aliases that Restarter recognizes
@bot.command(name='invite', aliases=['add'])
async def invite(ctx):
    # Embed message
    embed = discord.Embed(
        title="🔗 Invite",
        color=0xE74C3C  # Red color
    )
    embed.add_field(name="Invite the bot", value="Coming soon", inline=False)
    embed.add_field(name="Support", value="Join the support server for general discussion about the bot, bug reporting and for help: https://discord.gg/eNs4HBZF", inline=False)
    embed.set_footer(
        text="Envy Rebooter | https://envy.ink/rebooter",
        icon_url="https://example.com/path_to_logo.png"  # Replace with actual logo URL sometime
    )
    await ctx.send(embed=embed)

# Uptime command, with all the aliases that Restarter recognizes
@bot.command(name='uptime', aliases=['up', 'time', 'online'])
async def uptime(ctx):
    # Calculate the uptime
    now = datetime.utcnow()
    delta = now - start_time

    # Format the uptime duration
    days, seconds = delta.days, delta.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    uptime_duration = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

    # Embed message
    embed = discord.Embed(
        title="⏰ Uptime",
        color=0xE74C3C  # Red color
    )
    embed.add_field(name="Started", value=start_time.strftime("%a %d %b %Y at %H:%M UTC"), inline=False)
    embed.add_field(name="Alive", value=f"`{uptime_duration}`", inline=False)
    embed.set_footer(
        text="Envy Rebooter | https://envy.ink/rebooter",
        icon_url="https://example.com/path_to_logo.png"  # Replace with actual logo URL sometime
    )
    await ctx.send(embed=embed)

bot.run('token')
