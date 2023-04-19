from asyncio import get_event_loop_policy

from pyrogram.enums import ChatType
from pyrogram.errors import RPCError
from pyrogram.methods.utilities.idle import idle

from PyroUbot import *


async def main():
    await bot.start()
    await ubot.start()
    get_my_id.append(ubot.me.id)
    users = 0
    group = 0
    async for dialog in ubot.get_dialogs():
        if dialog.chat.type == ChatType.PRIVATE:
            users += 1
        elif dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
            group += 1
    get_my_peer[ubot.me.id] = {"group": group, "users": users}
    for _ubot in await get_userbots():
        ubot_ = Ubot(**_ubot)
        try:
            await ubot_.start()
            get_my_id.append(ubot_.me.id)
            users = 0
            group = 0
            async for dialog in ubot_.get_dialogs():
                if dialog.chat.type == ChatType.PRIVATE:
                    users += 1
                elif dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
                    group += 1
            get_my_peer[ubot_.me.id] = {"group": group, "users": users}
        except RPCError:
            await remove_ubot(int(_ubot["name"]))
            await rm_all(int(_ubot["name"]))
            await bot.send_message(OWNER_ID, f"✅ {_ubot['name']} Dihapus Dari Database")
            await rem_expired_date(int(_ubot["name"]))
            print(f"✅ {_ubot['name']} Dihapus Dari Database")
    await loadPlugins()
    await premium()
    await idle()


if __name__ == "__main__":
    get_event_loop_policy().get_event_loop().run_until_complete(main())
