import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "20809545")) #optional
API_HASH = getenv("API_HASH", "4e4b3d4e7f8694b215400f427110e827") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6527327885").split()))
OWNER_ID = int(getenv("OWNER_ID", "6527327885"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://xxudayberdiyov:<password>@cluster0.qw3o81u.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6560192550:AAElNEB6VQSnxO5YObGbwjPLZ3XrFam0Llg")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER", "1001705127552")
LOG_GROUP = getenv("LOG_GROUP", "1001919973733")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "AQCoNQ_a0aBVAoZbA3D0-rUxfYEaBMDnZo84Di6akUdbya3NmHJEPbuwPCzALK-4Aya87jbqb924ngwrOhcZ_pbTQKcfC7tXDh5dTjXO42Pwoj_JIjWHPHdrmmiXNy1gX9YtAai76OWpfn1CrE1crUTmUxEtJ__di-R3hChiCsxdOGILRMMsL3q6VEyEH1Jb2irTIMnv0sjTX9zcDecHgt4uBhyU5oMzWNL5dU8x5WUQpM610odogOxwlsO-3nWC9s19f2C2jHALT1WpC_DcwT3i6WMVaeuHWm6RWTBssigVMf6bpI2S1JrNKqRXmbg-nl25lGWHvuUiIBwL-S0LCe-JAAAAAYUPHo0A")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
