import sys
import unittest

sys.path.append('.')

from src.data import Object, Types
from src.lexer import conv, lexer


class TestLexer(unittest.TestCase):

    def test_converter(self):
        object = Object(value='30.40')
        conv(object)

        self.assertTrue(object.type == Types.FLOAT, 'converter failed, converting `UNDEFINED` to `FLOAT`')

    def test_lexer(self):
        response = [[
            Object(Types.STRING, 'testing lexer'),
            Object(Types.INTEGER, 87),
            Object(Types.FLOAT, 87.5),
            Object(Types.PUNCTUATION, '*'),
            Object(Types.PUNCTUATION, '+'),
            Object(Types.PUNCTUATION, '-'),
        ]]

        self.assertEqual(lexer('tests/test_lexer.flood'),
                         response, 'lexer did not returned excepted value')


if __name__ == '__main__':
    unittest.main()
