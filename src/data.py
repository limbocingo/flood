from dataclasses import dataclass
from enum import Enum
from typing import Any


class Types(Enum):
    INTEGER = 0
    STRING = 1
    FUNCTION = 2
    BOOLEAN = 3
    ARRAY = 4
    NULL = 5
    PUNCTUATION = 6
    KEYWORD = 7
    UNDEFINED = 8
    FLOAT = 9


@dataclass
class Object:
    type: Types = Types.UNDEFINED
    value: Any = Any
