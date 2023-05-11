from motor.motor_asyncio import AsyncIOMotorClient

from PyroUbot.config import MONGO_URL

mongo_client = AsyncIOMotorClient(MONGO_URL)
mongodb = mongo_client.pyro_ubot

from ..database.expired import *
from ..database.notes import *
from ..database.premium import *
from ..database.reseller import *
from ..database.saved import *
from ..database.userbot import *
