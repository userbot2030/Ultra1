import importlib
from asyncio import get_event_loop_policy

from pyrogram.methods.utilities.idle import idle

from PyroUbot import *
from PyroUbot.modules import loadModule


async def main():
    await bot.start()
    await ubot.start()
    for mod in loadModule():
        importlib.reload(importlib.import_module(f"PyroUbot.modules.{mod}"))
    for _ubot in await get_userbots():
        ubot_ = Ubot(**_ubot)
        try:
            await ubot_.start()
            for mod in loadModule():
                importlib.reload(importlib.import_module(f"PyroUbot.modules.{mod}"))
        except RPCError:
            await remove_ubot(int(_ubot["name"]))
            await rm_all(int(_ubot["name"]))
            await rem_expired_date(int(_ubot["name"]))
            await bot.send_message(OWNER_ID, f"✅ {_ubot['name']} Dihapus Dari Database")
            print(f"✅ {_ubot['name']} Dihapus Dari Database")
    await install_user_id()
    await loadPlugins()
    await expired_userbot()
    await idle()


if __name__ == "__main__":
    get_event_loop_policy().get_event_loop().run_until_complete(main())
