from datetime import datetime
from zoneinfo import ZoneInfo
from app.core import config


def current_time():
    return datetime.now(ZoneInfo(config.TZ))
