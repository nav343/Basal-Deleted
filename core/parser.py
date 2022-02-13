<<<<<<< HEAD
from utils.error import Position, SyntaxError
from utils.node import Node, NumberNode, StatementNode
from utils.token import EOF, Keyword, Number, Token
from utils.peekable import Peekable

class Parser:
    __slots__ = "tokens"

    def __init__(self, tokens: Peekable[Token]) -> None:
        self.tokens = tokens

    def next(self) -> Token:
        return next(self.tokens)

    def peek(self) -> Token:
        return self.tokens.peek()

    def current(self) -> Token:
        return self.tokens.current()

    def statemtents(self) -> Node:
        statements = []
        start: Position = self.current().position
        while self.current() != EOF:
            statements.append(self.statement())
        self.next()
        return StatementNode(statements, start.merged(self.current().position))
            
    def statement(self) -> Node:
        return self.expression()
    
    def expression(self) -> Node:
        match self.current():
            case Keyword(keyword = "let"):
                return self.define()
            case _:
                return self.factor()
            
    def factor(self) -> Node:
        match self.current():
            case Number(_):
                node = NumberNode(self.current())
                self.next()
                return node
            case t:
                raise SyntaxError(self.current().position, f"Unexpected Token: {t}")


def parse(tokens: Peekable[Token]) -> None:
    parser = Parser(tokens)
    parser.next()
    return parser.statemtents()
=======
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
        if isinstance(Tokens[token_number], Keyword) and token.keyword == "func":
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
                while True:
                    # print(tmp)
                    # print(Tokens[token_number + tmp].ident)
                    if isinstance(Tokens[end_of_params + tmp], RCurly):
                        break
                    if isinstance(Tokens[end_of_params + tmp], Keyword) and Tokens[end_of_params +tmp].keyword == "let":
                        if isinstance(Tokens[end_of_params + tmp + 1], Number):
                            raise SyntaxError(Tokens[end_of_params + tmp + 1].position, "Variable cannot be int")
                        node = VarNode(Tokens[token_number + 1], Tokens[token_number + 3], token_number, Tokens[end_of_params + tmp].position.line)
                        code.append(node)
                    elif isinstance(Tokens[end_of_params + tmp], Identifier) and Tokens[end_of_params + tmp].ident == "out":
                        node = OutNode(Tokens[end_of_params + tmp + 2], token_number, Tokens[end_of_params + tmp].position.line)
                        code.append(node)
                    
                    tmp += 1
            node = FuncNode(nameof_func, params, code, token_number, line_number)
            ast["program"].append(node)
        elif isinstance(Tokens[token_number], Keyword) and token.keyword == "let":
            if not infunc:
                if isinstance(Tokens[token_number + 1], Number):
                    raise SyntaxError(Tokens[token_number + 1].position, "Invalid variable name on line " + str(line_number) + ", word " + str(token_number + 2))
                node = VarNode(Tokens[token_number + 1], Tokens[token_number + 3], token_number, Tokens[token_number].position.line)
                ast["program"].append(node)
        elif isinstance(Tokens[token_number], Identifier) and token.ident == "out":
            if not infunc:
                node = OutNode(Tokens[token_number + 2], token_number, Tokens[token_number].position.line)
                ast["program"].append(node)
        

        token_number += 1
    return ast
>>>>>>> 3109dbcf6338e4751a81abbfcd549e8a7893e83a
