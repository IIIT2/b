## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgAdFssYeEm3Ke4poJmqlIXBG4-jVHYEjTlv52cIq_01ALAj7wJPsGpMNc1g0qxLw567ZVT1qSdtVX28sFB89ezlfn4WXAjORYiNANXAAHwIIqFpnamU_ZQl10QcbOupZNO3NfRGnXiYanAEylJVYs64tuQouDapKEvfYQ1DcPvkPyFuWt1Dvi5nkuoQ2BXPVgw6VaiBy749bvu7_OEQPPocMaCopG6cnxjCu3rtVZOYFYMtdofnXIXUPtOYRpZJLLC49daYVbjG6HonOi9_uAzN9Rd9Ug6U4Gjypcwi3TfbLIslVWLgctTZ91cgc2kDayG5zzaU7iMnu76M55QoDYovAAAAAStFkLQA")
BOT_TOKEN = getenv("BOT_TOKEN", "5349671561:AAHPEBffPCIXpMqowgXU8GdKyBoFYmTc0_E")
BOT_NAME = getenv("BOT_NAME", "Music")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "Oliver")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ZZZZ7Lz")
ALIVE_NAME = getenv("ALIVE_NAME", "Music")
BOT_USERNAME = getenv("BOT_USERNAME", "G_5_BOT")
OWNER_ID = getenv("OWNER_ID", "5036835528")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "NN8RN")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ZZZZ7LZ")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ZZZZ7LZ")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5036835528").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . ").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c354364952713db1a3360.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/c354364952713db1a3360.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/oliethon/b")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c354364952713db1a3360.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/c354364952713db1a3360.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c354364952713db1a3360.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/c354364952713db1a3360.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c354364952713db1a3360.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c354364952713db1a3360.jpg")
