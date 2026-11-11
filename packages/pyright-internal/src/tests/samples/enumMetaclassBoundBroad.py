# pyright: strict

from enum import Enum, EnumMeta
from typing import TypeVar

Member = TypeVar("Member", bound=Enum)


class CaseInsensitiveEnumMeta(EnumMeta):
    # Enum alone does not guarantee that cls is an instance of this metaclass.
    def __getitem__(cls: type[Member], key: str) -> Member:
        return super().__getitem__(key.upper())
