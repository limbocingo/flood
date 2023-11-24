"""
Functions and utilities for converting data.
"""
from typing import Any

from src.parser.data import Punctuation, Operators


def floatc(element: Any) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False


def boolc(element: Any) -> bool:
    if element == 'TRUE':
        return True
    
    elif element == 'FALSE':
        return False


def nullc(element: Any) -> None:
    return None


def puncc(element: Any) -> Punctuation:
    return Punctuation(element)

def opc(element: Any) -> Operators:
    return Operators(element)
