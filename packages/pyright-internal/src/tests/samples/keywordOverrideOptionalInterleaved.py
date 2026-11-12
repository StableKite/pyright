# Validate callable parameter kinds without changing diagnostic rules.
class Base:
    def configure(self, *, blocking: bool = False, timeout: float | None = None) -> tuple[bool, float | None]:
        return blocking, timeout

class Implementation(Base):
    def configure(self, selector: str | None = None, blocking: bool = False, get_all: bool = False, timeout: float | None = None) -> tuple[bool, float | None]:
        _ = selector, get_all
        return blocking, timeout

instance: Base = Implementation()
assert instance.configure(blocking=True, timeout=0.25) == (True, 0.25)
