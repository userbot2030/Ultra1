import logging
from typing import Callable

from pyrogram import Client
from pyrogram.enums import ChatType, ParseMode
from pyrogram.handlers import MessageHandler
from pyromod import listen
from rich.logging import RichHandler

from .config import *

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

get_my_id = []
get_my_peer = {}


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
        get_my_id.append(ubot.me.id)
        users = 0
        group = 0
        async for dialog in self.get_dialogs():
            if dialog.chat.type == ChatType.PRIVATE:
                users += 1
            elif dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
                group += 1
        get_my_peer[ubot.me.id] = {"group": group, "users": users}
        print(
            f"INFO: Started Ubot {self.me.first_name} {self.me.last_name or ''} | {self.me.id}"
        )
        if self not in self._ubot:
            self._ubot.append(self)


ubot = Ubot(
    name="PyroUbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
)

from .core.database import *
from .core.function import *
from .core.helpers import *
from .core.other import *
