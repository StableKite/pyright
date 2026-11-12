# Validate callable parameter kinds without changing diagnostic rules.
class Base:
    def configure(self, *args: bool, blocking: bool) -> bool:
        return all(args) and blocking

class Implementation(Base):
    def configure(self, blocking: bool = False, *args: bool) -> bool:  # EXPECT_ERROR
        return all(args) and blocking
