import asyncio

from pyrogram.enums import ChatType
from pyrogram.types import ChatPermissions

from PyroUbot import *
from PyroUbot.core.database import *
from PyroUbot.core.function import *
from PyroUbot.core.helpers import *


async def admin_bannen(client, message):
    if message.command[0] == "kick":
        user_id, reason = await extract_user_and_reason(message)
        if not user_id:
            return await message.reply_text("sᴀʏᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴘᴇɴɢɢᴜɴᴀ ɪᴛᴜ.")
        if user_id == (await client.get_me()).id:
            return await message.reply_text(
                "ᴀᴋᴜ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇɴᴇɴᴅᴀɴɢ ᴅɪʀɪᴋᴜ sᴇɴᴅɪʀɪ, ᴀᴋᴜ ʙɪsᴀ ᴘᴇʀɢɪ ᴊɪᴋᴀ ᴋᴀᴍᴜ ᴍᴀᴜ."
            )
        if user_id == OWNER_ID:
            return await message.reply_text("ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇɴᴇɴᴅᴀɴɢ ᴀɴɢɢᴏᴛᴀ ɪɴɪ")
        if user_id in (await list_admins(message)):
            return await message.reply_text(
                "sᴀʏᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇɴᴇɴᴅᴀɴɢ ᴀᴅᴍɪɴ, ᴀɴᴅᴀ ᴛᴀʜᴜ ᴀᴛᴜʀᴀɴɴʏᴀ, sᴀʏᴀ ᴊᴜɢᴀ."
            )
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await message.reply(error)
        msg = f"<b>👤 ᴅɪᴛᴇɴᴅᴀɴɢ:</b> {mention}\n<b>👑 ᴀᴅᴍɪɴ:</b> {message.from_user.mention}"
        if reason:
            msg += f"\n<b>💬 ᴀʟᴀsᴀɴ:</b> {reason}"
        try:
            await message.chat.ban_member(user_id)
            await message.reply(msg)
            await asyncio.sleep(1)
            await message.chat.unban_member(user_id)
        except Exception as error:
            await message.reply(error)
    elif message.command[0] == "ban":
        user_id, reason = await extract_user_and_reason(message)
        if not user_id:
            return await message.reply_text("sᴀʏᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪᴛᴜ.")
        if user_id == (await client.get_me()).id:
            return await message.reply_text(
                "ᴀᴋᴜ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙᴀɴɴᴇᴅ ᴅɪʀɪᴋᴜ sᴇɴᴅɪʀɪ, ᴀᴋᴜ ʙɪsᴀ ᴘᴇʀɢɪ ᴊɪᴋᴀ ᴋᴀᴍᴜ ᴍᴀᴜ."
            )
        if user_id == OWNER_ID:
            return await message.reply_text("ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙᴀɴɴᴇᴅ ᴀɴɢɢᴏᴛᴀ ɪɴɪ")
        if user_id in (await list_admins(message)):
            return await message.reply_text(
                "ᴀᴋᴜ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙᴀɴɴᴇᴅ ᴅɪʀɪᴋᴜ sᴇɴᴅɪʀɪ, ᴀᴋᴜ ʙɪsᴀ ᴘᴇʀɢɪ ᴊɪᴋᴀ ᴋᴀᴍᴜ ᴍᴀᴜ."
            )
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await message.reply(error)
        msg = (
            f"<b>👤 ᴅɪʙᴀɴɴᴇᴅ:</b> {mention}\n<b>👑 ᴀᴅᴍɪɴ:</b> {message.from_user.mention}"
        )
        if reason:
            msg += f"\n<b>💬 ᴀʟᴀsᴀɴ:</b> {reason}"
        try:
            await message.chat.ban_member(user_id)
            await message.reply(msg)
        except Exception as error:
            await message.reply(error)
    elif message.command[0] == "mute":
        user_id, reason = await extract_user_and_reason(message)
        if not user_id:
            return await message.reply_text("sᴀʏᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪᴛᴜ.")
        if user_id == (await client.get_me()).id:
            return await message.reply_text(
                "ᴀᴋᴜ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙɪsᴜᴋᴀɴ ᴅɪʀɪᴋᴜ sᴇɴᴅɪʀɪ, ᴀᴋᴜ ʙɪsᴀ ᴘᴇʀɢɪ ᴊɪᴋᴀ ᴋᴀᴍᴜ ᴍᴀᴜ."
            )
        if user_id == OWNER_ID:
            return await message.reply_text("ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙɪsᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪɴɪ")
        if user_id in (await list_admins(message)):
            return await message.reply_text(
                "sᴀʏᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙɪsᴜᴋᴀɴ ᴀᴅᴍɪɴ, ᴀɴᴅᴀ ᴛᴀʜᴜ ᴀᴛᴜʀᴀɴɴʏᴀ, sᴀʏᴀ ᴊᴜɢᴀ."
            )
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await message.reply(error)
        msg = f"<b>👤 ᴍᴇᴍʙɪsᴜᴋᴀɴ:</b> {mention}\n<b>👑 ᴀᴅᴍɪɴ:</b> {message.from_user.mention}"
        if reason:
            msg += f"\n<b>💬 ᴀʟᴀsᴀɴ:</b> {reason}"
        try:
            await message.chat.restrict_member(user_id, ChatPermissions())
            await message.reply(msg)
        except Exception as error:
            await message.reply(error)
    elif message.command[0] == "unmute":
        user_id = await extract_user(message)
        if not user_id:
            return await message.reply_text("sᴀʏᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪᴛᴜ.")
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await message.reply(error)
        try:
            await message.chat.unban_member(user_id)
            await message.reply(f"<b>✅ {mention} sᴜᴅᴀʜ ʙɪsᴀ ᴄʜᴀᴛ ʟᴀɢɪ</b>")
        except Exception as error:
            await message.reply(error)
    elif message.command[0] == "unban":
        user_id = await extract_user(message)
        if not user_id:
            return await message.reply_text("sᴀʏᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪᴛᴜ.")
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await message.reply(error)
        try:
            await message.chat.unban_member(user_id)
            await message.reply(f"<b>✅ {mention} sᴜᴅᴀʜ ᴊᴏɪɴ ʟᴀɢɪ</b>")
        except Exception as error:
            await message.reply(error)


