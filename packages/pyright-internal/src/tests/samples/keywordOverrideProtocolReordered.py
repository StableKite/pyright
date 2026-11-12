# Validate callable parameter kinds without changing diagnostic rules.
from typing import Protocol

class API(Protocol):
    def __call__(self, *, blocking: bool = False, timeout: float | None = None) -> tuple[bool, float | None]:
        return blocking, timeout

def implementation(timeout: float | None = None, blocking: bool = False) -> tuple[bool, float | None]:
    return blocking, timeout

callback: API = implementation
assert callback(blocking=True, timeout=0.25) == (True, 0.25)
