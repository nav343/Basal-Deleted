"""
The main file
"""
#import lexer
from core.lexer import lex
#import parser
from core.parser import parse

#open text file
file = open("file.txt", 'r')
filedata = file.read()
file.close()


tokens = lex(filedata, "file")
print(tokens)
ast = parse(tokens)
print(ast)
