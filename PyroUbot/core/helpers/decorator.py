from pyrogram import filters
from pyrogram.enums import ChatType

from PyroUbot import ubot

ONLY_UBOT = filters.user()


async def install_user_id():
    for X in ubot._get_my_id:
        ONLY_UBOT.add(X)


async def install_my_peer(client):
    users = len(
        [
            dialog.chat.id
            async for dialog in client.get_dialogs()
            if dialog.chat.type == ChatType.PRIVATE
        ]
    )
    group = len(
        [
            dialog.chat.id
            async for dialog in client.get_dialogs()
            if dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP)
        ]
    )
    client._get_my_peer[client.me.id] = {"pm": users, "gc": group}