async def global_banned(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("</b>ᴍᴇᴍᴘʀᴏsᴇs. . .</b>")
    if not user_id:
        return await Tm.edit("<b>ᴜsᴇʀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    done = 0
    failed = 0
    text = "<b>💬 ɢʟᴏʙᴀʟ {}</b>\n\n<b>✅ ʙᴇʀʜᴀsɪʟ: {} ᴄʜᴀᴛ</b>\n<b>❌ ɢᴀɢᴀʟ: {} ᴄʜᴀᴛ</b>\n<b>👤 ᴜsᴇʀ: <a href='tg://user?id={}'>{} {}</a></b>"
    if message.command[0] == "gban":
        async for dialog in client.get_dialogs():
            chat_type = dialog.chat.type
            if chat_type in [
                ChatType.GROUP,
                ChatType.SUPERGROUP,
                ChatType.CHANNEL,
            ]:
                chat_id = dialog.chat.id
                if user.id == OWNER_ID:
                    return await Tm.edit(
                        "ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ɢʙᴀɴ ᴅɪᴀ ᴋᴀʀᴇɴᴀ ᴅɪᴀ ᴘᴇᴍʙᴜᴀᴛ sᴀʏᴀ"
                    )
                elif not user.id == OWNER_ID:
                    try:
                        await client.ban_chat_member(chat_id, user.id)
                        done += 1
                        await asyncio.sleep(0.1)
                    except:
                        failed += 1
                        await asyncio.sleep(0.1)
        await Tm.delete()
        return await message.reply(
            text.format(
                "ʙᴀɴɴᴇᴅ", done, failed, user.id, user.first_name, (user.last_name or "")
            )
        )
    elif message.command[0] == "ungban":
        async for dialog in client.get_dialogs():
            chat_type = dialog.chat.type
            if chat_type in [
                ChatType.GROUP,
                ChatType.SUPERGROUP,
                ChatType.CHANNEL,
            ]:
                chat_id = dialog.chat.id
                try:
                    await client.unban_chat_member(chat_id, user.id)
                    done += 1
                    await asyncio.sleep(0.1)
                except:
                    failed += 1
                    await asyncio.sleep(0.1)
        await Tm.delete()
        return await message.reply(
            text.format(
                "ᴜɴʙᴀɴɴᴇᴅ",
                done,
                failed,
                user.id,
                user.first_name,
                (user.last_name or ""),
            )
        )
