from typing import assert_type
from typing import TypeAlias, TypeVar
T = TypeVar("T")
Identity: TypeAlias = T
class Box:
    def __init__(self) -> None:
        self.value: Identity[int] = 1
box = Box()
assert_type(box.value, int)
assert box.value == 1
