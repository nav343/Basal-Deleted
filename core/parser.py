from typing import Callable

from utils.error import *
from utils.node import *
from utils.scope import Scope
from utils.token import *
from utils.peekable import Peekable
from utils.type import Type

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

    def statemtents(self, scope: Scope) -> Node:
        statements = []
        start: Position = self.current().position
        while type(self.current()) != EOF:
            statements.append(self.statement(scope))
        self.next()
        return StatementNode(statements, start.merged(self.current().position))
            
    def statement(self, scope: Scope) -> Node:
        match self.current():
            case Keyword(keyword = "let"):
                return self.define(scope)
            case _:
                return self.expression(scope)
    
    def expression(self, scope: Scope) -> Node:
        return self.comparision(scope)
    
    def comparision(self, scope: Scope) -> Node:
        if type(self.current()) == Not:
            token = self.current()
            self.next()
            node = self.comparision(scope)
            t = node.type().get_result_type_unary(token)
            if t is None:
                raise TypeError(node.position(), f"Expected a boolean, found {node.type()}")
            return UnaryNode(token, node, t)
        return self.binary_op(scope, Parser.bitwise, Parser.bitwise, [Equals, NotEqual, GreaterThan, GreaterThanEqual, SmallerThan, SmallerThanEqual])
    
    def bitwise(self, scope: Scope) -> Node:
        return self.binary_op(scope, Parser.arithmetic, Parser.arithmetic, [ShiftLeft, ShiftRight, And, Or, Xor])
    
    def arithmetic(self, scope: Scope) -> Node:
        return self.binary_op(scope, Parser.term, Parser.term, [Plus, Minus])
    
    def term(self, scope: Scope) -> Node:
        return self.binary_op(scope, Parser.factor, Parser.factor, [Multiply, Divide, Mod])

    def factor(self, scope: Scope) -> Node:
        token = self.current()
        match token:
            case Minus() | Plus() | Increment() | Decrement():
                self.next()
                node = self.factor(scope)
                t = node.type().get_result_type_unary(token)
                if t is None:
                    raise TypeError(node.position(), f"Expected a number, found {node.type()}")
                return UnaryNode(token, node, t)
            case _:
                return self.power(scope)

    def power(self, scope: Scope) -> Node:
        return self.binary_op(scope, Parser.atom, Parser.atom, [Power])

    def atom(self, scope: Scope) -> Node:
        match self.current():
            case Number(_):
                node = NumberNode(self.current())
                self.next()
                return node
            case Identifier(_):
                match scope.get_variable(self.current()):
                    case None:
                        raise UndefinedVariableError(self.current().position, f"variable {self.current()} is not defined")
                    case t:
                        node = VarAcessNode(self.current(), t)
                        self.next()
                        return node
            case t:
                raise SyntaxError(self.current().position, f"Unexpected Token: {t}")
  
    def define(self, scope: Scope) -> Node:
        pos: Position = self.current().position
        match self.next():
            case Identifier(_):
                c = self.current()
                if type(self.next()) != Assign:
                    raise SyntaxError(self.current().position, f"Expected '=', got {self.current()}")
                self.next()
                expr = self.expression(scope)
                scope.register_variable(c, expr.type())
                return VarAssignNode(c, expr, pos.merged(expr.position()))
            case t:
                raise SyntaxError(self.current().position, f"Unexpected Token: {t}, expected an Identifier after 'let'")

    def binary_op(self, scope: Scope, left: Callable[["Parser", Scope], Node], right: Callable[["Parser", Scope], Node], op: list[Token]) -> Node:
        left_ = left(self, scope)
        token = self.current()
        while type(token) in op:
            self.next()
            right_ = right(self, scope)
            t = left_.type().get_result_type(right_.type(), token)
            if t is None:
                raise TypeError(right_.position(), f"Cannot apply operator {token} to types {left_.type()} and {right_.type()}")
            left_ = BinaryNode(token, left_, right_, Type.Null)
            token = self.current()
        return left_


def parse(tokens: Peekable[Token]) -> None:
    parser = Parser(tokens)
    parser.next()
    return parser.statemtents(Scope())
