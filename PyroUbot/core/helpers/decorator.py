import asyncio

from pyrogram.enums import ChatType

from PyroUbot import OWNER_ID, bot, ubot


async def install_my_peer(client):
    users = []
    groups = []
    async for dialog in client.get_dialogs():
        if dialog.chat.type == ChatType.PRIVATE:
            users.append(dialog.chat.id)
            await asyncio.sleep(5)
        elif dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
            groups.append(dialog.chat.id)
            await asyncio.sleep(5)
        client._get_my_peer[client.me.id] = {"pm": users, "gc": groups}
  

async def installPeer():
    tasks = [install_my_peer(client) for client in ubot._ubot]
    await asyncio.gather(*tasks, return_exceptions=True)
    await bot.send_message(OWNER_ID, "✅ sᴇᴍᴜᴀ ᴘᴇᴇʀ_ɪᴅ ʙᴇʀʜᴀsɪʟ ᴅɪɪɴsᴛᴀʟʟ")
