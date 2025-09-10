from typing import Iterator, Optional, TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T, next: Optional["Node[T]"]) -> None:
        self.value = value
        self.next = next


class LinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[Node[T]] = None
        self._size: int = 0

    def add_front(self, value: T) -> None:
        new_node = Node(value, self.head)  # new_node.next = old head
        self.head = new_node                # head now points to new node
        self._size += 1

    def add_back(self, value: T) -> None:
        new_node = Node(value, None)
        # self.head is None
        if not self.head:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node
        self._size += 1

    def find(self, value: T) -> Node[T]:
        """
        Find the first node containing `value`.

        Raises:
            ValueError: If the value is not found in the list.
        """
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return current_node
            current_node = current_node.next

        raise ValueError(f"{value} not found in list")

    def remove(self, value: T) -> None:
        current_node = self.head
        previous_node = None

        while current_node:
            if current_node.value == value:
                if previous_node is None:  # removing head
                    self.head = current_node.next
                else:
                    previous_node.next = current_node.next
                self._size -= 1
                return  # stop after first match
            previous_node = current_node
            current_node = current_node.next

        raise ValueError(f"{value} not found in list")

    def __iter__(self) -> Iterator[T]:
        current_node = self.head

        while current_node:
            yield current_node.value
            current_node = current_node.next

    def __len__(self) -> int:
        return self._size

    def __contains__(self, value: T) -> bool:
        try:
            self.find(value)
            return True
        except ValueError:
            return False

    def clear(self):
        self.head = None
        self._size = 0

    def __repr__(self) -> str:
        return f"LinkedList({list(self)!r})"
