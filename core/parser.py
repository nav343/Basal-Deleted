from utils.error import Position, SyntaxError
from utils.node import Node, NumberNode, StatementNode, VarAssignNode
from utils.token import EOF, Assign, Identifier, Keyword, Number, Token
from utils.peekable import Peekable

class Parser:
    __slots__ = "tokens"

    def __init__(self, tokens: Peekable[Token]) -> None:
        self.tokens = tokens

    def next(self) -> Token | None:
        return next(self.tokens, None)

    def peek(self) -> Token | None:
        return self.tokens.peek()

    def current(self) -> Token | None:
        return self.tokens.current()

    def statemtents(self) -> Node:
        statements = []
        start: Position = self.current().position
        while type(self.current()) != EOF:
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
            
    def define(self) -> Node:
        pos: Position = self.current().position
        match self.next():
            case Identifier(c):
                if type(self.next()) != Assign:
                    raise SyntaxError(self.current().position, f"Expected '=', got {self.current()}")
                self.next()
                expr = self.expression()
                return VarAssignNode(c, expr, pos.merged(expr.position()))
            case t:
                raise SyntaxError(self.current().position, f"Unexpected Token: {t}, expected an Identifier after 'let'")


def parse(tokens: Peekable[Token]) -> None:
    parser = Parser(tokens)
    parser.next()
    return parser.statemtents()
