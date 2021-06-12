import sys
from distest import TestCollector
from distest import run_dtest_bot

# The tests themselves

test_collector = TestCollector()
created_channel = None

@test_collector()
async def test_one_1(interface):
    await interface.assert_reply_equals("/neko", "にゃーん")

@test_collector()
async def test_one_2(interface):
    await interface.send_message("/inu")
    await interface.ensure_silence()

@test_collector()
async def test_two_1(interface):
    await interface.send_message("-neko")
    await interface.ensure_silence()  #  Command も反応しない

if __name__ == "__main__":
    run_dtest_bot(sys.argv, test_collector)