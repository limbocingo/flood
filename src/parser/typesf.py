"""
Types management.
"""
from typing import Any
from string import punctuation

from src.parser.data import Types, Keywords, Object
from src.parser.converters import boolc, nullc, puncc, floatc

BOOL = (Keywords.TRUE.value, Keywords.FALSE.value)
KEYW = (keyword.value for keyword in Keywords)

TYPESC = (
        # string doesn't appear here because its handled differently
        lambda element: (Types.INTEGER,     int,   element.isdigit()),
        lambda element: (Types.FLOAT,       float, floatc(element)),
        lambda element: (Types.PUNCTUATION, puncc, element in punctuation),
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
