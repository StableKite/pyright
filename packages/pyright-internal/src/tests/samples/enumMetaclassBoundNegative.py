# pyright: strict

from enum import Enum

from enumMetaclassBoundPositive import CaseInsensitiveEnumMeta, Color


class PlainColor(Enum):
    RED = 1


class OutsideDomain(Enum, metaclass=CaseInsensitiveEnumMeta):
    RED = 1


wrong_return: int = Color["red"]
Color[1]
CaseInsensitiveEnumMeta.__getitem__(PlainColor, "red")
OutsideDomain["red"]
CaseInsensitiveEnumMeta.__getitem__(int, "red")
