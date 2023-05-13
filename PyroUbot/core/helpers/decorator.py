from pyrogram import filters

from PyroUbot import ubot

from datetime import datetime, timedelta

from pytz import timezone



ONLY_UBOT = filters.user()


async def install_user_id():
    for X in ubot._get_my_id:
        ONLY_UBOT.add(X)
    now = datetime.now(timezone("Asia/Jakarta"))
    expire_date = now + timedelta(days=730)
    await set_expired_date(ubot.me.id, expire_date)
