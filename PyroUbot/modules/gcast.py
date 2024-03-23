from PyroUbot import *

__MODULE__ = "gcast"
__HELP__ = """
<b>◖ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢᴄᴀsᴛ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}ucast</code> [ᴛᴇxᴛ/ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ/ᴍᴇᴅɪᴀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ sᴇᴍᴜᴀ ᴜsᴇʀ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}gcast</code> [ᴛᴇxᴛ/ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ/ᴍᴇᴅɪᴀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ sᴇᴍᴜᴀ ɢʀᴏᴜᴘ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}send</code> [ᴜsᴇʀɪᴅ/ᴜsᴇʀɴᴀᴍᴇ - ᴛᴇxᴛ/ʀᴇᴘʟʏ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ ᴜsᴇʀ/ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟd
  
  <b>❑ ᴄᴍᴅ:</b> <code>{0}auto_gcast</code> (ǫᴜᴇʀʏ) - (ᴠᴀʟᴜᴇ)
      <b>❑> ǫᴜᴇʀʏ & ᴠᴀʟᴜᴇ:</b>
      <b>├➠ ON/OFF:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴅᴀɴ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ɢᴄᴀsᴛ ᴏᴛᴏᴍᴀᴛɪs
      <b>├➠ TEXT - ᴋᴀᴛᴀ-ᴋᴀᴛᴀ/ʀᴇᴘʟʏ_ᴛᴇxᴛ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴛᴇxᴛ ᴋᴇ ᴅᴀᴛᴀʙᴀsᴇ ɢᴄᴀsᴛ ᴏᴛᴏᴍᴀᴛɪs
      <b>├➠ DELAY - ᴀɴɢᴋᴀ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴅᴜʀᴀsɪ ᴅᴇʟᴀʏ ᴘᴀᴅᴀ sᴇᴛɪᴀᴘ ᴘᴜᴛᴀʀᴀɴ ɢᴄᴀsᴛ ᴏᴛᴏᴍᴀᴛɪs
      <b>╰➠ LIMIT - ON/OFF:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴅᴀɴ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ғᴜɴɢsɪ ᴄsᴋ ʟɪᴍɪᴛ ᴏᴛᴏᴍᴀᴛɪs sᴇᴛɪᴀᴘ 𝟷𝟻 ᴍᴇɴɪᴛ
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍᴋᴀɴ ᴘᴇsᴀɴ ɢᴄᴀsᴛ sᴇᴄᴀʀᴀ ᴏᴛᴏᴍᴀᴛɪs
"""


@PY.UBOT("bc")
@PY.TOP_CMD
async def _(client, message):
    _msg = f"<b>ᴍᴇᴍᴘʀᴏsᴇs...</b>"
    gcs = await message.reply(_msg)

    command, text = extract_type_and_msg(message)

    if command not in ["group", "users", "all"] or not text:
        return await gcs.edit(f"<code>{message.text.split()[0]}</code> <b>[ᴛʏᴘᴇ] [ᴛᴇxᴛ/ʀᴇᴘʟʏ]</b>")

    chats = await get_data_id(client, command)
    blacklist = await get_list_from_vars(client.me.id, "BL_ID")

    done = 0
    failed = 0
    for chat_id in chats:
        if chat_id in blacklist or chat_id in BLACKLIST_CHAT:
            continue

        try:
            await (text.copy(chat_id) if message.reply_to_message else client.send_message(chat_id, text))
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await (text.copy(chat_id) if message.reply_to_message else client.send_message(chat_id, text))
            done += 1
        except Exception:
            failed += 1
            pass

    await gcs.delete()
    _gcs = f"""
<b>ʙʀᴏᴀᴅᴄᴀsᴛ ᴛᴇʀᴋɪʀɪᴍ</b>
<b>ʙᴇʀʜᴀsɪʟ: {done} ɢʀᴏᴜᴘ</b>
<b>ɢᴀɢᴀʟ: {failed} ɢʀᴏᴜᴘ</b>
"""
    return await message.reply(_gcs)


@PY.UBOT("ucast")
@PY.TOP_CMD
async def _(client, message):
    await broadcast_users_cmd(client, message)


@PY.BOT("send")
@PY.UBOT("send")
@PY.TOP_CMD
async def _(client, message):
    await send_msg_cmd(client, message)


@PY.INLINE("^get_send")
@INLINE.QUERY
async def _(client, inline_query):
    await send_inline(client, inline_query)


AG = []
LT = []


