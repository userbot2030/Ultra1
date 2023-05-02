import asyncio

from pyrogram.enums import MessagesFilter
from pyrogram.raw.functions.messages import DeleteHistory


async def sosmed_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply(
            f"<code>{message.text}</code> ʟɪɴᴋ ʏᴛ/ɪɢ/ꜰʙ/ᴛᴡ/ᴛɪᴋᴛᴏᴋ"
        )
    else:
        bot = "thisvidbot"
        link = message.text.split()[1]
        await client.unblock_user(bot)
        Tm = await message.reply("<code>ᴘʀᴏᴄᴇssɪɴɢ . . .</code>")
        xnxx = await client.send_message(bot, link)
        await xnxx.delete()
        await asyncio.sleep(10)
        try:
            async for sosmed in client.search_messages(
                bot, filter=MessagesFilter.VIDEO
            ):
                if sosmed.video:
                    await sosmed.copy(
                        message.chat.id,
                        caption=f"<b>ᴜᴘʟᴏᴀᴅ ʙʏ <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a></b>",
                        reply_to_message_id=message.id,
                    )
                    await Tm.delete()
        except Exception:
            await Tm.edit(
                "<b>ᴠɪᴅᴇᴏ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ sɪʟᴀʜᴋᴀɴ ᴜʟᴀɴɢɪ ʙᴇʙᴇʀᴀᴘᴀ sᴀᴀᴛ ʟᴀɢɪ</b>"
            )
        user_info = await client.resolve_peer(bot)
        return await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))
