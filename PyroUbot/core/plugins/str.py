import asyncio
from datetime import datetime
from gc import get_objects
from time import time

from pyrogram.raw.functions import Ping
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import *


async def ping_cmd(client, message):
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    end = datetime.now()
    delta_ping = (end - start).microseconds / 1000
    ping1 = await get_vars(client.me.id, "EMOJI_PING1") or "6127475690531982315"
    ping2 = await get_vars(client.me.id, "EMOJI_PING2") or "6114073270854619005"
    ping3 = await get_vars(client.me.id, "EMOJI_PING3") or "6114074516395134769"
    if client.me.is_premium:
        _ping = f"""
<b><emoji id={ping1}>🏓</emoji> —ᴘᴏɴɢ:</b> <code>{str(delta_ping).replace('.', ',')} ms</code>
<b><emoji id={ping2}>⏰</emoji> —ᴜʙöᴛ :</b> <code>{bot.me.mention}</code>
<b><emoji id={ping3}>👑</emoji>—ɪ'ᴍ:</b> <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a></b>
"""
    else:
        _ping = f"""
<b>—ᴘᴏɴɢ: </b> <code>{str(delta_ping).replace('.', ',')} ms</code>
<b>—ᴜʙöᴛ: </b> <code>{bot.me.mention}</code>
<b>—ɪ'ᴍ: </b><a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a></b>
"""
    await message.reply(_ping)


async def start_cmd(client, message):
    if len(message.command) < 2:
        buttons = Button.start(message)
        msg = MSG.START(message)
        await message.reply(msg, reply_markup=InlineKeyboardMarkup(buttons))
    else:
        txt = message.text.split(None, 1)[1]
        msg_id = txt.split("_", 1)[1]
        send = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ...</b>")
        if "secretMsg" in txt:
            try:
                m = [obj for obj in get_objects() if id(obj) == int(msg_id)][0]
            except Exception as error:
                return await send.edit(f"<b>❌ ᴇʀʀᴏʀ:</b> <code>{error}</code>")
            user_or_me = [m.reply_to_message.from_user.id, m.from_user.id]
            if message.from_user.id not in user_or_me:
                return await send.edit(f"<b>❌ ᴘᴇsᴀɴ ɪɴɪ ʙᴜᴋᴀɴ ᴜɴᴛᴜᴋᴍᴜ <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>")
            else:
                text = await client.send_message(
                    message.chat.id,
                    m.text.split(None, 1)[1],
                    protect_content=True,
                    reply_to_message_id=message.id,
                )
                await send.delete()
                await asyncio.sleep(120)
                await message.delete()
                await text.delete()
        elif "copyMsg" in txt:
            try:
                m = [obj for obj in get_objects() if id(obj) == int(msg_id)][0]
            except Exception as error:
                return await send.edit(f"<b>❌ ᴇʀʀᴏʀ:</b> <code>{error}</code>")
            id_copy = int(m.text.split()[1].split("/")[-1])
            if "t.me/c/" in m.text.split()[1]:
                chat = int("-100" + str(m.text.split()[1].split("/")[-2]))
            else:
                chat = str(m.text.split()[1].split("/")[-2])
            try:
                get = await client.get_messages(chat, id_copy)
                await get.copy(message.chat.id, reply_to_message_id=message.id)
                await send.delete()
            except Exception as error:
                await send.edit(error)
