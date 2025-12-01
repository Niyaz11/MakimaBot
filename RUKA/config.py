import os
from dotenv import load_dotenv



load_dotenv()



def _to_int(val: str | None) -> int | None:
    try:
        return int(val) if val is not None else None
    except Exception:
        return None



def _to_list(val: str | None, cast_int: bool = False) -> list:
    if not val:
        return []
    items = [x.strip() for x in val.split(",") if x.strip()]
    if cast_int:
        out = []
        for x in items:
            try:
                out.append(int(x))
            except Exception:
                continue
        return out
    return items



class CONFIG_CLASS:
    BOT_TOKEN = ""
    API_ID = 23537462
    API_HASH = "c9599a5aa61ee8ca4f5e778d20c61f24"

    OWNER_LIST = _to_list(os.environ.get("7654385403"), cast_int=True)
    DEV_LIST = _to_list(os.environ.get("7654385403"), cast_int=True)
    SUDO_LIST = _to_list(os.environ.get("7654385403"), cast_int=True)
    SUPPORT_LIST = _to_list(os.environ.get("7654385403"), cast_int=True)
    WHITE_LIST = _to_list(os.environ.get("7654385403"), cast_int=True)

    SUPPORT_CHAT_ID=
    LOGS_CHANNEL= -1002456565415
    GBAN_LOGS= -1002456565415
    UPDATES_CHANNEL=""

    DB_URL = os.environ.get("") or os.environ.get("")

    SERVER_LOG_BOT_TOKEN = ""

    MEOW_API_TOKEN = os.environ.get("MEOW_API_TOKEN")

    def __init__(self):
        if not self.BOT_TOKEN:
            raise ValueError("BOT_TOKEN is required in environment variables!")
        if not self.API_ID:
            raise ValueError("API_ID is required and must be an integer!")
        if not self.API_HASH:
            raise ValueError("API_HASH is required!")
        if not self.DB_URL:
            raise ValueError("DB_URL is required!")


