import sys


def main(args: list[str]):
    sys.path.append('.')

    from src.lexer import lexer

    assert len(args) >= 2, "ERROR: no file found."
    print(lexer(args[1]))


if __name__ == '__main__':
    main(sys.argv)
