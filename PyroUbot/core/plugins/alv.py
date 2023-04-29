import os
from datetime import datetime
from time import time

import psutil
from pyrogram.raw.functions import Ping
from pyrogram.types import (InlineKeyboardMarkup, InlineQueryResultArticle,
                            InputTextMessageContent)

from .. import *


async def alive_cmd(client, message):
    try:
        x = await client.get_inline_bot_results(
            bot.me.username, f"alive {message.id} {message.from_user.id}"
        )
        await message.reply_inline_bot_result(x.query_id, x.results[0].id)
    except Exception as error:
        await message.reply(error)


async def alive_query(client, inline_query):
    get_id = inline_query.query.split()
    for my in ubot._ubot:
        if int(get_id[2]) == my.me.id:
            peer = my._get_my_peer[my.me.id]
            get_exp = await get_expired_date(my.me.id)
            exp = get_exp.strftime("%d-%m-%Y")
            if my.me.id == OWNER_ID:
                status = "<b>ᴘʀᴇᴍɪᴜᴍ</b> <code>[ꜰᴏᴜɴᴅᴇʀ]</code>"
            elif my.me.id in await get_seles():
                status = "<b>ᴘʀᴇᴍɪᴜᴍ</b> <code>[ᴀᴅᴍɪɴ]</code>"
            else:
                status = "<b>ᴘʀᴇᴍɪᴜᴍ</b> <code>[ᴍᴇᴍʙᴇʀ]</code>"
            if int(get_id[2]) == OWNER_ID:
                button = Button.alive(get_id)[0]
            else:
                button = Button.alive(get_id)[1]
            start = datetime.now()
            await my.invoke(Ping(ping_id=0))
            ping = (datetime.now() - start).microseconds / 1000
            uptime = await get_time((time() - start_time))
            msg = f"""
<b><a href=tg://user?id={my.me.id}>{my.me.first_name} {my.me.last_name or ''}</a></b>
    <b>sᴛᴀᴛᴜs:</b> {status} 
        <b>ᴇxᴘɪʀᴇᴅ_ᴏɴ:</b> <code>{exp}</code> 
        <b>ᴅᴄ_ɪᴅ:</b> <code>{my.me.dc_id}</code>
        <b>ᴘɪɴɢ_ᴅᴄ:</b> <code>{ping} ms</code>
        <b>ᴘᴇᴇʀ_ᴜsᴇʀs:</b> <code>{peer['users']} users</code>
        <b>ᴘᴇᴇʀ_ɢʀᴏᴜᴘ:</b> <code>{peer['group']} group</code>
        <b>sᴛᴀʀᴛ_ᴜᴘᴛɪᴍᴇ:</b> <code>{uptime}</code>
"""
            await client.answer_inline_query(
                inline_query.id,
                cache_time=0,
                results=[
                    (
                        InlineQueryResultArticle(
                            title="💬",
                            reply_markup=InlineKeyboardMarkup(button),
                            input_message_content=InputTextMessageContent(msg),
                        )
                    )
                ],
            )


async def stats_alive(client, callback_query):
    if not callback_query.from_user.id == OWNER_ID:
        return await callback_query.answer(
            f"❌ ᴛᴏᴍʙᴏʟ ɪɴɪ ʙᴜᴋᴀɴ ᴜɴᴛᴜᴋ ᴍᴜ {callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}",
            True,
        )
    uptime = await get_time((time() - start_time))
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    stats = f"""
UPTIME: {uptime}
BOT: {round(process.memory_info()[0] / 1024 ** 2)} MB
CPU: {cpu}%
RAM: {mem}%
DISK: {disk}%
UBOT: {len(ubot._ubot)}
MODULES: {len(HELP_COMMANDS) + len(HelpText)}
"""
    await callback_query.answer(stats, True)


async def alive_close(cln, cq):
    get_id = cq.data.split()
    if not cq.from_user.id == int(get_id[2]):
        return await cq.answer(
            f"❌ ᴛᴏᴍʙᴏʟ ɪɴɪ ʙᴜᴋᴀɴ ᴜɴᴛᴜᴋ ᴍᴜ {cq.from_user.first_name} {cq.from_user.last_name or ''}",
            True,
        )
    unPacked = unpackInlineMessage(cq.inline_message_id)
    for my in ubot._ubot:
        if cq.from_user.id == int(my.me.id):
            await my.delete_messages(
                unPacked.chat_id, [int(get_id[1]), unPacked.message_id]
            )
