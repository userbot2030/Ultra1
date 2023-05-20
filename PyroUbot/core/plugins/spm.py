import asyncio


async def spam_cmd(client, message):
    reply = message.reply_to_message
    msg = await message.reply("xsᴇᴅᴀɴɢ ᴅɪᴘʀᴏsᴇs", quote=False)
    if reply:
        try:
            for i in range(int(message.command[1])):
                await reply.copy(message.chat.id)
                await asyncio.sleep(0.1)
        except Exception as error:
            await msg.edit(error)
    else:
        if len(message.command) < 2:
            return await msg.edit(
                "sɪʟᴀʜᴋᴀɴ ᴋᴇᴛɪᴋ <code>help spam</code> ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴄᴀʀᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ"
            )
        else:
            try:
                for i in range(int(message.command[1])):
                    await message.reply(message.text.split(None, 2)[2], quote=False)
                    await asyncio.sleep(0.1)
            except Exception as error:
                await msg.edit(error)
    await msg.delete()
    await message.deletw()


async def dspam_cmd(client, message):
    reply = message.reply_to_message
    msg = await message.reply("xsᴇᴅᴀɴɢ ᴅɪᴘʀᴏsᴇs", quote=False)
    if reply:
        try:
            for i in range(int(message.command[1])):
                await reply.copy(message.chat.id)
                await asyncio.sleep(int(message.command[2]))
        except Exception as error:
            await msg.edit(error)
    else:
        if len(message.command) < 3:
            return await msg.edit(
                "sɪʟᴀʜᴋᴀɴ ᴋᴇᴛɪᴋ <code>help spam</code> ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴄᴀʀᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ"
            )
        else:
            try:
                for i in range(int(message.command[1])):
                    await message.reply(message.text.split(None, 3)[3], quote=False)
                    await asyncio.sleep(int(message.command[2]))
            except Exception as error:
                await msg.edit(error)
    await msg.delete()
    await message.deletw()
