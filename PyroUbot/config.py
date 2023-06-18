import os

API_ID = int(os.getenv("API_ID", "2237557"))

API_HASH = os.getenv("API_HASH", "5dcc2172391406707828d375603cc001")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6207982225:AAH0_iRRfJE9Wd5PgKhCH12emM9B_PUPfUM")

OWNER_ID = int(os.getenv("OWNER_ID", "1964437366"))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1001969856888"))

COMMAND = os.getenv("COMMAND", ". , : ; !")
PREFIX = COMMAND.split()

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001969856888").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "50"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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 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",
).split()

SESSION_STRING = os.getenv(
    "SESSION_STRING",
    "BQFQSxMAT_XDxxr14lUjIfLqW_lKowGdzUeob_bg0_Yko6ahmE5aJE9qrxnelMqJ5VuiUJ7CU2aIjHJ_DsvXneq6h-9jYSiKWIGHyR0UIBgESLNX_8NWKHJK_llBFXG8Dl9DVALBac-Ue4vnEcAtmKMjok5hswbrpH6mo0hdbxEMTTxQX4x5EzqVukABeLuizNu_8wkXekMYDJxBnB1MnFo6Hipd1jLyQzzOWhvoWV9fJw6auKs0nfSMWLQCWVXlM9mN-vcEEIV6y-a621Xp1Yo5G6IwcMwW2FcPFSwZZtxfQohP6fxZ4gKlnhgc4eG1O7Q1rfqKIj7O_COlD662W4uStlExrgAAAAB1Fu92AA",
)

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://PremUbot:sST5VL04n85JkcxS@cluster0.wixneuz.mongodb.net/?retryWrites=true&w=majority",
)
