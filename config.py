## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "5349671561:AAHPEBffPCIXpMqowgXU8GdKyBoFYmTc0_E")
BOT_NAME = getenv("BOT_NAME", "song")
API_ID = int(getenv("API_ID", "17694201"))
API_HASH = getenv("API_HASH", "eb8b38c80b362ae8673ac2b59bac17c6")
OWNER_NAME = getenv("OWNER_NAME", "Oliver")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Zzzz7lZ")
ALIVE_NAME = getenv("ALIVE_NAME", "NN8RN")
BOT_USERNAME = getenv("BOT_USERNAME", "G_5_BOT")
OWNER_ID = getenv("OWNER_ID", "5036835528")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "NN8RN")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "zzzz7lz")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "zzzz7lz")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5036835528").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c354364952713db1a3360.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/c354364952713db1a3360.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c354364952713db1a3360.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/c354364952713db1a3360.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c354364952713db1a3360.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/c354364952713db1a3360.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c354364952713db1a3360.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c354364952713db1a3360.jpg")
