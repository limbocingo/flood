"""
Types management.
"""
from string import punctuation
from types import FunctionTypea

from src.parser.data import Types, Keywords, Object
from src.parser.help import floatc, boolc, nullc

BOOL = (Keywords.TRUE.value, Keywords.FALSE.value)
KEYW = (keyword.value for keyword in Keywords)

TYPESC = (
        # string doesn't appear here because its handled differently
        (Types.INTEGER,     int,   element.isdigit()),
        (Types.FLOAT,       float, floatc(element)),
        (Types.PUNCTUATION, None,  element in punctuation),
        (Types.BOOLEAN,     boolc, element in BOOL),
        (Types.NULL,        nullc, element == 'NULL'),
        (Types.BUILTIN,     None,  element in KEYW),
    )


def typec(element: Any) -> tuple[Types, FunctionType | None]:
    element = element.upper() if isinstance(element, str) else element

    for type, func, condition in typesc:
        if condition: return type, func
    return Types.KEYWORD, None


def conv(object: Object) -> Object:
    type, func = typec(object.value)

    object.type = type
    object.value = func(object.value) if func else object.value
