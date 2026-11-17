from collections.abc import Callable
from dataclasses import dataclass
from typing import final


class ReadOnly:
    @property
    def call(self) -> Callable[[], int]:
        return lambda: 1

    def __init__(self) -> None:
        self.call: Callable[[], int] = lambda: 1  # readonly


class Slotted:
    __slots__ = ()

    def call(self) -> int:
        return 1

    def __init__(self) -> None:
        self.call: Callable[[], int] = self.call  # readonly


class FinalMethod:
    @final
    def call(self) -> int:
        return 1

    def __init__(self) -> None:
        self.call: Callable[[], int] = self.call  # readonly


@dataclass(frozen=True)
class Frozen:
    def call(self) -> int:
        return 1

    def __init__(self) -> None:
        self.call: Callable[[], int] = self.call  # readonly
