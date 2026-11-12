from typing import Protocol
class Writer(Protocol):
    def __call__(self, data: int) -> int: ...
class Parent:
    def push[T](self, data: T) -> T:
        return data
class Child(Parent):
    push: Writer
    def __init__(self) -> None:
        self.push = self._selected
    def _selected(self, data: int) -> int:
        return data + 1
def consume(parent: Parent) -> str:
    return parent.push(data="payload")
assert consume(Child()) == "payload"
