import sys
sys.path.append('.')

from src.parser.lexer import lex_file

print(lex_file('tests/test_executor.flood'))