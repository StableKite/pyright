# Callable instance override: bad self return.
# The override must retain reportIncompatibleMethodOverride.
from typing import Protocol, Self

class Parent:
    def clone(self) -> Self:
        return self
class Cloner(Protocol):
    def __call__(self) -> Parent: ...
class Child(Parent):
    clone: Cloner
    def __init__(self) -> None:
        self.clone = self._selected
    def _selected(self) -> Parent:
        return Parent()
child = Child()
assert isinstance(child.clone(), Child)
