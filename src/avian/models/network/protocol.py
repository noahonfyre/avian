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


def recv(conn: socket.socket) -> bytes:
    header: bytes = conn.recv(HEADER_SIZE)
    magic, payload_length = HEADER.unpack_from(header)

    if magic != MAGIC:
        raise ValueError(f"Protocol constant mismatch: magic={hex(magic)}")
    payload: bytes = conn.recv(payload_length)
    return payload
