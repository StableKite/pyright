# Validate callable parameter kinds without changing diagnostic rules.
class Base:
    @classmethod
    def configure(cls, *, blocking: bool = False, timeout: float | None = None) -> tuple[bool, float | None]:
        return blocking, timeout

class Implementation(Base):
    @classmethod
    def configure(cls, timeout: float | None = None, blocking: bool = False) -> tuple[bool, float | None]:
        return blocking, timeout

assert Implementation.configure(blocking=True, timeout=0.25) == (True, 0.25)
