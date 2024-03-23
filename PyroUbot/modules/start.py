import os
import asyncio
import psutil


from datetime import datetime
from gc import get_objects
from time import time

from pyrogram.raw import *
from pyrogram.raw.functions import Ping
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import *


@PY.UBOT("ping")
@PY.TOP_CMD
async def _(client, message):
    await ping_cmd(client, message)


@PY.BOT("start")
@PY.START
async def _(client, message):
    await start_cmd(client, message)


@PY.BOT("stats")
async def _(client, message):
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    end = datetime.now()
    delta_ping = (end - start).microseconds / 1000
    delta_ping_formatted = round(delta_ping, 3)
    uptime = await get_time((time() - start_time))
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    buttons = [[InlineKeyboardButton("ʀᴇғʀᴇsʜ", callback_data="kontol")]]
    _ping = f"""
<b>🖥️ [SYSTEM UBOT]
PING: {str(delta_ping_formatted).replace('.', ',')} ms
UBOT: {len(ubot._ubot)} user
UPTIME: {uptime}
OWNER:<b/> @Arabnihnge

<b>📊 [STATUS SERVER]
CPU: {cpu}%
RAM: {mem}%
DISK: {disk}%
MEMORY: {round(process.memory_info()[0] / 1024 ** 2)} MB</b>
"""
    await message.reply(_ping, reply_markup=InlineKeyboardMarkup(buttons))


@PY.CALLBACK("kontol")
async def _(client, callback_query):
    await callback_query.answer("ʀᴇғʀᴇsʜɪɴɢ...")
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    end = datetime.now()
    delta_ping = (end - start).microseconds / 1000
    delta_ping_formatted = round(delta_ping, 3)
    uptime = await get_time((time() - start_time))
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    _ping = f"""
<b>🖥️ [SYSTEM UBOT]
PING: {str(delta_ping_formatted).replace('.', ',')} ms
UBOT: {len(ubot._ubot)} user
UPTIME: {uptime}
OWNER:</b> @Arabnihnge

<b>📊 [STATUS SERVER]
CPU: {cpu}%
RAM: {mem}%
DISK: {disk}%
MEMORY: {round(process.memory_info()[0] / 1024 ** 2)} MB</b>
"""
    buttons = [[InlineKeyboardButton("ʀᴇғʀᴇsʜ", callback_data="kontol")]]
    try:
        await callback_query.message.edit(_ping, reply_markup=InlineKeyboardMarkup(buttons))
    except:
        return
