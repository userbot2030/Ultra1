import logging

from pyrogram import Client
from pyrogram.enums import ChatType
from pyrogram.filters import Filter
from pyrogram.handlers import MessageHandler
from pyromod import listen

from PyroUbot.config import *
from PyroUbot.modules import loadModule

logging.basicConfig(
    level=logging.ERROR,
    format="%(filename)s:%(lineno)s %(levelname)s: %(message)s",
    datefmt="%m-%d %H:%M",
    handlers=[logging.StreamHandler()],
)

get_my_peer = {}

async def get_peer_userbot(self):
    users = 0
    group = 0
    async for dialog in self.get_dialogs():
        if dialog.chat.type == ChatType.PRIVATE:
            users += 1
        elif dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
            group += 1
    get_my_peer[self.me.id] = {"pm": users, "gc": group}
    
    


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
        print(f"({self.me.id}b started")


class Ubot(Client):
    _ubot = []
    _get_my_id = []
    _translate = {}

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


async def install_my_peer():
    for X in ubot._ubot:
        await get_peer_userbot(X)


from PyroUbot.core.database import *
from PyroUbot.core.function import *
from PyroUbot.core.helpers import *
from PyroUbot.core.plugins import *
