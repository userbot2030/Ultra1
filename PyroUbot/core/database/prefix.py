from PyroUbot.core.database import mongo_client

prefixes = mongo_client["PyroUbot"]["prefixes"]


def get_pref(user_id):
    user = prefixes.users.find_one({"_id": user_id})
    if user:
        return user.get("expire_date")
    else:
        return None


def set_pref(user_id, expire_date):
    prefixes.users.update_one(
        {"_id": user_id}, {"$set": {"expire_date": expire_date}}, upsert=True
    )


def rem__pref(user_id):
    prefixes.users.update_one(
        {"_id": user_id}, {"$unset": {"expire_date": ""}}, upsert=True
    )
