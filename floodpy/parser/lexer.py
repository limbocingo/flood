"""
Lexer of the Flood programming language.
"""
from typing import Any

from floodpy.parser.data import Object, Types
from floodpy.parser.help import errast
from floodpy.parser.typesf import conv

from floodpy.parser.help import readf


def lexer(file: str = None, lines: list[str] = None) -> list[list[Object]]:
    """
    Tokenizes the file in multiple :class:`floodpy.data.Object`.

    file : `str`
        The file you want to lex.

    lines : `list[str]`
        A array of strings you want to be lexed.
    """
    lines = readf(file) if not lines else lines
    objs: list[list[Object]] = []

    start_char_arr = False

    undefined = (Types.UNDEFINED, Any)

    for row, line in enumerate(lines):
        objs.append([Object()])

        for col, ch in enumerate(line):
            obj = objs[row][-1]

            if ch == "\"":  # check if string starts or ends
                errast("you have to start the string in a new object",  
                       obj.value != Any and obj.type != Types.STRING,
                       row+1, col+1)

                start_char_arr = not start_char_arr

            elif start_char_arr:
                if obj.type == Types.UNDEFINED:
                    obj.type, obj.value = Types.STRING, ""
                obj.value += ch

            elif ch == ' ': 
                # convert last object in its corresponded type
                if obj.type == Types.UNDEFINED and obj.value:
                    conv(objs[row][-1])

                if (obj.type, obj.value) == undefined:
                    continue

                # and start a new one `UNDEFINED`.
                objs[row].append(Object())

            else:
                if obj.value == Any:
                    obj.value = ''

                errast("bad way to close a `str`.",
                       not start_char_arr and obj.type == Types.STRING,
                       row=row + 1, col=col)

                obj.value += ch

        if obj.type == Types.UNDEFINED:
            conv(objs[row][-1])

        errast("close the string you started.",
               start_char_arr,
               row=row + 1)

        objs[row][-1] = obj

    return objs
