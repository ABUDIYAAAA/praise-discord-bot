import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

intents = discord.Intents.all()
description = "praising contributors"
bot = commands.Bot(command_prefix="p ", description=description, intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()

        print(f"Synced {len(synced)} commands.")
    except Exception as e:
        print(f"Error syncing commands: {e}")


@discord.app_commands.allowed_installs(guilds=True)
@discord.app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@bot.tree.command(name="ping", description="Returns bot latency")
async def ping(interaction: discord.Interaction):
    await interaction.response.defer()
    latency = bot.latency * 1000
    await interaction.followup.send(content=f"Latency: {latency:.2f} ms")


async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


asyncio.run(load_extensions())

bot.run(os.getenv("DISCORD_BOT_TOKEN"))
