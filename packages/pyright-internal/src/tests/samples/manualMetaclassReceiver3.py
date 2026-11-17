from typing import Protocol, assert_type


class Meta(type):
    def create[T](cls: type[T]) -> T:
        value = cls()
        assert_type(value, T)
        return value

    def label[T](cls: type[T]) -> str:
        return super().__repr__()

    def return_class[T](cls: type[T]) -> type[T]:
        return cls


class ChildMeta(Meta):
    pass


class Right(metaclass=Meta):
    pass


class Derived(metaclass=ChildMeta):
    pass


def bounded[T: Right](cls: type[T]) -> T:
    return Meta.create(cls)


assert_type(Meta.create(Right), Right)
assert_type(Meta.create(Derived), Derived)
assert_type(bounded(Right), Right)
assert_type(Meta.label(Derived), str)
assert_type(Meta.return_class(Right), type[Right])


class NamedCallback(Protocol):
    def __call__(self, value: int) -> int: ...


class Fields(type):
    def call(cls, value: int) -> int:
        return value

    def __init__(cls, name: str, bases: tuple[type, ...], namespace: dict[str, object]) -> None:
        cls.call: NamedCallback = cls.call


class Stored(metaclass=Fields):
    pass


assert_type(Stored.call(value=1), int)
assert_type(Fields.call(Stored, value=1), int)
