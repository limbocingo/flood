"""
Functions and utilities for converting data.
"""
from typing import Any


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
