from typing import Protocol

class Writer[T](Protocol):
    def __call__(self, data: T) -> T: ...
class Parent[T]:
    def push(self, data: T) -> T:
        return data
class Child[T](Parent[T]):
    push: Writer[int]
    def __init__(self) -> None:
        self.push = self._selected
    def _selected(self, data: int) -> int:
        return data + 1

def consume(parent: Parent[str]) -> str:
    return parent.push(data="payload")
assert consume(Child[str]()) == "payload"
