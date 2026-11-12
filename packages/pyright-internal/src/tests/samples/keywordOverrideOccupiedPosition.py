# Validate callable parameter kinds without changing diagnostic rules.
class Base:
    def configure(self, prefix: bool, /, *, blocking: bool) -> bool:
        return prefix and blocking

class Implementation(Base):
    def configure(self, blocking: bool, extra: bool = False) -> bool:  # EXPECT_ERROR
        _ = extra
        return blocking
