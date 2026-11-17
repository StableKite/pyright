from collections.abc import Callable
from typing import Any, Generic, Self, TypeVar


T_co = TypeVar("T_co", covariant=True)


class Covariant(Generic[T_co]):
    def initial(self) -> T_co:
        raise NotImplementedError

    def call(self) -> T_co:  # error
        raise NotImplementedError

    def __init__(self) -> None:
        self.call: Callable[[], T_co] = self.initial


class SelfResult:
    def call(self) -> Self:  # error
        return self

    def __init__(self) -> None:
        self.call: Callable[[], Self] = self.call


class UnknownContract:
    def call(self) -> int:  # error
        return 1

    def __init__(self) -> None:
        self.call: Callable[..., Any] = self.call


class Dispatch:
    def initial(self, value: int) -> int:
        return value

    def other(self, other: int) -> int:
        return other

    def call(self, value: int) -> int:
        return value

    def __init__(self) -> None:
        self.call: Callable[[int], int] = self.initial


def alias_names(instance: Dispatch) -> int:
    instance.call = instance.initial
    alias = instance
    alias.call = instance.other
    return instance.call(value=1)  # error


class Result:
    def initial(self) -> int:
        return 1

    def boolean(self) -> bool:
        return True

    def call(self) -> int:
        return 1

    def __init__(self) -> None:
        self.call: Callable[[], int] = self.initial


def alias_result(instance: Result) -> bool:
    instance.call = instance.boolean
    alias = instance
    alias.call = instance.initial
    return instance.call()  # error
