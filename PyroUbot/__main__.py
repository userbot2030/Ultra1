import asyncio

from pyrogram import compose
from pyrogram.errors import RPCError

from PyroUbot import *


async def main():
    await bot.start()
    clients = []
    clients.append(ubot)
    for _ubot in await get_userbots():
        user_id = int(_ubot["name"])
        ubot_ = Ubot(**_ubot)
        try:
            clients.append(ubot_)
        except RPCError:
            await remove_ubot(user_id)
            await rm_all(user_id)
            await rem_expired_date(user_id)
            for X in await get_chat(user_id):
                await remove_chat(user_id, X)
            print(f"✅ {user_id} ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs")
    await asyncio.gather(
        compose(clients),
        loadPlugins(),
        expired_userbot(),
        install_all_peer(),
    )


if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())
