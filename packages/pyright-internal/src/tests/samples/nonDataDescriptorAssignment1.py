# Non-data descriptors are shadowed by instance writes. Replacements retain
# the specialized instance-read type, including contextual lambda inference.

from collections.abc import Callable
from types import FunctionType
from typing import Concatenate, Protocol, assert_type, overload


class Method[Owner, **P, Result](Protocol):
    def __call__(self, instance: Owner, /, *args: P.args, **kwargs: P.kwargs) -> Result: ...

    @overload
    def __get__(self, instance: None, owner: type[Owner], /) -> Callable[Concatenate[Owner, P], Result]: ...

    @overload
    def __get__(self, instance: Owner, owner: type[Owner] | None = None, /) -> Callable[P, Result]: ...


def rebindable[Owner, **P, Result](
    function: Callable[Concatenate[Owner, P], Result],
) -> Method[Owner, P, Result]:
    if not isinstance(function, FunctionType):
        raise TypeError("A real Python function is required")
    return function


class Subject:
    @rebindable
    def value(self, amount: int) -> int:
        return amount + 1

    def changed(self, amount: int) -> int:
        return amount + 2

    def switch(self) -> None:
        self.value = self.changed

    def contextual(self) -> None:
        self.value = lambda amount: assert_type(amount, int) + 3


class GenericSubject[T]:
    @rebindable
    def value(self, item: T) -> T:
        return item

    def changed(self, item: T) -> T:
        return item

    def switch(self) -> None:
        self.value = self.changed


class Child(GenericSubject[str]):
    def contextual(self) -> None:
        self.value = lambda item: assert_type(item, str).upper()


class Value[T]:
    @overload
    def __get__(self, instance: None, owner: type[object], /) -> "Value[T]": ...

    @overload
    def __get__(self, instance: object, owner: type[object] | None = None, /) -> T: ...

    def __get__(
        self, instance: object | None, owner: type[object] | None = None, /
    ) -> "Value[T] | T":
        raise NotImplementedError


class Values:
    items: Value[list[int]] = Value()

    def clear(self) -> None:
        self.items = []
        assert_type(self.items, list[int])


class InstanceMember:
    def __init__(self) -> None:
        self.value: Value[int] = Value()

    def replace(self) -> None:
        self.value = Value[int]()
        assert_type(self.value, Value[int])


def positive() -> None:
    subject = Subject()
    assert_type(subject.value(10), int)
    assert_type(Subject.value(subject, 10), int)
    assert subject.value(10) == 11
    subject.switch()
    assert subject.value(10) == 12
    assert Subject.value(subject, 10) == 11
    subject.contextual()
    assert subject.value(10) == 13
    assert isinstance(Subject.__dict__["value"], FunctionType)

    generic = Child()
    generic.switch()
    assert_type(generic.value("hello"), str)
    assert_type(Child.value(generic, "hello"), str)
    generic.contextual()
    assert generic.value("hello") == "HELLO"

    # Class writes replace the descriptor rather than shadowing it.
    Subject.value = Subject.changed
    assert subject.value(10) == 13
    assert Subject.value(subject, 10) == 12


if __name__ == "__main__":
    positive()
