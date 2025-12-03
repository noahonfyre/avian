import socket
import struct
import time
from pathlib import Path

from src.avian.models.transfer_stat_link import TransferStatLink
from src.avian.models.app_context import AppContext
from src.avian.network import packets


# TODO: convert single function to multi-method class
# TODO: store function parameters as instance attributes
def receive(ctx: AppContext, save_dir: Path, *, protocol_port: int, protocol_version: int, chunk_size: int) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        print(f"Setting up local environment...")
        if not save_dir.exists():
            save_dir.mkdir()

        print(f"Binding to port :{protocol_port}...")
        sock.bind(("0.0.0.0", protocol_port))
        print(f"Listening on :{protocol_port}...")
        sock.listen(1)

        while not ctx.termination_event.is_set():
            conn, addr = sock.accept()

            print(f"Incoming connection from {addr[0]}:{addr[1]}.")

            print("Exchanging configuration...")
            config_packet: bytes = struct.pack("!HI", protocol_version, chunk_size)
            conn.sendall(config_packet)

            if conn.recv(1) != packets.ACK:
                print("Peer rejected configuration! Closing connection...")
                conn.close()
                return

            print("Peer acknowledged configuration! Continuing...")

            print("Receiving file count...")
            file_count: int = struct.unpack("!I", conn.recv(4))[0]

            for i in range(file_count):
                filename_length: int = struct.unpack("!I", conn.recv(4))[0]
                filename: str = conn.recv(filename_length).decode()
                file_size: int = struct.unpack("!Q", conn.recv(8))[0]

                print(f"Received header for file {filename} ({file_size}B)!")

                bytes_received: int = 0

                with open(save_dir / filename, "ab+") as file:
                    start: float = time.perf_counter()

                    while bytes_received < file_size:
                        bytes_remaining: int = file_size - bytes_received
                        next_chunk_size: int = chunk_size if bytes_remaining >= chunk_size else bytes_remaining

                        chunk: bytes = conn.recv(next_chunk_size)
                        file.write(chunk)
                        bytes_received += len(chunk)

                        time_diff: float = time.perf_counter() - start

                        progress: float = bytes_received / file_size
                        speed: float = bytes_received / time_diff
                        eta: float = bytes_remaining / speed

                        ctx.chan.put(TransferStatLink(
                            progress=progress,
                            speed=speed,
                            eta=eta
                        ))