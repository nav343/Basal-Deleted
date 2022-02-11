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

class Operator(Token):
    @position
    def __init__(self, operator: str):
        self.operator= operator
    def __repr__(self) -> str:
        return f"Operator : '{self.operator}'"
class Identifier(Token):
    @position
    def __init__(self, ident: str):
        self.ident = ident
        
    def __repr__(self) -> str:
        return f"Identifier : '{self.ident}'"
