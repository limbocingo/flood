def read_by_lines(filepath: str) -> list[str]:
    with open(filepath, 'r') as fr:
        return fr.readlines()
