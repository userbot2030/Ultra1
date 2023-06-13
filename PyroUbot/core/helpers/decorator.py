import asyncio

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.errors import FloodWait

from PyroUbot import OWNER_ID, bot, ubot

ONLY_UBOT = filters.user()


async def install_user_id():
    for X in ubot._get_my_id:
        ONLY_UBOT.add(X)


async def install_my_peer(client):
    try:
        users = []
        group = []
        async for dialog in client.get_dialogs():
            if dialog.chat.type == ChatType.PRIVATE:
                users.append(dialog.chat.id)
            if dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
                group.append(dialog.chat.id)
        client._get_my_peer[client.me.id] = {"pm": users, "gc": group}
    except FloodWait as e:
        print(f"FloodWait occurred. Sleeping for {e.x} seconds.")
        await asyncio.sleep(e.x)
        await install_my_peer(client)
    except Exception as error:
        print(f"Error occurred: {error}")


async def install_all_peer():
    for client in ubot._ubot:
        await install_my_peer(client)
        print(f"({client.me.id}) berhasil diinstall ke ubot._get_my_peer")
    await bot.send_message(OWNER_ID, "✅ sᴇᴍᴜᴀ ᴘᴇᴇʀ_ɪᴅ ʙᴇʀʜᴀsɪʟ ᴅɪɪɴsᴛᴀʟʟ")
