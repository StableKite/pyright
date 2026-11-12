from typing import assert_type
type Identity[T] = list[T]
class Box:
    def __init__(self) -> None:
        self.value: Identity[int] = [1]
box = Box()
assert_type(box.value, list[int])
assert box.value == [1]
