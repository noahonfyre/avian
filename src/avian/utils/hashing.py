import hashlib
from pathlib import Path


def calculate_hash(path: Path) -> bytes:
    """
    Calculate the SHA256 hash of the file at `path`.
    """

    hash_func = hashlib.sha256()

    with open(path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_func.update(chunk)

    return hash_func.digest()


def verify_file_hash(path: Path, expected_hash: bytes) -> bool:
    """
    Compare the hash of the file at `path` with the expected hash.
    Returns `True` when the hash matches the expected hash and `False` otherwise.
    """
    calculated_hash: bytes = calculate_hash(path)
    return calculated_hash.lower() == expected_hash.lower()
