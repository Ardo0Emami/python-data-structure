import unittest
from doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    def test_add_front_and_len(self) -> None:
        dll = DoublyLinkedList[int]()
        dll.add_front(1)
        dll.add_front(2)
        dll.add_front(3)

        self.assertEqual(len(dll), 3)

        self.assertIsNotNone(dll.head)
        assert dll.head is not None  # static type narrowing for Pylance
        self.assertEqual(dll.head.value, 1)

        self.assertIsNotNone(dll.tail)
        assert dll.tail is not None
        self.assertEqual(dll.tail.value, 3)

    def test_add_back_and_len(self) -> None:
        dll = DoublyLinkedList[int]()
        dll.add_back(1)
        dll.add_back(2)
        dll.add_back(3)

        self.assertEqual(len(dll), 3)

        self.assertIsNotNone(dll.head)
        assert dll.head is not None
        self.assertEqual(dll.head.value, 3)

        self.assertIsNotNone(dll.tail)
        assert dll.tail is not None
        self.assertEqual(dll.tail.value, 1)


if __name__ == "__main":
    unittest.main()
