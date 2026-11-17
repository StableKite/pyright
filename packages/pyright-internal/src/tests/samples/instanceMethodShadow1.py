"""Real function descriptor and instance shadowing, with precise annotations."""
from collections.abc import Callable


class ExplicitInstance:
    def _initial(self, value: int) -> int:
        return value

    def call(self, value: int) -> int:
        return self._initial(value)

    def __init__(self) -> None:
        self.call: Callable[[int], int] = self._initial


class DeclaredInstance:
    def _initial(self, value: int) -> int:
        return value

    def __init__(self) -> None:
        self.call: Callable[[int], int]
        self.call = self._initial

    def call(self, value: int) -> int:
        return self._initial(value)


def positive() -> None:
    first = ExplicitInstance()
    second = DeclaredInstance()
    assert first.call(1) == ExplicitInstance.call(first, 1) == 1
    assert second.call(1) == DeclaredInstance.call(second, 1) == 1


positive()
