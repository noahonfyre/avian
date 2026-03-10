from pathlib import Path
from typing import List

from attr import dataclass


@dataclass(frozen=True)
class Message:
    pass


@dataclass(frozen=True)
class Shutdown(Message):
    pass


@dataclass(frozen=True)
class StartSender(Message):
    address: str
    port: int
    files: List[Path]


@dataclass(frozen=True)
class RejectedConnection(Message):
    address: str
    port: int
    cause: str


@dataclass(frozen=True)
class NewConnection(Message):
    address: str
    port: int


@dataclass(frozen=True)
class TransactionStart(Message):
    address: str
    port: int
    file_count: int


@dataclass(frozen=True)
class TransactionUpdate(Message):
    address: str
    port: int
    filename: str
    bytes_transferred: int
    file_size: int
    elapsed: float


@dataclass(frozen=True)
class TransactionConclude(Message):
    address: str
    port: int
    filename: str
