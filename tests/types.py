import sys

sys.path.append('.')

from src.lexer import read


def test_reader():
    strline = read('tests/types.flood')[0]
    strline = list(strline)
    strline[-1] = '' if strline[-1] == '\n' else strline[-1]
    strline = ''.join(strline)

    parsed = []
    tmp = []
    nlevel, level = 0, ''

    for index, character in enumerate(strline):
        if character == '[':
            assert eval('tmp' + level + '[-1]') != None, 'You did not started a new value with `,`.'

            t = eval('tmp' + level)
            exec('tmp' + level + '.append([])')
            print(t)
            
            assert nlevel <= 9, f'{index}: You can not go deeper than 9'

            level += '[-1]'
            nlevel += 1
            continue
        
        if character == ',':
            exec('tmp' + level + '.append(None)')
            continue

        if character == ']':
            level = level[:-4]
            nlevel -= 1
            continue

    print(tmp)

if __name__ == '__main__':
    test_reader()
