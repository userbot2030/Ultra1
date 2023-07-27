from pyrogram.types import MessageEntity

from PyroUbot import *


def get_entities(text):
    entities = []
    current_offset = 0

    while current_offset < len(text):
        entity_start = text.find("<", current_offset)
        if entity_start == -1:
            break

        entity_end = text.find(">", entity_start + 1)
        if entity_end == -1:
            break

        entity_type = text[entity_start + 1 : entity_end]
        entity_offset = entity_start
        entity_length = entity_end - entity_start + 1

        entity = MessageEntity(entity_type, entity_offset, entity_length)
        entities.append(entity)

        current_offset = entity_end + 1

    return entities


async def setprefix(client, message):
    Tm = await message.reply("ᴍᴇᴍᴘʀᴏsᴇs...", quote=True)
    if len(message.command) < 2:
        return await Tm.edit(f"<code>{message.text}</code> sɪᴍʙᴏʟ ᴘʀᴇғɪx")
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
                f"<code>{prefix}</code>" for prefix in set_prefix_ub
            )
            return await Tm.edit(f"<b>✅ ᴘʀᴇғɪx ᴛᴇʟᴀʜ ᴅɪᴜʙᴀʜ ᴋᴇ: {parsed_prefix}</b>")
        except Exception as error:
            await Tm.edit(str(error))
