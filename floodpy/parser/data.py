"""
Data required for the Flood lexer.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Any


class Types(Enum):
    """
    A Types class is necessary because Python don't provide
    all the types required to classify the tokens in the best way.
    """
    INTEGER = "INT"
    FLOAT = "FLOAT"
    STRING = "STR"
    BOOLEAN = "BOOL"
    ARRAY = "ARR"
    NULL = "NULL"
    PUNCTUATION = "PUNC"
    OPERATOR = "OP"
    KEYWORD = "KEYW"
    BUILTIN = "BUILT"
    UNDEFINED = "?"


class Operators(Enum):
    """
    Operators tokens.
    """
    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
    RAISE = "^"


class Punctuation(Enum):
    """
    Punctutation tokens.
    """
    BRACKET_R = ")"
    BRACKET_L = "("
    SQR_BRACKET_L = "["
    SQR_BRACKET_R = "]"
    COMMA = ","
    POINT = "."


class Keywords(Enum):
    """
    Builtin tokens.
    """
    TRUE = "TRUE"
    FALSE = "FALSE"

    NULL = "NULL"

    FUNCTION = "FUNC"
    VARIABLE = "VAR"


@dataclass
class Object:
    """
    A Object is basiclly a token, but instead of using
    a `dict` to store the information we use a Python `dataclass`. 
    """
    type: Types = Types.UNDEFINED
    value: object = Any

    def isdigit(self) -> bool:
        """
        Is like a implementation of `str.isdigit()` but in the 
        Object dataclass.
        """
        if self.value.isdigit():
            return True
        return False

    def isfloat(self) -> bool:
        """
        Tries to convert the value of the Object in a `float`, 
        if isn't possible simply throws `False`.
        """
        try:
            float(self.value)
            return True
        except ValueError:
            return False

    def isnull(self) -> bool:
        """
        Checks if the value in upper is equals to `NULL`.
        """
        if self.value.upper() == 'NULL':
            return True
        return False

    def ispunc(self) -> bool:
        """
        Gets all the punctuation symbols available and
        checks if the value is in that list of symbols.
        """
        if self.value in [punc.value for punc in Punctuation]:
            return True
        return False

    def isop(self) -> bool:
        """
        Works the same like `self.ispunc()` but instead of punctuation
        symblos is operators.
        """
        if self.value in [op.value for op in Operators]:
            return True
        return False

    def isbool(self) -> bool:
        """
        If the value in upper equals to `TRUE` then its `True`.
        Exactly the same with the `FALSE` keyword but its `False`.
        """
        if self.value.upper() in (Keywords.TRUE.value, 
                                  Keywords.FALSE.value):
            return True
        return False

    def isbuiltin(self) -> bool:
        """
        If the value in upper exists in the Keywords `class`.
        """
        if self.value.upper() in (keyword.value
                                  for keyword in Keywords):
            return True
        return False
