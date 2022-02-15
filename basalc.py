"""
The main file
"""

from core.lexer import lex
from core.parser import parse
from utils.peekable import Peekable


with open("file.txt", 'r') as file:
    filedata = Peekable(enumerate(file.read()))

tokens = Peekable(lex(filedata, "file"))
ast = parse(tokens)
print(ast)
