from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from error import Position
    
KEYWORDS = ("let", "if", "while", "for", "else", "func", "return")

def position(function):
    def new(self, position : Position, *args, **kwargs):
        self.position = position
        return function(self, *args, **kwargs)
        
    return new

class Token(ABC): 
    __slots__ = "position"

    @position
    def __init__(self):
        pass
   
    @abstractmethod
    def __repr__(self) -> str:
        ...

class Identifier(Token):
    __slots__ = "ident"

    @position
    def __init__(self, ident: str):
        self.ident = ident
        
    def __repr__(self) -> str:
        return f"'{self.ident}'"

class Plus(Token): 
    __slots__ = ()

    def __repr__(self) -> str:
        return "+"
    
class Minus(Token):
    __slots__ = ()

    def __repr__(self) -> str:
        return "-"
    
class Assign(Token):
    __slots__ = ()
  
    def __repr__(self) -> str:
        return "="

class Equals(Token):
    __slots__ = ()

    def __repr__(self) -> str:
        return "=="

class SemiColon(Token):
    __slots__ = ()

    def __repr__(self) -> str:
        return ";"

class Number(Token):
    __slots__ = "number"
    
    @position
    def __init__(self, number: int):
        self.number = number
        
    def __repr__(self) -> str:
        return f"{self.number}"

class Keyword(Token):
    __slots__ = "keyword"
   
    @position
    def __init__(self, keyword: str):
        self.keyword = keyword

    def __repr__(self) -> str:
        return f"'{self.keyword}'"

class EOF(Token):
    __slots__ = ()

    def __repr__(self) -> str:
        return "EOF"
 
class GreaterThan(Token):
    __slots__ = ()

    def __repr__(self) -> str:
        return ">"
        
class SmallerThan(Token):
    __slots__ = ()

    def __repr__(self) -> str:
        return "<"

class GreaterThanEqual(Token):
    __slots__ = ()

    def __repr__(self) -> str:
        return ">="
    
class SmallerThanEqual(Token):
    __slots__ = ()

    def __repr__(self) -> str:
        return "<="
    
class PlusAssign(Token):
    __slots__ = ()

    def __repr__(self) -> str:
        return "+="

class MinusAssign(Token):
    __slots__ = ()

    def __repr__(self) -> str:
        return "-="
