import logging

from aiohttp import ClientSession
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ParseMode
from pyrogram.handlers import MessageHandler
from pyromod import listen

from .config import *

aiosession = ClientSession()

logging.basicConfig(
    level=logging.ERROR,
    format="%(filename)s:%(lineno)s %(levelname)s: %(message)s",
    datefmt="%m-%d %H:%M",
    handlers=[logging.StreamHandler()],
)


class Bot(Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_message(self, filters: filters.Filter):
        def decorator(func):
            self.add_handler(MessageHandler(func, filters), -1)
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

    def on_message(self, filters: filters.Filter):
        def decorator(func):
            for ub in self._ubot:
                ub.add_handler(MessageHandler(func, filters), -1)
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
    name="Bot-PyroBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

ubot = Ubot(
    name="Ubot-PyroBot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
)

from .core.database import *
from .core.function import *
from .core.helpers import *
from .core.plugins import *
