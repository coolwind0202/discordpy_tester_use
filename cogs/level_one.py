import discord
from discord.ext import commands

class LevelOneCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener(name="on_message")
    async def nyan(self, message: discord.Message):
        if message.author.bot:
            return  #  無限ループを回避

        if message.content == "/neko":
            await message.channel.send("にゃーん")

def setup(bot):
    bot.add_cog(LevelOneCog(bot))