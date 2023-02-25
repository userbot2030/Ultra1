from motor.motor_asyncio import AsyncIOMotorClient
from PyroUbot.config import MONGO_URL

mongo_client = AsyncIOMotorClient(MONGO_URL)
mongodb = mongo_client.pyro_ubot

from PyroUbot.core.database.notes import *
from PyroUbot.core.database.premium import *
from PyroUbot.core.database.reseller import *
from PyroUbot.core.database.saved import *
from PyroUbot.core.database.userbot import *
