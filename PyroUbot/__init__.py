import logging

from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyromod import listen

from PyroUbot.config import *

import logging
import sys
from rich.logging import RichHandler

def handle_exception(exc_type, exc_value, exc_traceback):
    if "Connecting lost" in str(exc_value):
        print("Koneksi terputus. Menghentikan sistem...")
        os.system(f"kill -9 {os.getpid()} && git pull && python3 -m PyroUbot")
    else:
        os.system(f"kill -9 {os.getpid()} && git  && python3 -m PyroUbot")

sys.excepthook = handle_exception

logging.basicConfig(
    level=logging.ERROR,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%m-%d %H:%M",
    handlers=logging.StreamHandler()],
)

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
