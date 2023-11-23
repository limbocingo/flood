"""
Helpful functions and utilities.
"""
def repl(string: str, character: str, index: int) -> str:
    line        = list(string)
    line[index] = character
    line        = ''.join(line)
    
    return line


def readlns(filepath: str) -> list[str]:
    with open(filepath, 'r') as fr:
        return fr.readlines()
