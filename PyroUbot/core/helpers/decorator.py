from pyrogram import filters
from pyrogram.enums import ChatType

from PyroUbot import bot, ubot
from PyroUbot.config import OWMER_I

ONLY_UBOT = filters.user()
get_my_peer = {}


async def install_user_id():
    for X in ubot._get_my_id:
        ONLY_UBOT.add(X)


async def install_my_peer():
    users = 0
    group = 0
    for X in ubot._ubot:
        async for dialog in X.get_dialogs():
            if dialog.chat.type == ChatType.PRIVATE:
                users += 1
            elif dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
                group += 1
        get_my_peer[X.me.id] = {"pm": users, "gc": group}
        print(f"{X.me.id} install to get_my_peer")
    await bot.send_message(OWMER_ID, "✅ sᴇᴍᴜᴀ ᴘᴇᴇʀɪᴅ ᴛᴇʟᴀʜ ʙᴇʀʜᴀsɪʟ ᴅɪɪɴsᴛᴀʟʟ")
