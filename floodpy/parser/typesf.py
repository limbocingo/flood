"""
Manage the type of a :class:`floodpy.data.Object`.
"""
from types import FunctionType

from floodpy.parser.data import Types, Object
from floodpy.parser.converters import (
    boolc,
    nullc,
    puncc,
    floatc,
    opc,
    intc,
    builtinc,
)
 
# List of functions (lambdas) that checks the type
# of the object and gives the `type` & `converter` for it.
TYPEC = (
    # `str` & `list` doesn't appear here because its treated
    # differently than the other types.
    lambda object: (Types.INTEGER,     intc,      object.isdigit()),
    lambda object: (Types.FLOAT,       floatc,    object.isfloat()),
    lambda object: (Types.PUNCTUATION, puncc,     object.ispunc()),
    lambda object: (Types.OPERATOR,    opc,       object.isop()),
    lambda object: (Types.NULL,        nullc,     object.isnull()),
    lambda object: (Types.BOOLEAN,     boolc,     object.isbool()),
    lambda object: (Types.BUILTIN,     builtinc,  object.isbuiltin()),
)


def typec(object: Object) -> tuple[Types, 
                                   FunctionType]:
    """
    Executes every lambda in the `TYPEC` array, sees if the condition
    is True and returns returns the type & converter.

    object : `floodpy.data.Object`
        The object you want to type check.
    """
    for lmb in TYPEC:
        type, conv, cond = lmb(object)
        if cond:
            return type, conv
    return Types.KEYWORD, None


def conv(object: Object) -> None:
    """
    Converts value & the type into the corresponded one.

    object : `floodpy.data.Object`
        Object you want to convert.
    """
    type, func = typec(object.value)

    object.type = type
    object.value = func(object.value) if func else object.value
