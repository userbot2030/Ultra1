
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
