type Identity[T] = T
class Box:
    def __init__(self) -> None:
        self.value: Identity = 1
box = Box()
assert box.value == 1
