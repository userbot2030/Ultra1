import os

API_ID = int(os.getenv("API_ID", "17896688"))
API_HASH = os.getenv("API_HASH", "947327cf5ff0053a66bf7951f9db5658")
BOT_TOKEN = os.getenv("BOT_TOKEN", "6345423462:AAG8Wx78NJZt0fYadyOUoD1Nv85MRVqfG9A")
OWNER_ID = int(os.getenv("OWNER_ID", "1948147616"))
LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1001887551242"))
BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001969856888 -1001571197486").split()))
MAX_BOT = int(os.getenv("MAX_BOT", "40"))
RMBG_API = os.getenv("RMBG_API", "b5ZnjZ2nUUpbdEHfcrWdjWbC")
OPENAI_KEY = os.getenv(
    "OPENAI_KEY", "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"
)
MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://musik:7C53Z6w24PRr10oX@db-mongodb-sgp1-75036-98bec1b0.mongo.ondigitalocean.com/admin?tls=true&authSource=admin&replicaSet=db-mongodb-sgp1-75036",
)
