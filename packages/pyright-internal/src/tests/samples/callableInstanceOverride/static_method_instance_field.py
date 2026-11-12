# Callable instance override: static method instance field.
from typing import Protocol

class Writer(Protocol):
    def __call__(self, data: bytes) -> bytes: ...

class Parent:
    @staticmethod
    def push(data: bytes) -> bytes:
        return data

class Child(Parent):
    push: Writer
    def __init__(self) -> None:
        self.push = self._selected
    def _selected(self, data: bytes) -> bytes:
        return data

def consume(parent: Parent) -> bytes:
    return parent.push(data=b"instance")
def consume_class(cls: type[Parent]) -> bytes:
    return cls.push(data=b"descriptor")
assert consume(Child()) == b"instance"
assert consume_class(Child) == b"descriptor"
