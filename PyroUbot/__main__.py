from asyncio import get_event_loop_policy

from pyrogram.methods.utilities.idle import idle

from PyroUbot import *


async def main():
    await bot.start()
    await ubot.start()
    for _ubot in await get_userbots():
        ubot_ = Ubot(**_ubot)
        try:
            await ubot_.start()
        except RPCError:
            await remove_ubot(int(_ubot["name"]))
            await rm_all(int(_ubot["name"]))
            await rem_expired_date(int(_ubot["name"]))
            for X in await get_chat(int(_ubot["name"])):
                await remove_chat(int(_ubot["name"]), X)
            await bot.send_message(OWNER_ID, f"✅ {_ubot['name']} Dihapus Dari Database")
            print(f"✅ {_ubot['name']} Dihapus Dari Database")
    await loadPlugins()
    await expired_userbot()
    await install_user_id()
    await install_my_peer()
    await bot.send_message(OWNER_ID, "Install peer id telah selesai")
    await idle()


if __name__ == "__main__":
    get_event_loop_policy().get_event_loop().run_until_complete(main())
