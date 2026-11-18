# pyright: strict

from typing import Literal, overload


class Base:
    @overload
    def pick(self, value: int, *, label: str) -> int: ...
    @overload
    def pick(self, value: str, *, label: str) -> str: ...
    def pick(self, value: int | str, *, label: str) -> int | str:
        return value


class MissingFirst(Base):
    @overload
    def pick(self, value: str, *, label: str) -> str: ...
    @overload
    def pick(self, value: bytes, *, label: str) -> bytes: ...
    def pick(self, value: str | bytes, *, label: str) -> str | bytes:
        return value


class ReversedOrder(Base):
    @overload
    def pick(self, value: str, *, label: str) -> str: ...
    @overload
    def pick(self, value: int, *, label: str) -> int: ...
    def pick(self, value: int | str, *, label: str) -> int | str:
        return value


class IncompatibleReturn(Base):
    @overload
    def pick(self, value: Literal[1], *, label: str) -> str: ...
    @overload
    def pick(self, value: int, *, label: str) -> int: ...
    @overload
    def pick(self, value: str, *, label: str) -> str: ...
    def pick(self, value: int | str, *, label: str) -> int | str:
        return label if value == 1 else value


class WrongKeyword(Base):
    @overload
    def pick(self, value: int, *, renamed: str) -> int: ...
    @overload
    def pick(self, value: str, *, renamed: str) -> str: ...
    def pick(self, value: int | str, *, renamed: str) -> int | str:
        return value


class Generic:
    @overload
    def lookup(self, *, mode: Literal["text"], value: int) -> str: ...
    @overload
    def lookup[T](self, *, mode: Literal["value"], value: T) -> T: ...
    def lookup[T](self, *, mode: str, value: T) -> T | str:
        return str(value) if mode == "text" else value


class WrongGenericReturn(Generic):
    @overload
    def lookup(self, *, mode: Literal["value"], value: Literal[1]) -> str: ...
    @overload
    def lookup(self, *, mode: Literal["text"], value: int) -> str: ...
    @overload
    def lookup[T](self, *, mode: Literal["value"], value: T) -> T: ...
    def lookup[T](self, *, mode: str, value: T) -> T | str:
        return str(value) if mode == "text" or value == 1 else value
