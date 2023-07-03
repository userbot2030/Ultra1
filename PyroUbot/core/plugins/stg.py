from PyroUbot import *


async def setprefix(client, message):
    Tm = await message.reply("ᴍᴇᴍᴘʀᴏsᴇs...", quote=True)
    if len(message.command) < 2:
        return await Tm.edit(f"<code>{message.text} sɪᴍʙᴏʟ ᴘʀᴇғɪx</code>")
    else:
        try:
            client.set_prefix(client.me.id, message.command[1])
            await set_pref(client.me.id, message.command[1])
            return await Tm.edit(f"<b>✅ ᴘʀᴇғɪx ᴛᴇʟᴀʜ ᴅɪᴜʙᴀʜ ᴋᴇ: {message.command[1]}")
        except Exception as error:
            await Tm.edit(error)


async def coba(client, message):
    await message.reply(message.command)
