import asyncio
from gc import get_objects

from pyrogram.enums import ChatType

from PyroUbot import *


async def broadcast_group_cmd(client, message):
    sent = 0
    failed = 0
    slowmode = 2
    proses = await get_vars(client.me.id, "EMOJI_PROSES") or "5960640164114993927"
    msg = await message.reply(f"<emoji id={proses}>⏳</emoji> ꜱᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏꜱᴇꜱ ɢɪᴋᴇꜱ....")
    async for dialog in client.get_dialogs(limit=None):
        await client.slowmode(2)
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


async def send_msg_cmd(client, message):
    if message.reply_to_message:
        if len(message.command) < 2:
            chat_id = message.chat.id
        else:
            chat_id = message.text.split()[1]
        send_done = await get_vars(client.me.id, "SEND_DONE") or "6111585093220830556"
        if not client.me.id == bot.me.id:
            if message.reply_to_message.reply_markup:
                try:
                    x = await client.get_inline_bot_results(bot.me.username, f"get_send {id(message)}")
                    await client.send_inline_bot_result(chat_id, x.query_id, x.results[0].id)
                    tm = await message.reply(f"<emoji id={send_done}>✅</emoji> ᴘᴇsᴀɴ ʙᴇʀʜᴀsɪʟ ᴅɪᴋɪʀɪᴍ ᴋᴇ {chat_id}")
                    await asyncio.sleep(5)
                    await message.delete()
                    await tm.delete()
                except Exception as error:
                    await message.reply(error)
        else:
            try:
                await message.reply_to_message.copy(chat_id)
                tm = await message.reply(f"<emoji id={send_done}>✅</emoji> ᴘᴇsᴀɴ ʙᴇʀʜᴀsɪʟ ᴅɪᴋɪʀɪᴍ ᴋᴇ {chat_id}")
                await asyncio.sleep(3)
                await message.delete()
                await tm.delete()
            except Exception as t:
                return await message.reply(f"{t}")
    else:
        if len(message.command) < 3:
            return await message.reply("ᴋᴇᴛɪᴋ ʏᴀɴɢ ʙᴇɴᴇʀ")
        chat_id = message.text.split(None, 2)[1]
        chat_text = message.text.split(None, 2)[2]
        try:
            await client.send_message(chat_id, chat_text)
            tm = await message.reply(f"{send_done} ᴘᴇsᴀɴ ʙᴇʀʜᴀsɪʟ ᴅɪᴋɪʀɪᴍ ᴋᴇ {chat_id}")
            await asyncio.sleep(3)
            await message.delete()
            await tm.delete()
        except Exception as t:
            return await message.reply(f"{t}")


async def send_inline(client, inline_query):
    _id = int(inline_query.query.split()[1])
    m = [obj for obj in get_objects() if id(obj) == _id][0]
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="get send!",
                    reply_markup=m.reply_to_message.reply_markup,
                    input_message_content=InputTextMessageContent(m.reply_to_message.text),
                )
            )
        ],
    )
