type Identity[T] = T
class Box:
    def __init__(self) -> None:
        self.value: Identity[int] = "wrong"
box = Box()
assert box.value == 1
