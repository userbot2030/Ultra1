import emoji

from PyroUbot import *


def contains_premium_emoji(text):
    for char in text:
        if char in emoji.UNICODE_EMOJI["en"]:
            return True
    return False


async def setprefix(client, message):
    Tm = await message.reply("ᴍᴇᴍᴘʀᴏsᴇs...", quote=True)
    if len(message.command) < 2:
        return await Tm.edit(f"<code>{message.text} sɪᴍʙᴏʟ ᴘʀᴇғɪx</code>")
    else:
        set_prefix_ub = []
        for prefix in message.command[1:]:
            if prefix.lower() == "none":
                set_prefix_ub.append("")
            else:
                set_prefix_ub.append(prefix)
        try:
            ubot.set_prefix(message.from_user.id, set_prefix_ub)
            await set_pref(message.from_user.id, set_prefix_ub)
            formatted_prefix = (
                " ".join(set_prefix_ub).encode("ascii", "xmlcharrefreplace").decode()
            )
            return await Tm.edit(f"<b>✅ ᴘʀᴇғɪx ᴛᴇʟᴀʜ ᴅɪᴜʙᴀʜ ᴋᴇ:</b> {formatted_prefix}")
        except Exception as error:
            await Tm.edit(error)
