# Validate callable parameter kinds without changing diagnostic rules.
class Base:
    def configure(self, *, blocking: bool = False, timeout: float | None = None) -> tuple[bool, float | None]:
        return blocking, timeout

class Implementation(Base):
    def configure(self, selector: str | None = None) -> tuple[bool, float | None]:  # EXPECT_ERROR
        _ = selector
        return False, None
