from abc import ABC, abstractclassmethod

class Error(Exception, ABC):
    @abstractclassmethod
    def __str__(self) -> str:
        ...
        
class Position:
    def __init__(self, line, start, end, file):
        self.line = line
        self.start = start
        self.end = end
        self.file = file

class IllegalCharError(Error):
    def __init__(self, position: Position, char: str):
        self.file = position.file
        self.line = position.line
        self.start = position.start
        self.end = position.end
        self.char = char

    def __str__(self) -> str:
        return f"Illegal character at {self.file}:{self.line}:{self.start}-{self.end} : {self.char}"
