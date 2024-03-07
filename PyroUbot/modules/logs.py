"create by: NorSodikin.t.me"
"request by: dhilnihnge.t.me"

import wget

from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                            InlineQueryResultArticle, InputTextMessageContent)


from PyroUbot import *

__MODULE__ = "logs"
__HELP__ = """
<b>◖ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʟᴏɢs◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}logs</code> (on/off)
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴀᴛᴀᴜ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ᴄʜᴀɴɴᴇʟ ʟᴏɢs
"""


TEXT = {}


async def send_log(client, chat_id, message, message_text, message_link, msg):
    TEXT[int(client.me.id)] = {"user": message_link, "msg": message_text}
    try:
        x = await client.get_inline_bot_results(
            bot.me.username, f"logs_inline {client.me.id}_{message.chat.id}_{message.id}"
        )
        await client.send_inline_bot_result(
            chat_id,
            x.query_id,
            x.results[0].id,
        )
        return await message.forward(chat_id)
    except Exception:
        del TEXT[int(client.me.id)]


@PY.INLINE("^logs_inline")
@INLINE.QUERY
async def _(client, inline_query):
    data = inline_query.query.split()[1].split("_")
    await client.answer_inline_query(
        inline_query.id,
        cache_time=60,
        results=[
            InlineQueryResultArticle(
                title="logs!",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "ɢᴏ ᴛᴏ ᴍᴇssᴀɢᴇ",
                                url=TEXT[int(data[1])]["user"],
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                "ɢᴇᴛ ғᴏʀᴡᴀʀᴅ ᴍᴇssᴀɢᴇ",
                                callback_data=f"forward_msg {int(data[0])}_{int(data[1])}_{int(data[2])}",
                        )
                    ]
                ),
                input_message_content=InputTextMessageContent(
                    TEXT[int(data[1])]["msg"]
                ),
            )
        ],
    )
    del TEXT[int(inline_query.query.split()[1])]


@PY.CALLBACK("forward_msg")
@INLINE.DATA
async def _(client, callback_query):
    data = callback_query.data.split()[1].split("_")
    try:
        user = [x for x in ubot._ubot if int(x.me.id) == int(data[0])]
        if user:
            logs = await get_vars(user[0].me.id, "ID_LOGS")
            get = await user[0].get_messages(int(data[1]), int(data[2]))
            msg = await get.forward(int(logs))
            await asyncio.sleep(10)
            return await msg.delete()
    except Exception as error:
        print(error)
        return await callback_query.answer(
            "❌ ᴘᴇsᴀɴ ᴛᴇʀsᴇʙᴜᴛ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴅɪᴛᴇʀᴜsᴋᴀɴ ᴋᴇ ʟᴏɢs", True
        )
      

@PY.LOGS_PRIVATE()
async def _(client, message):
    logs = await get_vars(client.me.id, "ID_LOGS")
    on_logs = await get_vars(client.me.id, "ON_LOGS")

    if logs and on_logs:
        type = "ᴘʀɪᴠᴀᴛᴇ"
        user_link = f"[{message.from_user.first_name} {message.from_user.last_name or ''}](tg://user?id={message.from_user.id})"
        message_link = f"tg://openmessage?user_id={message.from_user.id}&message_id={message.id}"
        message_text = f"""
<b>📩 ᴀᴅᴀ ᴘᴇsᴀɴ ᴍᴀsᴜᴋ</b>
    <b>•> ᴛɪᴘᴇ ᴘᴇsᴀɴ:</b> <code>{type}</code>
    <b>•> ᴅᴀʀɪ: {user_link}</b>
"""
        await send_log(client, int(logs), message, message_text, message_link, "LOGS_PRIVATE")


@PY.LOGS_GROUP()
async def _(client, message):
    logs = await get_vars(client.me.id, "ID_LOGS")
    on_logs = await get_vars(client.me.id, "ON_LOGS")

    if logs and on_logs:
        type = "ɢʀᴏᴜᴘ"
        user_link = f"[{message.from_user.first_name} {message.from_user.last_name or ''}](tg://user?id={message.from_user.id})"
        message_link = message.link
        message_text = f"""
<b>📩 ᴀᴅᴀ ᴘᴇsᴀɴ ᴍᴀsᴜᴋ</b>
    <b>•> ᴛɪᴘᴇ ᴘᴇsᴀɴ:</b> <code>{type}</code>
    <b>•> ᴅᴀʀɪ: {user_link}</b>
"""
        await send_log(client, int(logs), message, message_text, message_link, "LOGS_GROUP")


@PY.UBOT("logs")
@PY.TOP_CMD
async def _(client, message):
    if len(message.command) < 2:
        return await message.reply("ʜᴀʀᴀᴘ ʙᴀᴄᴀ ᴍᴇɴᴜ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴀʜᴜɪ ᴄᴀʀᴀ ᴘᴇɴɢɢᴜɴᴀᴀɴɴʏᴀ.")

    query = {"on": True, "off": False, "none": False}
    command = message.command[1].lower()

    if command not in query:
        return await message.reply("ᴏᴘsɪ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ. ʜᴀʀᴀᴘ ɢᴜɴᴀᴋᴀɴ 'on' ᴀᴛᴀᴜ 'off'.")

    value = query[command]

    vars = await get_vars(client.me.id, "ID_LOGS")

    if not vars:
        logs = await create_logs(client)
        await set_vars(client.me.id, "ID_LOGS", logs)

    if command == "none" and vars:
        try:
            await client.delete_channel(vars)
        except Exception:
            pass
        await set_vars(client.me.id, "ID_LOGS", value)

    await set_vars(client.me.id, "ON_LOGS", value)
    return await message.reply(f"<b>✅ <code>LOGS</code> ʙᴇʀʜᴀsɪʟ ᴅɪsᴇᴛᴛɪɴɢ ᴋᴇ:</b> <code>{value}</code>")


async def create_logs(client):
    logs = await client.create_channel(f"Logs Arab Ultra")
    url = wget.download("https://telegra.ph//file/ea39b52686ec35ed9950a.jpg")
    photo_video = {"video": url} if url.endswith(".mp4") else {"photo": url}
    await client.set_chat_photo(
        logs.id,
        **photo_video,
    )
    return logs.id
