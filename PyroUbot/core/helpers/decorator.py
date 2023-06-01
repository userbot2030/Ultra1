from pyrogram import filters
from pyrogram.enums import ChatType

from PyroUbot import ubot

ONLY_UBOT = filters.user()
get_my_peer = {}


async def install_user_id():
    for X in ubot._get_my_id:
        ONLY_UBOT.add(X)


async def get_peer_userbot(self):
    users = 0
    group = 0
    async for dialog in self.get_dialogs():
        if dialog.chat.type == ChatType.PRIVATE:
            users += 1
        elif dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
            group += 1
    return users, group 


async def install_my_peer():
    for X in ubot._ubot:
       users, group = await get_peer_userbot(X)
       get_my_peer[X.me.id] = {"pm": users, "gc": group}

