import platform
import subprocess
from pathlib import Path


def resolve_app_path(identifier: str) -> Path:
    """
    Returns the Path object of the platform-specific application path.
    """
    match platform.system():
        case "Windows":
            return Path.home() / f".{identifier}"
        case "Darwin":
            return Path.home() / "Library" / "Application Support" / f".{identifier}"
        case _:
            return Path.home() / ".config" / f".{identifier}"


def open_folder(path: Path):
    """
    Opens a subprocess with the platform-specific file explorer and the given `path` as argument.
    """
    match platform.system():
        case "Windows":
            subprocess.Popen(["explorer", str(path)])
        case "Darwin":
            subprocess.Popen(["open", str(path)])
        case _:
            subprocess.Popen(["xdg-open", str(path)])
