import discord
from discord.ext import commands

EXT = (
    "level_one",
    "level_two",
    "level_three"
)
    
class MyTestableBot(commands.Bot):
    def __init__(self, command_prefix: str, **options):
        super().__init__(command_prefix, **options)
        for ext_name in EXT:
            self.load_extension("cogs." + ext_name)

    async def on_ready(self):
        print("ready...")