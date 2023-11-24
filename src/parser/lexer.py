"""
Lexer for the Flood programming language.
"""
from typing import Any

from src.parser.data import Object, Types
from src.parser.help import repl, errast
from src.parser.typesf import conv

from src.parser.help import readf

# keywords, ints, floats, strings
# arrays

def lexer(path: str) -> list[list[Object]]:
    lines = readf(path)
    objs: list[list[Object]] = []
    
    start_char_arr = False

    undefined = (Types.UNDEFINED, Any)

    for row, line in enumerate(lines):
        objs.append([Object()])

        for col, ch in enumerate(line):
            obj = objs[row][-1]

            if ch == "\"":
                errast("you have to start the string in a new object", 
                       obj.value != Any and obj.type != Types.STRING, 
                       row+1, col+1)

                start_char_arr = not start_char_arr 

            elif start_char_arr:
                if obj.type == Types.UNDEFINED:
                    obj.type, obj.value = Types.STRING, ""
                obj.value += ch

            elif ch == ' ':
                if obj.type == Types.UNDEFINED and obj.value:
                    conv(objs[row][-1])

                if (obj.type, obj.value) == undefined:
                    continue

                objs[row].append(Object())

            else:
                if obj.value == Any:
                    obj.value = ''

                errast("attempted to end a string without adding a space **after**", 
                       not start_char_arr and obj.type == Types.STRING, 
                       row = row + 1, col = col)
                
                obj.value += ch

        if obj.type == Types.UNDEFINED:
            conv(objs[row][-1])

        errast("close the string you started.", 
               start_char_arr, 
               row = row + 1)

        objs[row][-1] = obj

    return objs


def parse(): ...


def lexer(filepath) -> list[list[Object]]:
    lines = cleanlns(readlns(filepath))

    objects: list[list[Object]] = []
    point, in_str = None, False

    for row, line in enumerate(lines):
        line = repl(line, '', -1) if line[-1] == '\n' else line

        if not len(line.replace(' ', '')):
            objects.append([])
            continue

        while line[-1] == ' ':
            line = repl(line, '', -1)

        objects.append([Object()])

        for column, character in enumerate(line):
            if character == '"':
                if len(objects) != 0:
                    if objects[row][-1].value != Any and \
                       objects[row][-1].type == Types.UNDEFINED:
                        objects[row][-1].value += character
                        continue

                in_str = not in_str
                point = column

            elif in_str:
                if objects[row][-1].type == Types.UNDEFINED:
                    objects[row][-1].type = Types.STRING
                    objects[row][-1].value = ''
                objects[row][-1].value += character

            elif character == ' ':
                if objects[row][-1].type == Types.UNDEFINED and \
                   objects[row][-1].value != Any:
                    conv(objects[row][-1])

                if objects[row][-1].value != Any:
                    objects[row].append(Object())

            else:
                if objects[row][-1].value == Any:
                    objects[row][-1].value = ''
                objects[row][-1].value += character

        if objects[row][-1].type == Types.UNDEFINED:
            conv(objects[row][-1])

        if in_str:
            print(f'{filepath}:{row}:{point}: string was started but not closed.')
            exit(0)

        array = []

        in_arr = False
        level = 'array[-1]'

        for row, line in enumerate(objects):
            array.append([])
            for column, object in enumerate(line):
                if object.value == '[':
                    if isinstance(eval(level), Object):
                        exec(level + '.value' + '.append(Object(Types.ARRAY, []))')
                        level += '.value[-1]'
                    else:
                        exec(level + '.append(Object(Types.ARRAY, []))')
                        level += '[-1]'

                    in_arr = True

                elif object.value == ']':
                    if not in_arr:
                        print(
                            f'{filepath}:{row+1}:{column+1}: you tried to end a array you never started.')
                        exit(0)

                    if level[-6:] == '.value':
                        level = level[:-6]
                        continue

                    i = 4
                    while level[:-i][-1] == '[':
                        i += 1
                    level = level[:-i]

                else:
                    try:
                        exec(level + '.value' + '.append(object)')
                    except AttributeError:
                        exec(level + '.append(object)')
    return array
