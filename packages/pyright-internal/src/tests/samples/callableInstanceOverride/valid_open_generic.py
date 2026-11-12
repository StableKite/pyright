from typing import Protocol

class Writer[T](Protocol):
    def __call__(self, data: T) -> T: ...
class Parent[T]:
    def push(self, data: T) -> T:
        return data
class Child[T](Parent[T]):
    push: Writer[T]
    def __init__(self) -> None:
        self.push = self._selected
    def _selected(self, data: T) -> T:
        return data

def consume(parent: Parent[str]) -> str:
    return parent.push(data="payload")
assert consume(Child[str]()) == "payload"
