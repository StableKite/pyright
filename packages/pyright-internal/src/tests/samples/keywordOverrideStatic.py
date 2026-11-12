# Validate callable parameter kinds without changing diagnostic rules.
class Base:
    @staticmethod
    def configure(*, blocking: bool = False, timeout: float | None = None) -> tuple[bool, float | None]:
        return blocking, timeout

class Implementation(Base):
    @staticmethod
    def configure(timeout: float | None = None, blocking: bool = False) -> tuple[bool, float | None]:
        return blocking, timeout

assert Implementation.configure(blocking=True, timeout=0.25) == (True, 0.25)
