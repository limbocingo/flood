import sys
sys.path.append('.')

from src.parser.lexer import lexer

print(lexer('tests/test_executor.flood'))