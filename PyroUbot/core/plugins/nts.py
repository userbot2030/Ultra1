from .. import *


async def addnote_cmd(client, message):
    note_name = get_arg(message)
    reply = message.reply_to_message
    if not reply:
        return await message.reply(
            "ʙᴀʟᴀs ᴘᴇsᴀɴ ᴅᴀɴ ɴᴀᴍᴀ ᴘᴀᴅᴀ ᴄᴀᴛᴀᴛᴀɴ ᴜɴᴛᴜᴋ ᴍᴇɴʏɪᴍᴘᴀɴ ᴄᴀᴛᴀᴛᴀɴ"
        )
    if await get_note(client.me.id, note_name):
        return await message.reply(f"Catatan {note_name} sudah ada")
    copy = await client.copy_message(client.me.id, message.chat.id, reply.id)
    await save_note(client.me.id, note_name, copy.id)
    await client.send_message(
        client.me.id,
        f"👆🏻 ᴘᴇsᴀɴ ᴅɪᴀᴛᴀs ɪɴɪ ᴊᴀɴɢᴀɴ ᴅɪʜᴀᴘᴜs ᴀᴛᴀᴜ ᴄᴀᴛᴀᴛᴀɴ ᴀᴋᴀɴ ʜɪʟᴀɴɢ \n\n👉🏻 Ketik: <code>{PREFIX[0]}delnote {note_name}</code> ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ᴄᴀᴛᴀᴛᴀɴ ᴅɪᴀᴛᴀs",
    )
    await message.reply("ᴄᴀᴛᴀᴛᴀɴ ʙᴇʀʜᴀsɪʟ ᴅɪ sɪᴍᴘᴀɴ")


async def get_cmd(client, message):
    note_name = get_arg(message)
    if not note_name:
        return await message.reply("ᴀᴘᴀ ʏᴀɴɢ ᴀɴᴅᴀ ᴄᴀʀɪ")
    note = await get_note(client.me.id, note_name)
    if not note:
        return await message.reply(f"ᴄᴀᴛᴀᴛᴀɴ {note_name} ᴛɪᴅᴀᴋ ᴀᴅᴀ")
    msg = message.reply_to_message or message
    await client.copy_message(
        message.chat.id,
        client.me.id,
        note,
        reply_to_message_id=msg.id,
    )


async def delnote_cmd(client, message):
    note_name = get_arg(message)
    if not note_name:
        return await message.reply("ᴀᴘᴀ ʏᴀɴɢ ɪɴɢɪɴ ᴀɴᴅᴀ ʜᴀᴘᴜs?")
    note = await get_note(client.me.id, note_name)
    if not note:
        return await message.reply(f"ᴄᴀᴛᴀᴛᴀɴ {note_name} ᴛɪᴅᴀᴋ ᴀᴅᴀ")
    await rm_note(client.me.id, note_name)
    await message.reply(f"ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢʜᴀᴘᴜs ᴄᴀᴛᴀᴛᴀɴ {note_name}")
    await client.delete_messages(client.me.id, [int(note), int(note) + 1])


async def notes_cmd(client, message):
    msg = f"📝 ᴅᴀꜰᴛᴀʀ ᴄᴀᴛᴀᴛᴀɴ {client.me.first_name} {client.me.last_name or ''}\n\n"
    allnotes = await all_notes(client.me.id)
    for notes in allnotes:
        msg += f"• {notes}\n"
    await message.reply(msg)
