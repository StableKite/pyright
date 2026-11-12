from typing import assert_type
type Identity[T] = T
class Box[U]:
    def __init__(self, value: U) -> None:
        self.value: Identity[U] = value
box = Box[int](1)
assert_type(box.value, int)
assert box.value == 1
