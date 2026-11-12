# Callable instance override: bad protocol return.
# The override must retain reportIncompatibleMethodOverride.
from typing import Protocol

class Writer(Protocol):
    def __call__(self, data: bytes) -> int: ...

class Parent:
    def __init__(self) -> None:
        self.items: list[bytes] = []
    def push(self, data: bytes) -> None:
        self.items.append(data)

class Child(Parent):
    def __init__(self) -> None:
        super().__init__()
        self.push: Writer = self._selected
    def _selected(self, data: bytes) -> int:
        self.items.append(data)
        return len(data)

def consume(parent: Parent) -> None:
    parent.push(data=b"instance")

def consume_class(cls: type[Parent], parent: Parent) -> None:
    cls.push(parent, data=b"descriptor")

child = Child()
consume(child)
consume_class(Child, child)
assert child.items == [b"instance", b"descriptor"]
