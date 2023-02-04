import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5985594223").split()))
OWNER_ID = int(getenv("OWNER_ID", "5985594223"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://<username>:<password>@cluster0.xhasha8.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6023104043:AAHOtw06fOuD5r8bdYMJf1FZsZ9Sow_SjtE")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAJq5pWeGX50rK_bqv07eeNk1ZZ9zT-F3n3yfIXB_dOcWYM3xhFIYF9GWT3OYODVOsRa_Fdy9dFeve59A9DE2aHEOFsYYs-nRs1B7oZtiGWnUAjEtAJlGD0GGtY6c3oiU1cNK3VkDso_3Kn7Nlyf0QpYD_20du6WT9u1wQ9LGNVBeoOBYnKXL8FO5x3MSzxppqvkoG-4HkoOecckGsGAFKAVOcXSibtPtF1yvuLXPOLYXC4ARoqVlsZOv0DSAYjBwVUT2uJmyua5v7VwT4b09mLbc9mwDFFtwSeoZQWa4Nc8PwjqEZFsMj9Xr1agQFHHMlngJAR1Mt_Kv_PKVIQiHBTQAAAAFkxOtvAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
