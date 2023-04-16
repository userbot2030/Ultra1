import logging
from typing import Callable

from pyrogram import Client
from pyrogram.enums import ParseMode
from pyrogram.handlers import MessageHandler
from pyromod import listen
from rich.logging import RichHandler

from ..config import *

logging.basicConfig(
    level=logging.INFO,
    format="%(filename)s:%(lineno)s %(levelname)s: %(message)s",
    datefmt="%m-%d %H:%M",
    handlers=[RichHandler()],
)
console = logging.StreamHandler()
console.setLevel(logging.ERROR)
console.setFormatter(
    logging.Formatter("%(filename)s:%(lineno)s %(levelname)s: %(message)s")
)
logging.getLogger("").addHandler(console)


bot = Client(
    name="PyroBot",
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
    name="PyroUbot",
    api_id=API_ID,
    api_hash=APi_HASH,
    session_string=SESSION_STRING,
)


get_my_id = []
get_my_peer = {}

from ..core.database import *
from ..core.function import *
from ..core.helders import *
from ..core.other import *
