import logging

from pyrogram import Client, filters
from pyrogram.enums import ChatType, ParseMode
from pyrogram.handlers import MessageHandler
from pyromod import listen

from PyroUbot.config import *

logging.basicConfig(
    level=logging.INFO,
    format="%(filename)s:%(lineno)s %(levelname)s: %(message)s",
    datefmt="%m-%d %H:%M",
    handlers=[logging.StreamHandler()],
)


class Bot(Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_message(self):
        def decorator(func, filter=filters.Filter, group=-1):
            self.add_handler(MessageHandler(func, filter), group)
            return func

        return decorator

    async def start(self):
        await super().start()
        print(f"STARTED BOT {self.me.first_name} | {self.me.id}")


class Ubot(Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._ubot = []
        self._get_my_id = []
        self._translate = {}
        self._get_my_peer = {}

    def on_message(self):
        def decorator(func, filter=filters.Filter, group=-1):
            for ub in self._ubot:
                ub.add_handler(MessageHandler(func, filter), group)
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
            print(f"STARTED UBOT {self.me.first_name} | {self.me.id}")


bot = Bot(
    name=BOT_TOKEN.split(":")[0],
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

ubot = Ubot(
    name=OWNER_ID,
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
)


from PyroUbot.core.database import *
from PyroUbot.core.function import *
from PyroUbot.core.helpers import *
from PyroUbot.core.plugins import *
