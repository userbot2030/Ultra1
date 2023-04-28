from pyrogram import filters

from .. import get_my_id

ONLY_UBOT = filters.user()


async def install_user_id():
    for X in get_my_id:
        ONLY_UBOT.add(X)
