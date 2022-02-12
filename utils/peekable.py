from typing import Generic, TypeVar, Iterable

T = TypeVar('T')

class Peekable(Generic[T]):
    def __init__(self, iterator: Iterable[T]):
        self.next: T | None = next(iterator, None)
        self.iterator = iterator

    def __iter__(self):
        return self

    def __next__(self) -> T:
        if self.next is None:
            raise StopIteration
        res = self.next
        self.next = next(self.iterator, None)
        return res

    def peek(self):
        return self.next
