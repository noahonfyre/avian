import socket
import struct
import time
from pathlib import Path
from typing import List

from avian.models.channel import Channel
from avian.models.constants import CHUNK_SIZE, LOGGER, PROTOCOL_VERSION
from avian.models.messages import (
    Message,
    RejectedConnection,
    TransactionStart,
    TransactionUpdate,
)
from avian.models.network.protocol import ACK, recv, send
from avian.services.service import Service
from avian.utils.hashing import calculate_hash


class SenderService(Service):
    def __init__(
        self, outgoing: Channel[Message], files: List[Path], address: str, port: int
    ) -> None:
        self.outgoing: Channel[Message] = outgoing
        self.files: List[Path] = files
        self.address: str = address
        self.port: int = port
        self.file_count: int = len(self.files)

    def run(self) -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            LOGGER.info("Initializing sender service...")

            LOGGER.info(f"Connecting {self.address}:{self.port}...")
            sock.connect((self.address, self.port))

            LOGGER.info("Transferring version...")
            send(sock, struct.pack("!I", PROTOCOL_VERSION))

            if recv(sock) != ACK:
                LOGGER.warning(
                    f"Connection rejected from {self.address}:{self.port} due to version mismatch."
                )
                self.outgoing.send(
                    RejectedConnection(
                        self.address,
                        self.port,
                        f"Connection rejected from {self.address}:{self.port} due to version mismatch.",
                    )
                )
                return

            LOGGER.info("Version match! Continuing...")

            send(sock, struct.pack("!I", self.file_count))
            self.outgoing.send(
                TransactionStart(
                    address=self.address, port=self.port, file_count=self.file_count
                )
            )

            for file in self.files:
                LOGGER.info(f"Calculating file hash of file {file.name}...")
                file_hash: bytes = calculate_hash(file)

                self.send_file(sock, file)
                send(sock, struct.pack("!32s", file_hash))

                if recv(sock) != ACK:
                    LOGGER.warning(f"Integrity check failed for {file.name}, aborting.")
                    return

            LOGGER.info(f"Connection with {self.address}:{self.port} concluded.")
            LOGGER.info("Concluding sender service...")

    def send_file(self, conn: socket.socket, path: Path) -> None:
        filename: str = path.name
        send(conn, filename.encode())
        file_size: int = path.stat().st_size
        send(conn, struct.pack("!Q", file_size))
        LOGGER.info(f"Starting transfer of {filename} ({file_size}B)...")

        transferred = 0

        with open(path, "rb") as file:
            while transferred < file_size:
                start = time.perf_counter()
                chunk: bytes = file.read(CHUNK_SIZE)
                if not chunk:
                    break
                send(conn, chunk)
                transferred += len(chunk)
                elapsed = time.perf_counter() - start
                self.outgoing.send(
                    TransactionUpdate(
                        address=self.address,
                        port=self.port,
                        filename=filename,
                        bytes_transferred=transferred,
                        file_size=file_size,
                        elapsed=elapsed,
                    )
                )
        LOGGER.info(f"File {filename} successfully transferred.")
