import sys


def main(args: list[str]):
    sys.path.append('.')

    from src.lexer import lexer
    from src.executor import execute

    assert len(args) >= 2, "ERROR: no file found."
    
    objects = lexer(args[1])
    execute(objects)


if __name__ == '__main__':
    main(sys.argv)