@PY.UBOT("auto_gcast")
@PY.TOP_CMD
async def _(client, message):
    """
    CREATE BY: NORSODIKIN.T.ME
    REQUEST BY DHILNIHNGE.T.ME:
    """
    msg = await message.reply("<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>", quote=True)
    type, value = extract_type_and_text(message)
    auto_text_vars = await get_vars(client.me.id, "AUTO_TEXT")

    if type == "on":
        if not auto_text_vars:
            return await msg.edit("<b>ʜᴀʀᴀᴘ sᴇᴛᴛɪɴɢ ᴛᴇxᴛ ɢᴄᴀsᴛ ᴀɴᴅᴀ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ</b>")

        if client.me.id not in AG:
            await msg.edit("<b>ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴅɪᴀᴋᴛɪғᴋᴀɴ</b>")

            AG.append(client.me.id)

            done = 0
            while client.me.id in AG:
                delay = await get_vars(client.me.id, "DELAY_GCAST") or 1
                blacklist = await get_chat(client.me.id)
                txt = random.choice(auto_text_vars)

                group = 0
                async for dialog in client.get_dialogs():
                    if dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP) and dialog.chat.id not in blacklist:
                        try:
                            await asyncio.sleep(1)
                            await client.send_message(dialog.chat.id, f"{txt} {random.choice(range(999))}")
                            group += 1
                        except FloodWait as e:
                            await asyncio.sleep(e.value)
                            await client.send_message(dialog.chat.id, f"{txt} {random.choice(range(999))}")
                            group += 1
                        except Exception:
                            pass

                if client.me.id not in AG:
                    return

                done += 1
                await msg.reply(
                    f"<b>ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴘᴜᴛᴀʀᴀɴ {done} ʙᴇʀʜᴀsɪʟ ᴅᴀɴ ᴛᴇʀᴋɪʀɪᴍ ᴋᴇ: {group} ɢʀᴏᴜᴘ\n\nᴍᴇɴᴜɴɢɢᴜ {delay} ᴍᴇɴɪᴛ ʟᴀɢɪ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʟᴀɴɢ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ</b>",
                    quote=True,
                )
                await asyncio.sleep(int(60 * int(delay)))
        else:
            return await msg.delete()

    elif type == "off":
        if client.me.id in AG:
            AG.remove(client.me.id)
            return await msg.edit("<b>ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴛᴇʟᴀʜ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ</b>")
        else:
            return await msg.delete()

    elif type == "text":
        if not value:
            return await msg.edit("<b>ʜᴀʀᴀᴘ ᴍᴀsᴜᴋᴋᴀɴ ᴛᴇxᴛ ᴜɴᴛᴜᴋ ᴅɪ sɪᴍᴘᴀɴ sᴇʙᴀɢᴀɪ ᴛᴇxᴛ ᴀᴜᴛᴏ ɢᴄᴀsᴛ</b>")
        await add_auto_text(client, value)
        return await msg.edit("<b>ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴛᴇxᴛ: ʙᴇʀʜᴀsɪʟ ᴅɪ sɪᴍᴘᴀɴ</b>")

    elif type == "delay":
        await set_vars(client.me.id, "DELAY_GCAST", value)
        return await msg.edit(f"<b>ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴅᴇʟᴀʏ: ʙᴀʀʜᴀsɪʟ ᴋᴇ sᴇᴛᴛɪɴɢ {value} ᴍᴇɴɪᴛ</b>")

    elif type == "remove":
        if not value:
            return await msg.edit("<b>ʜᴀʀᴀᴘ ᴍᴀsᴜᴋᴋᴀɴ ᴀɴɢᴋᴀ ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ʟɪsᴛ ᴛᴇxᴛ</b>")
        if value == "all":
            await set_vars(client.me.id, "AUTO_TEXT", [])
            return await msg.edit("<b>sᴇᴍᴜᴀ ᴛᴇxᴛ ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs</b>")
        try:
            value = int(value) - 1
            auto_text_vars.pop(value)
            await set_vars(client.me.id, "AUTO_TEXT", auto_text_vars)
            return await msg.edit(f"<b>ᴀᴜᴛᴏ ɢᴄᴀsᴛ ʀᴇᴍᴏᴠᴇ: ᴛᴇxᴛ ᴋᴇ {value+1} ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs\n\nsɪʟᴀʜᴋᴀɴ ᴋᴇᴛɪᴋ: <code>{message.text.split()[0]} list</code>, ᴋᴇᴍʙᴀʟɪ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴄᴇᴋ ᴀᴘᴀᴋᴀʜ sᴜᴅᴀʜ ᴛᴇʀʜᴀᴘᴜs</b>")
        except Exception as error:
            return await msg.edit(str(error))

    elif type == "list":
        if not auto_text_vars:
            return await msg.edit("<b>ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴛᴇxᴛ ᴋᴏsᴏɴɢ</b>")
        txt = "<b>ᴅᴀғᴛᴀʀ ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴛᴇxᴛ</b>\n\n"
        for num, x in enumerate(auto_text_vars, 1):
            txt += f"{num}: {x}\n\n"
        txt += f"<b>\nᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ᴛᴇxᴛ ᴋᴇᴛɪᴋ: <code>{message.text.split()[0]} remove ᴀɴɢᴋᴀ/ᴀʟʟ</code></b>"
        return await msg.edit(txt)

    elif type == "limit":
        if value == "off":
            if client.me.id in LT:
                LT.remove(client.me.id)
                return await msg.edit("<b>ᴀᴜᴛᴏ ᴄᴇᴋ ʟɪᴍɪᴛ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ</b>")
            else:
                return await msg.delete()

        elif value == "on":
            if client.me.id not in LT:
                LT.append(client.me.id)
                await msg.edit("<b>ᴀᴜᴛᴏ ᴄᴇᴋ ʟɪᴍɪᴛ sᴛᴀʀᴛᴇᴅ</b>")
                while client.me.id in LT:
                    for x in range(2):
                        await limit_cmd(client, message)
                        await asyncio.sleep(5)
                    await asyncio.sleep(1200)
            else:
                return await msg.delete()
        else:
            return await msg.edit("<b>~ʜᴀʀᴀᴘ ᴍᴀsᴜᴋᴋᴀɴ ᴠᴀʟᴇᴜ ᴏɴ/ᴏғғ ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ</b>")
    else:
        return await msg.edit("<b>ǫᴜᴇʀʏ ʏᴀɴɢ ᴅɪᴍᴀsᴜᴋᴋᴀɴ sᴀʟᴀʜ</b>")


async def add_auto_text(client, text):
    auto_text = await get_vars(client.me.id, "AUTO_TEXT") or []
    auto_text.append(text)
    await set_vars(client.me.id, "AUTO_TEXT", auto_text)


def extract_type_and_text(message):
    args = message.text.split(None, 2)
    if len(args) < 2:
        return None, None

    type = args[1]
    msg = message.reply_to_message.text if message.reply_to_message else args[2] if len(args) > 2 else None
    return type, msg
