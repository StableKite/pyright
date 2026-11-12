# Callable instance override: self callback grandchild.
from typing import Protocol, Self, assert_type

class Cloner[T](Protocol):
    def __call__(self) -> T: ...
class Parent:
    def clone(self) -> Self:
        return self
class Child(Parent):
    def __init__(self) -> None:
        self.clone: Cloner[Self] = self._selected
    def _selected(self) -> Self:
        return self
class GrandChild(Child):
    pass
def consume_class(cls: type[Parent], parent: Parent) -> Parent:
    return cls.clone(parent)
child = GrandChild()
assert_type(child.clone(), GrandChild)
assert child.clone() is child
assert consume_class(GrandChild, child) is child
