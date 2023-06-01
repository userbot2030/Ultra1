messages = [
               i
                    for i in await user.get_messages(
                        chat_id=message.chat.id,
                        message_ids=range(
                            message.reply_to_message.id,
                            message.reply_to_message.id + 1,
                        ),
                        replies=-1,
                    )
                    if not i.empty and not i.media
                ]

await messages.forward(message.chat.id)
