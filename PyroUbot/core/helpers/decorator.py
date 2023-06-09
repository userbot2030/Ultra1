from pyrogram import filters
from pyrogram.enums import ChatType

from PyroUbot import bot, ubot
from PyroUbot.config import OWNER_ID

ONLY_UBOT = filters.user()


async def install_user_id():
    for X in ubot._get_my_id:
        ONLY_UBOT.add(X)


async def install_my_peer(self):
    users = len(
        [
            dialog.chat.id
            async for dialog in self.get_dialogs()
            if dialog.chat.type == ChatType.PRIVATE
        ]
    )
    group = len(
        [
            dialog.chat.id
            async for dialog in self.get_dialogs()
            if dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP)
        ]
    )
    self._get_my_peer[self.me.id] = {"pm": users, "gc": group}


async def install_all_peer():
    for self in ubot._ubot:
        await install_my_peer(self)
    await bot.send_message(OWNER_ID, "✅ sᴇᴍᴜᴀ ᴘᴇᴇʀɪᴅ ᴛᴇʟᴀʜ ʙᴇʀʜᴀsɪʟ ᴅɪɪɴsᴛᴀʟʟ")
