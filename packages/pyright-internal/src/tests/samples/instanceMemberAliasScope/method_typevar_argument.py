type Identity[T] = T
class Box:
    def configure[U](self, value: U) -> U:
        self.value: Identity[U] = value
        return value
