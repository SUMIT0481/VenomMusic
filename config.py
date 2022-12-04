from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "15443180"))
API_HASH = getenv("API_HASH", "7cd4725247752f02ad24e8c89a70b3a0")

ASS_HANDLER = list(getenv("ASS_HANDLER", "/").split())
BOT_TOKEN = getenv("BOT_TOKEN", "5797628793:AAFrv1qBSEVBXXA0jnI3VLvjLP_RjhqLBhA")


DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001739380859"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://bsdk:betichod@cluster0.fgj1r9z.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5564090687").split()))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6c1fb04031bf2238e1f56.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/6d4e8e492ae6895826524.jpg")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/og_family_group")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", " https://t.me/ogvenomeditz")

STRING_SESSION = getenv("STRING_SESSION", "AQAW0_gBOIfxn_qNmEK3DbgyBfXlSabSg9CNLg1add9Kv1Dofrry89I5WtUuaqg9hfzEIsXFRN83xnJC9DLiOmG9hM3IZf3T9K3vQ12QkqSQliPFaz7x2czgia3uTVY0UY2dDf98YHIrNcB_j-aCBMpUdBGSYtr1HV71y9zjN8L_hCZUci7FidShcmwSX00jUcj36b9QXfzAVtd2TaygvQLYxLk1ycpfNK9dCZ0ArUPBC1W-4dxG4fOPl9nG8vT2rfBkfOWRN3OiRveRS1H6hrzCaZpsZdSw2uf8J2PxchJXkYhLJHiHYW1qVnkOZdJc7L8rRFgonzfMqNTlzE8dWVGpAAAAAUbYwo8A")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5689431546").split()))
