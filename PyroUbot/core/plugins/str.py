import asyncio
import random
from gc import get_objects
from time import time

from pyrogram.raw.functions import Ping
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import *


async def ping_cmd(client, message):
    ub_uptime = await get_uptime(client.me.id)
    uptime = await get_time(time() - ub_uptime)

    start_time = time()
    await message.reply_text("Pong!")
    end_time = time()
    delta_ping = (end_time - start_time) * 1000
    prefix = await ubot.get_prefix(client.me.id)

    emot_pong = await get_vars(client.me.id, "EMOJI_PING_PONG") or "6111585093220830556"
    emot_uptime = await get_vars(client.me.id, "EMOJI_UPTIME") or "6113661520929885715"
    emot_mention = (
        await get_vars(client.me.id, "EMOJI_MENTION") or "6114013639528682251"
    )

    if client.me.is_premium:
        _ping = f"""
<b><emoji id={emot_pong}>🏓</emoji> ᴘɪᴡᴡ!! :</b> <code>{delta_ping:.2f} ms</code>
<b><emoji id={emot_uptime}>⏰</emoji> ᴘʀᴇғɪxᴇs :</b> <code>{format(next((p) for p in prefix))}</code>
<b><emoji id={emot_mention}>👑</emoji> <b>— {bot.me.mention}</b>
"""
    else:
        _ping = f"""
<b>❏ ᴘɪᴡᴡ!! :</b> <code>{delta_ping:.2f} ms</code>
<b>├ ᴘʀᴇғɪxᴇs :</b> <code>{format(next((p) for p in prefix))}</code>
<b>╰ <b>— {bot.me.mention}</b>
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
                return await send.edit(
                    f"<b>❌ ᴘᴇsᴀɴ ɪɴɪ ʙᴜᴋᴀɴ ᴜɴᴛᴜᴋᴍᴜ <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>"
                )
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
