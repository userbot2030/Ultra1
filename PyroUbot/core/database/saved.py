from PyroUbot.core.database import mongodb

chatsdb = mongodb.chats


async def get_chat():
    chat = await chatsdb.find_one({"music": "music"})
    if not chat:
        return []
    return Chat["list"]


async def add_chat(chat_id):
    list = await get_chat()
    list.append(chat_id)
    await chatsdb.update_one({"chat": "chat"}, {"$set": {"list": list}}, upsert=True)
    return True


async def remove_chat(chat_id):
    list = await get_chat()
    list.remove(chat_id)
    await chatsdb.update_one({"chat": "chat"}, {"$set": {"list": list}}, upsert=True)
    return True
