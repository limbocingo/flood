"""
List of convertors.
"""
from typing import Any

from floodpy.parser.data import Punctuation, Operators, Keywords


def intc(element: Any) -> bool:
    return int(element)


def floatc(element: Any) -> float:
    return float(element)


def boolc(element: Any) -> bool:
    if element == 'TRUE':
        return True

    elif element == 'FALSE':
        return False


def nullc(element: Any) -> None:
    return None


def puncc(element: Any) -> Punctuation:
    """`floodpy.data.Punctuation`"""
    return Punctuation(element)


def opc(element: Any) -> Operators:
    """`floodpy.data.Operators`"""
    return Operators(element)


def builtinc(element: Any) -> Keywords:
    """`floodpy.data.Keywords`"""
    return Keywords(element)
