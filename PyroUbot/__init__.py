import logging

from pyrogram import Client
from pyrogram.filters import Filter
from pyrogram.handlers import MessageHandler
from pyromod import listen
from rich.logging import RichHandler

from PyroUbot.config import *

logging.basicConfig(
    level=logging.INFO,
    format="%(filename)s: %(lineno)s: %(levelname)s: %(message)s",
    datefmt="%m-%d %H:%M",
    handlers=[RichHandler()],
)
console = logging.StreamHandler()
console.setLevel(logging.ERROR)
console.setFormatter(Formatter("%(filename)s: %(lineno)s: %(levelname)s: %(message)s"))
logging.getLogger("").addHandler(console)


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
        print(f"({self.me.id} started")


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
            print(f"({self.me.id}) started")


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
