import logging

from pyrogram import Client
from pyrogram.enums import ChatType, ParseMode
from pyrogram.filters import Filter
from pyrogram.handlers import MessageHandler
from pyromod import listen

from PyroUbot.config import *
from PyroUbot.modules import loadModule
logging.basicConfig(
    level=logging.ERROR,
    format="%(filename)s:%(lineno)s %(levelname)s: %(message)s",
    datefmt="%m-%d %H:%M",
    handlers=[logging.StreamHandler()],
)


class Bot(Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_message(self, filters=Filter, group=-1):
        def decorator(func):
            self.add_handler(MessageHandler(func, filters), group)
            return func

        return decorator

    async def start(self):
        await super().start()
        for mod in loadModule():
            importlib.reload(importlib.import_module(f"PyroUbot.modules.{mod}"))
        print(f"STARTED BOT {self.me.first_name} | {self.me.id}")


class Ubot(Client):
    _ubot = []
    _get_my_id = []
    _translate = {}
    _get_my_peer = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_message(self, filters=Filter, group=-1):
        def decorator(func):
            for ub in self._ubot:
                ub.add_handler(MessageHandler(func, filters), group)
            return func

        return decorator

    async def start(self):
        await super().start()
        if self not in self._ubot:
            self._ubot.append(self)
            self._get_my_id.append(self.me.id)
            self._translate[self.me.id] = {"negara": "id"}
            users = 0
            group = 0
            async for dialog in self.get_dialogs():
                if dialog.chat.type == ChatType.PRIVATE:
                    users += 1
                elif dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
                    group += 1
            self._get_my_peer[self.me.id] = {"group": group, "users": users}
        for mod in loadModule():
            importlib.reload(importlib.import_module(f"PyroUbot.modules.{mod}"))
            print(
                f"STARTED UBOT {self.me.first_name}  {self.me.last_name or ''} | {self.me.id}"
            )


bot = Bot(
    name="Bot-Premium",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

ubot = Ubot(
    name="Ubot-Premium",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
)


from PyroUbot.core.database import *
from PyroUbot.core.function import *
from PyroUbot.core.helpers import *
from PyroUbot.core.plugins import *
