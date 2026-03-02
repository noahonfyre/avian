import socket
import struct
import time
from pathlib import Path
from typing import Tuple

from avian.models import Channel
from avian.models.constants import LOGGER, VERSION
from avian.models.messages import Message, TransactionStart, TransactionUpdate
from avian.models.network.protocol import ACK, NACK, recv, send
from avian.services import Service
from avian.utils.hashing import verify_file_hash


class ReceiverService(Service):
    def __init__(self, outgoing: Channel[Message], save_path: Path, port: int) -> None:
        self.outgoing: Channel[Message] = outgoing
        self.save_path: Path = save_path
        self.port: int = port
        self.file_count: int = 0

    def run(self) -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            LOGGER.info("Initializing receiver service...")
            if not self.save_path.exists():
                LOGGER.info("Creating download folder...")
                self.save_path.mkdir(parents=True)

            LOGGER.info(f"Binding to :{self.port}...")
            sock.bind(("0.0.0.0", self.port))
            sock.listen()
            LOGGER.info(f"Listening on :{self.port}.")

            i = 0

            while True:
                # TODO: change break logic
                if i > 0:
                    break
                conn, addr = sock.accept()
                try:
                    self.handle_connection(conn, addr)
                except Exception as e:
                    LOGGER.warning(f"Failed to handle {addr[0]}:{addr[1]}: {e}")
                i += 1

            LOGGER.info("Concluding receiver service...")

    def handle_connection(self, conn: socket.socket, addr: Tuple[str, int]) -> None:
        LOGGER.info(f"Incoming connection: {addr[0]}:{addr[1]}")

        LOGGER.info("Checking peer version...")
        peer_version: int = struct.unpack("!I", recv(conn))[0]

        if peer_version != VERSION:
            LOGGER.warning(f"Rejecting {addr[0]}:{addr[1]} due to version mismatch.")
            send(conn, NACK)
            return
        LOGGER.info("Version match! Continuing...")

        send(conn, ACK)

        self.file_count: int = struct.unpack("!I", recv(conn))[0]
        self.outgoing.send(TransactionStart(addr[0], addr[1], self.file_count))

        while self.file_count > 0:
            file: Path = self.receive_file(conn, addr)
            LOGGER.info("Getting file hash...")
            file_hash: bytes = struct.unpack("!32s", recv(conn))[0]
            LOGGER.info("Checking file integrity...")
            verified: bool = verify_file_hash(file, file_hash)
            if not verified:
                LOGGER.warning("File integrity check failed.")
                send(conn, NACK)
                return

            LOGGER.info("File integrity check successful.")
            send(conn, ACK)
            self.file_count -= 1

        LOGGER.info(f"Connection with {addr[0]}:{addr[1]} concluded.")

    def receive_file(self, conn: socket.socket, addr: Tuple[str, int]) -> Path:
        filename: str = recv(conn).decode()
        file_size: int = struct.unpack("!Q", recv(conn))[0]
        LOGGER.info(f"Starting transfer of {filename} ({file_size}B)...")

        destination: Path = self.save_path / Path(filename).name
        transferred = 0

        with open(destination, "wb") as file:
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
