import os

import wget

from PyroUbot import *


@PY.UBOT("thumb")
@PY.TOP_CMD
async def _(client, message):
    reply = message.reply_to_message
    msg = await message.reply("<b>🔄 sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs....</b>")

    if len(message.command) < 2:
        return await msg.edit(f"<b>❌ {message.text} ʟɪɴᴋ ᴛᴇʟᴇɢʀᴀᴘʜ</b>")

    elif not message.command[1].endswith((".jpg", ".png")):
        return await msg.edit("<b>ʟɪɴᴋ ʏᴀɴɢ ᴅɪᴍᴀsᴜᴋᴋᴀɴ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ</b>")

    elif reply.video:
        await msg.edit("<b>📥 sᴇʙᴇɴᴛᴀʀ ᴅɪᴅᴏᴡɴʟᴏᴀᴅ ᴅᴜʟᴜ ᴠɪᴅᴇᴏ ɴʏᴀ</b>")
        media = await client.download_media(reply)
        thumbnail = wget.download(message.command[1])

        try:
            await client.send_video(
                message.chat.id,
                video=media,
                thumb=thumbnail,
                duration=reply.video.duration,
                supports_streaming=True,
                caption=reply.caption or "",
            )
            [os.remove(file) for file in (thumbnail, media) if file and os.path.exists(file)]
            return await msg.delete()

        except Exception as error:
            return await msg.edit(str(error))

    else:
        return await msg.edit("<b>ᴍᴀᴀғ, ʜᴀɴʏᴀ ᴠɪᴅᴇᴏ ʏᴀɴɢ ᴅɪᴅᴜᴋᴜɴɢ</b>")
