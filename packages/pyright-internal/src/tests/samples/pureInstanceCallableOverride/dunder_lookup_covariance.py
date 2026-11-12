# Callable instance override: dunder lookup covariance.
# The override must retain reportIncompatibleMethodOverride.
from typing import Protocol

class StringCall(Protocol):
    def __call__(self) -> str: ...

class Parent:
    def __call__(self) -> object:
        return object()

class Child(Parent):
    def __init__(self) -> None:
        self.__call__: StringCall = self._selected
    def _selected(self) -> str:
        return "selected"

child = Child()
actual = child()
assert isinstance(actual, str), type(actual).__name__
