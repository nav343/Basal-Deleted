from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from error import Position

def position(function):
    def new(self, position : Position, *args, **kwargs):
        function(self, *args, **kwargs)
        self.position = position
        
    return new

class Token(ABC): 
    @position
    def __init__(self):
        pass
   
    @abstractmethod
    def __repr__(self) -> str:
        ...

class Identifier(Token):
    @position
    def __init__(self, ident: str):
        self.ident = ident
        
    def __repr__(self) -> str:
        return f"'{self.ident}'"

class Plus(Token):    
    def __repr__(self) -> str:
        return "+"

class EOF(Token):
    def __repr__(self) -> str:
        return "EOF"
