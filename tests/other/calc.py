import sys
sys.path.append('.')

from src.parser.file import lexer

lexed_file = lexer('tests/test_executor.flood')

i = 0
l = 0
z = [int(i) if i.isdigit() else i for i in z.split(' ')]
while i < len(z) - 1:
    i += 1

    print(z)

    if '(' in z or ')' in z:
        continue

    if z[i] in ('*', '/'):
        a = z[i-1]
        b = z[i+1]

        del z[i]
        del z[i]
        del z[i-1]

        z.append(a*b)
