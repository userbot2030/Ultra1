import asyncio

from pyrogram.errors import RPCError
from pyrogram.methods.utilities.idle import idle

from PyroUbot import (Ubot, bot, check_expired_userbots, get_chat,
                      get_userbots, install_all_peer, loadPlugins,
                      rem_expired_date, remove_chat, remove_ubot, rm_all, ubot)


async def start_ubot(ubot_id):
    ubot_ = Ubot(**ubot_id)
    try:
        await asyncio.wait_for(ubot_.start(), timeout=30)
    except asyncio.TimeoutError:
        print(f"[𝗜𝗡𝗙𝗢] - ({ubot_id['name']}) 𝗧𝗜𝗗𝗔𝗞 𝗗𝗔𝗣𝗔𝗧 𝗠𝗘𝗥𝗘𝗦𝗣𝗢𝗡")
    except RPCError:
        await remove_ubot(int(ubot_id["name"]))
        await rm_all(int(ubot_id["name"]))
        await rem_expired_date(int(ubot_id["name"]))
        for X in await get_chat(int(ubot_id["name"])):
            await remove_chat(int(ubot_id["name"]), X)
        print(f"✅ {ubot_id['name']} 𝗕𝗘𝗥𝗛𝗔𝗦𝗜𝗟 𝗗𝗜𝗛𝗔𝗣𝗨𝗦")


async def main():
    await asyncio.gather()
    userbots = await get_userbots()
    tasks = [start_ubot(ubot_id) for ubot_id in userbots]
    await asyncio.gather(
        idle(),
        check_expired_userbots(),
        install_all_peer(),
        loadPlugins(),
        *tasks,
        ubot.start(),
        bot.start(),
    )


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
