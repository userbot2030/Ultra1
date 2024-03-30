import asyncio

from pyrogram.enums import ChatType
from pyrogram.types import ChatPermissions

from PyroUbot import *


__MODULE__ = "staff"
__HELP__ = """
<b>◖ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜱᴛᴀꜰꜰ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}kick</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴇɴᴅᴀɴɢ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ɢʀᴜᴘ 

  <b>❑ ᴄᴍᴅ:</b> <code>{0}ban</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙʟᴏᴋɪʀ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ɢʀᴜᴘ 

  <b>❑ ᴄᴍᴅ:</b> <code>{0}mute</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙɪsᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ɢʀᴜᴘ 

  <b>❑ ᴄᴍᴅ:</b> <code>{0}unmute</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟᴇᴘᴀs ᴘᴇᴍʙʟᴏᴋɪʀᴀɴ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ɢʀᴜᴘ 

  <b>❑ ᴄᴍᴅ:</b> <code>{0}unban</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟᴇᴘᴀs ᴘᴇᴍʙɪsᴜᴀɴ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ɢʀᴜᴘ

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}staff</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴀʜᴜɪ ᴅᴀꜰᴛᴀʀ sᴇᴍᴜᴀ ᴀᴅᴍɪɴ ᴅɪᴅᴀʟᴀᴍ ɢʀᴜᴘ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}invite</code> [ᴜsᴇʀɴᴀᴍᴇ] 
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜɴᴅᴀɴɢ ᴀɴɢɢᴏᴛᴀ ᴋᴇ ɢʀᴜᴘ ᴀɴᴅᴀ
"""



