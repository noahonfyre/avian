import logging
from pathlib import Path

ID: str = "avian"
NAME: str = "Avian"
VERSION: str = "0.1.0"
PROTOCOL_VERSION: int = 1
PROTOCOL_PORT: int = 9250
CHUNK_SIZE: int = 4096
AVIAN_PATH: Path = Path.home() / ".avian"
SAVE_PATH: Path = AVIAN_PATH / "saved"

LOGGER = logging.getLogger(ID)
