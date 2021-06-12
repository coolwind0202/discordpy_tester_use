import os
from bot import MyTestableBot

bot = MyTestableBot(command_prefix="-")
bot.run(os.getenv("DISCORD_TOKEN"))