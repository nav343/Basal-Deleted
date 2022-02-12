from utils.token import *

class Node:
    def __init__(self, content, token_number, line_number):
        # self.name = name
        self.content = content
        self.column = token_number
        self.line = line_number

class VarNode(Node):
    def __init__(self, name, content, token_number, line_number):
        self.name = name

class OutNode(Node):
    def __init__(self, content, token_number, line_number): pass
        
class FuncNode(Node):
    def __init__(self, name, parameters ,content, token_number, line_number):
        self.name = name
        self.parameters = parameters

        
def parse(Tokens):
    token_number = 0
    line_number = 1
    ast = {"program":[]}
    for token in Tokens:
        # print(token)
        
        if isinstance(token, Identifier) and token.ident == "var":
            if isinstance(Tokens[token_number + 1], Number):
                print("Error on line", line_number, "word count:", token_number + 2)
                print("Variable cannot be int")
            node = VarNode(Tokens[token_number + 1], Tokens[token_number + 3], token_number, line_number)
            ast["program"].append([node])
        if isinstance(token, Identifier) and token.ident == "out":
            node = OutNode(Tokens[token_number + 2], token_number, line_number)
        if isinstance(token, Identifier) and token.ident == "func":
            pass
        if isinstance(token, EOF):
            line_number += 1
        token_number += 1
    return ast
