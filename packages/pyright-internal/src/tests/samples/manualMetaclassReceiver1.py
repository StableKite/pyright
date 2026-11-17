from collections.abc import Callable
from enum import Enum, EnumMeta
from functools import partial
from types import FunctionType
from typing import TypedDict

class Meta(type):
    def label[T](cls: type[T]) -> str:
        return super().__repr__()

    def forwarded[T](cls: type[T]) -> str:
        return cls.label()

    def explicit[T](cls: type[T]) -> str:
        return Meta.label(cls)

class Right(metaclass=Meta):
    pass

class Child(Right):
    pass

class KwRight(TypedDict):
    cls: type[Right]

def invoke(f: Callable[[type[Right]], str]) -> str:
    return f(Right)

def identity[**P, R](f: Callable[P, R]) -> Callable[P, R]:
    return f

assert isinstance(Meta.label, FunctionType)
bound: Callable[[], str] = Right.label
alias = Meta.label
typed: Callable[[type[Right]], str] = Meta.label
right_kw: KwRight = {'cls': Right}
for result in (
    Meta.label(Right), Meta.label(Child), Right.label(), bound(), alias(Right),
    typed(Right), invoke(Meta.label), Meta.label(cls=Right), Meta.label(*(Right,)),
    Meta.label(**right_kw), partial(Meta.label, Right)(), partial(Meta.label)(Right),
    partial(Meta.label, cls=Right)(), identity(Meta.label)(Right),
    Right.forwarded(), Right.explicit(),
):
    assert 'Right' in result or 'Child' in result

class FoldMeta(EnumMeta):
    def __getitem__[E](cls: type[E], name: str) -> E:
        return super().__getitem__(name.upper())

class Direct(Enum, metaclass=FoldMeta):
    RED = 1

direct: Direct = identity(FoldMeta.__getitem__)(Direct, 'red')
assert direct is Direct.RED
