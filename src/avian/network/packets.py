import struct

ACK = struct.pack("!?", True)
NACK = struct.pack("!?", False)