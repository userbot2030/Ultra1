import asyncio

from pyrogram.errors import RPCError
from pyrogram.methods.utilities.idle import idle

from PyroUbot import bot, ubot, get_userbots, Ubot, remove_ubot, rm_all, rem_expired_date, get_chat, remove_chat, loadPlugins, install_user_id, expired_userbot


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


if __name__ == "__main__":
    asyncio.run(main())
 
