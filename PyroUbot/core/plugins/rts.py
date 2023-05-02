import importlib
import random
from datetime import datetime, timedelta

from pytz import timezone

from .. import *
from ..modules import loadModule


async def login_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply(
            f"<code>{message.text}</code> <b>sᴛʀɪɴɢ ᴘʏʀᴏɢʀᴀᴍ</b>"
        )
    try:
        ub = Ubot(
            name=f"ubot{random.randrange(9999)}",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=message.command[1],
        )
        await ub.start()
        now = datetime.now(timezone("Asia/Jakarta"))
        expire_date = now + timedelta(days=30)
        await set_expired_date(ub.me.id, expire_date)
        await add_ubot(
            user_id=int(ub.me.id),
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=message.command[1],
        )
        for mod in loadModule():
            importlib.reload(importlib.import_module(f"PyroUbot.modules.{mod}"))
        return await message.reply(
            f"<b>✅ ʙᴇʀʜᴀsɪʟ ʟᴏɢɪɴ ᴅɪ ᴀᴋᴜɴ: <a href='tg://user?id={ub.me.id}'>{ub.me.first_name} {ub.me.last_name or ''}</a></b>"
        )
    except Exception as error:
        return await message.reply(f"<code>{error}</code>")


async def restart_cmd(client, message):
    msg = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ</b>")
    for X in ubot._ubot:
        if message.from_user.id == X.me.id:
            for _ubot_ in await get_userbots():
                if X.me.id == int(_ubot_["name"]):
                    try:
                        ubot._ubot.remove(X)
                        UB = Ubot(**_ubot_)
                        await UB.start()
                        for mod in loadModule():
                            importlib.reload(
                                importlib.import_module(f"PyroUbot.modules.{mod}")
                            )
                        return await msg.edit(
                            f"<b>✅ ʀᴇsᴛᴀʀᴛ ʙᴇʀʜᴀsɪʟ ᴅɪʟᴀᴋᴜᴋᴀɴ {UB.me.first_name} {UB.me.last_name or ''} | {UB.me.id}</b>"
                        )
                    except Exception as error:
                        return await msg.edit(f"<b>{error}</b>")
