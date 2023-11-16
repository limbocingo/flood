import sys
from dataclasses import dataclass
from enum import Enum
from typing import Any

class Types(Enum):
    INTEGER = 0
    STRING = 1
    FUNCTION = 2
    BOOLEAN = 3
    LIST = 4
    NONE = 5
    PUNCTUATION = 6
    KEYWORD = 7
    UNDEFINED = 8


@dataclass
class Object:
    type: Types
    value: Any


obj = Object(Types.UNDEFINED, Any)
obj.type = Types.STRING
obj.value = "test"
print(isinstance(obj, Object))
from string import punctuation
print(punctuation)
