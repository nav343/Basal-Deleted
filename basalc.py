"""
The main file
"""

from core.lexer import lex
from core.parser import parse


with open("file.txt", 'r') as file:
    filedata = file.read()

tokens = lex(filedata, "file")
print(tokens)
ast = parse(tokens)
print(ast["program"][0].code[0].content)
