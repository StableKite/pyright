# Callable instance override: incomplete overloaded callback.
# The override must retain reportIncompatibleMethodOverride.
from typing import Protocol, overload

class Writer(Protocol):
    def __call__(self, data: bytes) -> bytes: ...
class Parent:
    @overload
    def push(self, data: bytes) -> bytes: ...
    @overload
    def push(self, data: str) -> str: ...
    def push(self, data: bytes | str) -> bytes | str:
        return data
class Child(Parent):
    def __init__(self) -> None:
        self.push: Writer = self._selected
    def _selected(self, data: bytes) -> bytes:
        return data.decode().encode()
def consume(parent: Parent) -> tuple[bytes, str]:
    return parent.push(data=b"bytes"), parent.push(data="str")
def consume_class(cls: type[Parent], parent: Parent) -> tuple[bytes, str]:
    return cls.push(parent, data=b"bytes"), cls.push(parent, data="str")
child = Child()
assert consume(child) == (b"bytes", "str")
assert consume_class(Child, child) == (b"bytes", "str")
