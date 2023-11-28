"""
Parse the tokens the :function:`floodpy.parser.lexer.lexer` gave.
This file has multiple parsers.
"""
from floodpy.parser.data import Object


def arrays(lines: list[list[Object]]) -> list[list[Object]]:
    """
    Parse arrays with symbols `[]` or `()`.

    lines : `list[list[Object]]`
        The array of tokens you want to parse.
    """
    pass


def calc(lines: list[list[Object]]) -> list[list[Object]]:
    """
    Goes line by line and replace the operations with a calculated one.

    lines : `list[list[Object]]`
        The array of tokens you want to parse.
    """
    pass
