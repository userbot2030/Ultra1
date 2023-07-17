import asyncio
import math
import os
from datetime import timedelta
from gc import get_objects
from time import time

from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                            InlineQueryResultArticle, InputTextMessageContent)

from PyroUbot import *


async def copy_bot_msg(client, message):
    if message.from_user.id not in ubot._get_my_id:
        return
    Tm = await message.reply("ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ")
    link = get_arg(message)
    if not link:
        return await Tm.edit(
            f"<b><code>{message.text}</code> [ʟɪɴᴋ_ᴋᴏɴᴛᴇɴ_ᴛᴇʟᴇɢʀᴀᴍ]</b>"
        )
    msg_id = int(link.split("/")[-1])
    chat = str(link.split("/")[-2])
    try:
        get = await client.get_messages(chat, msg_id)
        await get.copy(message.chat.id)
        await Tm.delete()
    except Exception as error:
        await Tm.edit(error)


COPY_ID = {}


async def copy_ubot_msg(client, message):
    msg = message.reply_to_message or message
    Tm = await message.reply("<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴄᴏᴘʏ ᴍᴏʜᴏɴ ʙᴇʀsᴀʙᴀʀ</b>")
    link = get_arg(message)
    if not link:
        return await Tm.edit(
            f"<b><code>{message.text}</code> [ʟɪɴᴋ_ᴋᴏɴᴛᴇɴ_ᴛᴇʟᴇɢʀᴀᴍ]</b>"
        )
    if link.startswith(("https", "t.me")):
        msg_id = int(link.split("/")[-1])
        if "t.me/c/" in link:
            chat = int("-100" + str(link.split("/")[-2]))
            try:
                get = await client.get_messages(chat, msg_id)
                text = get.caption or ""
                if get.photo:
                    media = await client.download_media(
                        get,
                        progress=progress,
                        progress_args=(Tm, time(), "ᴅᴏᴡɴʟᴏᴀᴅ ᴘʜᴏᴛᴏ\n"),
                    )
                    await client.send_photo(
                        message.chat.id, media, caption=text, reply_to_message_id=msg.id
                    )
                    await Tm.delete()
                    os.remove(media)

                elif get.video:
                    media = await client.download_media(
                        get,
                        progress=progress,
                        progress_args=(Tm, time(), "ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ\n"),
                    )
                    thumbnail = await client.download_media(get.video.thumbs[-1])
                    await client.send_video(
                        message.chat.id,
                        video=media,
                        duration=get.video.duration,
                        caption=text,
                        thumb=thumbnail,
                        reply_to_message_id=msg.id,
                    )
                    await Tm.delete()
                    os.remove(media)
                    os.remove(thumbnail)

                elif get.audio:
                    media = await client.download_media(
                        get,
                        progress=progress,
                        progress_args=(Tm, time(), "ᴅᴏᴡɴʟᴏᴀᴅ ᴀᴜᴅɪᴏ\n"),
                    )
                    thumbnail = await client.download_media(get.audio.thumbs[-1])
                    await client.send_audio(
                        message.chat.id,
                        audio=media,
                        duration=get.audio.duration,
                        caption=text,
                        thumb=thumbnail,
                        reply_to_message_id=msg.id,
                    )
                    await Tm.delete()
                    os.remove(media)
                    os.remove(thumbnail)

                elif get.voice:
                    media = await client.download_media(
                        get,
                        progress=progress,
                        progress_args=(Tm, time(), "ᴅᴏᴡɴʟᴏᴀᴅ ᴠᴏɪᴄᴇ\n"),
                    )
                    await client.send_voice(
                        message.chat.id,
                        voice=media,
                        caption=text,
                        reply_to_message_id=msg.id,
                    )
                    await Tm.delete()
                    os.remove(media)

                elif get.document:
                    media = await client.download_media(
                        get,
                        progress=progress,
                        progress_args=(Tm, time(), "ᴅᴏᴡɴʟᴏᴀᴅ ᴅᴏᴄᴜᴍᴇɴᴛ\n"),
                    )
                    thumbnail = await client.download_media(get.document.thumbs[-1])
                    await client.send_document(
                        message.chat.id,
                        document=media,
                        caption=text,
                        thumb=thumbnail,
                        reply_to_message_id=msg.id,
                    )
                    await Tm.delete()
                    os.remove(media)
                    os.remove(thumbnail)

                elif get.animation:
                    media = await client.download_media(
                        get,
                        progress=progress,
                        progress_args=(Tm, time(), "ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴɪᴍᴀᴛɪᴏɴ\n"),
                    )
                    thumbnail = await client.download_media(get.animation.thumbs[-1])
                    await client.send_animation(
                        message.chat.id,
                        animation=media,
                        caption=text,
                        thumb=thumbnail,
                        reply_to_message_id=msg.id,
                    )
                    await Tm.delete()
                    os.remove(media)
                    os.remove(thumbnail)
                else:
                    await get.copy(message.chat.id, reply_to_message_id=msg.id)
                    await Tm.delete()
            except Exception as e:
                await Tm.edit(str(e))
        else:
            chat = str(link.split("/")[-2])
            try:
                get = await client.get_messages(chat, msg_id)
                await get.copy(message.chat.id, reply_to_message_id=msg.id)
                await Tm.delete()
            except Exception:
                try:
                    text = f"get_msg {id(message)}"
                    x = await client.get_inline_bot_results(bot.me.username, text)
                    results = await client.send_inline_bot_result(
                        message.chat.id,
                        x.query_id,
                        x.results[0].id,
                        reply_to_message_id=msg.id,
                    )
                    COPY_ID[client.me.id] = int(results.updates[1].message.id)
                except Exception as error:
                    return await Tm.edit(str(error))
    else:
        await Tm.edit("ᴍᴀsᴜᴋᴋɪɴ ʟɪɴᴋ ʏᴀɴɢ ᴠᴀʟɪᴅ")


