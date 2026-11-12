# Callable instance override: bad concrete self return.
# The override must retain reportIncompatibleMethodOverride.
from typing import Protocol, Self

class Cloner[T](Protocol):
    def __call__(self) -> T: ...
class Parent:
    def clone(self) -> Self:
        return self
class Child(Parent):
    clone: Cloner[Child]
    def __init__(self) -> None:
        self.clone = self._selected
    def _selected(self) -> Child:
        return Child()
class GrandChild(Child):
    pass
def consume_class(cls: type[Parent], parent: Parent) -> Parent:
    return cls.clone(parent)
child = GrandChild()
assert child.clone() is child
assert consume_class(GrandChild, child) is child
