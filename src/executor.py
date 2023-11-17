from src.data import Types, Object
from type import FunctionType


class BuiltFunctions:

    @staticmethod
    def out(*args, **kwargs) -> None:
        for arg in *args:
            print(arg, end=' ')

def builtin(token: str, *args) -> FunctionType:
    if token == 'out':
        BuiltFunctions.out(args)


def execute(objects: list[list[Object]]) -> None:
    for line in objects:
        for object in line:
            if object.type == Types.KEYWORD:
                builtin(object.value)            
    