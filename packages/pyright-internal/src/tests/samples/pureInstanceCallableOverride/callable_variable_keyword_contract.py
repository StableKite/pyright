# Callable instance override: callable variable keyword contract.
# The override must retain reportIncompatibleMethodOverride.
from collections.abc import Callable
from typing import Protocol

class Writer(Protocol):
    def __call__(self, data: bytes) -> None: ...
class Parent:
    def __init__(self) -> None:
        self.push: Callable[[bytes], None] = self._selected
    def _selected(self, data: bytes) -> None:
        pass
class Child(Parent):
    def __init__(self) -> None:
        super().__init__()
        self.push: Writer = self._selected
def replace(parent: Parent) -> None:
    def positional(data: bytes, /) -> None:
        pass
    parent.push = positional
child = Child()
replace(child)
child.push(data=b"keyword")
