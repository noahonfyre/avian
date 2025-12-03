import platform
from pathlib import Path


def app_dir(app_name: str) -> Path:
    match platform.system():
        case "Windows":
            return Path.home() / "AppData" / "Roaming" / app_name
        case "Darwin":
            return Path.home() / "Library" / "Application Support" / app_name
        case _:
            return Path.home() / ".config" / app_name