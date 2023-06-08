import asyncio
import os

from pyrogram.errors import RPCError
from pyrogram.methods.utilities.idle import idle

from PyroUbot import *


async def main():
    await bot.start()
    await ubot.start()
    for _ubot in await get_userbots():
        ubot_ = Ubot(**_ubot)
        try:
            await ubot_.start()
        except RPCError:
            user_id = int(_ubot["name"])
            await remove_ubot(user_id)
            await rm_all(user_id)
            await rem_expired_date(user_id)
            for X in await get_chat(user_id):
                await remove_chat(user_id, X)
            print(f"✅ {user_id} ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs")
    await loadPlugins()
    await install_all_peer()
    await install_user_id()
    await expired_userbot()
    await idle()


if __name__ == "__main__":
    try:
        asyncio.get_event_loop_policy().get_event_loop().run_until_complete(main())
    except Exception:
        os.system(f"kill -9 {os.getpid()} && rm -rf *.session* && python3 -m PyroUbot")
