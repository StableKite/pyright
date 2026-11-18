# pyright: strict

from __future__ import annotations

from typing import Literal, NamedTuple, assert_type, overload


class Direction(NamedTuple):
    x: float
    y: float

    @overload
    def __add__(self, value: Direction, /) -> Direction: ...
    @overload
    def __add__(self, value: tuple[float, ...], /) -> tuple[float, ...]: ...
    @overload
    def __add__[T](self, value: tuple[T, ...], /) -> tuple[float | T, ...]: ...
    def __add__[T](self, value: tuple[T, ...], /) -> tuple[float | T, ...]:
        return value if isinstance(value, Direction) else tuple(self) + value


class Generic:
    @overload
    def lookup(self, *, mode: Literal["text"], value: int) -> str: ...
    @overload
    def lookup[T](self, *, mode: Literal["value"], value: T) -> T: ...
    def lookup[T](self, *, mode: str, value: T) -> T | str:
        return str(value) if mode == "text" else value


class Specialized(Generic):
    @overload
    def lookup(self, *, mode: Literal["value"], value: Literal[1]) -> Literal[1]: ...
    @overload
    def lookup(self, *, mode: Literal["text"], value: int) -> str: ...
    @overload
    def lookup[T](self, *, mode: Literal["value"], value: T) -> T: ...
    def lookup[T](self, *, mode: str, value: T) -> T | str:
        return str(value) if mode == "text" else value


direction = Direction(1, 2)
assert_type(direction + direction, Direction)
assert_type(direction + ("text",), tuple[float | str, ...])
assert_type(Specialized().lookup(mode="value", value=1), Literal[1])
assert_type(Specialized().lookup(mode="text", value=2), str)
