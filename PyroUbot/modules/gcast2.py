import asyncio
from gc import get_objects

from pyrogram.enums import ChatType

from PyroUbot import *


__MODULE__ = "gcast2"
__HELP__ = """
<b>◖ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢᴄᴀsᴛ 2◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}ucast</code> [ᴛᴇxᴛ/ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ/ᴍᴇᴅɪᴀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ sᴇᴍᴜᴀ ᴜsᴇʀ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}gcast</code> [ᴛᴇxᴛ/ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ/ᴍᴇᴅɪᴀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ sᴇᴍᴜᴀ ɢʀᴏᴜᴘ
  
• Untuk Menggunakan Button Gunakan Format : <code> Teks ~ button_teks:button_url</code>
"""

@PY.UBOT("gcast")
@PY.TOP_CMD
async def _(client, message):
    await broadcast_group_cmd(client, message)


@PY.UBOT("ucast")
@PY.TOP_CMD
async def _(client, message):
    await broadcast_users_cmd(client, message)


@PY.INLINE("^gcast_button")
@INLINE.QUERY
async def _(client, inline_query):
    await gcast_inline(client, inline_query)
 

async def broadcast_group_cmd(client, message):
    sent = 0
    failed = 0
    proses = await get_vars(client.me.id, "EMOJI_PROSES") or "5960640164114993927"
    msg = await message.reply(f"<emoji id={proses}>⏳</emoji> ꜱᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏꜱᴇꜱ ɢɪᴋᴇꜱ....")
    async for dialog in client.get_dialogs(limit=None):
        if dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
            if message.reply_to_message:
                send = message.reply_to_message
            else:
                if len(message.command) < 2:
                    await msg.delete()
                    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "6247033234861853924"
                    return await message.reply(f"<emoji id={gagal}>❎</emoji> ᴇʀᴏʀʀ!! ᴍᴏʜᴏɴ ʙᴀʟᴀs sᴇsᴜᴀᴛᴜ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ sᴇsᴜᴀᴛᴜ")
                else:
                    send = message.text.split(None, 1)[1]
            chat_id = dialog.chat.id
            if chat_id not in await get_chat(client.me.id):
                try:
                    if message.reply_to_message:
                        await send.copy(chat_id)
                    else:
                        await client.send_message(chat_id, send)
                    sent += 1
                    await asyncio.sleep(2)
                except Exception:
                    failed += 1
    await msg.delete()
    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "5438630285635757876"
    sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "5787188704434982946"
    gcast_done = await get_vars(client.me.id, "GCAST_DONE") or "6289678459065077018"
    await message.reply(f"<b>ɢɪᴋᴇꜱ ʟᴜ ᴛᴇʟᴀʜ ꜱᴇʟᴇꜱᴀɪ <emoji id={gcast_done}>❗️</emoji>\n\n<emoji id={sukses}>✅</emoji> ᴘᴇsᴀɴ ᴛᴇʀᴋɪʀɪᴍ ᴋᴇ <code>{sent}</code> ɢʀᴏᴜᴘ\n<emoji id={gagal}>❎</emoji> ɢᴀɢᴀʟ ᴛᴇʀᴋɪʀɪᴍ ᴋᴇ <code>{failed}</code> ɢʀᴏᴜᴘ</b>")


async def broadcast_users_cmd(client, message):
    sent = 0
    failed = 0
    proses = await get_vars(client.me.id, "EMOJI_PROSES") or "5960640164114993927"
    msg = await message.reply(f"<emoji id={proses}>⏳</emoji> ꜱᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏꜱᴇꜱ ᴜᴄᴀꜱᴛ...")
    async for dialog in client.get_dialogs(limit=None):
        if dialog.chat.type == ChatType.PRIVATE:
            if message.reply_to_message:
                send = message.reply_to_message
            else:
                if len(message.command) < 2:
                    await msg.delete()
                    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "5438630285635757876"
                    return await message.reply(f"<emoji id={gagal}>❎</emoji> ᴇʀᴏʀʀ!! ᴍᴏʜᴏɴ ʙᴀʟᴀs sᴇsᴜᴀᴛᴜ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ sᴇsᴜᴀᴛᴜ")
                else:
                    send = message.text.split(None, 1)[1]
            chat_id = dialog.chat.id
            try:
                if message.reply_to_message:
                    await send.copy(chat_id)
                else:
                    await client.send_message(chat_id, send)
                sent += 1
                await asyncio.sleep(3)
            except Exception:
                failed += 1
    await msg.delete()
    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "5438630285635757876"
    sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "5787188704434982946"
    gcast_done = await get_vars(client.me.id, "GCAST_DONE") or "6289678459065077018"
    await message.reply(f"<b>ᴘᴇꜱᴀɴ ᴜᴄᴀꜱᴛ ʟᴜ ᴛᴇʟᴀʜ ꜱᴇʟᴇꜱᴀɪ ᴅɪʟᴀᴋᴜᴋᴀɴ <emoji id={gcast_done}>❗️</emoji>\n<emoji id={sukses}>✅</emoji> ᴘᴇsᴀɴ ᴛᴇʀᴋɪʀɪᴍ ᴋᴇ <code>{sent}</code> ᴜsᴇʀ\n<emoji id={gagal}>❎</emoji> ɢᴀɢᴀʟ ᴋᴇ <code>{failed}</code> ᴜsᴇʀ</b>")


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
