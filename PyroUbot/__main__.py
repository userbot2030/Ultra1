import asyncio

from pyrogram.errors import RPCError

from PyroUbot import (Ubot, bot, check_expired_userbots, get_chat,
                      get_userbots, install_all_peer, loadPlugins,
                      rem_expired_date, remove_chat, remove_ubot, rm_all, ubot)


async def main():
    await asyncio.gather(ubot.start(), bot.start())
    for _ubot in await get_userbots():
        user_id = int(_ubot["name"])
        ubot_ = Ubot(**_ubot)
        try:
            await asyncio.wait_for(ubot_.start(), timeout=30)
        except asyncio.TimeoutError:
            print(f"[𝗜𝗡𝗙𝗢] - ({user_id}) 𝗧𝗜𝗗𝗔𝗞 𝗗𝗔𝗣𝗔𝗧 𝗠𝗘𝗥𝗘𝗦𝗣𝗢𝗡")
        except RPCError:
            await remove_ubot(user_id)
            await rm_all(user_id)
            await rem_expired_date(user_id)
            for X in await get_chat(user_id):
                await remove_chat(user_id, X)
            print(f"✅ {user_id} 𝗕𝗘𝗥𝗛𝗔𝗦𝗜𝗟 𝗗𝗜𝗛𝗔𝗣𝗨𝗦")
    await asyncio.gather(
        loadPlugins(), check_expired_userbots(), install_all_peer(), vidle()
    )


if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())
