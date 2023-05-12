import asyncio

from pyrogram.enums import ChatType

from PyroUbot import *


async def broadcast_group_cmd(client, message):
    sent = 0
    failed = 0
    msg = await message.reply("sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs")
    async for dialog in client.get_dialogs():
        if dialog.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
            if message.reply_to_message:
                send = message.reply_to_message
            else:
                if len(message.command) < 2:
                    await msg.delete()
                    return await message.reply("ᴍᴏʜᴏɴ ʙᴀʟᴀs sᴇsᴜᴀᴛᴜ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ sᴇsᴜᴀᴛᴜ")
                else:
                    send = message.text.split(None, 1)[1]
            chat_id = dialog.chat.id
            if chat_id not in await get_chat():
                try:
                    if message.reply_to_message:
                        await send.copy(chat_id)
                    else:
                        await client.send_message(chat_id, send)
                    sent += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    failed += 1
                    await asyncio.sleep(0.1)
    await msg.delete()
    return await message.reply(
        f"💬 ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ sᴇʟᴇsᴀɪ\n\n✅ ʙᴇʀʜᴀsɪʟ ᴛᴇʀᴋɪʀɪᴍ: {send} \n❌ ɢᴀɢᴀʟ ᴛᴇʀᴋɪʀɪᴍ: {failed}"
    )


async def broadcast_users_cmd(client, message):
    sent = 0
    failed = 0
    msg = await message.reply("sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs")
    async for dialog in client.get_dialogs():
        if dialog.chat.type == ChatType.PRIVATE:
            if message.reply_to_message:
                send = message.reply_to_message
            else:
                if len(message.command) < 2:
                    await msg.delete()
                    return await message.reply("ᴍᴏʜᴏɴ ʙᴀʟᴀs sᴇsᴜᴀᴛᴜ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ sᴇsᴜᴀᴛᴜ")
                else:
                    send = message.text.split(None, 1)[1]
            chat_id = dialog.chat.id
            if chat_id not in BLACKLIST_CHAT:
                try:
                    if message.reply_to_message:
                        await send.copy(chat_id)
                    else:
                        await client.send_message(chat_id, send)
                    sent += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    failed += 1
                    await asyncio.sleep(0.1)
    await msg.delete()
    return await message.reply(
        f"💬 ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ sᴇʟᴇsᴀɪ\n\n✅ ʙᴇʀʜᴀsɪʟ ᴛᴇʀᴋɪʀɪᴍ: {send} \n❌ ɢᴀɢᴀʟ ᴛᴇʀᴋɪʀɪᴍ: {failed}"
    )


async def send_msg_cmd(client, message):
    if message.reply_to_message:
        if len(message.command) < 2:
            chat_id = message.chat.id
        else:
            chat_id = message.text.split()[1]
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
