from PyroUbot.core.database import mongo_client

prefixes = mongo_client["PyroUbot"]["prefixes"]


async def get_pref(user_id):
    user = await prefixes.users.find_one({"_id": user_id})
    if user:
        return user.get("prefix")
    else:
        return None


async def set_pref(user_id, expire_date):
    await prefixes.users.update_one(
        {"_id": user_id}, {"$set": {"prefix": expire_date}}, upsert=True
    )


async def rem__pref(user_id):
    await prefixes.users.update_one(
        {"_id": user_id}, {"$unset": {"prefix": ""}}, upsert=True
    )