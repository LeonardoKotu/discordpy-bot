import disnake
from disnake.ext import commands

intents = disnake.Intents().all()

bot = commands.InteractionBot(intents=intents)

bot.load_extension("cogs.info")
bot.load_extension("cogs.ticket")


@bot.event
async def on_ready():
    pass

bot.run(os.environ["DISCORD_TOKEN"])
