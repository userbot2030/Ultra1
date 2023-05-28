import asyncio
from datetime import datetime

from pytz import timezone

from PyroUbot import bot, ubot
from PyroUbot.config import LOGS_MAKER_UBOT
from PyroUbot.core.database import (get_expired_date, rem_expired_date,
                                    remove_ubot, rm_all, get_chat, remove_chat)


def expired_msg_bot(X, time, clock):
    date_text = f"""
<b>🗓️ ᴛᴀɴɢɢᴀʟ:</b> <code>{time}</code>
<b>🕕 ᴊᴀᴍ:</b> <code>{clock}</code>
"""
    expired_text = f"""
<b>❏ ᴘᴇᴍʙᴇʀɪᴛᴀʜᴜᴀɴ</b>
<b>├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>╰ ɪᴅ:</b> <code>{X.me.id}</code>

<b>► ᴍᴀsᴀ ᴀᴋᴛɪꜰ ᴜsᴇʀʙᴏᴛ ᴛᴇʟᴀʜ ʜᴀʙɪs ᴛᴇʀɪᴍᴀᴋᴀsɪʜ sᴜᴅᴀʜ ᴍᴇᴍᴀᴋᴀɪ ᴜsᴇʀʙᴏᴛ @{bot.me.username} ᴊᴀɴɢᴀɴ ʟᴜᴘᴀ ᴏʀᴅᴇʀ ʟᴀɢɪ ʏᴀ</b>
"""
    return date_text, expired_text


async def expired_userbot():
    while True:
        now = datetime.now(timezone("Asia/Jakarta"))
        time = now.strftime("%d-%m-%Y")
        clock = now.strftime("%H:%M:%S")
        for X in ubot._ubot:
            try:
                exp = (await get_expired_date(X.me.id)).strftime("%d-%m-%Y")
                if time == exp:
                    for chat in await get_chat(X.me.id):
                        await remove_chat(X.me.id, chat)
                    await rm_all(X.me.id)
                    await remove_ubot(X.me.id)
                    await rem_expired_date(X.me.id)
                    ubot._get_my_id.remove(X.me.id)
                    ubot._ubot.remove(X)
                    await X.log_out()
                    date_text, expired_text = expired_msg_bot(X, time, clock)
                    await bot.send_message(LOGS_MAKER_UBOT, expired_text)
            except:
                pass
        await asyncio.sleep(300)
