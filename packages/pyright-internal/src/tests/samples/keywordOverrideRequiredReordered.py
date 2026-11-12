# Validate callable parameter kinds without changing diagnostic rules.
class Base:
    def configure(self, *, blocking: bool, timeout: float | None) -> tuple[bool, float | None]:
        return blocking, timeout

class Implementation(Base):
    def configure(self, timeout: float | None, blocking: bool) -> tuple[bool, float | None]:
        return blocking, timeout

instance: Base = Implementation()
assert instance.configure(blocking=True, timeout=0.25) == (True, 0.25)
