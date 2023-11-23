"""
Helpful functions and utilities.
"""
from typing import Any


def repl(string: str, character: str, index: int) -> str:
    line        = list(string)
    line[index] = character
    line        = ''.join(line)
    
    return line


def readlns(filepath: str) -> list[str]:
    with open(filepath, 'r') as fr:
        return fr.readlines()


def floatc(element: Any) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False
