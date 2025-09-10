from typing import TypeVar, Generic

T = TypeVar("T")


class StackEmptyError(IndexError):
    """Raised when pop/peek is attempted on an empty stack"""


class Stack(Generic[T]):
    """simple LIFO stack with push, pop, peek, size, is_empty."""

    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if self.is_empty():
            raise StackEmptyError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> T:
        if self.is_empty():
            raise StackEmptyError("Peek from empty stack")
        return self._items[-1]

    # ----helpers----
    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"Stack({self._items!r})"

    def __iter__(self):
        return reversed(self._items)

    def __len__(self) -> int:
        return self.size()
