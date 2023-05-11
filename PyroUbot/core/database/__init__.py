from motor.motor_asyncio import AsyncIOMotorClient

from PyroUbot.config import MONGO_URL

mongo_client = AsyncIOMotorClient(MONGO_URL)
mongodb = mongo_client.pyro_ubot

from .core.database.expired import *
from .core.database.notes import *
from .core.database.premium import *
from .core.database.reseller import *
from .core.database.saved import *
from .core.database.userbot import *
