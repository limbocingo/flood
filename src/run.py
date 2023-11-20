import sys
import json


def main(args: list[str]):
    sys.path.append('.')

    from src.lexer import lexer
    from src.executor import execute

    assert len(args) >= 2, "ERROR: no file found."
    
    objects = lexer(args[1])
    with open(f'objects.json', 'w') as fw:
        r = []
        for index, line in enumerate(objects):
            for object in line:
                r.append({'line': index + 1, 'type': object.type.value, 'value': object.value})

        json.dump(r, fw, indent=4, sort_keys=True)

    execute(objects)


if __name__ == '__main__':
    main(sys.argv)
