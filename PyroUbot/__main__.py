import asyncio

from aiohttp import ClientSession
from pyrogram.errors import RPCError
from pyrogram.methods.utilities.idle import idle

from PyroUbot import (Ubot, bot, expired_userbot, get_chat, get_userbots,
                      install_user_id, loadPlugins, rem_expired_date,
                      remove_chat, remove_ubot, rm_all, ubot)


async def start_client(client):
    try:
        await client.start()
    except RPCError:
        user_id = int(client["name"])
        await remove_ubot(user_id)
        await rm_all(user_id)
        await rem_expired_date(user_id)
        for chat_id in await get_chat(user_id):
            await remove_chat(user_id, chat_id)
        print(f"✅ {user_id} ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs")


async def main():
    await asyncio.gather(start_client(bot), start_client(ubot))
    for _ubot in await get_userbots():
        ubot_ = Ubot(**_ubot)
        await start_client(ubot_)
    await loadPlugins()
    await install_user_id()
    await expired_userbot()
    await idle()
    await ClientSession().close()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
