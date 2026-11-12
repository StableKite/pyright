# Validate callable parameter kinds without changing diagnostic rules.
from typing import Protocol

class API(Protocol):
    def __call__(self, *, blocking: bool = False, timeout: float | None = None) -> tuple[bool, float | None]:
        return blocking, timeout

def implementation(timeout: float | None = None) -> tuple[bool, float | None]:
    return False, timeout

callback: API = implementation  # EXPECT_ERROR
