import sys
sys.path.append('.')

from src.parser.file import lexer

lexer('tests/test_executor.flood')