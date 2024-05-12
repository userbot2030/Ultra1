import asyncio
from gc import get_objects

from pyrogram.enums import ChatType
from pyrogram.errors import BadRequest

from PyroUbot import *

__MODULE__ = "gcast2"
__HELP__ = """
 Bantuan Untuk Gcast2

• cmd : <code>{0}ucast</code> [balas pesan/kirim pesan]
• Penjelasan : Untuk pengirim pesan ke semua pengguna.

• cmd : <code>{0}gcast</code> [balas pesan/kirim pesan]
• Penjelasan : Untuk pengirim pesan ke semua grup.

• cmd : <code>{0}stopgcast</code>
• Penjelasan : Untuk membatalkan proses gcast.
  
• Untuk Menggunakan Button Gunakan Format : <code> Teks ~ button_teks:button_url</code>
"""


def get_message(message):
    msg = (
        message.reply_to_message
        if message.reply_to_message
        else ""
        if len(message.command) < 2
        else " ".join(message.command[1:])
    )
    return msg



async def get_broadcast_id(client, query):
    chats = []
    chat_types = {
        "group": [ChatType.GROUP, ChatType.SUPERGROUP],
        "users": [ChatType.PRIVATE],
    }
    async for dialog in client.get_dialogs():
        if dialog.chat.type in chat_types[query]:
            # Periksa apakah top_message ada sebelum mengakses id-nya
            if dialog.top_message is not None: 
                chats.append(dialog.chat.id)
            else:
                print(f"Melewati dialog tanpa top_message: {dialog.chat.id}")  # Log untuk debugging

    return chats 


"""
async def broadcast_groupcmd(client, message):
    msg = await message.reply("Processing...", quote=True)
    blacklist = await get_chat(client.me.id)
    done = 0
    async for dialog in client.get_dialogs(limit=None):
        if dialog.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
            if message.reply_to_message:
                send = message.reply_to_message
            else:
                if len(message.command) < 2:
                    return await msg.edit(
                        "Silakan balas ke pesan atau berikan pesan.")
                else:
                    send = message.text.split(None, 1)[1]
            chat_id = dialog.chat.id
            if chat_id not in blacklist and chat_id not in BLACKLIST_CHAT:
                try:
                    if message.reply_to_message:
                        await send.copy(chat_id)
                    else:
                        await client.send_message(chat_id, send)
                    done += 1
                except Exception:
                    pass
                
    return await msg.edit(f"**Successfully Sent Message To `{done}` Groups chat**.")
"""

broadcast_running = False

@PY.UBOT("gcast")
@PY.TOP_CMD
async def broadcast_group_cmd(client, message):
    global broadcast_running

    msg = await message.reply("Processing...", quote=True)

    send = get_message(message)
    if not send:
        return await msg.edit("Silakan balas ke pesan atau berikan pesan.")

    broadcast_running = True

    chats = await get_broadcast_id(client, "group")
    blacklist = await get_chat(client.me.id)

    done = 0
    failed = 0
    
    for chat_id in chats:

        if not broadcast_running:
            break
        
        if chat_id not in blacklist and chat_id not in BLACKLIST_CHAT:
            
            try:
                if message.reply_to_message:
                    await send.copy(chat_id)
                else:
                    await client.send_message(chat_id, send)
                done += 1
                await asyncio.sleep(0.1)
            except Exception:
                failed += 1
                pass
                #await asyncio.sleep(1)
                                
    broadcast_running = True

    if done > 0:
        await msg.edit(f"**<emoji id=5780777456428388142>👍</emoji>Berhasil Terkirim:** `{done}` \n**<emoji id=5019523782004441717>❌</emoji>Gagal Mengirim Pesan Ke:** `{failed}`.")
    else:
        await msg.edit(f"**Pesan Broadcast Berhasil Dibatalkan**.")


@PY.UBOT("stopgcast")
@PY.TOP_CMD
async def cancel_broadcast(client, message):
    global broadcast_running

    if not broadcast_running:
        return await message.reply_text("<code>Tidak ada pengiriman pesan broadcast yang sedang berlangsung.</code>")

    broadcast_running = True
    await message.delete()
  

@PY.UBOT("ucast")
@PY.TOP_CMD
async def broadcast_users_cmd(client, message):
    msg = await message.reply("Processing...")
    blacklist = await get_chat(client.me.id)
    done = 0
    async for dialog in client.get_dialogs(limit=None):
        if dialog.chat.type == ChatType.PRIVATE:
            if message.reply_to_message:
                send = message.reply_to_message
            else:
                if len(message.command) < 2:
                    return await msg.edit(
                        "Silakan balas ke pesan atau berikan pesan.")
                else:
                    send = message.text.split(None, 1)[1]
            chat_id = dialog.chat.id
            if chat_id not in blacklist and chat_id not in DEVS:
                try:
                    if message.reply_to_message:
                        await send.copy(chat_id)
                    else:
                        await client.send_message(chat_id, send)
                    done += 1
                except Exception:
                    pass
 
    await msg.edit(f"**Successfully Sent Message To `{done}` Groups chat**")


@PY.INLINE("^gcast_button")
@INLINE.QUERY
async def gcast_inline(client, inline_query):
    get_id = int(inline_query.query.split(None, 1)[1])
    m = [obj for obj in get_objects() if id(obj) == get_id][0]
    buttons, text = await gcast_create_button(m)
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="get button!",
                    reply_markup=buttons,
                    input_message_content=InputTextMessageContent(text),
                )
            )
        ],
    )
