from PytoUbot.core.database import mongo_client

collection = mongo_client["PyroUbot"]["notes"]


async def get_note(user_id, note_name):
    result = await collection.find_one({"_id": user_id})
    if result is not None:
        try:
            note_id = result["notes"][note_name]
            return note_id
        except KeyError:
            return None
    else:
        return None


async def rm_note(user_id, note_name):
    await collection.update_one(
        {"_id": user_id}, {"$unset": {f"notes.{note_name}": ""}}
    )


async def all_notes(user_id):
    results = await collection.find_one({"_id": user_id})
    try:
        notes_dic = results["notes"]
        key_list = notes_dic.keys()
        return key_list
    except:
        return None
