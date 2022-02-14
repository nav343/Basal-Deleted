from abc import ABC, abstractmethod
from utils.type import Type
from utils.error import Position
from utils.token import Identifier, Number


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
    __match_args__ = ("statements",)

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
    __slots__ = "name"
    __match_args__ = ("statements",)

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
