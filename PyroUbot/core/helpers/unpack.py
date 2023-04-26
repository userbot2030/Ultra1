from base64 import urlsafe_b64decode
from struct import unpack

from attrify import Attrify as Atr
from gc import get_objects

from pykeyboard import InlineKeyboard
from pyrogram.types import (
    InlineKeyboardButton,
    InlineQueryResultArticle,
    InputTextMessageContent,
)

def unpackInlineMessage(inline_message_id: str):
    dc_id, message_id, chat_id, query_id = unpack(
        "<iiiq",
        urlsafe_b64decode(
            inline_message_id + "=" * (len(inline_message_id) % 4),
        ),
    )
    temp = {
        "dc_id": dc_id,
        "message_id": message_id,
        "chat_id": int(str(chat_id).replace("-1", "-1001")),
        "query_id": query_id,
        "inline_message_id": inline_message_id,
    }
    return Atr(temp)



async def create_button(m):
    buttons = InlineKeyboard(row_width=2)
    keyboard = []
    if "|" not in m.text.split(None, 1)[1]:
        msg = []
        for X in m.text.split(None, 1)[1].split():
            keyboard.append(
                InlineKeyboardButton(X.split(":", 1)[0], url=X.split(":", 1)[1])
            )
            msg.append(X.split(":")[0])
        buttons.add(*keyboard)
        if m.reply_to_message:
            text_or_rep = m.reply_to_message.text
        else:
            msg_text = ""
            for Z in msg:
                msg_text += f"{Z} "
            text_or_rep = msg_text
    else:
        for X in m.text.split("|", 1)[1].split():
            keyboard.append(
                InlineKeyboardButton(X.split(":", 1)[0], url=X.split(":", 1)[1])
            )
        buttons.add(*keyboard)
        text_or_rep = m.text.split("|", 1)[0].split(None, 1)[1]
    return buttons, text_or_rep
