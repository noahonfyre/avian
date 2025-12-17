import socket
import struct
import time
from pathlib import Path
from queue import Queue
from src.avian.network import packets


# TODO: convert single function to multi-method class
# TODO: store function parameters as instance attributes
def send(target: str, filepaths: list[Path], *, chan: Queue, protocol_port: int, protocol_version: int, chunk_size: int) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        print(f"Connecting to {target}:{protocol_port}...")
        sock.connect((target, protocol_port))

        print("Receiving peer configuration...")
        peer_protocol_version, peer_chunk_size = struct.unpack("!HI", sock.recv(6))

        print("Comparing protocol versions...")
        if protocol_version != peer_protocol_version:
            print(f"Protocol version mismatch! {protocol_version} != {peer_protocol_version}")
            sock.sendall(packets.NACK)
            return

        print(f"Protocol versions match! {protocol_version} == {peer_protocol_version}")
        sock.sendall(packets.ACK)

        print("Sending file count...")
        file_count_packet: bytes = struct.pack("!I", len(filepaths))
        sock.sendall(file_count_packet)

        for filepath in filepaths:
            if not filepath.is_file():
                continue
            filename: str = filepath.name
            file_size: int = filepath.stat().st_size

            print(f"Sending file header for {filename} ({file_size}B)...")
            file_header_packet: bytes = struct.pack("!I", len(filename)) + filename.encode() + struct.pack("!Q", file_size)
            sock.sendall(file_header_packet)

            bytes_sent: int = 0

            with open(filepath, "rb") as file:
                start: float = time.perf_counter()

                while bytes_sent < file_size:
                    bytes_remaining: int = file_size - bytes_sent
                    next_chunk_size: int = chunk_size if bytes_remaining >= chunk_size else bytes_remaining

                    chunk: bytes = file.read(next_chunk_size)
                    sock.sendall(chunk)
                    bytes_sent += len(chunk)

                    time_diff: float = time.perf_counter() - start

                    progress: float = bytes_sent / file_size
                    speed: float = bytes_sent / time_diff
                    eta: float = bytes_remaining / speed

                    chan.put(TransferStatLink(
                        progress=progress,
                        speed=speed,
                        eta=eta
                    ))