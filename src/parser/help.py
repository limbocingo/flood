def repl(string: str, character: str, index: int) -> str:
    line        = list(string)
    line[index] = character
    line        = ''.join(line)
    
    return line