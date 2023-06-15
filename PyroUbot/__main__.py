import asyncio

from pyrogram.errors import RPCError
from pyrogram.methods.utilities.idle import idle

from PyroUbot import *


async def main():
    await asyncio.gather(bot.start(), ubot.start())
    for _ubot in await get_userbots():
        user_id = int(_ubot["name"])
        ubot_ = Ubot(**_ubot)
        try:
            await asyncio.wait_for(ubot_.start(), timeout=120)
        except asyncio.TimeoutError:
            print(f"[INFO] - ({user_id}) ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇʀᴇsᴘᴏɴ")
        except RPCError:
            await remove_ubot(user_id)
            await rm_all(user_id)
            await rem_expired_date(user_id)
            for X in await get_chat(user_id):
                await remove_chat(user_id, X)
            print(f"✅ {user_id} ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs")
    await asyncio.gather(
        loadPlugins(),
        install_all_peer(),
        expired_userbot(),
        idle(),
    )


if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())
