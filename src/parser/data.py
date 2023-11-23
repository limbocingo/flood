"""
Data required for the Flood lexer.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Any


class Types(Enum):
    INTEGER     = 'INT'
    FLOAT       = 'FLOAT'
    STRING      = 'STRING'
    BOOLEAN     = 'BOOL'
    ARRAY       = 'LIST'
    NULL        = 'NULL'
    PUNCTUATION = 'PUNC'
    KEYWORD     = 'KEYW'
    BUILTIN     = 'BUILT'
    UNDEFINED   = 'UNDEFINED'


class Keywords(Enum):
    TRUE  = 'true'
    FALSE = 'false'



@dataclass
class Object:
    type: Types = Types.UNDEFINED
    value: Any  = Any
