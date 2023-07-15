from PyroUbot import *


async def setprefix(client, message):
    Tm = await message.reply("ᴍᴇᴍᴘʀᴏsᴇs...", quote=True)
    if len(message.command) < 2:
        return await Tm.edit(f"<code>{message.text} sɪᴍʙᴏʟ ᴘʀᴇғɪx</code>")
    else:
        if message.command[1].lower() == "none":
            prefix = [""]
        else:
            prefix = message.command[1:]
        try:
            ubot.set_prefix(message.from_user.id, prefix)
            await set_pref(message.from_user.id, prefix)
            return await Tm.edit(f"<b>✅ ᴘʀᴇғɪx ᴛᴇʟᴀʜ ᴅɪᴜʙᴀʜ ᴋᴇ: {' '.join(prefix)}")
        except Exception as error:
            await Tm.edit(error)
