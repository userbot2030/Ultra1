from .. import *




@PY.UBOT("getblacklist", FILTERS.ME_OWNER)
async def _(client, message):
    await get_blacklist(client, message)


@PY.BOT("prem")
@PY.UBOT("prem")
async def _(client, message):
    await prem_user(client, message)


@PY.BOT("unprem", FILTERS.OWNER)
@PY.UBOT("unprem", FILTERS.ME_OWNER)
async def _(client, message):
    await unprem_user(client, message)


@PY.UBOT("getprem", FILTERS.OWNER)
@PY.UBOT("getprem", FILTERS.ME_OWNER)
async def _(cliebt, message):
    await get_prem_user(client, message)


@PY.BOT("seles", FILTERS.OWNER)
@PY.UBOT("seles", FILTERS.ME_OWNER)
async def _(client, message):
    await seles_user(client, message)


@PY.BOT("unseles", FILTERS.OWNER)
@PY.UBOT("unseles", PREFIX, FILTERS.ME_OWNER)
async def _(client, message):
    await unseles_user(client, message)


@PY.BOT("getseles", FILTERS.OWNER)
@PY.UBOT("getseles", FILTERS.ME_OWNER)
async def _(client, message):
    await get_seles_user(client, message)


@PY.BOT("time", FILTERS.OWNER)
@PY.UBOT("time", FILTERS.ME_OWNER)
async def _(client, message):
    await expired_add(client, message)


@PY.BOT("cek", FILTERS.OWNER)
@PY.UBOT("cek", FILTERS.ME_OWNER)
async def _(client, message):
    await expired_cek(client, message)
