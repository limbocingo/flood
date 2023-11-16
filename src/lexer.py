from string import punctuation
from typing import Any

from src.data import Object, Types
from src.file import read_by_lines

from pprint import pprint


def is_float(element: any) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False


def conv(object: Object) -> Any | Types:
    if object.value.isdigit():
        object.value = int(object.value)
        object.type = Types.INTEGER

    elif is_float(object.value):
        object.value = float(object.value)
        object.type = Types.FLOAT

    elif object.value in list(punctuation):
        object.type = Types.PUNCTUATION

    elif object.value.upper() in ('TRUE', 'FALSE'):
        object.type = Types.BOOLEAN
        object.value = True if object.value.upper() == "TRUE" else False

    else:
        object.type = Types.KEYWORD


def lexer(filepath) -> list[list[Object]]:
    lines = read_by_lines(filepath)

    objects: list[list[Object]] = []
    point, in_str = None, False

    for row, line in enumerate(lines):
        line     = list(line)
        line[-1] = '' if line[-1] == '\n' else line[-1]
        line     = ''.join(line)

        objects.append([Object()])

        for column, character in enumerate(line):
            if character == '"':
                if len(objects) != 0:
                    if objects[row][-1].value != Any and objects[row][-1].type == Types.UNDEFINED:
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
                if objects[row][-1].type == Types.UNDEFINED:
                    conv(objects[row][-1])

                objects[row].append(Object())

            else:
                if objects[row][-1].value == Any:
                    objects[row][-1].value = ''
                objects[row][-1].value += character

        if objects[row][-1].type == Types.UNDEFINED:
            conv(objects[row][-1])

        if in_str:
            print(f'{filepath}:{row}:{point}: string started but didn\'t end.')
            exit(0)

        array  = []

        in_arr = False
        level  = 'array[-1]'

        for row, line in enumerate(objects):
            array.append([])
            for column, object in enumerate(line):
                # TODO: 'Object' object has no attribute 'append'
                if object.value == '[':
                    if isinstance(eval(level), Object):
                        exec(level + '.value' + '.append(Object(Types.ARRAY, []))')

                    exec(level + '.append(Object(Types.ARRAY, []))')

                    level += '[-1]'

                    in_arr = True

                elif object.value == ']':
                    if not in_arr:
                        print(f'{filepath}:{row+1}:{column+1}: you tried to end a array you never started.')
                        exit(0)

                    if level[-6:] == '.value':
                        level = level[:-6]
                        continue

                    i = 4
                    while level[:-i][-1] == '[':
                        i += 1
                    level = level[:-i]

                else:
                    ...
                    #print(level)
                    # try:
                    #     exec(level + '.value' + '.append(object.value)')
                    # except AttributeError:
                    #     exec(level + '.append(object.value)')


        #pprint(array)


    return objects
