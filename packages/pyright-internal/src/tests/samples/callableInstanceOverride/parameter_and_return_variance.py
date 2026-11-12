# Callable instance override: parameter and return variance.
from typing import Protocol

class Writer(Protocol):
    def __call__(self, data: object) -> str: ...
class Parent:
    def push(self, data: bytes) -> object:
        return data
class Child(Parent):
    push: Writer
    def __init__(self) -> None:
        self.push = self._selected
    def _selected(self, data: object) -> str:
        return str(data)
def consume(parent: Parent) -> object:
    return parent.push(data=b"instance")
def consume_class(cls: type[Parent], parent: Parent) -> object:
    return cls.push(parent, data=b"descriptor")
child = Child()
assert isinstance(consume(child), str)
assert consume_class(Child, child) == b"descriptor"
