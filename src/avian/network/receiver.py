import socket
import struct
import time
from pathlib import Path
from typing import Optional, Tuple

from avian.models import Channel
from avian.models.constants import LOGGER, VERSION
from avian.models.messages import (
    Message,
    NewConnection,
    RejectedConnection,
    TransactionStart,
    TransactionUpdate,
)
from avian.network.protocol import ACK, NACK, recv, send
from avian.services import Service
from avian.utils.hashing import verify_file_hash


class Receiver(Service):
    def __init__(
            self,
            outgoing: Channel[Message],
            save_path: Path,
            port: int,
            sock: Optional[socket.socket] = None,
    ) -> None:
        self.outgoing: Channel[Message] = outgoing
        self.save_path: Path = save_path
        self.port: int = port
        self.sock = sock or socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.file_count: int = 0

    def run(self) -> None:
        LOGGER.info("Initializing receiver service...")
        if not self.save_path.exists():
            LOGGER.info("Creating download folder...")
            self.save_path.mkdir(parents=True)

        LOGGER.info(f"Binding to :{self.port}...")
        self.sock.bind(("0.0.0.0", self.port))
        self.sock.listen()
        LOGGER.info(f"Listening on :{self.port}.")

        while True:
            conn, addr = self.sock.accept()
            LOGGER.info(f"Incoming connection: {addr[0]}:{addr[1]}")

            peer_version: int = struct.unpack("!I", recv(conn))[0]

            if peer_version != VERSION:
                LOGGER.warning(
                    f"Rejecting {addr[0]}:{addr[1]} due to version mismatch."
                )
                send(conn, NACK)
                self.outgoing.send(RejectedConnection(
                    addr[0],
                    addr[1],
                    f"Rejecting {addr[0]}:{addr[1]} due to version mismatch."
                ))
                continue

            send(conn, ACK)

            self.outgoing.send(NewConnection(address=addr[0], port=addr[1]))

            self.file_count: int = struct.unpack("!I", recv(self.sock))[0]
            self.outgoing.send(TransactionStart(addr[0], addr[1], self.file_count))

            while self.file_count > 0:
                file: Path = self.receive_file(conn, addr)
                verified: bool = self.verify(conn, file)

                if not verified:
                    LOGGER.warning(f"{file.name} failed integrity verification.")
                    send(conn, NACK)

                send(conn, ACK)
                self.file_count -= 1

    def receive_file(self, conn: socket.socket, addr: Tuple[str, int]) -> Path:
        filename: str = recv(conn).decode()
        file_size: int = struct.unpack("!I", recv(conn))[0]
        LOGGER.info(f"Starting transfer of {filename} ({file_size}B)...")

        destination: Path = self.save_path / filename
        transferred = 0

        with open(destination, "ab+") as file:
            while transferred < file_size:
                start = time.perf_counter()
                chunk: bytes = recv(conn)
                if not chunk:
                    break
                file.write(chunk)
                transferred += len(chunk)
                elapsed = time.perf_counter() - start
                self.outgoing.send(
                    TransactionUpdate(
                        address=addr[0],
                        port=addr[1],
                        filename=filename,
                        bytes_transferred=transferred,
                        file_size=file_size,
                        elapsed=elapsed,
                    )
                )
        LOGGER.info(f"File {filename} saved in {destination}.")
        return destination

    @staticmethod
    def verify(conn: socket.socket, destination: Path) -> bool:
        file_hash = struct.unpack("!32s", recv(conn))[0]
        return verify_file_hash(destination, file_hash)
