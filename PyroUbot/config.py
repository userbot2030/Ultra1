import os

API_ID = int(os.getenv("API_ID", "17896688"))
API_HASH = os.getenv("API_HASH", "947327cf5ff0053a66bf7951f9db5658")
BOT_TOKEN = os.getenv("BOT_TOKEN", "6622316489:AAFu3gq8rm1ZZzvPxzg8jsHcosXs9vQ9UAg")
OWNER_ID = int(os.getenv("OWNER_ID", "1948147616"))
LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1001769286350"))
BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001969856888 -1001571197486").split()))
MAX_BOT = int(os.getenv("MAX_BOT", "50"))
RMBG_API = os.getenv("RMBG_API", "b5ZnjZ2nUUpbdEHfcrWdjWbC")
OPENAI_KEY = os.getenv(
    "OPENAI_KEY", "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"
)
MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://kjmenfes:fadhil123@cluster0.inkz42g.mongodb.net/?retryWrites=true&w=majority",
)
