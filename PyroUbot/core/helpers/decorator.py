from pyrogram.enums import ChatType

from PyroUbot import OWNER_ID, bot, ubot


async def install_my_peer(client):
    try:
        users = []
        group = []
        async for dialog in client.get_dialogs():
            if dialog.chat.type == ChatType.PRIVATE:
                users.append(dialog.chat.id)
            if dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
                group.append(dialog.chat.id)
            client._get_my_peer[client.me.id] = {"pm": users, "gc": group}
    except Exception as error:
        print(f"Error occurred: {error}")


async def install_all_peer():
    for client in ubot._ubot:
        await install_my_peer(client)
        print(f"[𝗜𝗡𝗙𝗢] - ({client.me.id}) - 𝗜𝗡𝗦𝗧𝗔𝗟𝗟 𝗨𝗕𝗢𝗧._𝗚𝗘𝗧_𝗠𝗬_𝗣𝗘𝗘𝗥")
    await bot.send_message(OWNER_ID, "✅ sᴇᴍᴜᴀ ᴘᴇᴇʀ_ɪᴅ ʙᴇʀʜᴀsɪʟ ᴅɪɪɴsᴛᴀʟʟ")
