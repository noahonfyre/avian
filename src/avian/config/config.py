from pathlib import Path

from src.avian.utils import app_dir


class Config:
    PROTOCOL_VERSION: int = 1
    PROTOCOL_PORT: int = 9250
    APP_PATH: Path = app_dir("avian")
    DOWNLOAD_PATH: Path = Path.home() / "Downloads"
    LANG_PATH: Path = APP_PATH / "lang"
    CONFIG_PATH: Path = APP_PATH / "config.json"

    CHUNK_SIZE: int = 4096

    # Additional Services
    ENABLE_RENDEZVOUS: bool = False
    RENDEZVOUS_HOST: str = "localhost"
    RENDEZVOUS_PORT: int = 9240

    ENABLE_DISCOVERY: bool = False
    DISCOVERY_PORT: int = 9245

    ENABLE_RESOLUTION: bool = True
    RESOLUTION_HOST: str = "1.1.1.1"
    RESOLUTION_PORT: int = 80