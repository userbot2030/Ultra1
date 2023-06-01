import asyncio

from pyrogram.raw.functions.messages import DeleteHistory

from PyroUbot import *


async def quotly_cmd(self, ctx):
    if len(ctx.text.split()) > 1:
        check_arg = isArgInt(ctx.command[1])
        if check_arg[0]:
            if check_arg[1] < 2 or check_arg[1] > 10:
                return await message.reply(
                    "<code>Argumen yang anda berikan salah...</code>", del_in=6
                )
            try:
                messages = [
                    i
                    for i in await self.get_messages(
                        chat_id=ctx.chat.id,
                        message_ids=range(
                            ctx.reply_to_message.id,
                            ctx.reply_to_message.id + (check_arg[1]),
                        ),
                        replies=-1,
                    )
                    if not i.empty and not i.media
                ]
            except Exception as e:
                return await ctx.reply(f"<code>Error : {e}</code>")
            try:
                make_quotly = await pyrogram_to_quotly(messages)
                bio_sticker = BytesIO(make_quotly)
                bio_sticker.name = "biosticker.webp"
                return await ctx.reply_sticker(bio_sticker)
            except Exception as e:
                return await ctx.reply(f"<code>Error : {e}</code>")
    try:
        messages_one = await self.get_messages(
            chat_id=ctx.chat.id, message_ids=ctx.reply_to_message.id, replies=-1
        )
        messages = [messages_one]
    except Exception as e:
        return await ctx.reply(f"<code>Error : {e}</code>")
    try:
        make_quotly = await pyrogram_to_quotly(messages)
        bio_sticker = BytesIO(make_quotly)
        bio_sticker.name = "biosticker.webp"
        return await ctx.reply_sticker(bio_sticker)
    except Exception as e:
        return await ctx.reply(f"<code>Error : {e}</code>")


async def quotly_cmd_test(client, message):
    info = await message.reply("<b>ᴍᴇᴍᴘʀᴏsᴇs.....</b>", quote=True)
    if message.reply_to_message:
        if len(message.command) < 2:
            msg = [message.reply_to_message]
        else:
            try:
                count = int(message.command[1])
            except Exception as error:
                await info.edit(error)
            msg = [
                i
                for i in await client.get_messages(
                    chat_id=message.chat.id,
                    message_ids=range(
                        message.reply_to_message.id, message.reply_to_message.id + count
                    ),
                    replies=-1,
                )
            ]
        await client.unblock_user("@QuotLyBot")
        for x in msg:
            await x.forward("@QuotLyBot")
        await asyncio.sleep(5)
        await info.delete()
        async for quotly in client.get_chat_history("@QuotLyBot", limit=1):
            if not quotly.sticker:
                await message.reply(
                    f"❌ @QuotLyBot ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇʀᴇsᴘᴏɴ ᴘᴇʀᴍɪɴᴛᴀᴀɴ", quote=True
                )
            else:
                await message.reply_sticker(quotly.sticker.file_id)
        user_info = await client.resolve_peer("@QuotLyBot")
        return await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))
