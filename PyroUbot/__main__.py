import asyncio
import threading

from pyrogram.methods.utilities.idle import idle

from PyroUbot import *


async def main():
    await threading.Thread(target=bot.start).start()
    await threading.Thread(target=ubot.start).start()
    for _ubot in await get_userbots():
        ubot_ = Ubot(**_ubot)
        try:
            await ubot_.start()
        except:
            user_id = int(_ubot["name"])
            await remove_ubot(user_id)
            await rm_all(user_id)
            await rem_expired_date(user_id)
            for X in await get_chat(user_id):
                await remove_chat(user_id, X)
            print(f"✅ {user_id} ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs")
    await loadPlugins()
    await install_all_peer()
    await install_user_id()
    await expired_userbot()
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop_policy().get_event_loop().run_until_complete(main())
