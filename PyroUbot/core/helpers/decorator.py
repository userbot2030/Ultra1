from pyrogram import filters
from pyrogram.enums import ChatType

from PyroUbot import bot, ubot
from PyroUbot.config import OWNER_ID

ONLY_UBOT = filters.user()


async def install_user_id():
    for X in ubot._get_my_id:
        ONLY_UBOT.add(X.id)


async def install_my_peer(client):
    users = len(
        [
            dialog.chat.id
            async for dialog in client.iter_dialogs()
            if dialog.chat.type == ChatType.PRIVATE
        ]
    )
    group = len(
        [
            dialog.chat.id
            async for dialog in client.iter_dialogs()
            if dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP)
        ]
    )
    client._get_my_peer[client.me.id] = {"pm": users, "gc": group}


async def install_all_peer():
    for client in ubot._ubot:
        await install_my_peer(client)
        print(f"peer_id ({client.me.id}) telah diinstal ke get_my_peer")
    await bot.send_message(OWNER_ID, "✅ semua peer_id telah berhasil diinstal")
