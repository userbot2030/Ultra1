from .. import *


async def addnote_cmd(client, message):
    note_name = get_arg(message)
    reply = message.reply_to_message
    if not reply:
        return await message.reply(
            "Balas pesan dan nama pada catatan untuk menyimpan catatan"
        )
    if await get_note(client.me.id, note_name):
        return await message.reply(f"Catatan {note_name} sudah ada")
    copy = await client.copy_message(client.me.id, message.chat.id, reply.id)
    await save_note(client.me.id, note_name, copy.id)
    await client.send_message(
        client.me.id,
        f"👆🏻 Pesan diatas ini jangan dihapus atau catatan akan hilang\n\n👉🏻 Ketik: <code>{PREFIX[0]}delnote {note_name}</code> untuk menghapus catatan diatas",
    )
    await message.reply("Catatan berhasil di simpan")


async def get_cmd(client, message):
    note_name = get_arg(message)
    if not note_name:
        return await message.reply("apa yang anda cari")
    note = await get_note(client.me.id, note_name)
    if not note:
        return await message.reply(f"Note {note_name} Tidak ada")
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
        return await message.reply("Apa yang ingin Anda hapus?")
    note = await get_note(client.me.id, note_name)
    if not note:
        return await message.reply(f"catatan {note_name} tidak ada")
    await rm_note(client.me.id, note_name)
    await message.reply(f"Berhasil menghapus catatan {note_name}")
    await client.delete_messages(client.me.id, [int(note), int(note) + 1])


async def notes_cmd(client, message):
    msg = f"Catatan {client.me.first_name} {client.me.last_name or ''}\n\n"
    all_notes = await all_notes(client.me.id)
    for notes in all_notes:
        msg += f"• {notes}\n"
    await message.reply(msg)
