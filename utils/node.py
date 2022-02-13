from abc import ABC, abstractmethod
from utils.type import Type
from utils.error import Position
from utils.token import Number


class Node(ABC):
    __slots__ = ()
    
    @abstractmethod
    def position(self) -> Position:
        ...
        
    @abstractmethod
    def type(self) -> Type:
        ...

class NumberNode(Node):
    __slots__ = "number"

    def __init__(self, number: Number):
        self.number = number
        
    def position(self) -> Position:
        return self.number.position
    
    def type(self) -> Type:
        return Type.Number

class StatementNode(Node):
    __slots__ = "statements", "pos"

    def __init__(self, statements: list[Node], pos: Position):
        self.statements = statements
        self.pos = pos
        
    def position(self) -> Position:
        return self.pos
    
    def type(self) -> Type:
        return Type.Null
