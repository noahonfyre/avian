import hashlib
from pathlib import Path


def calculate_hash(path: Path) -> bytes:
    hash_func = hashlib.sha256()

    with open(path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_func.update(chunk)

    return hash_func.digest()


def verify_file_hash(path: Path, expected_hash: bytes) -> bool:
    calculated_hash: bytes = calculate_hash(path)
    return calculated_hash.lower() == expected_hash.lower()
