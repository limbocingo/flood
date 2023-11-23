"""
Data required for the Flood lexer.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Any


class Types(Enum):
    INTEGER     = "INT"
    FLOAT       = "FLOAT"
    STRING      = "STR"
    BOOLEAN     = "BOOL"
    ARRAY       = "ARR"
    NULL        = "NULL"
    PUNCTUATION = "PUNC"
    KEYWORD     = "KEYW"
    BUILTIN     = "BUILT"
    UNDEFINED   = "?"


class Operators(Enum):
    PLUS     = "+"
    MINUS    = "-"
    MULTIPLY = "*"
    RAISE    = "^"


class Punctuation(Enum):
    BRACKET_R     = ")"
    BRACKET_L     = "("
    SQR_BRACKET_L = "["
    SQR_BRACKET_R = "]"
    COMMA         = ","
    POINT         = "."


class Keywords(Enum):
    TRUE     = "TRUE"
    FALSE    = "FALSE"
    
    NULL     = "NULL"

    FUNCTION = "FUNC"
    VARIABLE = "VAR"


@dataclass
class Object:
    type: Types = Types.UNDEFINED
    value: object  = Any
