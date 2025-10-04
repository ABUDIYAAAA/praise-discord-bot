import discord
from discord.ext import commands
from discord import app_commands
import json
import os
from datetime import datetime
import asyncio


class Shoutout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


async def setup(bot):
    print("Shoutouts loaded")
    await bot.add_cog(Shoutout(bot))
