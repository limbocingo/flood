"""
Types management.
"""
from typing import Any
from string import punctuation

from src.parser.data import Types, Keywords, Object, Punctuation, Operators
from src.parser.converters import boolc, nullc, puncc, floatc

BOOL = (Keywords.TRUE.value, Keywords.FALSE.value)
KEYW = (keyword.value for keyword in Keywords)

TYPESC = (
        # string doesn't appear here because its handled differently
        lambda element: (Types.INTEGER,     int,   element.isdigit()),
        lambda element: (Types.FLOAT,       float, floatc(element)),
        lambda element: (Types.PUNCTUATION, puncc, element in [punc.value for punc in Punctuation]),
        lambda element: (Types.OPER, opc,   element in [op.value for op in Operators]),
        lambda element: (Types.BOOLEAN,     boolc, element in BOOL),
        lambda element: (Types.NULL,        nullc, element == 'NULL'),
        lambda element: (Types.BUILTIN,     None,  element in KEYW),
    )


def typec(element: Any):
    element = element.upper() if isinstance(element, str) else element

    for lmb in TYPESC:
        type, conv, cond = lmb(element)
        if cond: return type, conv
    return Types.KEYWORD, None


def conv(object: Object):
    type, func = typec(object.value)

    object.type = type
    object.value = func(object.value) if func else object.value
