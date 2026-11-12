# Callable instance override: bad return variance.
# The override must retain reportIncompatibleMethodOverride.
from typing import Protocol

class Writer(Protocol):
    def __call__(self, data: object) -> object: ...
class Parent:
    def push(self, data: bytes) -> bytes:
        return data
class Child(Parent):
    push: Writer
    def __init__(self) -> None:
        self.push = self._selected
    def _selected(self, data: object) -> object:
        return object()
def consume(parent: Parent) -> bytes:
    return parent.push(data=b"instance")
def consume_class(cls: type[Parent], parent: Parent) -> object:
    return cls.push(parent, data=b"descriptor")
child = Child()
assert isinstance(consume(child), bytes)
assert consume_class(Child, child) == b"descriptor"
