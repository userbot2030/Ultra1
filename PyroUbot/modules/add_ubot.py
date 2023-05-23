from PyroUbot import *


@PY.CALLBACK("bahan")
async def _(client, callback_query):
    await need_api(client, callback_query)


@PY.CALLBACK("add_ubot")
async def _(client, callback_query):
    await bikin_ubot(client, callback_query)


@PY.BOT("getubot")
async def _(client, message):
    await cek_ubot(client, message)


@PY.CALLBACK("cek_masa_aktif")
async def _(client, callback_query):
    await cek_userbot_expired(client, callback_query)


@PY.CALLBACK("del_ubot")
async def _(client, callback_query):
    await hapus_ubot(client, callback_query)
