from typing import Protocol

class Writer[T](Protocol):
    def __call__(self, data: object) -> T: ...
class Parent[T]:
    def push(self, data: T) -> T:
        return data
class Child[T](Parent[T]):
    def __init__(self, value: T) -> None:
        self.value = value
        self.push: Writer[T] = self._selected
    def _selected(self, data: object) -> T:
        return self.value

def consume(parent: Parent[str]) -> str:
    return parent.push(data="payload")
assert consume(Child[str]("payload")) == "payload"
