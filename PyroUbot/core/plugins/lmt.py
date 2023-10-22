from asyncio import sleep

from pyrogram.raw.functions.messages import DeleteHistory, StartBot
from PyroUbot import *

async def limit_cmd(client, message):
    await client.unblock_user("SpamBot")
    bot_info = await client.resolve_peer("SpamBot")
    if client.me.is_premium:
    msg = await message.reply("<emoji>{emot_proses}>😘</emoji><code>ᴘʀᴏᴄᴇssɪɴɢ ᴋᴀʟᴏ ʟɪᴍɪᴛ ᴊᴀɴɢᴀɴ ꜱᴀʟᴀʜɪɴ ɢᴜᴀ ʏᴀ . . .</code>")
    response = await client.invoke(
        StartBot(
            bot=bot_info,
            peer=bot_info,
            random_id=client.rnd_id(),
            start_param="start",
        )
    )
    
    await sleep(1)
    await msg.delete()
    status = await client.get_messages("SpamBot", response.updates[1].message.id + 1)
    await status.copy(message.chat.id, reply_to_message_id=message.id)
    return await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))
