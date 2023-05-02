import asyncio
import os
import random

import cv2
from PIL import Image
from pyrogram import emoji
from pyrogram.enums import ParseMode
from pyrogram.errors import StickersetInvalid
from pyrogram.raw.functions.messages import DeleteHistory, GetStickerSet
from pyrogram.raw.types import InputStickerSetShortName

from .. import *


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


async def quotly_cmd(client, message):
    if message.reply_to_message:
        await client.unblock_user("@QuotLyBot")
        sg_m = await message.reply_to_message.forward("@QuotLyBot")
    else:
        if len(message.command) < 2:
            return await message.reply("ᴍᴏʜᴏɴ ᴋᴇᴛɪᴋ sᴇsᴜᴀᴛᴜ ᴀᴛᴀᴜ ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ")
        else:
            await client.unblock_user("@QuotLyBot")
            sg_m = await client.send_message(
                "@QuotLyBot", message.text.split(None, 1)[1]
            )
    sg_i = await message.reply("<b>ᴍᴇᴍᴘʀᴏsᴇs</b>")
    await sg_m.delete()
    await asyncio.sleep(6)
    async for msg in client.get_chat_history("@QuotLyBot", limit=1):
        if msg.sticker:
            dl = await msg.download()
            await sg_i.delete()
            await message.reply_sticker(dl)
        elif msg.text:
            await sg_i.delete()
            await message.reply("ɢᴀɢᴀʟ ᴍᴇᴍʙᴜᴀᴛ ᴋᴜᴛɪᴘᴀɴ")
        user_info = await client.resolve_peer("@QuotLyBot")
        await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))


