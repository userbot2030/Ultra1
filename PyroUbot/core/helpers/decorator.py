import asyncio

from pyrogram.enums import ChatType

from PyroUbot import OWNER_ID, bot, ubot


async def install_my_peer(client):
    users = []
    groups = []
    try:
        async for dialog in client.get_dialogs():
            if dialog.chat.type == ChatType.PRIVATE:
                users.append(dialog.chat.id)
            elif dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
                groups.append(dialog.chat.id)
            client._get_my_peer[client.me.id] = {"pm": users, "gc": groups}
    except Exception as E:
        print(f"ERROR: {E}")


async def install_all_peer():
    tasks = []
    for client in ubot._ubot:
        tasks.append(install_my_peer(client))
    await asyncio.gather(*tasks)
    await bot.send_message(OWNER_ID, "✅ sᴇᴍᴜᴀ ᴘᴇᴇʀ_ɪᴅ ʙᴇʀʜᴀsɪʟ ᴅɪɪɴsᴛᴀʟʟ")
