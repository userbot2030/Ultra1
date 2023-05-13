from datetime import datetime, timedelta

from pyrogram import filters
from pytz import timezone

from PyroUbot import set_expired_date, ubot

ONLY_UBOT = filters.user()


async def install_user_id():
    for X in ubot._get_my_id:
        ONLY_UBOT.add(X)
    now = datetime.now(timezone("Asia/Jakarta"))
    expire_date = now + timedelta(days=7)
    await set_expired_date(ubot.me.id, expire_date)
