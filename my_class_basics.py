"""
person module
-------------
provides the `Person` class with age validation and a birthday helper
"""


class Person:
    """Represents a person with a name and validated age."""
    def __init__(self, name: str, age: int):
        self.name = name
        self._age = age

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if value < 0:
            raise ValueError("age can't be negative")
        self._age = value

    def birthday(self) -> None:
        """Increment age by one year."""
        self.age += 1

    def say_hello(self) -> str:
        return f"hello my name is {self.name} and i'm {self.age} years old"

    # A __repr__ should ideally produce a string that,
    # if pasted into Python, could recreate the object
    # (or at least looks like valid code). Using !r helps.
    def __repr__(self) -> str:
        return f"Person(name={self.name!r}, age={self.age})"


if __name__ == "__main__":
    # p = Person("Ardo0", 39)
    # print(p.say_hello())
    # p.birthday()
    # print(p.say_hello())

    # try:
    #     p.age = -5
    # except ValueError as e:
    #     print("validation works:", e)

    print(repr(Person("Test", 20)))
