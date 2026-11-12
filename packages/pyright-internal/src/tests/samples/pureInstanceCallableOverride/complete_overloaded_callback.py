# Callable instance override: complete overloaded callback.
from typing import Protocol, overload

class Writer(Protocol):
    @overload
    def __call__(self, data: bytes) -> bytes: ...
    @overload
    def __call__(self, data: str) -> str: ...
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
    @overload
    def _selected(self, data: bytes) -> bytes: ...
    @overload
    def _selected(self, data: str) -> str: ...
    def _selected(self, data: bytes | str) -> bytes | str:
        return data
def consume(parent: Parent) -> tuple[bytes, str]:
    return parent.push(data=b"bytes"), parent.push(data="str")
def consume_class(cls: type[Parent], parent: Parent) -> tuple[bytes, str]:
    return cls.push(parent, data=b"bytes"), cls.push(parent, data="str")
child = Child()
assert consume(child) == (b"bytes", "str")
assert consume_class(Child, child) == (b"bytes", "str")
