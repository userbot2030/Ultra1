"create by: NorSodikin.t.me"
"request by: dhilnihnge.t.me"

import wget

from PyroUbot import *

__MODULE__ = "logs"
__HELP__ = """
<b>◖ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʟᴏɢs◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}logs</code> (on/off)
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴀᴛᴀᴜ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ᴄʜᴀɴɴᴇʟ ʟᴏɢs
"""


async def send_log(client, chat_id, message, message_text, msg):
    try:
        await client.send_message(chat_id, message_text, disable_web_page_preview=True)
        await message.forward(chat_id)
    except Exception as error:
        print(f"{msg} - {error}")


@PY.LOGS_PRIVATE()
async def _(client, message):
    logs = await get_vars(client.me.id, "ID_LOGS")
    on_logs = await get_vars(client.me.id, "ON_LOGS")

    if logs and on_logs:
        type = "ᴘʀɪᴠᴀᴛᴇ"
        user_link = f"[{message.from_user.first_name} {message.from_user.last_name or ''}](tg://user?id={message.from_user.id})"
        message_link = f"tg://openmessage?user_id={message.from_user.id}&message_id={message.id}"
        message_text = f"""
<b>📩 Ada Pesan Masuk !!</b>
    <b>➥ Tipe Pesan:</b> <code>{type}</code>
    <b>➥ Link Pesan:</b> [KLIK DISINI BRE]({message_link})
    
<b>⤵️ Dibawah ini adalah pesan terusan dari user: {user_link}</b>
            <b>⬇ ⬇ ⬇ ⬇ ⬇ ⬇ ⬇</b>
"""
        await send_log(client, int(logs), message, message_text, "LOGS_PRIVATE")


@PY.LOGS_GROUP()
async def _(client, message):
    logs = await get_vars(client.me.id, "ID_LOGS")
    on_logs = await get_vars(client.me.id, "ON_LOGS")

    if logs and on_logs:
        type = "ɢʀᴏᴜᴘ"
        user_link = f"[{message.from_user.first_name} {message.from_user.last_name or ''}](tg://user?id={message.from_user.id})"
        message_link = message.link
        message_text = f"""
<b>📩 Ada Pesan Masuk !!</b>
    <b>➥ Type Pesan:</b> <code>{type}</code>
    <b>➥ Link Pesan:</b> [KLIK DISINI BRE]({message_link})
    
<b>⤵️ Dibawah ini adalah pesan terusan dari user: {user_link}</b>
"""
        await send_log(client, int(logs), message, message_text, "LOGS_GROUP")


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
    logs = await client.create_channel(f"• ʟᴏɢs ᴀʀᴀʙ ᴜʙᴏᴛ •")
    url = wget.download("https://telegra.ph//file/ea39b52686ec35ed9950a.jpg")
    photo_video = {"video": url} if url.endswith(".mp4") else {"photo": url}
    await client.set_chat_photo(
        logs.id,
        **photo_video,
    )
    return logs.id
