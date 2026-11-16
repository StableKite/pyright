# This sample tests member access "set" operations when the target
# member is an object that doesn't provide a __set__ method.

# pyright: strict

from typing import Any, Generic, TypeVar, overload


_T = TypeVar("_T")


class ParentA:
    pass


class Column(Generic[_T]):
    def __init__(self, type: type[_T]) -> None: ...

    @overload
    def __get__(self: "Column[_T]", instance: None, type: Any) -> "Column[_T]": ...

    @overload
    def __get__(self: "Column[_T]", instance: ParentA, type: Any) -> _T: ...

    def __get__(
        self, instance: ParentA | None, type: Any
    ) -> _T | None | "Column[_T]": ...


class ChildA(ParentA):
    attr1: Column[str] = Column(str)
    attr2 = Column(str)


ChildA.attr1
ChildA().attr1
ChildA.attr2
ChildA().attr2

foo = ChildA()

# An instance write shadows this non-data descriptor with a value that
# preserves its specialized instance-read type, str.
foo.attr1 = ""

# The inferred descriptor type follows the same instance-write rule.
foo.attr2 = ""