@PY.UBOT("kick", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def admin_kick(client, message):
    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "5438630285635757876"
    user_id, reason = await extract_user_and_reason(message)
    if not user_id:
        return await message.reply_text(f"<emoji id={gagal}>❎</emoji> sᴀʏᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴘᴇɴɢɢᴜɴᴀ ɪᴛᴜ.")
    if user_id == (await client.get_me()).id:
        return await message.reply_text("ᴀᴋᴜ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇɴᴇɴᴅᴀɴɢ ᴅɪʀɪᴋᴜ sᴇɴᴅɪʀɪ, ᴀᴋᴜ ʙɪsᴀ ᴘᴇʀɢɪ ᴊɪᴋᴀ ᴋᴀᴍᴜ ᴍᴀᴜ.")
    if user_id == OWNER_ID:
        return await message.reply_text(f"<emoji id={gagal}>❎</emoji> ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇɴᴇɴᴅᴀɴɢ ᴀɴɢɢᴏᴛᴀ ɪɴɪ")
    if user_id in (await list_admins(message)):
        return await message.reply_text("sᴀʏᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇɴᴇɴᴅᴀɴɢ ᴀᴅᴍɪɴ, ᴀɴᴅᴀ ᴛᴀʜᴜ ᴀᴛᴜʀᴀɴɴʏᴀ, sᴀʏᴀ ᴊᴜɢᴀ.")
    try:
        mention = (await client.get_users(user_id)).mention
    except Exception as error:
        await message.reply(error)
    alasan = await get_vars(client.me.id, "EMOJI_ALASAN") or "6114013639528682251"
    emoji_global = await get_vars(client.me.id, "EMOJI_GLOBAL") or "6111585093220830556"
    gban_user = await get_vars(client.me.id, "GBAN_USER") or "6172475875368373616"
    msg = f"<b><emoji id={emoji_global}>😎</emoji> ᴅɪᴛᴇɴᴅᴀɴɢ:</b> {mention}\n<b><emoji id={gban_user}>👑</emoji> ᴀᴅᴍɪɴ:</b> {message.from_user.mention}"
    if reason:
        msg += f"\n<b><emoji id={alasan}>💬</emoji> ᴀʟᴀsᴀɴ:</b> {reason}"
    try:
        await message.chat.ban_member(user_id)
        await message.reply(msg)
        await asyncio.sleep(1)
        await message.chat.unban_member(user_id)
    except Exception as error:
        await message.reply(error)



@PY.UBOT("ban", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def admin_ban(client, message):
    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "5438630285635757876"
    user_id, reason = await extract_user_and_reason(message)
    if not user_id:
        return await message.reply_text(f"<emoji id={gagal}>❎</emoji> sᴀʏᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪᴛᴜ.")
    if user_id == (await client.get_me()).id:
        return await message.reply_text("ᴀᴋᴜ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙᴀɴɴᴇᴅ ᴅɪʀɪᴋᴜ sᴇɴᴅɪʀɪ, ᴀᴋᴜ ʙɪsᴀ ᴘᴇʀɢɪ ᴊɪᴋᴀ ᴋᴀᴍᴜ ᴍᴀᴜ.")
    if user_id == OWNER_ID:
        return await message.reply_text(f"<emoji id={gagal}>❎</emoji> ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙᴀɴɴᴇᴅ ᴀɴɢɢᴏᴛᴀ ɪɴɪ")
    if user_id in (await list_admins(message)):
        return await message.reply_text("ᴀᴋᴜ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙᴀɴɴᴇᴅ ᴅɪʀɪᴋᴜ sᴇɴᴅɪʀɪ, ᴀᴋᴜ ʙɪsᴀ ᴘᴇʀɢɪ ᴊɪᴋᴀ ᴋᴀᴍᴜ ᴍᴀᴜ.")
    try:
        mention = (await client.get_users(user_id)).mention
    except Exception as error:
        await message.reply(error)
    alasan = await get_vars(client.me.id, "EMOJI_ALASAN") or "6114013639528682251"
    emoji_global = await get_vars(client.me.id, "EMOJI_GLOBAL") or "6111585093220830556"
    gban_user = await get_vars(client.me.id, "GBAN_USER") or "6172475875368373616"
    msg = f"<b><emoji id={emoji_global}>😎</emoji> ᴅɪʙᴀɴɴᴇᴅ:</b> {mention}\n<b><emoji id={gban_user}>👑</emoji> ᴀᴅᴍɪɴ:</b> {message.from_user.mention}"
    if reason:
        msg += f"\n<b><emoji id={alasan}>💬</emoji> ᴀʟᴀsᴀɴ:</b> {reason}"
    try:
        await message.chat.ban_member(user_id)
        await message.reply(msg)
    except Exception as error:
        await message.reply(error)



@PY.UBOT("mute", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def admin_mute(client, message):
    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "5438630285635757876"
    user_id, reason = await extract_user_and_reason(message)
    if not user_id:
        return await message.reply_text(f"<emoji id={gagal}>❎</emoji> sᴀʏᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪᴛᴜ.")
    if user_id == (await client.get_me()).id:
        return await message.reply_text("ᴀᴋᴜ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙɪsᴜᴋᴀɴ ᴅɪʀɪᴋᴜ sᴇɴᴅɪʀɪ, ᴀᴋᴜ ʙɪsᴀ ᴘᴇʀɢɪ ᴊɪᴋᴀ ᴋᴀᴍᴜ ᴍᴀᴜ.")
    if user_id == OWNER_ID:
        return await message.reply_text(f"<emoji id={gagal}>❎</emoji> ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙɪsᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪɴɪ")
    if user_id in (await list_admins(message)):
        return await message.reply_text("sᴀʏᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙɪsᴜᴋᴀɴ ᴀᴅᴍɪɴ, ᴀɴᴅᴀ ᴛᴀʜᴜ ᴀᴛᴜʀᴀɴɴʏᴀ, sᴀʏᴀ ᴊᴜɢᴀ.")
    try:
        mention = (await client.get_users(user_id)).mention
    except Exception as error:
        await message.reply(error)
    alasan = await get_vars(client.me.id, "EMOJI_ALASAN") or "6114013639528682251"
    emoji_global = await get_vars(client.me.id, "EMOJI_GLOBAL") or "6111585093220830556"
    gban_user = await get_vars(client.me.id, "GBAN_USER") or "6172475875368373616"
    msg = f"<b><emoji id={emoji_global}>😎</emoji> ᴍᴇᴍʙɪsᴜᴋᴀɴ:</b> {mention}\n<b><emoji id={gban_user}>⚠️</emoji> ᴀᴅᴍɪɴ:</b> {message.from_user.mention}"
    if reason:
        msg += f"\n<b><emoji id={alasan}>⛔️</emoji> ᴀʟᴀsᴀɴ:</b> {reason}"
    try:
        await message.chat.restrict_member(user_id, ChatPermissions())
        await message.reply(msg)
    except Exception as error:
        await message.reply(error)



@PY.UBOT("unmute", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def admin_unmute(client, message):
    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "5438630285635757876"
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply_text(f"<emoji id={gagal}>❎</emoji> sᴀʏᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪᴛᴜ.")
    try:
        sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "5787188704434982946"
        mention = (await client.get_users(user_id)).mention
    except Exception as error:
        await message.reply(error)
    try:
        await message.chat.unban_member(user_id)
        await message.reply(f"<b><emoji id={sukses}>✅</emoji> {mention} sᴜᴅᴀʜ ʙɪsᴀ ᴄʜᴀᴛ ʟᴀɢɪ</b>")
    except Exception as error:
        await message.reply(error)



@PY.UBOT("unban", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def admin_unban(client, message):
    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "5438630285635757876"
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply_text(f"<emoji id={gagal}>❎</emoji> sᴀʏᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪᴛᴜ.")
    try:
        sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "5787188704434982946"
        mention = (await client.get_users(user_id)).mention
    except Exception as error:
        await message.reply(error)
    try:
        await message.chat.unban_member(user_id)
        await message.reply(f"<b><emoji id={sukses}>✅</emoji> {mention} sᴜᴅᴀʜ ʙɪsᴀ ᴊᴏɪɴ ʟᴀɢɪ</b>")
    except Exception as error:
        await message.reply(error)



@PY.UBOT("gban", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def global_banned(client, message):
    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "5438630285635757876"
    proses = await get_vars(client.me.id, "EMOJI_PROSES") or "5960640164114993927"
    user_id, reason = await extract_user_and_reason(message)
    Tm = await message.reply(f"<b><emoji id={proses}>⏳</emoji> ᴍᴇᴍᴘʀᴏsᴇs. . .</b>")
    if not user_id:
        return await Tm.edit(f"<b><emoji id={gagal}>❎</emoji> ᴜsᴇʀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    done = 0
    failed = 0
    emoji_global = await get_vars(client.me.id, "EMOJI_GLOBAL") or "6111585093220830556"
    gban_user = await get_vars(client.me.id, "GBAN_USER") or "6172475875368373616"
    sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "5787188704434982946"
    text = "<b>{} ɢʟᴏʙᴀʟ {}</b>\n\n<b>{} ʙᴇʀʜᴀsɪʟ: {} ᴄʜᴀᴛ</b>\n<b>{} ɢᴀɢᴀʟ: {} ᴄʜᴀᴛ</b>\n<b>{} ᴜsᴇʀ: <a href='tg://user?id={}'>{} {}</a></b>"
    if reason:
        text += "\n<b>💬 ᴀʟᴀsᴀɴ:</b> {}"
    async for dialog in client.get_dialogs():
        chat_type = dialog.chat.type
        if chat_type in [
            ChatType.GROUP,
            ChatType.SUPERGROUP,
            ChatType.CHANNEL,
        ]:
            chat_id = dialog.chat.id
            if user.id == OWNER_ID:
                return await Tm.edit("ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ɢʙᴀɴ ᴅɪᴀ ᴋᴀʀᴇɴᴀ ᴅɪᴀ ᴘᴇᴍʙᴜᴀᴛ sᴀʏᴀ")
            elif not user.id == OWNER_ID:
                try:
                    await client.ban_chat_member(chat_id, user.id)
                    done += 1
                    await asyncio.sleep(0.1)
                except:
                    failed += 1
                    await asyncio.sleep(0.1)
    await Tm.delete()
    return await message.reply(text.format(f"<emoji id={emoji_global}>💬</emoji>", "ʙᴀɴɴᴇᴅ", f"<emoji id={sukses}>✅</emoji>", done, f"<emoji id={gagal}>❎</emoji>", failed, f"<emoji id={gban_user}>👤</emoji>", user.id, user.first_name, (user.last_name or ""), reason))



@PY.UBOT("ungban", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def global_unbanned(client, message):
    user_id = await extract_user(message)
    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "5438630285635757876"
    proses = await get_vars(client.me.id, "EMOJI_PROSES") or "5960640164114993927"
    Tm = await message.reply(f"<b><emoji id={proses}>⏳</emoji></b> ᴍᴇᴍᴘʀᴏsᴇs. . .</b>")
    if not user_id:
        return await Tm.edit(f"<b><emoji id={gagal}>❎</emoji> ᴜsᴇʀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    done = 0
    failed = 0
    emoji_global = await get_vars(client.me.id, "EMOJI_GLOBAL") or "6111585093220830556"
    gban_user = await get_vars(client.me.id, "GBAN_USER") or "6172475875368373616"
    sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "5787188704434982946"
    text = "<b>{} ɢʟᴏʙᴀʟ {}</b>\n\n<b>{} ʙᴇʀʜᴀsɪʟ: {} ᴄʜᴀᴛ</b>\n<b>{} ɢᴀɢᴀʟ: {} ᴄʜᴀᴛ</b>\n<b>{} ᴜsᴇʀ: <a href='tg://user?id={}'>{} {}</a></b>"
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
    return await message.reply(text.format(f"<emoji id={emoji_global}>💬</emoji>", "ᴜɴʙᴀɴɴᴇᴅ", f"<emoji id={sukses}>✅</emoji>", done, f"<emoji id={gagal}>❎</emoji>", failed, f"<emoji id={gban_user}>👤</emoji>", user.id, user.first_name, (user.last_name or "")))

