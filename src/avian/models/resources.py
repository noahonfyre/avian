from importlib.resources import files
from importlib.resources.abc import Traversable


def get_resource(location: str) -> Traversable:
    return files("avian").joinpath(f"assets/{location}")
