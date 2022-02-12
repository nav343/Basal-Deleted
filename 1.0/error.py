from abc import ABC
from token import position

class Error(Exception, ABC):
    __slots__ = "position", "details"

    def __str__(self) -> str:
        return f"{self.__class__.__name__} in {self.position.file} at {self.position.line}:{self.position.start} to {self.position.line_end}:{self.position.end} :: {self.details}"
        
class Position:
    __slots__ = "line", "start", "end", "file", "line_end"
    
    def __init__(self, line: int, start: int, end: int, file: str):
        self.line = line
        self.line_end = line
        self.start = start
        self.end = end
        self.file = file

class IllegalCharError(Error):
    __slots__ = "char"

    @position
    def __init__(self, char: str):
        self.details = f"Illegal character '{char}'"

class NumberLexError(Error):
    __slots__ = "char"

    @position
    def __init__(self, char: str):
        self.details = f"Unknown character found while lexing a number: '{char}'"

