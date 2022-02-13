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

<<<<<<< HEAD
    def __init__(self, statements: list[Node], pos: Position):
        self.statements = statements
        self.pos = pos
=======
class OutNode(Node):
    def __init__(self, content, token_number, line_number): 
        self.content = content

>>>>>>> 3109dbcf6338e4751a81abbfcd549e8a7893e83a
        
    def position(self) -> Position:
        return self.pos
    
    def type(self) -> Type:
        return Type.Null
