"""
Helpful functions and utilities.
"""
def repl(string: str, character: str, index: int, condition: bool = None) -> str:
    if condition != None and not condition:
        return string

    string        = list(string)
    string[index] = character
    string        = ''.join(string)
    
    return string


def cleanf(lines: list[str]) -> list[str]:
    result = []
    
    for line in lines:
        line = repl(line, "", -1, line[-1] == '\n')
        
        if not line:
            continue

        if not len(line.replace(" ", "")):
            continue
        
        while line[-1] == " ":
            line = repl(line, "", -1)

        while line[0] == " ":
            line = repl(line, "", 0)

        result.append(line)

    return result


def readf(filepath: str) -> list[str]:
    with open(filepath, 'r') as fr:
        return cleanf(fr.readlines())


def errast(message, condition, row: str | int = '?', col: str | int = '?') -> None:
    if not condition:
        return

    print(f'{row if row else '?'}:{col if col else '?'}', message)
    exit(1)
