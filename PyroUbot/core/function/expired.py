from datetime import datetime

from pytz import timezone

from PyroUbot import bot, ubot
from PyroUbot.config import OWNER_ID
from PyroUbot.core.database import get_expired_date, rem_expired_date, remove_ubot, rm_all


async def premium():
    time = datetime.now(timezone("Asia/Jakarta")).strftime("%d-%m-%Y")
    for X in ubot._ubot:
        try:
            exp = (await get_expired_date(X.me.id)).strftime("%d-%m-%Y")
            if time == exp:
                await rem_expired_date(X.me.id)
                await remove_ubot(X.me.id)
                await rm_all(X.me.id)
                ubot._ubot.remove(X)
                await bot.send_message(
                    OWNER_ID,
                    f"<b>{X.me.first_name} {X.me.last_name or ''} | <code>{X.me.id}</code> berhasil dihapus</b>",
                )
        except:
            pass
