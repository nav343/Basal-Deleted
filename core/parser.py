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
