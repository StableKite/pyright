# Validate callable parameter kinds without changing diagnostic rules.
class Base:
    def configure(self, prefix: int, /, *, blocking: bool = False, timeout: float | None = None) -> tuple[bool, float | None]:
        return blocking, timeout

class Implementation(Base):
    def configure(self, other: int, /, timeout: float | None = None, blocking: bool = False) -> tuple[bool, float | None]:
        _ = other
        return blocking, timeout

instance: Base = Implementation()
assert instance.configure(7, blocking=True, timeout=0.25) == (True, 0.25)