def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "ᴋʙ", 2: "ᴍʙ", 3: "ɢʙ", 4: "ᴛʙ"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return f"{str(round(size, 2))} {dict_power_n[raised_to_pow]}"


def time_formatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        (f"{str(days)} ʜᴀʀɪ, " if days else "")
        + (f"{str(hours)} ᴊᴀᴍ, " if hours else "")
        + (f"{str(minutes)} ᴍᴇɴɪᴛ, " if minutes else "")
        + (f"{str(seconds)} ᴅᴇᴛɪᴋ, " if seconds else "")
        + (f"{str(milliseconds)} ᴍɪᴋʀᴏᴅᴇᴛɪᴋ, " if milliseconds else "")
    )
    return tmp[:-2]


async def progress(current, total, message, start, type_of_ps, file_name=None):
    now = time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        if elapsed_time == 0:
            return
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "{0}{1} {2}%\n".format(
            "".join("•" for _ in range(math.floor(percentage / 10))),
            "".join("~" for _ in range(10 - math.floor(percentage / 10))),
            round(percentage, 2),
        )
        tmp = progress_str + "{0} of {1}\nᴇsᴛɪᴍᴀsɪ: {2}".format(
            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)
        )
        if file_name:
            try:
                await message.edit(
                    f"""
<b>{type_of_ps}</b>

<b>ғɪʟᴇ_ɪᴅ:</b> <code>{file_name}</code>

<b>{tmp}</b>
"""
                )
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass
        else:
            try:
                await message.edit(f"{type_of_ps}\n{tmp}")
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass


async def copy_inline_msg(client, inline_query):
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="get message!",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="🔐 ʙᴜᴋᴀ ᴋᴏɴᴛᴇɴ ʀᴇsᴛʀɪᴄᴛᴇᴅ 🔐",
                                    callback_data=f"copymsg_{int(inline_query.query.split()[1])}",
                                )
                            ],
                        ]
                    ),
                    input_message_content=InputTextMessageContent(
                        "<b>🔒 ᴋᴏɴᴛᴇɴ ʏᴀɴɢ ᴍᴀᴜ ᴅɪᴀᴍʙɪʟ ʙᴇʀsɪꜰᴀᴛ ʀᴇsᴛʀɪᴄᴛᴇᴅ\n\n✅ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴅɪʙᴀᴡᴀʜ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴋᴀ ᴋᴏɴᴛᴇɴ ʀᴇsᴛʀɪᴄᴛᴇᴅ</b>"
                    ),
                )
            )
        ],
    )


async def copy_callback_msg(client, callback_query):
    try:
        q = int(callback_query.data.split("_", 1)[1])
        m = [obj for obj in get_objects() if id(obj) == q][0]
        if not callback_query.from_user.id == m.from_user.id:
            return await callback_query.answer(
                f"❌ ᴛᴏᴍʙᴏʟ ɪɴɪ ʙᴜᴋᴀɴ ᴜɴᴛᴜᴋ ᴍᴜ {callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}",
                True,
            )
        else:
            await m._client.unblock_user(bot.me.username)
            await callback_query.edit_message_text("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ</b>")
            copy = await m._client.send_message(
                bot.me.username, f"/copy {m.text.split()[1]}"
            )
            msg = m.reply_to_message or m
            await asyncio.sleep(1.5)
            await copy.delete()
            async for get in m._client.search_messages(bot.me.username, limit=1):
                await m._client.copy_message(
                    m.chat.id, bot.me.username, get.id, reply_to_message_id=msg.id
                )
                await m._client.delete_messages(m.chat.id, COPY_ID[m._client.me.id])
                await get.delete()
    except Exception as error:
        await callback_query.edit_message_text(f"<code>{error}</code>")
