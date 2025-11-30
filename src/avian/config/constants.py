from pathlib import Path

from src.avian.utils.paths import app_dir


class Constants:
    PROTOCOL_VERSION: int = 1
    NEGOTIATION_PORT: int = 9250
    APP_PATH: Path = app_dir("avian")
    LANG_PATH: Path = APP_PATH / "lang"
    CONFIG_PATH: Path = APP_PATH / "config.json"
