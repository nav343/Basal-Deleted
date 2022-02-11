from abc import ABC, abstractmethod


class Token(ABC):    
    @abstractmethod
    def __repr__(self) -> str:
        ...

def position(function):
    def new(self, position, *args, **kwargs):
        function(self, *args)
        self.position = position
        
    return new


class Identifier(Token):
    @position
    def __init__(self, ident: str):
        self.ident = ident
        
    def __repr__(self) -> str:
        return f"Identifier : '{self.ident}'"