async def kang_cmd(client, message):
    await client.unblock_user("stickers")
    user = message.from_user
    replied = message.reply_to_message
    Tm = await message.reply("ʙᴏʟᴇʜ ᴊᴜɢᴀ ɴɪ sᴛɪᴄᴋᴇʀɴʏᴀ ᴄᴏʟᴏɴɢ ᴀʜʜ...")
    media_ = None
    emoji_ = None
    is_anim = False
    is_video = False
    resize = False
    ff_vid = False
    if replied and replied.media:
        if replied.photo:
            resize = True
        elif replied.document and "image" in replied.document.mime_type:
            resize = True
            replied.document.file_name
        elif replied.document and "tgsticker" in replied.document.mime_type:
            is_anim = True
            replied.document.file_name
        elif replied.document and "video" in replied.document.mime_type:
            resize = True
            is_video = True
            ff_vid = True
        elif replied.animation:
            resize = True
            is_video = True
            ff_vid = True
        elif replied.video:
            resize = True
            is_video = True
            ff_vid = True
        elif replied.sticker:
            if not replied.sticker.file_name:
                await Tm.edit("sᴛɪᴋᴇʀ ᴛɪᴅᴀᴋ ᴍᴇᴍɪʟɪᴋɪ ɴᴀᴍᴀ!")
                return
            emoji_ = replied.sticker.emoji
            is_anim = replied.sticker.is_animated
            is_video = replied.sticker.is_video
            if not (
                replied.sticker.file_name.endswith(".tgs")
                or replied.sticker.file_name.endswith(".webm")
            ):
                resize = True
                ff_vid = True
        else:
            await Tm.edit("ꜰɪʟᴇ ᴛɪᴅᴀᴋ ᴅɪᴅᴜᴋᴜɴɢ")
            return
        media_ = await client.download_media(replied, file_name="tomimusic/modules/")
    else:
        await Tm.edit("sɪʟᴀʜᴋᴀɴ ʀᴇᴘʟʏ ᴋᴇ ᴍᴇᴅɪᴀ ꜰᴏᴛᴏ/ɢɪꜰ/sᴛɪᴄᴋᴇʀ!")
        return
    if media_:
        args = get_arg(message)
        pack = 1
        if len(args) == 2:
            emoji_, pack = args
        elif len(args) == 1:
            if args[0].isnumeric():
                pack = int(args[0])
            else:
                emoji_ = args[0]

        if emoji_ and emoji_ not in (
            getattr(emoji, _) for _ in dir(emoji) if not _.startswith("_")
        ):
            emoji_ = None
        if not emoji_:
            emoji_ = "✨"

        u_name = f"{user.first_name} {user.last_name or ''}"
        packname = f"Sticker_u{user.id}_v{pack}"
        custom_packnick = f"{u_name} ᴋᴀɴɢ ᴘᴀᴄᴋ ᴠᴏʟ.{pack}"
        packnick = f"{custom_packnick}"
        cmd = "/newpack"
        if resize:
            media_ = await resize_media(media_, is_video, ff_vid)
        if is_anim:
            packname += "_animated"
            packnick += " (Animated)"
            cmd = "/newanimated"
        if is_video:
            packname += "_video"
            packnick += " (Video)"
            cmd = "/newvideo"
        exist = False
        while True:
            try:
                exist = await client.invoke(
                    GetStickerSet(
                        stickerset=InputStickerSetShortName(short_name=packname), hash=0
                    )
                )
            except StickersetInvalid:
                exist = False
                break
            limit = 50 if (is_video or is_anim) else 120
            if exist.set.count >= limit:
                pack += 1
                packname = f"a{user.id}_by_userge_{pack}"
                packnick = f"{custom_packnick} Vol.{pack}"
                if is_anim:
                    packname += f"_anim{pack}"
                    packnick += f" (Animated){pack}"
                if is_video:
                    packname += f"_video{pack}"
                    packnick += f" (Video){pack}"
                await Tm.edit(
                    f"ᴍᴇᴍʙᴜᴀᴛ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ ʙᴀʀᴜ {pack} ᴋᴀʀᴇɴᴀ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ sᴜᴅᴀʜ ᴘᴇɴᴜʜ"
                )
                continue
            break
        if exist is not False:
            await client.send_message("stickers", "/addsticker")
            await asyncio.sleep(2)
            await client.send_message("stickers", packname)
            await asyncio.sleep(2)
            limit = "50" if is_anim else "120"
            while limit in await get_response(message, client):
                pack += 1
                packname = f"a{user.id}_by_{user.username}_{pack}"
                packnick = f"{custom_packnick} vol.{pack}"
                if is_anim:
                    packname += "_anim"
                    packnick += " (Animated)"
                if is_video:
                    packname += "_video"
                    packnick += " (Video)"
                await Tm.edit(
                    "ᴍᴇᴍʙᴜᴀᴛ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ ʙᴀʀᴜ "
                    + str(pack)
                    + " ᴋᴀʀᴇɴᴀ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ sᴜᴅᴀʜ ᴘᴇɴᴜʜ"
                )
                await client.send_message("stickers", packname)
                await asyncio.sleep(2)
                if await get_response(message, client) == "Invalid pack selected.":
                    await client.send_message("stickers", cmd)
                    await asyncio.sleep(2)
                    await client.send_message("stickers", packnick)
                    await asyncio.sleep(2)
                    await client.send_document("stickers", media_)
                    await asyncio.sleep(2)
                    await client.send_message("Stickers", emoji_)
                    await asyncio.sleep(2)
                    await client.send_message("Stickers", "/publish")
                    await asyncio.sleep(2)
                    if is_anim:
                        await client.send_message(
                            "Stickers", f"<{packnick}>", parse_mode=ParseMode.MARKDOWN
                        )
                        await asyncio.sleep(2)
                    await client.send_message("Stickers", "/skip")
                    await asyncio.sleep(2)
                    await client.send_message("Stickers", packname)
                    await asyncio.sleep(2)
                    return await Tm.edit(
                        f"sᴛɪᴄᴋᴇʀ ʙᴇʀʜᴀsɪʟ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ!\n         <a href=https://t.me/addstickers/{packname}>🔥 ᴋʟɪᴋ ᴅɪsɪɴɪ 🔥</a>\nᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ sᴛɪᴄᴋᴇʀs"
                    )
            await client.send_document("stickers", media_)
            await asyncio.sleep(2)
            if (
                await get_response(message, client)
                == "Sorry, the file type is invalid."
            ):
                return await Tm.edit(
                    "ɢᴀɢᴀʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ sᴛɪᴄᴋᴇʀ, ɢᴜɴᴀᴋᴀɴ @stIckerS ʙᴏᴛ ᴜɴᴛᴜᴋ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ sᴛɪᴄᴋᴇʀ ᴀɴᴅᴀ."
                )
            await client.send_message("Stickers", emoji_)
            await asyncio.sleep(2)
            await client.send_message("Stickers", "/done")
        else:
            await Tm.edit("ᴍᴇᴍʙᴜᴀᴛ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ ʙᴀʀᴜ")
            await client.send_message("stickers", "/addsticker")
            await asyncio.sleep(2)
            await client.send_message("Stickers", packnick)
            await asyncio.sleep(2)
            await client.send_document("stickers", media_)
            await asyncio.sleep(2)
            if (
                await get_response(message, client)
                == "Sorry, the file type is invalid."
            ):
                return await Tm.edit(
                    "ɢᴀɢᴀʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ sᴛɪᴄᴋᴇʀ, ɢᴜɴᴀᴋᴀɴ @stIckerS ʙᴏᴛ ᴜɴᴛᴜᴋ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ sᴛɪᴄᴋᴇʀ ᴀɴᴅᴀ."
                )
            await client.send_message("Stickers", emoji_)
            await asyncio.sleep(2)
            await client.send_message("Stickers", "/publish")
            await asyncio.sleep(2)
            if is_anim:
                await client.send_message("Stickers", f"<{packnick}>")
                await asyncio.sleep(2)
            await client.send_message("Stickers", "/skip")
            await asyncio.sleep(2)
            await client.send_message("Stickers", packname)
            await asyncio.sleep(2)
        await Tm.edit(
            f"sᴛɪᴄᴋᴇʀ ʙᴇʀʜᴀsɪʟ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ!\n         <a href=https://t.me/addstickers/{packname}>🔥 ᴋʟɪᴋ ᴅɪsɪɴɪ 🔥</a>\nᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ sᴛɪᴄᴋᴇʀs"
        )
        await asyncio.sleep(2)
        if os.path.exists(str(media_)):
            os.remove(media_)
        user_info = await client.resolve_peer("@stickers")
        await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))


async def get_response(message, client):
    return [x async for x in client.get_chat_history("Stickers", limit=1)][0].text


async def tiny_cmd(client, message):
    reply = message.reply_to_message
    if not (reply and (reply.media)):
        return await message.reply("sɪʟᴀʜᴋᴀɴ ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ sᴛɪᴄᴋᴇʀ!")
    Tm = await message.reply("ᴘʀᴏᴄᴇssɪɴɢ...")
    ik = await client.download_media(reply)
    im1 = Image.open("PyroUbot/storage/TM_BLACK.png")
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
