"""
Types management.
"""
from string import punctuation
from types import FunctionType

from src.parser.data import Types, Keywords, Object
from src.parser.help import floatc

BOOL = (Keywords.TRUE.value, Keywords.FALSE.value)
KEYW = (keyword.value for keyword in Keywords)


def typec(element: Any) -> tuple[Types, FunctionType]:
    element = element.upper() if isinstance(element, str) else element
    
    typesc = (
        # string doesn't appear here because its handled differently
        (Types.INTEGER,     int,   element.isdigit()),
        (Types.FLOAT,       float, floatc(element)),
        (Types.PUNCTUATION, None,  element in punctuation),
        (Types.BOOLEAN,     None,  element in BOOL),
        (Types.NULL,        None,  element == 'NULL'),
        (Types.KEYWORD,     None,  element in KEYW),
    )

    for type, func, condition in typesc:
        if check[1]: return check[0], check[1]

    if element.isdigit(): 
        return Types.INTEGER, int

    elif floatc(element):
        return Types.FLOAT, float

    elif element in punctuation: 
        return Types.PUNCTUATION, None

    elif element in BOOL: 
        return Types.BOOLEAN, None

    elif element in KEYW: 
        return Types.BUILTIN, None

    elif element == 'NULL': 
        return Types.NULL

    else: 
        return Types.KEYWORD


def conv(object: Object) -> Object:
    objectt = typec(object.value)

    if objectt is Types.INTEGER:
        object.value = int(object.value)

    elif objectt is Types.FLOAT:
        object.value = float(object.value)

    elif objectt is Types.BOOLEAN:
        object.value = True if object.value.upper() == "TRUE" else False

    elif objectt is Types.NULL:
        object.value = None

    object.type = objectt
