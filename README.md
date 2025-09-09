# Python Data Structures

This project contains clean, tested implementations of core data structures in Python:

## Stack
- Generic, type-safe LIFO stack
- Methods: `push`, `pop`, `peek`, `is_empty`, `size`
- Works with `for` loops and `len()`
- Raises `StackEmptyError` on invalid pop/peek
- Fully tested with `unittest`
- Type-checked with `mypy`
- Style-checked with `flake8`

### Example
```python
from stack import Stack

s = Stack[int]()
s.push(1)
s.push(2)
print(s.pop())  # 2
print(s.pop())  # 1
```

---

## BaseSortedList
- Keeps items sorted as added
- Supports any type with custom comparison
- Optional reverse sorting
- Fully tested, type-checked, style-checked

### Example
```python
from sorted_list import BaseSortedList

def compare(x, y):
    return x - y

lst = BaseSortedList(compare)
lst.add(3)
lst.add(1)
lst.add(2)
print(list(lst))  # [1, 2, 3]
---

```

---

## Queue
- Generic, type-safe FIFO queue
- Methods: `enqueue`, `dequeue`, `peek`, `is_empty`
- Supports: `len()`, `repr()`
- Raises `IndexError` on invalid `dequeue` or `peek`
- Fully tested with `unittest`
- Type-checked with `mypy`
- Style-checked with `flake8`

### Example
```python
from queue import Queue

q = Queue[int]()
q.enqueue(10)
q.enqueue(20)

print(q.peek())     # 10
print(q.dequeue())  # 10
print(q.dequeue())  # 20
print(q.is_empty()) # True


```

---

## DoublyLinkedList
- Generic, type-safe doubly linked list
- Methods: `add_front`, `add_back`, `find`, `remove`
- Supports: `len()`, `in`, `iter()`, `repr()`
- Fully tested with `unittest`
- Type-checked with `mypy`
- Style-checked with `flake8`

### Example
```python
from doubly_linked_list import DoublyLinkedList

dll = DoublyLinkedList[int]()
dll.add_back(1)
dll.add_back(2)
dll.add_back(3)

print(list(dll))      # [1, 2, 3]
print(dll.find(2))    # DoublyNode(2)
dll.remove(2)
print(2 in dll)       # False

```

