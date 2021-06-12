from typing import Union
import asyncio

import discord
from discord.ext import commands

class LevelThreeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener(name="on_message_delete")
    async def get_deleter(self, message: discord.Message):
        guild: discord.Guild = message.guild

        async for entry in guild.audit_logs(limit=100, action=discord.AuditLogAction.message_delete, after=message.created_at):
            delete_message_author: Union[discord.Member, discord.User] = entry.target

            if delete_message_author != message.author:
                continue

            embed = discord.Embed(title="メッセージが削除されました")
            embed.add_field(name="送信者", value=str(message.author))
            embed.add_field(name="削除者", value=str(entry.user))
            await asyncio.sleep(5)
            await message.channel.send(
                embed=embed
            )
            break
        else:
            await message.channel.send(f"{message.author}はメッセージを自分で削除しました。")

def setup(bot):
    bot.add_cog(LevelThreeCog(bot))