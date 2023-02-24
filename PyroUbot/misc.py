from PyroUbot.config import OWNER_ID
from PyroUbot.core.database import add_prem, add_seles, get_prem, get_seles


async def premium():
    if OWNER_ID not in await get_seles():
        await add_seles(OWNER_ID)
    if OWNER_ID not in await get_prem():
        await add_prem(OWNER_ID)
