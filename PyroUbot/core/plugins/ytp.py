import os
from time import time 
from datetime import timedelta

import wget
from pyrogram.errors import FloodWait, MessageNotModified
from youtubesearchpython import VideosSearch

from PyroUbot import *


def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return f"{str(round(size, 2))} {dict_power_n[raised_to_pow]}B"


def time_formatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        (f"{str(days)} day(s), " if days else "")
        + (f"{str(hours)} hour(s), " if hours else "")
        + (f"{str(minutes)} minute(s), " if minutes else "")
        + (f"{str(seconds)} second(s), " if seconds else "")
        + (f"{str(milliseconds)} millisecond(s), " if milliseconds else "")
    )
    return tmp[:-2]


async def progress(current, total, message, start, type_of_ps, file_name=None):
    now = time.time()
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
            "".join("🔴" for _ in range(math.floor(percentage / 10))),
            "".join("🔘" for _ in range(10 - math.floor(percentage / 10))),
            round(percentage, 2),
        )
        tmp = progress_str + "{0} of {1}\nETA: {2}".format(
            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)
        )
        if file_name:
            try:
                await message.edit(
                    f"{type_of_ps}\n<b>File Name:</b> <code>{file_name}</code>\n{tmp}"
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


async def vsong_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "❌ <b>ᴠɪᴅᴇᴏ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ,</b>\nᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴀɴ ᴊᴜᴅᴜʟ ᴠɪᴅᴇᴏ ᴅᴇɴɢᴀɴ ʙᴇɴᴀʀ.",
        )
    infomsg = await message.reply_text("<b>🔍 ᴘᴇɴᴄᴀʀɪᴀɴ...</b>", quote=False)
    try:
        search = VideosSearch(message.text.split(None, 1)[1], limit=1).result()[
            "result"
        ][0]
        link = f"https://youtu.be/{search['id']}"
    except Exception as error:
        return await infomsg.edit(f"<b>🔍 ᴘᴇɴᴄᴀʀɪᴀɴ...\n\n{error}</b>")
    await infomsg.edit(f"<b>📥 ᴅᴏᴡɴʟᴏᴀᴅᴇʀ...</b>")
    try:
        (
            file_name,
            title,
            url,
            duration,
            views,
            channel,
            thumb,
            data_ytp,
        ) = await YoutubeDownload(link, as_video=True)
    except Exception as error:
        return await infomsg.edit(f"<b>📥 ᴅᴏᴡɴʟᴏᴀᴅᴇʀ...\n\n{error}</b>")
    thumbnail = wget.download(thumb)
    await client.send_video(
        message.chat.id,
        video=file_name,
        thumb=thumbnail,
        file_name=title,
        duration=duration,
        supports_streaming=True,
        caption=data_ytp.format(
            "ᴠɪᴅᴇᴏ",
            title,
            timedelta(seconds=duration),
            views,
            channel,
            url,
            bot.me.mention,
        ),
        reply_to_message_id=message.id,
    )
    await infomsg.delete()
    for files in (thumbnail, file_name):
        if files and os.path.exists(files):
            os.remove(files)


async def song_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "❌ <b>ᴀᴜᴅɪᴏ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ,</b>\nᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴀɴ ᴊᴜᴅᴜʟ ᴠɪᴅᴇᴏ ᴅᴇɴɢᴀɴ ʙᴇɴᴀʀ.",
        )
    infomsg = await message.reply_text("<b>🔍 ᴘᴇɴᴄᴀʀɪᴀɴ...</b>", quote=False)
    try:
        search = VideosSearch(message.text.split(None, 1)[1], limit=1).result()[
            "result"
        ][0]
        link = f"https://youtu.be/{search['id']}"
    except Exception as error:
        return await infomsg.edit(f"<b>🔍 ᴘᴇɴᴄᴀʀɪᴀɴ...\n\n{error}</b>")
    await infomsg.edit(f"<b>📥 ᴅᴏᴡɴʟᴏᴀᴅᴇʀ...</b>")
    try:
        (
            file_name,
            title,
            url,
            duration,
            views,
            channel,
            thumb,
            data_ytp,
        ) = await YoutubeDownload(link, as_video=False)
    except Exception as error:
        return await infomsg.edit(f"<b>📥 ᴅᴏᴡɴʟᴏᴀᴅᴇʀ...\n\n{error}</b>")
    thumbnail = wget.download(thumb)
    c_time = time()
    file_stark = f"{search['id']}.mp3"
    await client.send_audio(
        message.chat.id,
        audio=file_name,
        thumb=thumbnail,
        file_name=title,
        performer=channel,
        duration=duration,
        caption=data_ytp.format(
            "ᴀᴜᴅɪᴏ",
            title,
            timedelta(seconds=duration),
            views,
            channel,
            url,
            bot.me.mention,
        ),
        progress=progress,
        progress_args=(infomsg, c_time, "<b>📥 ᴅᴏᴡɴʟᴏᴀᴅᴇʀ...</b>", file_stark),
        reply_to_message_id=message.id,
    )
    await infomsg.delete()
    for files in (thumbnail, file_name):
        if files and os.path.exists(files):
            os.remove(files)
