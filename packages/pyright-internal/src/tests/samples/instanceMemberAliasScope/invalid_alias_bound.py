type Identity[T: int] = T
class Box:
    def __init__(self) -> None:
        self.value: Identity[str] = "bad"
box = Box()
assert box.value == 1
