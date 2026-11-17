from typing import assert_type


class Meta(type):
    def label[T](cls: type[T]) -> str:
        return super().__repr__()

    def mixed[T](cls: type[T], other: type[T], choose_first: bool) -> str:
        return Meta.label(identity(cls if choose_first else other))  # error

    def erased_return[T](cls: type[T]) -> str:
        # An ordinary type[T] return does not promise the input metaclass.
        return Meta.label(identity(cls))  # error


class OtherMeta(type):
    pass


class Right(metaclass=Meta):
    pass


class Wrong(metaclass=OtherMeta):
    pass


def identity[T](value: type[T]) -> type[T]:
    return value


def merge[T](first: type[T], second: type[T]) -> type[T]:
    return first if first is second else second


def unproved[T](cls: type[T]) -> str:
    return Meta.label(cls)  # error


assert_type(Meta.label(identity(Right)), str)
Meta.label(identity(Wrong))  # error
Meta.label(merge(Right, Wrong))  # error


class TagMeta(type):
    def tag(cls) -> str:
        return cls.__name__


class KeywordMeta(TagMeta):
    def bad[T](*, cls: type[T]) -> str:
        return super().tag()  # error


class Good(metaclass=KeywordMeta):
    pass


KeywordMeta.bad(cls=Good)
