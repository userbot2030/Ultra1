import asyncio
from datetime import datetime

from pyrogram.types import InlineKeyboardMarkup
from pytz import timezone

from PyroUbot import bot, ubot
from PyroUbot.config import LOGS_MAKER_UBOT
from PyroUbot.core.database import (get_chat, get_expired_date, rem_uptime,
                                    rem_expired_date, remove_chat, remove_ubot,
                                    rm_all)
from PyroUbot.core.helpers import MSG, Button


async def expired_userbot(X):
    try:
        time = datetime.now(timezone("Asia/Jakarta")).strftime("%d-%m-%Y")
        exp = (await get_expired_date(X.me.id)).strftime("%d-%m-%Y")
        if time == exp:
            for chat in await get_chat(X.me.id):
                await remove_chat(X.me.id, chat)
            await rm_all(X.me.id)
            await remove_ubot(X.me.id)
            await rem_uptime(X.me.id)
            await rem_expired_date(X.me.id)
            ubot._get_my_id.remove(X.me.id)
            ubot._ubot.remove(X)
            await X.log_out()
            expired_text = MSG.EXPIRED_MSG_BOT(X)
            expired_button = Button.expired_button_bot()
            await bot.send_message(
                LOGS_MAKER_UBOT,
                expired_text,
                reply_markup=InlineKeyboardMarkup(expired_button),
            )
    except Exception as e:
        print(f"Error: - {X.me.id} - :{str(e)}")


async def expiredUserbots():
    while True:
        tasks = [expired_userbot(X) for X in ubot._ubot]
        await asyncio.gather(*tasks)
        await asyncio.sleep(3600)
