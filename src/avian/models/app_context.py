from dataclasses import dataclass
from queue import Queue
from threading import Event

from src.avian.config import Config


@dataclass
class AppContext:
    config: Config
    chan: Queue
    termination_event: Event