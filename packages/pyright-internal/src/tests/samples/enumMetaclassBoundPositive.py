# pyright: strict

from enum import Enum, EnumMeta
from typing import TypeVar, assert_type

Member = TypeVar("Member", bound="CaseInsensitiveEnum")


class CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(cls: type[Member], key: str) -> Member:
        return super().__getitem__(key.upper())


class CaseInsensitiveEnum(Enum, metaclass=CaseInsensitiveEnumMeta):
    pass


class Color(CaseInsensitiveEnum):
    RED = 1


class ChildMeta(CaseInsensitiveEnumMeta):
    pass


class OtherBase(CaseInsensitiveEnum, metaclass=ChildMeta):
    pass


class Shade(OtherBase):
    BLUE = 2


def lookup(cls: type[Member], key: str) -> Member:
    return cls[key]


assert_type(Color["red"], Color)
assert_type(Shade["blue"], Shade)
assert_type(CaseInsensitiveEnumMeta.__getitem__(Color, "red"), Color)
assert_type(lookup(Color, "red"), Color)
assert_type(lookup(Shade, "blue"), Shade)
