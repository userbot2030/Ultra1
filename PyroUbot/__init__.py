import importlib
import logging
import sys

from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyromod import listen

from PyroUbot.config import *


def restart_program():
    os.system(f"kill -9 {os.getpid()} && python3 -m PyroUbot")


try:
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)s %(levelname)s: %(message)s",
        datefmt="%m-%d %H:%M",
        handlers=[logging.StreamHandler()],
    )
except Exception as e:
    logging.exception(e)
    logging.error("Terjadi kesalahan. Program akan di-restart.")
    restart_program()


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
        print(f"Userbot ({self.me.id}) Started")


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
