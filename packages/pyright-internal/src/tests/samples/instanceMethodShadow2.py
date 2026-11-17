from collections.abc import Callable
from typing import Protocol, assert_type


class Dispatch:
    def initial(self, other: int) -> int:
        return other

    def call(self, value: int) -> int:
        return value

    def __call__(self, value: int) -> int:
        return value

    def __init__(self) -> None:
        self.call: Callable[[int], int] = self.initial
        self.__call__: Callable[[int], int] = self.initial


class Child(Dispatch):
    def invoke(self) -> int:
        return super().call(value=1)

    def proxy(self) -> int:
        parent = super()
        return parent.call(value=1)


class Positional(Protocol):
    def call(self, value: int, /) -> int: ...


class Callback(Protocol):
    def __call__(self, value: int) -> int: ...


class Named:
    def call(self, value: int) -> int:
        return value

    def __init__(self) -> None:
        self.call: Callback = self.call


def use(instance: Dispatch, named: Named) -> None:
    assert_type(instance.call(1), int)
    assert_type(Dispatch.call(instance, value=1), int)
    assert_type(instance(value=1), int)
    assert_type(Dispatch.__call__(instance, value=1), int)
    assert_type(named.call(value=1), int)
    positional: Positional = instance
    assert_type(positional.call(1), int)


class Inherited:
    def call(self, value: int) -> int:
        return value


class AnnotatedChild(Inherited):
    def __init__(self) -> None:
        self.call: Callable[[int], int] = self.call


def inherited(instance: AnnotatedChild) -> None:
    assert_type(instance.call(1), int)
    assert_type(AnnotatedChild.call(instance, value=1), int)
