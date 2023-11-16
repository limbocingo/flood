from string import punctuation
from typing import Any

from src.data import Object, Types
from src.file import read_by_lines


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

    lexed: list[list[Object]] = []
    point, in_str = None, False

    for row, line in enumerate(lines):
        line = list(line)
        line[-1] = '' if line[-1] == '\n' else line[-1]
        line = ''.join(line)

        lexed.append([Object()])

        for column, character in enumerate(line):
            if character == '"':
                if len(lexed) != 0:
                    if lexed[row][-1].value != Any and lexed[row][-1].type == Types.UNDEFINED:
                        lexed[row][-1].value += character
                        continue

                in_str = not in_str
                point = column

            elif in_str:
                if lexed[row][-1].type == Types.UNDEFINED:
                    lexed[row][-1].type = Types.STRING
                    lexed[row][-1].value = ''
                lexed[row][-1].value += character

            elif character == ' ':
                if lexed[row][-1].type == Types.UNDEFINED:
                    conv(lexed[row][-1])

                lexed[row].append(Object())

            else:
                if lexed[row][-1].value == Any:
                    lexed[row][-1].value = ''
                lexed[row][-1].value += character

        if lexed[row][-1].type == Types.UNDEFINED:
            conv(lexed[row][-1])

        if in_str:
            print(f'{filepath}:{row}:{point}: string started but didn\'t end.')
            exit(0)

    return lexed
