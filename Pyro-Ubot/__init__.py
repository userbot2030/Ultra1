import random
from logging import *

from pyrogram import Client
from pyrogram.enums import ParseMode
from pyrogram.handlers import MessageHandler
from rich.logging import RichHandler

from Pyro-Ubot.config import API_ID, API_HASH, BOT_TOKEN, SESSION_STRING

basicConfig(
    level=INFO,
    format="%(filename)s:%(lineno)s %(levelname)s: %(message)s",
    datefmt="%m-%d %H:%M",
    handlers=[RichHandler()],
)
console = StreamHandler()
console.setLevel(ERROR)
console.setFormatter(Formatter("%(filename)s:%(lineno)s %(levelname)s: %(message)s"))
getLogger("").addHandler(console)


bot = Client(
    name=int(random.randrange(999999)),
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    parse_mode=ParseMode.HTML,
)


class Ubot(Client):
    __module__ = "pyrogram.client"
    _ubot = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs, parse_mode=ParseMode.HTML)

    def on_message(self, filters=None, group=0):
        def decorator(func):
            for ub in self._ubot:
                ub.add_handler(MessageHandler(func, filters), group)
            return func

        return decorator

    async def start(self):
        await super().start()
        if self not in self._ubot:
            self._ubot.append(self)


ubot = Ubot(
    name=int(random.randrange(999999)),
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
)

get_my_id = []
