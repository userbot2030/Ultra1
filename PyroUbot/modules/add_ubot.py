from PyroUbot import *


@PY.CALLBACK("bayar_dulu")
async def _(client, callback_query):
    await payment_userbot(client, callback_query)


@PY.CALLBACK("add_ubot")
async def _(client, callback_query):
    await bikin_ubot(client, callback_query)


@PY.CALLBACK("cek_ubot")
@PY.BOT("getubot", FILTERS.OWNER)
async def _(client, message):
    await cek_ubot(client, message)


@PY.CALLBACK("cek_masa_aktif")
async def _(client, callback_query):
    await cek_userbot_expired(client, callback_query)


@PY.CALLBACK("del_ubot")
async def _(client, callback_query):
    await hapus_ubot(client, callback_query)
