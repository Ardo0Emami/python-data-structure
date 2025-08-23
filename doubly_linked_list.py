from typing import Generic, TypeVar, Optional

T = TypeVar("T")

class DoublyNode(Generic[T]):
    def __init__(self, value: T, prev: Optional["DoublyNode[T]"] = None,
                  next: Optional["DoublyNode[T]"] = None) -> None:
        self.value = value
        self.prev = prev
        self.next = next

    def __repr__(self) -> str:
        return f"DoublyNode({self.value!r})"


class DoublyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[DoublyNode[T]] = None
        self.tail: Optional[DoublyNode[T]] = None
        self._size = 0

    def __len__(self) -> int:
        return self._size
