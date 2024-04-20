from PyroUbot import *


async def setprefix(client, message):
    Tm = await message.reply("ᴍᴇᴍᴘʀᴏsᴇs...", quote=True)
    if len(message.command) < 2:
        return await Tm.edit(f"<code>{message.text}</code> sɪᴍʙᴏʟ ᴘʀᴇғɪx")
    else:
        ub_prefix = []
        for prefix in message.command[1:]:
            if prefix.lower() == "none":
                ub_prefix.append("")
            else:
                ub_prefix.append(prefix)
        try:
            ubot.set_prefix(message.from_user.id, ub_prefix)
            await set_pref(message.from_user.id, ub_prefix)
            sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "5787188704434982946"
            parsed_prefix = " ".join(f"<code>{prefix}</code>" for prefix in ub_prefix)
            return await Tm.edit(f"<b><emoji id={sukses}>✅</emoji> ᴘʀᴇғɪx ᴛᴇʟᴀʜ ᴅɪᴜʙᴀʜ ᴋᴇ: {parsed_prefix}</b>")
        except Exception as error:
            return await Tm.edit(str(error))


async def change_emot(client, message):
    try:
        sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "5787188704434982946"
        proses = await get_vars(client.me.id, "EMOJI_PROSES") or "5960640164114993927"
        gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "5438630285635757876"
        msg = await message.reply(f"<emoji id={proses}>⏳</emoji> ꜱᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏꜱᴇꜱ...", quote=True)

        if not client.me.is_premium:
            return await msg.edit("<b>ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ᴀᴋᴜɴ ᴀɴᴅᴀ ʜᴀʀᴜs ᴘʀᴇᴍɪᴜᴍ ᴛᴇʀʟᴇʙɪʜ</b>")

        if len(message.command) < 3:
            return await msg.edit(f"<b><emoji id={gagal}>⚠️</emoji> ᴛᴏʟᴏɴɢ ᴍᴀsᴜᴋᴋᴀɴ ǫᴜᴇʀʏ ᴅᴀɴ ᴠᴀʟᴇᴜ ɴʏᴀ</b>")

        query_mapping = {"ping1": "EMOJI_PING1", "ping2": "EMOJI_PING2", "ping3": "EMOJI_PING3", "sukses": "EMOJI_SUKSES", "gagal": "EMOJI_GAGAL", "alasan": "EMOJI_ALASAN", "proses": "EMOJI_PROSES", "gban_user": "GBAN_USER", "kang_pack": "KANG_PACK", "emoji_global": "EMOJI_GLOBAL", "user": "EMOJI_USER", "admin": "EMOJI_ADMIN", "gcast_done": "GCAST_DONE", "send_done": "SEND_DONE"}
        command, mapping, value = message.command[:6]

        if mapping.lower() in query_mapping:
            query_var = query_mapping[mapping.lower()]
            emoji_id = None
            if message.entities:
                for entity in message.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break

            if emoji_id:
                await set_vars(client.me.id, query_var, emoji_id)
                await msg.edit(f"<b><emoji id={sukses}>✅</emoji> <code>{query_var}</code> ʙᴇʀʜᴀsɪʟ ᴅɪ sᴇᴛᴛɪɴɢ ᴋᴇ:</b> <emoji id={emoji_id}>{value}</emoji>")
            else:
                await msg.edit("<b>ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ᴀᴋᴜɴ ᴀɴᴅᴀ ʜᴀʀᴜs ᴘʀᴇᴍɪᴜᴍ ᴛᴇʀʟᴇʙɪʜ</b>")
        else:
            await msg.edit(f"<b><emoji id={gagal}>❎</emoji> ᴍᴀᴘᴘɪɴɢ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>")

    except Exception as error:
        await msg.edit(str(error))
