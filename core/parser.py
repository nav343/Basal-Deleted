from utils.token import *
from utils.node import *
from utils.error import SyntaxError

def parse(Tokens):
    token_number = 0
    line_number = 1
    ast = {"program":[]}
    infunc = False
    for token in Tokens:
        # print(token)
        if isinstance(token, Keyword) and token.keyword == "func":
            infunc = True
            params = []
            nameof_func = Tokens[token_number + 1].ident
            end_of_params = 0
            code = []
            if isinstance(Tokens[token_number + 2], LParen):
                tmp = 3
                while True:
                    # print(tmp)
                    # print(Tokens[token_number + tmp].ident)
                    if Tokens[token_number + tmp] == ",":
                        pass
                    if isinstance(Tokens[token_number + tmp], Identifier):
                        params.append(Tokens[token_number + tmp].ident)
                    elif isinstance(Tokens[token_number + tmp], RParen):
                        end_of_params = tmp
                        break
                    tmp += 1
            if isinstance(Tokens[token_number + end_of_params + 1], LCurly):
                tmp = 2
                print(Tokens[token_number + tmp], "asdas")
                while True:
                    # print(tmp)
                    # print(Tokens[token_number + tmp].ident)
                    if isinstance(Tokens[end_of_params + tmp], RCurly):
                        break
                    if isinstance(Tokens[end_of_params + tmp], Keyword) and Tokens[end_of_params +tmp].keyword == "let":
                        if isinstance(Tokens[end_of_params + tmp + 1], Number):
                            raise SyntaxError(Tokens[end_of_params + tmp + 1].position, "Variable cannot be int")
                        node = VarNode(Tokens[token_number + 1], Tokens[token_number + 3], token_number, line_number)
                        code.append(node)

                    
                    tmp += 1
            print("_________________________________")

            print(code)
            node = FuncNode(nameof_func, params, code, token_number, line_number)
            ast["program"].append(node)
        elif isinstance(token, Keyword) and token.keyword == "let":
            if not infunc:
                if isinstance(Tokens[token_number + 1], Number):
                    print("Error on line", line_number, "word count:", token_number + 2)
                    print("Variable cannot be int")
                    raise SyntaxError("Invalid variable name on line " + str(line_number) + ", word " + str(token_number + 2))
                    break
                node = VarNode(Tokens[token_number + 1], Tokens[token_number + 3], token_number, line_number)
                ast["program"].append([node])
        elif isinstance(token, Identifier) and token.ident == "out":
            node = OutNode(Tokens[token_number + 2], token_number, line_number)
        
        
        token_number += 1
    return ast
