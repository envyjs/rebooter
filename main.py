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
    embed = discord.Embed(
        title="📋 Information",
        description="To get the invite link for this bot, please use `r.invite`.",
        color=0x2ECC71  # Green color
    )
    embed.add_field(name="Author", value="Envy Rebooter is made by Envy, a global community.", inline=False)
    embed.add_field(
        name="Support",
        value="Join the support server for general discussion about the bot, bug reporting, and for help: [Support Server](https://www.example.com)",
        inline=False
    )
    embed.set_footer(
        text="Envy Rebooter | https://envy.js.org",
        icon_url="https://example.com/path_to_logo.png"  # Replace with actual logo URL sometime
    )

    await ctx.send(embed=embed)restarter.mattcowley.co.uk/donate

bot.run('token')
