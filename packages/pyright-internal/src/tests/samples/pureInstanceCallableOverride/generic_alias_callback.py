# Callable instance override: generic alias callback.
from typing import Protocol

class Writer[T](Protocol):
    def __call__(self, data: T) -> T: ...
type State[T] = T
class Parent[T]:
    def push(self, data: T) -> T:
        return data
class Child(Parent[int]):
    def __init__(self) -> None:
        self.push: State[Writer[int]] = self._selected
    def _selected(self, data: int) -> int:
        return data + 1
def consume(parent: Parent[int]) -> int:
    return parent.push(data=2)
def consume_class(cls: type[Parent[int]], parent: Parent[int]) -> int:
    return cls.push(parent, data=2)
child = Child()
assert consume(child) == 3
assert consume_class(Child, child) == 2
