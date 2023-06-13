import asyncio

from pyrogram import filters
from pyrogram.enums import ChatType

from PyroUbot import ubot

ONLY_UBOT = filters.user()


async def install_user_id():
    for X in ubot._get_my_id:
        ONLY_UBOT.add(X)


async def install_my_peer(client):
    users = [
        dialog.chat.id
        async for dialog in client.get_dialogs()
        if dialog.chat.type == ChatType.PRIVATE
    ]
    group = [
        dialog.chat.id
        async for dialog in client.get_dialogs()
        if dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP)
    ]
    client._get_my_peer[client.me.id] = {"pm": users, "gc": group}



async def install_all_peer():
    for client in ubot._ubot:
        try:
            await install_my_peer(client)
        except Exception as error:
            print(f"error: {error}")
    await bot.send_message("✅ sᴇᴍᴜᴀ ᴘᴇᴇʀ_ɪᴅ ʙᴇʀʜᴀsɪʟ ᴅɪɪɴsᴛᴀʟʟ")
