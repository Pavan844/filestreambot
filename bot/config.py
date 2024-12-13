from os import environ as env
from dotenv import load_dotenv

load_dotenv()


class Telegram:
    API_ID = int(env.get("26009823", ))
    API_HASH = env.get("e545fc56028ee9404ef5b5bec64503ca")
    OWNER_ID = int(env.get("OWNER_ID", 6059507751))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "Kannadamovies844bot")
    BOT_TOKEN = env.get("6880540335:AAGIPoc1_TPahTKxUHAoRhHB5Rm328cNtwE")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1002197394981))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 12))


class Server:
    BASE_URL = env.get("BASE_URL", "https://filestreambot-2jts.onrender.com")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 8080))


class DB:
    DB_URL = env.get("DB_URL", "mongodb+srv://pkmoviesdb:C2C4VqSwGdigpbjQ@cluster0.7rk54.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")


class Util:
    PING_INTERVAL = int(env.get("PING_INTERVAL ", 1200))  # 20 minutes
    SUB_CHANNEL = int(env.get("SUB_CHANNEL", 0))
    SUB_CHANNEL_LINK = env.get("SUB_CHANNEL_LINK", "t.me/pkmovies4u")


# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    "version": 1,
    "formatters": {
        "default": {
            "format": "[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s",
            "datefmt": "%d/%m/%Y %H:%M:%S",
        },
    },
    "handlers": {
        "file_handler": {
            "class": "logging.FileHandler",
            "filename": "event-log.txt",
            "formatter": "default",
        },
        "stream_handler": {"class": "logging.StreamHandler", "formatter": "default"},
    },
    "loggers": {
        "uvicorn": {"level": "INFO", "handlers": ["file_handler", "stream_handler"]},
        "uvicorn.error": {
            "level": "WARNING",
            "handlers": ["file_handler", "stream_handler"],
        },
        "bot": {"level": "INFO", "handlers": ["file_handler", "stream_handler"]},
        "ping": {"level": "INFO", "handlers": ["file_handler", "stream_handler"]},
    },
}
