class Box:
    def configure[U](self, value: U) -> U:
        type Local = U
        self.value: Local = value
        return value
