# Callable instance override: classvar callable object.
# The override must retain reportIncompatibleMethodOverride.
from typing import Protocol, ClassVar

class Writer(Protocol):
    def __call__(self, data: bytes) -> None: ...

class Parent:
    def __init__(self) -> None:
        self.items: list[bytes] = []
    def push(self, data: bytes) -> None:
        self.items.append(data)

class WriterObject:
    def __call__(self, data: bytes) -> None:
        pass

class Child(Parent):
    push: ClassVar[Writer] = WriterObject()
    def __init__(self) -> None:
        super().__init__()
    def _selected(self, data: bytes) -> None:
        self.items.append(data)

def consume(parent: Parent) -> None:
    parent.push(data=b"instance")

def consume_class(cls: type[Parent], parent: Parent) -> None:
    cls.push(parent, data=b"descriptor")

child = Child()
consume(child)
consume_class(Child, child)
assert child.items == [b"instance", b"descriptor"]
