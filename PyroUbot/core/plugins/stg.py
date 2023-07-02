from PyroUbot import *


async def setprefix(client, message):
    Tm = await message.reply("ᴍᴇᴍᴘʀᴏsᴇs...", quote=True)
    if len(message.command) < 2:
        return await Tm.edit(f"<code>{message.text} sɪᴍʙᴏʟ ᴘʀᴇғɪx</code>")
    else:
        if message.command[1] == "none":
            setting = ""
        else:
            setting = message.command[1]
        try:
            await set_pref(client.me.id, setting)
            ubot.set_prefix(client.me.id, setting)
            return await Tm.edit(f"<b>✅ ᴘʀᴇғɪx ᴛᴇʟᴀʜ ᴅɪᴜʙᴀʜ ᴋᴇ: {setting}")
        except Exception as error:
            await Tm.edit(error)


async def coba(client, message):
    await message.reply("good")
