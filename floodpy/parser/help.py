"""
Helpful functions and utilities.
"""
def repl(string: str, 
         character: str, 
         index: int, 
         condition: bool = None) -> str:
    """
    Replace the char that is in the index given.

    string : `str`
        The original text.
    
    character : `str`
        New character.
    
    index : `int`
        Where is the character you want to replace.
    
    condition : `bool` `optional`
        Add a condition, if its `True` the code will continue
        else will stop and return the original string.
    """
    if condition != None and not condition:
        return string

    string        = list(string)
    string[index] = character
    string        = ''.join(string)
    
    return string


def cleanf(lines: list[str]) -> list[str]:
    """
    Cleans all the lines given of `\n`, empty string 
    and unecessary spaces.

    lines : `list[str]`
        The array of string you want to clean.
    """
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
    """
    Reads a file by lines.

    filepath : `str`
        Where's the file located.
    """
    with open(filepath, 'r') as fr:
        return cleanf(fr.readlines())


def errast(message, condition, row: str | int = '?', col: str | int = '?') -> None:
    """
    Helps with the error handling.

    message : `str`
        What is the error caused by.
    
    condition : `bool`
        If the condition is true will throw the error.
    
    row : `int` `optional`
        Postion where the error happened.

    col : `int` `optional`
        Postion where the error happened.
    """
    if not condition:
        return

    print(f'{row if row else '?'}:{col if col else '?'}', message)
    exit(1)
