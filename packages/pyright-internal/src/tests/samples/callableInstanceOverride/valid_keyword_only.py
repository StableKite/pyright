# Callable instance override: valid keyword only.
from typing import Protocol

class Writer(Protocol):
    def __call__(self, *, data: bytes) -> None: ...

class Parent:
    def __init__(self) -> None:
        self.items: list[bytes] = []
    def push(self, *, data: bytes) -> None:
        self.items.append(data)

class Child(Parent):
    push: Writer
    def __init__(self) -> None:
        super().__init__()
        self.push = self._selected
    def _selected(self, *, data: bytes) -> None:
        self.items.append(data)

def consume(parent: Parent) -> None:
    parent.push(data=b"instance")

def consume_class(cls: type[Parent], parent: Parent) -> None:
    cls.push(parent, data=b"descriptor")

child = Child()
consume(child)
consume_class(Child, child)
assert child.items == [b"instance", b"descriptor"]
