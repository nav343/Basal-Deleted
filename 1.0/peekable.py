from typing import Protocol

class Iterator(Protocol):
    def __iter__(self):
        ...
        
    def __next__(self):
        ...

class Peekable:
    def __init__(self, iterator: Iterator):
        self.next = next(iterator, None)
        self.iterator = iterator

    def __iter__(self):
        self

    def __next__(self):
        if self.next is None:
            raise StopIteration
        res = self.next
        self.next = next(self.iterator, None)
        return res

    def peek(self):
        return self.next
