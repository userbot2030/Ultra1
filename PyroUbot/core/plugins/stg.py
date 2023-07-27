from PyroUbot import *


async def set_prefix(client, message):
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

            parsed_prefix = " ".join(
                f"<code>{prefix}</code>"
                if not prefix.startswith(("@", "#", "/"))
                else prefix
                for prefix in set_prefix_ub
            )

            return await Tm.edit(f"<b>✅ ᴘʀᴇғɪx ᴛᴇʟᴀʜ ᴅɪᴜʙᴀʜ ᴋᴇ: {parsed_prefix}</b>")
        except Exception as error:
            await Tm.edit(str(error))
