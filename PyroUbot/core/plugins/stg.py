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
            client.set_prefix(client.me.id, prefix)
            await set_pref(client.me.id, prefix)
            return await Tm.edit(
                f"<b>✅ ᴘʀᴇғɪx ᴛᴇʟᴀʜ ᴅɪᴜʙᴀʜ ᴋᴇ: {' '.join(message.command[1:])}"
            )
        except Exception as error:
            await Tm.edit(error)
