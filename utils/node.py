from abc import ABC, abstractmethod
from utils.type import Type
from utils.error import Position
from utils.token import *


class Node(ABC):
    __slots__ = ()
    
    @abstractmethod
    def position(self) -> Position:
        ...
        
    @abstractmethod
    def type(self) -> Type:
        ...
    
    @abstractmethod
    def __repr__(self) -> str:
        ...

class NumberNode(Node):
    __slots__ = "number"
    __match_args__ = ("number",)

    def __init__(self, number: Number):
        self.number = number
        
    def position(self) -> Position:
        return self.number.position
    
    def type(self) -> Type:
        return Type.Number
    
    def __repr__(self) -> str:
        return f"NumberNode({self.number})"

class FloatNode(Node):
    __slots__ = "float"
    __match_args__ = ("float",)

    def __init__(self, float: Float):
        self.float = float
        
    def position(self) -> Position:
        return self.float.position
    
    def type(self) -> Type:
        return Type.Float
    
    def __repr__(self) -> str:
        return f"FloatNode({self.float})"

class StatementNode(Node):
    __slots__ = "statements", "pos"
    __match_args__ = ("statements",)

    def __init__(self, statements: list[Node], pos: Position):
        self.statements = statements
        self.pos = pos
        
    def position(self) -> Position:
        return self.pos
    
    def type(self) -> Type:
        return Type.Null
    
    def __repr__(self) -> str:
        return f"StatementNode({self.statements})"

class VarAssignNode(Node):
    __slots__ = "name", "node", "pos"
    __match_args__ = ("name", "node")

    def __init__(self, name: Identifier, node: Node, pos: Position):
        self.name = name
        self.node = node
        self.pos = pos
        
    def position(self) -> Position:
        return self.pos
    
    def type(self) -> Type:
        return Type.Null
    
    def __repr__(self) -> str:
        return f"VarAssignNode({self.name} = {self.node})"

class VarAcessNode(Node):
    __slots__ = "name", "type_"
    __match_args__ = ("name",)

    def __init__(self, name: Identifier, type_: Type):
        self.name = name
        self.type_ = type_
        
    def position(self) -> Position:
        return self.name.pos

    def type(self) -> Type:
        return self.type_
    
    def __repr__(self) -> str:
        return f"VarAssignNode({self.name} = {self.node})"

class BinaryNode(Node):
    __slots__ = "op", "type_", "left", "right"
    __match_args__ = ("op", "left", "right")

    def __init__(self, op: Token, left: Node, right: Node, type_ : Type ):
        self.left = left
        self.right = right
        self.op = op
        self.type_ = type_
        
    def position(self) -> Position:
        return self.left.position().merged(self.right.position())

    def type(self) -> Type:
        return self.type_

    def __repr__(self) -> str:
        return f"BinaryNode({self.left} {self.op} {self.right})"

class UnaryNode(Node):
    __slots__ = "op", "type_", "expr"
    __match_args__ = ("op", "expr")

    def __init__(self, op: Token, expr: Node, type_ : Type ):
        self.expr = expr
        self.op = op
        self.type_ = type_

    def position(self) -> Position:
        return self.op.position.merged(self.expr.position())

    def type(self) -> Type:
        return self.type_

    def __repr__(self) -> str:
        return f"UnaryNode({self.op} {self.expr})"

class CallNode(Node):
    __slots__ = "function", "arguments", "type_", "pos"
    __match_args__ = ("function", "arguments")

    def __init__(self, function: Identifier, arguments: list[Node], type_ : Type, pos: Position):
        self.function = function
        self.arguments = arguments
        self.pos = pos
        self.type_ = type_

    def position(self) -> Position:
        return self.pos

    def type(self) -> Type:
        return self.type_

    def __repr__(self) -> str:
        return f"CallNode({self.function}({self.arguments}))"

class FunctionNode(Node):
    __slots__ = "name", "type_", "parameters", "body", "pos"
    __match_args__ = ("name", "body")

    def __init__(self, name: Identifier, parameters: list[Type], body: Node, type_ : Type, pos: Position):
        self.name = name
        self.parameters = parameters
        self.type_ = type_
        self.body = body
        self.pos = pos

    def position(self) -> Position:
        return self.pos

    def type(self) -> Type:
        return self.type_

    def __repr__(self) -> str:
        return f"FunctionNode({self.name}({self.parameters}) -> {self.type_} : {self.body})"

class IfNode(Node):
    __slots__ = "condition", "then", "else_", "pos"
    __match_args__ = ("condition", "then", "else_")

    def __init__(self, condition: Node, then: Node, else_: Node | None, pos: Position):
        self.condition = condition
        self.else_ = else_
        self.then = then
        self.pos = pos

    def position(self) -> Position:
        return self.pos

    def type(self) -> Type:
        return Type.Null

    def __repr__(self) -> str:
        return f"IfNode({self.condition} ? {self.then} : {self.else_})"

class WhileNode(Node):
    __slots__ = "condition", "body", "pos"
    __match_args__ = ("condition", "body")

    def __init__(self, condition: Node, body: Node, pos: Position):
        self.condition = condition
        self.body = body
        self.pos = pos

    def position(self) -> Position:
        return self.pos

    def type(self) -> Type:
        return Type.Null

    def __repr__(self) -> str:
        return f"WhileNode({self.condition} : {self.body})"

class ForNode(Node):
    __slots__ = "i", "iterator", "body", "pos"
    __match_args__ = ("i", "iterator", "body")

    def __init__(self, i: Identifier, iterator: Node, body: Node, pos: Position):
        self.i = i
        self.iterator = iterator
        self.body = body
        self.pos = pos

    def position(self) -> Position:
        return self.pos

    def type(self) -> Type:
        return Type.Null

    def __repr__(self) -> str:
        return f"ForNode({self.i} : {self.iterator} -> {self.body})"

class CharNode(Node):
    __slots__ = "char"
    __match_args__ = ("char", )

    def __init__(self, char: Char):
        self.char = char

    def position(self) -> Position:
        return self.char.position

    def type(self) -> Type:
        return Type.Char

    def __repr__(self) -> str:
        return f"CharNode({self.char})"

class StringNode(Node):
    __slots__ = "string"
    __match_args__ = ("string",)

    def __init__(self, string: String):
        self.string = string

    def position(self) -> Position:
        return self.string.position

    def type(self) -> Type:
        return Type.Char

    def __repr__(self) -> str:
        return f"StringNode({self.string})"
