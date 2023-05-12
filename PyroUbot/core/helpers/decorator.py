from pyrogram import filters

from PyroUbot import ubot 
ONLY_UBOT = filters.user()


async def install_user_id():
    for X in ubot._get_my_id:
        ONLY_UBOT.add(X)
