import logging
from pathlib import Path

from avian.utils.paths import resolve_app_path

ID: str = "avian"
NAME: str = "Avian"
VERSION: str = "0.1.0"
PROTOCOL_VERSION: int = 1
AVIAN_PATH: Path = resolve_app_path(ID)
RESOLVER_TARGET = "https://api.ipify.org?format=json"

LOGGER = logging.getLogger(ID)
