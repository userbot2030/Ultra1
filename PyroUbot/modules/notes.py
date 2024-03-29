from pyrogram.types import *

from PyroUbot import *

__MODULE__ = "notes"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ɴᴏᴛᴇs 』</b>

<b>ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}addnote</code>
   <i>menyimpan sebuah catatan</i>

<b>ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}get</code>
   <i>mendapatkan catatan yang di simpan</i>
 
<b>ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}delnote</code>
   <i>menghapus catatan yang di simpan</i>
 
<b>ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}listnote</code>
  <i>melihat daftar catatan yang di simpan</i>

<b>ꜰᴏʀᴍᴀᴛ: <code>| ɴᴀᴍᴀ ᴛᴏᴍʙᴏʟ - ᴜʀʟ/ᴄᴀʟʟʙᴀᴄᴋ |</code>
   <i>untuk membuat button pada catatan</i>
  
"""


def detect_url_links(text):
    link_pattern = (
        r"(?:https?://)?(?:www\.)?[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})+(?:[/?]\S+)?"
    )
    link_found = re.findall(link_pattern, text)
    return link_found


def detect_button_and_text(text):
    button_matches = re.findall(r"\| ([^|]+) - ([^|]+) \|", text)
    text_matches = (
        re.search(r"(.*?) \|", text, re.DOTALL).group(1) if "|" in text else text
    )
    return button_matches, text_matches


def create_inline_keyboard(text, user_id=False, is_back=False):
    keyboard = []
    button_matches, text_matches = detect_button_and_text(text)

    prev_button_data = None
    for button_text, button_data in button_matches:
        data = (
            button_data.split(";same")[0]
            if detect_url_links(button_data.split(";same")[0])
            else f"_gtnote {int(user_id.split('_')[0])}_{user_id.split('_')[1]} {button_data.split(';same')[0]}"
        )
        cb_data = data if user_id else button_data.split(";same")[0]
        if ";same" in button_data:
            if prev_button_data:
                if detect_url_links(cb_data):
                    keyboard[-1].append(InlineKeyboardButton(button_text, url=cb_data))
                else:
                    keyboard[-1].append(
                        InlineKeyboardButton(button_text, callback_data=cb_data)
                    )
            else:
                if detect_url_links(cb_data):
                    button_row = [InlineKeyboardButton(button_text, url=cb_data)]
                else:
                    button_row = [
                        InlineKeyboardButton(button_text, callback_data=cb_data)
                    ]
                keyboard.append(button_row)
        else:
            if button_data.startswith("http"):
                button_row = [InlineKeyboardButton(button_text, url=cb_data)]
            else:
                button_row = [InlineKeyboardButton(button_text, callback_data=cb_data)]
            keyboard.append(button_row)

        prev_button_data = button_data

    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)

    if user_id and is_back:
        markup.inline_keyboard.append(
            [
                InlineKeyboardButton(
                    "ᴋᴇᴍʙᴀʟɪ",
                    f"_gtnote {int(user_id.split('_')[0])}_{user_id.split('_')[1]}",
                )
            ]
        )

    return markup, text_matches


@PY.UBOT("addnote|addcb")
@PY.TOP_CMD
async def _(client, message):
    args = get_arg(message)
    reply = message.reply_to_message
    query = "notes_cb" if message.command[0] == "addcb" else "notes"

    if not args or not reply:
        return await message.reply(
            f"<code>{message.text.split()[0]}</code> <b>[ɴᴀᴍᴇ] [ᴛᴇxᴛ/ʀᴇᴘʟʏ]</b>"
        )

    vars = await get_vars(client.me.id, args, query)

    if vars:
        return await message.reply(f"<b>ᴄᴀᴛᴀᴛᴀɴ {args} ꜱᴜᴅᴀʜ ᴀᴅᴀ</n>")

    value = None
    type_mapping = {
        "text": reply.text,
        "photo": reply.photo,
        "voice": reply.voice,
        "audio": reply.audio,
        "video": reply.video,
        "animation": reply.animation,
        "sticker": reply.sticker,
    }

    for media_type, media in type_mapping.items():
        if media:
            send = await reply.copy(client.me.id)
            value = {
                "type": media_type,
                "message_id": send.id,
            }
            break

    if value:
        await set_vars(client.me.id, args, value, query)
        return await message.reply(
            f"<b>ᴄᴀᴛᴀᴛᴀɴ <code>{args}</code> ʙᴇʀʜᴀsɪʟ ᴛᴇʀsɪᴍᴘᴀɴ</b>"
        )
    else:
        return await message.reply(
            f"<code>{message.text.split()[0]}</code> <b>[ɴᴀᴍᴇ] [ᴛᴇxᴛ/ʀᴇᴘʟʏ]</b>"
        )


@PY.UBOT("delnote|delcb")
@PY.TOP_CMD
async def _(client, message):
    args = get_arg(message)

    if not args:
        return await message.reply(
            f"<code>{message.text.split()[0]}</code> <b>[ɴᴀᴍᴇ]</b>"
        )

    query = "notes_cb" if message.command[0] == "delcb" else "notes"
    vars = await get_vars(client.me.id, args, query)

    if not vars:
        return await message.reply(f"<b>ᴄᴀᴛᴀᴛᴀɴ {args} ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>")

    await remove_vars(client.me.id, args, query)
    await client.delete_messages(client.me.id, int(vars["message_id"]))
    return await message.reply(f"<b>ᴄᴀᴛᴀɴ {args} ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs</b>")


@PY.UBOT("get")
@PY.TOP_CMD
async def _(client, message):
    msg = message.reply_to_message or message
    args = get_arg(message)

    if not args:
        return await message.reply(
            f"<code>{message.text.split()[0]}</code> <b>[ɴᴀᴍᴇ]</b>"
        )

    data = await get_vars(client.me.id, args, "notes")

    if not data:
        return await message.reply(
            f"<b>ᴄᴀᴛᴀᴛᴀɴ {args} ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>"
        )

    m = await client.get_messages(client.me.id, int(data["message_id"]))

    if data["type"] == "text":
        if matches := re.findall(r"\| ([^|]+) - ([^|]+) \|", m.text):
            try:
                x = await client.get_inline_bot_results(
                    bot.me.username, f"get_notes {client.me.id} {args}"
                )
                return await client.send_inline_bot_result(
                    message.chat.id,
                    x.query_id,
                    x.results[0].id,
                    reply_to_message_id=msg.id,
                )
            except Exception as error:
                await message.reply(error)
        else:
            return await m.copy(message.chat.id, reply_to_message_id=msg.id)
    else:
        return await m.copy(message.chat.id, reply_to_message_id=msg.id)


@PY.UBOT("listnote|listcb")
@PY.TOP_CMD
async def _(client, message):
    query = "notes_cb" if message.command[0] == "listcb" else "notes"
    vars = await all_vars(client.me.id, query)
    if vars:
        msg = "<b>❏ ᴅᴀғᴛᴀʀ ᴄᴀᴛᴀᴛᴀɴ</b>\n\n"
        for x, data in vars.items():
            msg += f" {x} |({data['type']})\n"
        msg += f"<b>\n❏ ᴛᴏᴛᴀʟ ᴄᴀᴛᴀᴛᴀɴ: {len(vars)}</b>"
    else:
        msg = "<b>ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴄᴀᴛᴀᴛᴀɴ</b>"

    return await message.reply(msg, quote=True)


@PY.INLINE("^get_notes")
async def _(client, inline_query):
    query = inline_query.query.split()
    data = await get_vars(int(query[1]), query[2], "notes")
    item = [x for x in ubot._ubot if int(query[1]) == x.me.id]
    for me in item:
        m = await me.get_messages(int(me.me.id), int(data["message_id"]))
        buttons, text = create_inline_keyboard(m.text, f"{int(query[1])}_{query[2]}")
        return await client.answer_inline_query(
            inline_query.id,
            cache_time=0,
            results=[
                (
                    InlineQueryResultArticle(
                        title="get notes!",
                        reply_markup=buttons,
                        input_message_content=InputTextMessageContent(text),
                    )
                )
            ],
        )


@PY.CALLBACK("_gtnote")
async def _(client, callback_query):
    _, user_id, *query = callback_query.data.split()
    data_key = "notes_cb" if bool(query) else "notes"
    query_eplit = query[0] if bool(query) else user_id.split("_")[1]
    data = await get_vars(int(user_id.split("_")[0]), query_eplit, data_key)
    item = [x for x in ubot._ubot if int(user_id.split("_")[0]) == x.me.id]
    for me in item:
        m = await me.get_messages(int(me.me.id), int(data["message_id"]))
        buttons, text = create_inline_keyboard(
            m.text, f"{int(user_id.split('_')[0])}_{user_id.split('_')[1]}", bool(query)
        )
        return await callback_query.edit_message_text(text, reply_markup=buttons)
