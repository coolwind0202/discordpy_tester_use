import pytest
import discord.ext.test as dpytest
from bot import MyTestableBot
import discord

@pytest.fixture
def bot(event_loop):
    intents = discord.Intents.all()
    bot = MyTestableBot("-", loop=event_loop, intents=intents)
    dpytest.configure(bot, num_guilds=2, num_members=3)
    return bot

@pytest.mark.asyncio
async def test_one_1(bot: MyTestableBot):
    await dpytest.message("/neko")
    assert dpytest.verify().message().content("にゃーん")

@pytest.mark.asyncio
async def test_one_2(bot: MyTestableBot):
    await dpytest.message("/inu")
    assert dpytest.verify().message().nothing()

@pytest.mark.asyncio
async def test_two_1(bot: MyTestableBot):
    guild: discord.Guild = bot.guilds[0]
    await guild.create_role(name="にゃーん")
    message = await dpytest.message("-neko")
    new_message: discord.Message = await message.channel.fetch_message(message.id)
    
    assert str(new_message.reactions[0].emoji) == "😺"

@pytest.mark.asyncio
async def test_two_2(bot: MyTestableBot):
    guild: discord.Guild = bot.guilds[0]
    await guild.create_role(name="にゃーん")
    message: discord.Message = await dpytest.message("-neko", guild.text_channels[0])
    assert discord.utils.get(message.author.roles, name="にゃーん") is not None

'''
@pytest.mark.asyncio
async def test_three_1(bot: MyTestableBot):
    guild: discord.Guild = bot.guilds[0]
    channel: discord.TextChannel = guild.text_channels[0]

    member_0: discord.Member = discord.utils.get(guild.members, name="TestUser0")
    overwrite = discord.PermissionOverwrite()
    overwrite.manage_messages = True
    await dpytest.set_permission_overrides(member_0, channel, overwrite)

    member_1: discord.Member = discord.utils.get(guild.members, name="TestUser1")
    message: discord.Message = await dpytest.message("Hello!", guild.text_channels[0], member_1)
    await message.delete()

    expected_embed = discord.Embed(title="メッセージが削除されました")
    expected_embed.add_field(name="送信者", value=str(member_1))
    expected_embed.add_field(name="削除者", value=str(member_0))

    assert dpytest.verify().message().embed(expected_embed)
'''