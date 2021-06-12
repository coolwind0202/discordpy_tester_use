import discord
from discord.ext import commands

class LevelTwoCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def neko(self, ctx: commands.Context):
        await ctx.message.add_reaction("😺")
        role = discord.utils.get(ctx.guild.roles, name="にゃーん")
        await ctx.author.add_roles(role)

def setup(bot):
    bot.add_cog(LevelTwoCog(bot))