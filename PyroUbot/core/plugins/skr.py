import asyncio
import imghdr
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


async def kang_cmd_bot(client, message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a sticker/image to kang it.")
    if not message.from_user:
        return await message.reply_text(
            "You are an anonymous admin, kang stickers in my PM."
        )
    msg = await message.reply_text("Kanging Sticker..")
    args = message.text.split()
    if len(args) > 1:
        sticker_emoji = str(args[1])
    elif message.reply_to_message.sticker and message.reply_to_message.sticker.emoji:
        sticker_emoji = message.reply_to_message.sticker.emoji
    else:
        sticker_emoji = "✨"
    doc = message.reply_to_message.photo or message.reply_to_message.document
    try:
        if message.reply_to_message.sticker:
            sticker = await create_sticker(
                await get_document_from_file_id(
                    message.reply_to_message.sticker.file_id
                ),
                sticker_emoji,
            )
        elif doc:
            if doc.file_size > 10000000:
                return await msg.edit("Ukuran file terlalu besar.")
            temp_file_path = await client.download_media(doc)
            image_type = imghdr.what(temp_file_path)
            if image_type not in ["jpeg", "png", "webp"]:
                return await msg.edit("Format tidak didukung! ({})".format(image_type))
            try:
                temp_file_path = await resize_file_to_sticker_size(temp_file_path)
            except Exception as e:
                return await msg.edit_text(str(e))
            sticker = await create_sticker(
                await upload_document(client, temp_file_path, message.chat.id),
                sticker_emoji,
            )
            if os.path.isfile(temp_file_path):
                os.remove(temp_file_path)
        else:
            return await msg.edit("Tidak, tidak bisa kang itu.")
    except ShortnameOccupyFailed as SDF:
        return await message.reply(str(SDF))
    except Exception as e:
        return await message.reply(str(e))
    packname = f"stkr_{str(message.from_user.id)}_by_{bot.me.username}"
    limit = 0
    packnum = 0
    try:
        if limit >= 50:
            return await msg.delete()
        stickerset = await get_sticker_set_by_name(client, packname)
        if not stickerset:
            stickerset = await create_sticker_set(
                client,
                message.from_user.id,
                gen_font(
                    f"{message.from_user.first_name} {message.from_user.last_name or ''} kang pack",
                    font["sᴍᴀʟʟᴄᴀᴘs"],
                ),
                packname,
                [sticker],
            )
        elif stickerset.set.count >= 120:
            packnum += 1
            packname = f"stk{packnum}in{message.from_user.id}by{client.me.username}"
            limit += 1
        else:
            try:
                await add_sticker_to_set(client, stickerset, sticker)
            except StickerEmojiInvalid:
                return await msg.edit("[ERROR]: INVALID_EMOJI_IN_ARGUMENT")
        limit += 1
        await msg.edit(
            f"""
<b>sᴛɪᴄᴋᴇʀ ʙᴇʀʜᴀsɪʟ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ!
    <a href=https://t.me/addstickers/{packname}>🔥 ᴋʟɪᴋ ᴅɪsɪɴɪ 🔥</a>
    ᴇᴍᴏᴊɪ: {sticker_emoji}
ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ sᴛɪᴄᴋᴇʀs</b>
"""
        )
    except StickerPngNopng as SPN:
        await message.reply(str(SPN))
    except StickerPngDimensions as SPD:
        await message.reply(str(SPD))
    except Exception as error:
        await message.reply(str(error))


async def get_response(client, message):
    async for data in client.search_messages(bot.me.username, limit=1):
        results = data
    return results


async def delete_results(msg, copy_send, reply_copy_send, results):
    for trash in (msg, copy_send, reply_copy_send, results):
        await trash.delete()


async def kang_cmd(client, message):
    reply = message.reply_to_message
    msg = await message.reply("<b>sɪʟᴀʜᴋᴀɴ ᴛᴜɴɢɢᴜ</b>")
    if message.reply_to_message:
        if reply.sticker or reply.photo:
            await client.unblock_user(bot.me.username)
            copy_send = await reply.copy(bot.me.username)
            reply_copy_send = await copy_send.reply("/kang")
            await asyncio.sleep(2)
            results = await get_response(client, message)
            await results.copy(message.chat.id)
            return await delete_results(msg, copy_send, reply_copy_send, results)
        else:
            return await msg.edit("<b>ʜᴀʀᴀᴘ ʀᴇᴘʟʏ ᴋᴇ ᴘʜᴏᴛᴏ/sᴛɪᴄᴋᴇʀ</b>")
    else:
        return await msg.edit("<b>ʜᴀʀᴀᴘ ʀᴇᴘʟʏ ᴋᴇ ᴘʜᴏᴛᴏ/sᴛɪᴄᴋᴇʀ</b>")
