from pyrogram import filters

from PyroUbot import ubot
from PyroUbot.config import OWNER_ID


class PY:
    def DEVS(command, prefix):
        def wrapper(func):
            @ubot.on_message(
                filters.command(command, prefix) & filters.me & filters.user(OWNER_ID)
            )
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    def UBOT(command, prefix):
        def wrapper(func):
            @ubot.on_message(filters.command(command, prefix) & filters.me)
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper
