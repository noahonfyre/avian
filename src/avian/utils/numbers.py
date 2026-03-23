import math
from enum import Enum

from attr import dataclass


@dataclass
class Prefix:
    symbol: str
    exponent: int


def fmt(value: int | float, unit: str) -> str:
    """
    Returns the formatted string with the given unit and decimal prefix.
    """
    prefix = get_prefix(value)
    scaled: int = value / (10 ** prefix.exponent)
    return f"{scaled:.2f}{prefix.symbol}{unit}"


def fmt_bin(value: int | float, unit: str) -> str:
    """
    Returns the formatted string with the given unit and binary prefix.
    """
    prefix = get_bin_prefix(value)
    scaled: int = value / (2 ** prefix.exponent)
    return f"{scaled:.2f}{prefix.symbol}{unit}"


class BinaryPrefixes(Enum):
    TEBI = Prefix("Ti", 40)
    GIBI = Prefix("Gi", 30)
    MEBI = Prefix("Mi", 20)
    KIBI = Prefix("Ki", 10)
    BASE = Prefix("", 0)


class DecimalPrefixes(Enum):
    TERA = Prefix("T", 12)
    GIGA = Prefix("G", 9)
    MEGA = Prefix("M", 6)
    KILO = Prefix("k", 3)
    BASE = Prefix("", 0)


def get_prefix(value: int | float) -> Prefix:
    """
    Returns the best decimal prefix for `value`.
    """
    if value == 0:
        return DecimalPrefixes.BASE.value

    magnitude: int = math.floor(math.log10(value))

    for member in DecimalPrefixes:
        if member.value.exponent <= magnitude:
            return member.value
    return DecimalPrefixes.BASE.value


def get_bin_prefix(value: int | float) -> Prefix:
    """
    Returns the best binary prefix for `value`.
    """
    if value == 0:
        return BinaryPrefixes.BASE.value

    magnitude: int = math.floor(math.log2(value))

    for member in BinaryPrefixes:
        if member.value.exponent <= magnitude:
            return member.value
    return BinaryPrefixes.BASE.value
