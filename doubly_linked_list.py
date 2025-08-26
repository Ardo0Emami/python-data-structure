from typing import Generic, TypeVar, Optional

T = TypeVar("T")


class DoublyNode(Generic[T]):
    def __init__(self, value: T,
                 prev: Optional["DoublyNode[T]"] = None,
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

    def add_front(self, value: T) -> None:
        new_node = DoublyNode(value, None, self.head)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            self.head = new_node

        self._size += 1

    def add_back(self, value: T) -> None:
        new_node = DoublyNode(value, self.tail, None)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def __len__(self) -> int:
        return self._size
