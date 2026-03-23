from importlib.resources import files
from importlib.resources.abc import Traversable


def get_resource(location: str) -> Traversable:
    """
    Returns the Traversable object of the asset at `location`.
    """
    return files("avian").joinpath(f"assets/{location}")
