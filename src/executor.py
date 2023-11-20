from types import FunctionType
from sys import stdout
from string import punctuation

from src.data import Object, Types

BUILTIN = [
    'out',
    'call',
    'func',
    'end'
]

VARS = {}
VAR  = False

FUNCS = {}
FUNC  = None

CALC  = []

class BuiltFunctions:

    @staticmethod
    def out(args) -> None:
        for arg in args:
            stdout.write(str(arg.value) + ' ')
        stdout.write('\n')


def get_arg(args: list, arg: int):
    try: return args[arg].value
    except IndexError: return


def builtin(token, args) -> FunctionType:
    global FUNCS, FUNC

    if token == 'out':
        if FUNC:
            FUNCS[FUNC]['commands'].append((BuiltFunctions.out, args))
            return
        BuiltFunctions.out([arg.value for arg in args])

    elif token == 'func':
        FUNC = args[0].value
        FUNCS[args[0].value] = {'args': {arg.value: None for arg in args[1:]}, 'commands': []}

    elif token == 'call':
        func_args = FUNCS[args[0].value]['args']

        if len(func_args) > len(args[1:]):
            print(f'ERROR: missing arguments, function: `{args[0]}`')
            exit(0)

        for func_arg_index, func_arg in enumerate(func_args):
            func_args[func_arg] = args[func_arg_index + 1].value

        FUNCS[args[0].value]['args'] = func_args

        commands = FUNCS[args[0].value]['commands']
        for command, args in commands:
            for arg in range(len(args)):
                if args[arg].type == Types.KEYWORD and args[arg].value.startswith('$'):
                    var = args[arg].value.split('$', 1)[-1]
                    argument_value  = func_args.get(var)
                    if argument_value:
                        args[arg].value = argument_value
                        continue

                    get_var = VARS.get(var)
                    if not get_var:
                        print(f'ERROR: unknow variable `{var}`')
                        exit(0)

                    args[arg].value = get_var.value

            command(args)

    elif token == 'end':
        FUNC = None


def punc(token):
    pass


def execute(objects: list[list[Object]]) -> None:
    for row, line in enumerate(objects):
        for column, object in enumerate(line):
            if object.type is Types.KEYWORD:
                builtin(object.value, line[column+1:])
            
            elif object.type is Types.PUNCTUATION:
                if object.value == '=':
                    if len

    print(VARS)
