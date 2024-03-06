from asyncio import sleep

from pyrogram.raw.functions.messages import DeleteHistory, StartBot

from PyroUbot import *


async def limit_cmd(client, message):
    await client.unblock_user("SpamBot")
    bot_info = await client.resolve_peer("SpamBot")
    proses = await get_vars(client.me.id, "EMOJI_PROSES") or "5960640164114993927"
    msg = await message.reply(f"<b><emoji id={proses}>⏳</emoji> ᴘʀᴏᴄᴇssɪɴɢ ɴɪʜ ʙʀᴇᴇ. . .</b>")
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
    emoji = "<emoji id=5787188704434982946>✅</emoji>" if status.text.startswith(("Kabar", "Good")) else "<emoji id=5438630285635757876>🔠</emoji>"
    await message.reply(f"{emoji} {status.text}")
    return await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))
