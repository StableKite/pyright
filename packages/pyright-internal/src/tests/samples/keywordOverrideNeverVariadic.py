# Validate callable parameter kinds without changing diagnostic rules.
from typing import Never

class Base:
    def configure(self, *args: Never, blocking: bool) -> bool:
        _ = args
        return blocking

class Implementation(Base):
    def configure(self, blocking: bool, *args: Never) -> bool:
        _ = args
        return blocking

instance: Base = Implementation()
assert instance.configure(blocking=True)
