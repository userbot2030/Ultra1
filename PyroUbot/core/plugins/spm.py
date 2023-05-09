import asyncio


async def spam_cmd(client, message):
    if message.command[0] == "spam":
        if message.reply_to_message:
            spam = await message.reply("ᴅɪᴘʀᴏsᴇs")
            try:
                quantity = int(message.text.split(None, 2)[1])
                spam_text = message.text.split(None, 2)[2]
            except Exception as error:
                return await spam.edit(error)
            await asyncio.sleep(1)
            await message.delete()
            await spam.delete()
            for i in range(quantity):
                await client.send_message(
                    message.chat.id,
                    spam_text,
                    reply_to_message_id=message.reply_to_message.id,
                )
                await asyncio.sleep(0.3)
        else:
            if len(message.command) < 3:
                await message.reply_text("⚡ ᴜsᴀɢᴇ:\n.sᴘᴀᴍ ᴊᴜᴍʟᴀʜ sᴘᴀᴍ, ᴛᴇxᴛ sᴘᴀᴍ")
            else:
                spam = await message.reply("Diproses")
                try:
                    quantity = int(message.text.split(None, 2)[1])
                    spam_text = message.text.split(None, 2)[2]
                except Exception as error:
                    return await spam.edit(error)
                await asyncio.sleep(1)
                await message.delete()
                await spam.delete()
                for i in range(quantity):
                    await client.send_message(message.chat.id, spam_text)
                    await asyncio.sleep(0.3)
    elif message.command[0] == "dspam":
        if message.reply_to_message:
            if len(message.command) < 3:
                return await message.reply_text(
                    "⚡ ᴜsᴀɢᴇ:\n.ᴅsᴘᴀᴍ ᴊᴜᴍʟᴀʜ sᴘᴀᴍ, ᴊᴜᴍʟᴀʜ ᴅᴇʟᴀʏ ᴅᴇᴛɪᴋ, ʙᴀʟᴀs ᴘᴇsᴀɴ"
                )
            spam = await message.reply("ᴅɪᴘʀᴏsᴇs")
            try:
                quantity = int(message.text.split(None, 3)[1])
                delay_msg = int(message.text.split(None, 3)[2])
            except Exception as error:
                return await spam.edit(error)
            await asyncio.sleep(1)
            await message.delete()
            await spam.delete()
            for i in range(quantity):
                await message.reply_to_message.copy(message.chat.id)
                await asyncio.sleep(delay_msg)
        if len(message.command) < 4:
            return await message.reply_text(
                "⚡ ᴜsᴀɢᴇ:\n.ᴅsᴘᴀᴍ ᴊᴜᴍʟᴀʜ sᴘᴀᴍ, ᴊᴜᴍʟᴀʜ ᴅᴇʟᴀʏ ᴅᴇᴛɪᴋ, ᴛᴇxᴛ sᴘᴀᴍ"
            )
        else:
            spam = await message.reply("ᴅɪᴘʀᴏsᴇs")
            try:
                quantity = int(message.text.split(None, 3)[1])
                delay_msg = int(message.text.split(None, 3)[2])
                spam_text = message.text.split(None, 3)[3]
            except Exception as error:
                return await spam.edit(error)
            await asyncio.sleep(1)
            await message.delete()
            await spam.delete()
            for i in range(quantity):
                await client.send_message(message.chat.id, spam_text)
                await asyncio.sleep(delay_msg)
