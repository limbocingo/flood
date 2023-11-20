from dataclasses import dataclass
from enum import Enum
from typing import Any


class Types(Enum):
    INTEGER     = 0
    FLOAT       = 1
    STRING      = 2
    BOOLEAN     = 4
    ARRAY       = 5
    NULL        = 6
    PUNCTUATION = 7
    KEYWORD     = 8
    UNDEFINED   = 9


@dataclass
class Object:
    type: Types = Types.UNDEFINED
    value: Any  = Any
