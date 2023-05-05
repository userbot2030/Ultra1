from datetime import datetime
import asyncio
from pytz import timezone

from PyroUbot import bot, get_my_id, ubot
from PyroUbot.config import LOGS_MAKER_UBOT
from PyroUbot.core.database import (get_expired_date, rem_expired_date,
                                    remove_ubot, rm_all)

def msg_bot(X, time, clock):
    text_expired = f"<b>❏ ᴘᴇᴍʙᴇʀɪᴛᴀʜᴜᴀɴ\n ├ ᴀᴋᴜɴ <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>\n ╰ ɪᴅ <code>{X.me.id}</code>\n\n► ᴍᴀsᴀ ᴀᴋᴛɪꜰ ᴜsᴇʀʙᴏᴛ ᴛᴇʟᴀʜ ʜᴀʙɪs ᴛᴇʀɪᴍᴀᴋᴀsɪʜ sᴜᴅᴀʜ ᴍᴇᴍᴀᴋᴀɪ ᴜsᴇʀʙᴏᴛ @{bot.me.username} ᴊᴀɴɢᴀɴ ʟᴜᴘᴀ ᴏʀᴅᴇʀ ʟᴀɢɪ ʏᴀ</b>"
    text_date_msg = f"<b>🗓️ ᴛᴀɴɢɢᴀʟ:</b> <code>{time}</code>\n<b>🕕 ᴊᴀᴍ:</b> <code>{clock}</code>"
    return [text_expired, text_date_msg]

async def expired_userbot():
    while True:
        now = datetime.now(timezone("Asia/Jakarta"))
        time = now.strftime("%d-%m-%Y")
        clock = now.strftime("%H:%M:%S")
        for X in ubot._ubot:
            try:
                exp = (await get_expired_date(X.me.id)).strftime("%d-%m-%Y")
                if time == exp:
                    await X.log_out()
                    ubot._ubot.remove(X)
                    await rm_all(X.me.id)
                    get_my_id.remove(X.me.id)
                    await remove_ubot(X.me.id)
                    await rem_expired_date(X.me.id)
                    await bot.send_message(
                        LOGS_MAKER_UBOT,
                        msg_bot(X, time, clock)[0])
            except:
                pass
        await asyncio.sleep(3600)
        await bot.send_message(
            LOGS_MAKER_UBOT,
            msg_bot(X, time, clock)[1]
        )
