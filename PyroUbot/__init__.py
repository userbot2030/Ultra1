import logging
import os

from pyrogram import Client
from pyrogram.enums import ParseMode
from pyrogram.handlers import MessageHandler
from pyromod import listen

from PyroUbot.config import *


class ConnectionHandler(logging.Handler):
    def emit(self, record):
        for X in ["OSErro", "socket"]:
            if X in record.getMessage():
                os.system(f"kill -9 {os.getpid()} && python3 -m PyroUbot")


logger = logging.getLogger()
logger.setLevel(logging.ERROR)

formatter = logging.Formatter("[%(levelname)s] - %(name)s - %(message)s", "%d-%b %H:%M")
stream_handler = logging.StreamHandler()

stream_handler.setFormatter(formatter)
connection_handler = ConnectionHandler()

logger.addHandler(stream_handler)
logger.addHandler(connection_handler)


class Bot(Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs, parse_mode=ParseMode.HTML)

    def on_message(self, filters=None, group=-1):
        def decorator(func):
            self.add_handler(MessageHandler(func, filters), group)
            return func

        return decorator

    async def start(self):
        await super().start()


class Ubot(Client):
    _ubot = []
    _get_my_id = []
    _translate = {}
    _get_my_peer = {}
    _prefix = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs, parse_mode=ParseMode.HTML)

    def on_message(self, filters=None, group=-1):
        def decorator(func):
            for ub in self._ubot:
                ub.add_handler(MessageHandler(func, filters), group)
            return func

        return decorator

    def set_prefix(self, prefix):
        self._prefix[self.me.id] = prefix

    def get_prefix(self):
        for ub in self._ubot:
            self._prefix[ub.me.id]
        return

    async def start(self):
        await super().start()
        handler = await get_pref(self.me.id)
        if handler:
            self._prefix[self.me.id] = handler
        else:
            self._prefix[self.me.id] = "."
        self._ubot.append(self)
        self._get_my_id.append(self.me.id)
        self._translate[self.me.id] = {"negara": "id"}
        print(f"[𝐈𝐍𝐅𝐎] - ({self.me.id}) - 𝐒𝐓𝐀𝐑𝐓𝐄𝐃")


bot = Bot(
    name="bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

ubot = Ubot(
    name="ubot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
)


from PyroUbot.core.database import *
from PyroUbot.core.function import *
from PyroUbot.core.helpers import *
from PyroUbot.core.plugins import *
