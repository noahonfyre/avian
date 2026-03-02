import socket
import struct

"""
Packet composition:
1B Magic number
4B Payload length
xB Payload (binary encrypted JSON)
"""

MAGIC: int = 0xAE

HEADER: struct.Struct = struct.Struct("!BI")
HEADER_SIZE: int = HEADER.size

ACK: bytes = "ack".encode()
NACK: bytes = "nack".encode()


def send(conn: socket.socket, payload: bytes) -> None:
    conn.sendall(HEADER.pack(MAGIC, len(payload)) + payload)


def recv_exact(conn: socket.socket, size: int) -> bytes:
    buffer = b""
    while len(buffer) < size:
        chunk = conn.recv(size - len(buffer))
        if not chunk:
            raise ConnectionError("Frame reception failed.")
        buffer += chunk
    return buffer


def recv(conn: socket.socket) -> bytes:
    header: bytes = recv_exact(conn, HEADER_SIZE)
    magic, payload_length = HEADER.unpack(header)

    if magic != MAGIC:
        raise ValueError(f"Protocol constant mismatch: magic={hex(magic)}")
    payload: bytes = recv_exact(conn, payload_length)
    return payload
