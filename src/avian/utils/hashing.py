import hashlib
from pathlib import Path


def calculate_hash(destination: Path) -> bytes:
    hash_func = hashlib.sha256()

    with open(destination, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_func.update(chunk)

    return hash_func.digest()


def verify_file_hash(filepath: Path, expected_hash: bytes) -> bool:
    calculated_hash: bytes = calculate_hash(filepath)
    return calculated_hash.lower() == expected_hash.lower()
