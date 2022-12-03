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

STRING_SESSION = getenv("STRING_SESSION", "AQBQecosuHwaZaxYiVcAygF_QOKz_6iK8VrvFCgFEA31wPErI6tgrTKv6p-9gV-qzxJx7JEyaWqRypiKTXvLX2VAZGyazGCuw5crakUSF5YVDEwKk_awSMVhIyFGv875l3hrTwyt8ouoDs8ifNqxopbh4znEwrDVh1ic9L2fQnOMt0UjKFgHj9Rs77NX9e9W4RcKOqxoB5FUQvMRd31ksulaNXePNo98MReGsWOwsw-d-XzOaHJxmeTA9rB_vQJY7VBsze4RNhy9zHusmsZyD2ok_YF0qwKkhcMPqxSh8tIMddvefBguG28raVKeMjLlbsuGIq_C1ZFVCuULXG5EFyg2AAAAAUbYwo8A")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5564090687").split()))
