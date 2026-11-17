from collections.abc import Callable


class Dispatch:
    def initial(self, other: int) -> int:
        return other

    def call(self, value: int) -> int:
        return value

    def __init__(self) -> None:
        self.call: Callable[[int], int] = self.initial


def reject(instance: Dispatch) -> None:
    instance.call("text")  # error
    Dispatch.call(instance, "text")  # error
    instance.call(value=1)  # error
    wrong_result: str = instance.call(1)  # error
    instance.call = Dispatch.initial  # error
    wrong_result = Dispatch.call(instance, 1)  # error


class BadContract:
    def call(self, value: int) -> int:  # error
        return value

    def initial(self, other: int) -> str:
        return str(other)

    def __init__(self) -> None:
        self.call: Callable[[int], str] = self.initial


class NarrowResult(Dispatch):
    def call(self, value: int) -> bool:  # error
        return True


class WideParameter(Dispatch):
    def call(self, value: object) -> int:  # error
        return 1


class Source[T]:
    def initial(self) -> T:
        raise NotImplementedError

    def call(self) -> T:
        raise NotImplementedError

    def __init__(self) -> None:
        self.call: Callable[[], T] = self.initial


def variance(strings: Source[str]) -> None:
    objects: Source[object] = strings  # error
