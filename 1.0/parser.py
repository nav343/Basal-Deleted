import lexer
from token import *

Tokens = lexer.lex(contents='var a = 2; \nvar b = 3;', filename="hi")
#print(tokens)
class Node:
    def __init__(self, name, content):
        self.name = name
        self.content = content

class VarNode(Node):
    def __init__(self, name, content):
        super().__init__(name, content)

def parse():
    token_number = 0
    line_number = 1
    ast = {"program":[]}
    for token in Tokens:
        # print(token)
        
        if isinstance(token, Identifier) and token.ident == "var":
            node = VarNode(Tokens[token_number + 1], Tokens[token_number + 3])
            ast["program"].append([node])
            
        token_number += 1
    return ast
ast = parse()
print(ast)
