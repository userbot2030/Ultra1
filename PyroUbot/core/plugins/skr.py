import asyncio
import os
import random

import cv2
from PIL import Image
from pyrogram.errors import *
from pyrogram.raw.functions.messages import *
from pyrogram.raw.types import *

from PyroUbot import *
from PyroUbot.core.plugins import *


async def memes_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply("<code>memes</code> [ᴛᴇxᴛ]")
    text = f"#{random.randrange(67)} {message.text.split(None, 1)[1]}"
    TM = await message.reply("<code>ᴍᴇᴍᴘʀᴏsᴇs</code>")
    x = await client.get_inline_bot_results("StickerizerBot", text)
    saved = await client.send_inline_bot_result(
        client.me.id, x.query_id, x.results[0].id
    )
    saved = await client.get_messages(client.me.id, int(saved.updates[1].message.id))
    await client.send_sticker(
        message.chat.id, saved.sticker.file_id, reply_to_message_id=message.id
    )
    await saved.delete()
    await TM.delete()


async def tiny_cmd(client, message):
    reply = message.reply_to_message
    if not (reply and (reply.media)):
        return await message.reply("sɪʟᴀʜᴋᴀɴ ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ sᴛɪᴄᴋᴇʀ!")
    Tm = await message.reply("ᴘʀᴏᴄᴇssɪɴɢ...")
    ik = await client.download_media(reply)
    im1 = Image.open("storage/TM_BLACK.png")
    if ik.endswith(".tgs"):
        await client.download_media(reply, "Tm.tgs")
        await bash("lottie_convert.py man.tgs json.json")
        json = open("json.json", "r")
        jsn = json.read()
        jsn = jsn.replace("512", "2000")
        ("json.json", "w").write(jsn)
        await bash("lottie_convert.py json.json Tm.tgs")
        file = "man.tgs"
        os.remove("json.json")
    elif ik.endswith((".gif", ".mp4")):
        iik = cv2.VideoCapture(ik)
        busy = iik.read()
        cv2.imwrite("i.png", busy)
        fil = "i.png"
        im = Image.open(fil)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove(fil)
        os.remove("k.png")
    else:
        im = Image.open(ik)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove("k.png")
    await asyncio.gather(
        Tm.delete(),
        client.send_sticker(
            message.chat.id,
            sticker=file,
            reply_to_message_id=message.id,
        ),
    )
    os.remove(file)
    os.remove(ik)


async def memify_cmd(client, message):
    if not message.reply_to_message:
        return await message.reply("ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ ꜰᴏᴛᴏ ᴀᴛᴀᴜ sᴛɪᴄᴋᴇʀ!")
    reply_message = message.reply_to_message
    if not reply_message.media:
        return await message.reply("ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ ꜰᴏᴛᴏ ᴀᴛᴀᴜ sᴛɪᴄᴋᴇʀ")
    file = await client.download_media(reply_message)
    Tm = await message.reply("ᴘʀᴏᴄᴇssɪɴɢ . . .")
    text = get_arg(message)
    if len(text) < 1:
        return await Tm.edit(f"ʜᴀʀᴀᴘ ᴋᴇᴛɪᴋ {PREFIX[0]}mmf ᴛᴇxᴛ")
    meme = await add_text_img(file, text)
    await asyncio.gather(
        Tm.delete(),
        client.send_sticker(
            message.chat.id,
            sticker=meme,
            reply_to_message_id=message.id,
        ),
    )
    os.remove(meme)
