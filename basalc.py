"""
The main file
"""

from core.lexer import lex
from core.parser import parse
from utils.peekable import Peekable


with open("file.txt", 'r') as file:
    filedata = Peekable(enumerate(file.read()))

tokens = Peekable(lex(filedata, "file"))
print(tokens)
ast = parse(tokens)
print(ast["program"][0].code[0].content)
