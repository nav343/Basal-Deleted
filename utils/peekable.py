from typing import Generic, Iterator, TypeVar

T = TypeVar('T')

class Peekable(Generic[T]):
    __slots__ = "just", "next", "iterator"

    def __init__(self, iterator: Iterator[T]):
        self.iterator = iterator
        self.next: T | None = next(self.iterator, None)
        self.just: T | None = None

    def __iter__(self):
        return self

    def __next__(self) -> T:
        if self.next is None:
            raise StopIteration
        self.just = self.next
        self.next = next(self.iterator, None)
        return self.just

    def __copy__(self) -> "Peekable[T]":
        result = self.__class__(self.iterator)
        result.just = self.just
        return result

    def peek(self):
        return self.next
    
    def current(self):
        return self.just
