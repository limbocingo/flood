TYPES = [
    'LIST',
    'STR',
    ''
]


def read(filepath: str) -> list:
    with open(filepath, 'r') as file_readable:
        return file_readable.readlines()
