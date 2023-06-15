import logging
import os

from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyromod import listen
from rich.logging import RichHandler

from PyroUbot.config import *


def handle_connection_lost(record):
    for x in ["Connection", "timed"]:
        if X in record.getMessage():
            os.system(
                f"kill -9 {os.getpid()} && rm -rf *.session* && python3 -m PyroUbot"
            )


logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%m-%d %H:%M",
)

console = logging.StreamHandler()
console.setLevel(logging.ERROR)
console.setFormatter(
    logging.Formatter("%(filename)s:%(lineno)s %(levelname)s: %(message)s")
)

root_logger = logging.getLogger()
root_logger.addHandler(RichHandler())
root_logger.addHandler(console)
root_logger.addFilter(handle_connection_lost)


class Bot(Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_message(self, filters=None, group=-1):
        def decorator(func):
            for ub in self._ubot:
                ub.add_handler(MessageHandler(func, filters), group)
            return func

        return decorator

    async def start(self):
        await super().start()
        self._ubot.append(self)
        self._get_my_id.append(self.me.id)
        self._translate[self.me.id] = {"negara": "id"}
        print(f"[𝐈𝐍𝐅𝐎] - ({self.me.id}) - 𝐒𝐓𝐀𝐑𝐓𝐄𝐃")


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
