import asyncio
from gc import get_objects

from pyrogram.enums import ChatType

from PyroUbot import *


async def broadcast_group_cmd(client, message):
    sent = 0
    failed = 0
    msg = await message.reply(
        "sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs\n\nᴘᴇsᴀɴ ᴀɴᴅᴀ ᴀᴋᴀɴ ᴛᴇʀᴋɪʀɪᴍ sᴇᴛɪᴀᴘ 3 ᴅᴇᴛɪᴋ sᴇᴋᴀʟɪ ᴍᴏʜᴏɴ ʙᴇʀsᴀʙᴀʀ"
    )
    for dialog in client._get_my_peer["gc"]:
        if message.reply_to_message:
            send = message.reply_to_message
        else:
            if len(message.command) < 2:
                await msg.delete()
                return await message.reply("ᴍᴏʜᴏɴ ʙᴀʟᴀs sᴇsᴜᴀᴛᴜ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ sᴇsᴜᴀᴛᴜ")
            else:
                send = message.text.split(None, 1)[1]
        if dialog not in await get_chat(client.me.id):
            try:
                if message.reply_to_message:
                    await send.copy(dialog)
                else:
                    if "~>" not in send:
                        await client.send_message(dialog, send)
                    else:
                        x = await client.get_inline_bot_results(
                                bot.me.username, f"gcast_button {id(message)}"
                            )
                        await client.send_inline_bot_result(
                                dialog,
                                x.query_id,
                                x.results[0].id,
                            )
                    sent += 1
                await asyncio.sleep(3)
            except Exception:
                failed += 1
                await asyncio.sleep(0.3)
    await msg.delete()
    return await message.reply(
        f"💬 ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ sᴇʟᴇsᴀɪ\n\n✅ ʙᴇʀʜᴀsɪʟ ᴛᴇʀᴋɪʀɪᴍ: {sent} \n❌ ɢᴀɢᴀʟ ᴛᴇʀᴋɪʀɪᴍ: {failed}"
    )


async def broadcast_users_cmd(client, message):
    sent = 0
    failed = 0
    msg = await message.reply(
        "sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs\n\nᴘᴇsᴀɴ ᴀɴᴅᴀ ᴀᴋᴀɴ ᴛᴇʀᴋɪʀɪᴍ sᴇᴛɪᴀᴘ 3 ᴅᴇᴛɪᴋ sᴇᴋᴀʟɪ ᴍᴏʜᴏɴ ʙᴇʀsᴀʙᴀʀ"
    )
    for dialog in client._get_my_peer["pm"]:
        if message.reply_to_message:
            send = message.reply_to_message
        else:
            if len(message.command) < 2:
                await msg.delete()
                return await message.reply("ᴍᴏʜᴏɴ ʙᴀʟᴀs sᴇsᴜᴀᴛᴜ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ sᴇsᴜᴀᴛᴜ")
            else:
                  send = message.text.split(None, 1)[1]
            if dialog not in await get_chat():
                try:
                    if message.reply_to_message:
                        await send.copy(dialog)
                    else:
                        await client.send_message(dialog, send)
                    sent += 1
                    await asyncio.sleep(3)
                except Exception:
                    failed += 1
                    await asyncio.sleep(0.3)
    await msg.delete()
    return await message.reply(
        f"💬 ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ sᴇʟᴇsᴀɪ\n\n✅ ʙᴇʀʜᴀsɪʟ ᴛᴇʀᴋɪʀɪᴍ: {sent} \n❌ ɢᴀɢᴀʟ ᴛᴇʀᴋɪʀɪᴍ: {failed}"
    )


async def send_msg_cmd(client, message):
    if message.reply_to_message:
        if len(message.command) < 2:
            chat_id = message.chat.id
        else:
            chat_id = message.text.split()[1]
        if message.reply_to_message.reply_markup:
            try:
                x = await client.get_inline_bot_results(
                    bot.me.username, f"get_send {id(message)}"
                )
                await client.send_inline_bot_result(
                    chat_id, x.query_id, x.results[0].id
                )
                tm = await message.reply(f"✅ ᴘᴇsᴀɴ ʙᴇʀʜᴀsɪʟ ᴅɪᴋɪʀɪᴍ ᴋᴇ {chat_id}")
                await asyncio.sleep(5)
                await message.delete()
                await tm.delete()
            except Exception as error:
                await message.reply(error)
        else:
            try:
                await message.reply_to_message.copy(chat_id, protect_content=True)
                tm = await message.reply(f"✅ ᴘᴇsᴀɴ ʙᴇʀʜᴀsɪʟ ᴅɪᴋɪʀɪᴍ ᴋᴇ {chat_id}")
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
            await client.send_message(chat_id, chat_text, protect_content=True)
            tm = await message.reply(f"✅ ᴘᴇsᴀɴ ʙᴇʀʜᴀsɪʟ ᴅɪᴋɪʀɪᴍ ᴋᴇ {chat_id}")
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
                    input_message_content=InputTextMessageContent(
                        m.reply_to_message.text
                    ),
                )
            )
        ],
    )


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
