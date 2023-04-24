import logging
from typing import Callable

from pyrogram import Client, filters
from pyrogram.enums import ChatType, ParseMode
from pyrogram.handlers import MessageHandler
from pyromod import listen
from rich.logging import RichHandler

from .config import *

logging.basicConfig(
    level=logging.WARNING,
    format="%(filename)s:%(lineno)s %(levelname)s: %(message)s",
    datefmt="%m-%d %H:%M",
    handlers=[RichHandler(), logging.FileHandler(filename="logs.txt")],
)
console = logging.StreamHandler()
console.setLevel(logging.ERROR)
console.setFormatter(
    logging.Formatter("%(filename)s:%(lineno)s %(levelname)s: %(message)s")
)
logging.getLogger("").addHandler(console)


class Bot(Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs, parse_mode=ParseMode.HTML)

    def on_message(self, filters: filters.Filter):
        def decorator(func):
            for b in self._bot:
                b.add_handler(MessageHandler(func, filters), -1)
            return func

        return decorator

    async def start(self):
        await super().start()
        print(f"STARTED BOT {self.me.first_name} | {self.me.id}")


class Ubot(Client):
    _ubot = []
    _get_my_id = []
    _get_my_peer = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs, parse_mode=ParseMode.HTML)

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
            self.get_my_id.append(self.me.id)
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
    name="PyroBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

ubot = Ubot()

from .core.database import *
from .core.function import *
from .core.helpers import *
