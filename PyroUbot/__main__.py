import asyncio
import os

from pyrogram.errors import RPCError
from pyrogram.methods.utilities.idle import idle

from PyroUbot import *


async def start_client(client):
    await client.start()
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


async def main():
    await asyncio.gather(bot.start(), ubot.start())
    ubot_client = asyncio.create_task(start_client(ubot))
    await asyncio.gather(bot_client, ubot_client)
    await loadPlugins()
    await install_user_id()
    await expired_userbot()
    await idle()


if __name__ == "__main__":
    if __name__ == "__main__":
        loop = asyncio.get_event_loop()
        asyncio.run(main())
        try:
            loop.run_until_complete(main())
            loop.run_forever()
        except KeyboardInterrupt:
            os.system(f"kill -9 {os.getpid()} && python3 -m PyroUbot")
        finally:
            loop.stop()
