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
