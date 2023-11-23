def repl(string: str, character: str, index: int) -> str:
    line        = list(string)
    line[index] = character
    line        = ''.join(line)
    
    return line


def is_float(element: Any) -> bool:
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