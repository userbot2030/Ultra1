from pyrogram import filters

from PyroUbot import get_my_id

ONLY_UBOT = filters.user()


async def pybot():
    for X in get_my_id:
        ONLY_UBOT.add(X)
