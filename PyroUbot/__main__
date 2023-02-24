from asyncio import get_event_loop_policy

from pyrogram.errors import RPCError
from pyrogram.methods.utilities.idle import idle

from PyroUbot import bot, ubot
from PyroUbot.core.functions.plugins import loadPlugins
from PyroUbot.misc import premium
from PyroUbot.core.database.userbot import get_userbots, remove_ubot


async def main():
    await bot.start()
    await ubot.start()
    get_my_id.append(ubot.me.id)
    for _ubot in await get_userbots():
        ubot_ = Ubot(**_ubot)
        try:
            await ubot_.start()
            get_my_id.append(ubot_.me.id)
        except RPCError:
            await remove_ubot(int(_ubot["name"]))
            print(f"✅ {_ubot['name']} Berhasil Dihapus Dari Database")
    await loadPlugins()
    await premium()
    await idle()


if __name__ == "__main__":
    get_event_loop_policy().get_event_loop().run_until_complete(main())
