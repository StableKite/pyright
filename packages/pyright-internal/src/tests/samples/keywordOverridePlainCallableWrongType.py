# Validate callable parameter kinds without changing diagnostic rules.
from typing import Callable

def implementation(blocking: str, timeout: float | None) -> tuple[bool, float | None]:
    return bool(blocking), timeout

callback: Callable[[bool, float | None], tuple[bool, float | None]] = implementation  # EXPECT_ERROR
