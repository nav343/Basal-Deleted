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
        return f"Identifier: '{self.ident}'"

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
        return f"Keyword: '{self.keyword}'"

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

class NotEqual(Token):
    __slots__ = ()

    def __repr__(self) -> str:
        return "!="

class Not(Token):
    __slots__ = ()

    def __repr__(self) -> str:
        return "!"

class Multiply(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return "*"

class MultiplyAssign(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return "*="

class Divide(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return "/"

class DivideAssign(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return "/="
    
class Mod(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return "%"

class ModAssign(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return "%="
    
class Or(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return "|"

class OrAssign(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return "|="
    
class And(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return "&"

class AndAssign(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return "&="
    
class Xor(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return "^"

class XorAssign(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return "^="
    
class Power(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return "**"

class PowerAssign(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return "**="

class Colon(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return ":"

class Comma(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return ","

class RParen(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return ")"

class LParen(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return "("

class RSquare(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return "]"

class LSquare(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return "["

class RCurly(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return "}"

class LCurly(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return "{"

class Char(Token):
    __slots__ = "char"
    
    @position
    def __init__(self, char: str):
        self.char = char
    
    def __repr__(self) -> str:
        return f"Char: '{self.char!r}'"

class Question(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return "?"

class Dot(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return "."

class Arrow(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return "->"

class FatArrow(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return "=>"

class String(Token):
    __slots__ = "string"

    @position
    def __init__(self, string: str):
        self.string = string
        
    def __repr__(self) -> str:
        return f"\"{self.string!r}\""

class Increment(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return "++"

class Decrement(Token):
    __slots__ = ()
    
    def __repr__(self) -> str:
        return "--"
