from collections.abc import Callable
from functools import partial
from typing import TypedDict


class Meta(type):
    def label[T](cls: type[T]) -> str:
        return super().__repr__()


class Right(metaclass=Meta):
    pass


class Wrong:
    pass


class WrongKeyword(TypedDict):
    cls: type[Wrong]


alias = Meta.label
typed: Callable[[type[Right]], str] = Meta.label
bad_typed: Callable[[type[Wrong]], str] = Meta.label  # error
wrong_keyword: WrongKeyword = {"cls": Wrong}


def identity[**P, R](function: Callable[P, R]) -> Callable[P, R]:
    return function


def invoke(function: Callable[[type[Wrong]], str]) -> str:
    return function(Wrong)


def direct() -> str:
    return Meta.label(Wrong)  # error


def alias_call() -> str:
    return alias(Wrong)  # error


def typed_call() -> str:
    return typed(Wrong)  # error


def callback_call() -> str:
    return invoke(Meta.label)  # error


def keyword_call() -> str:
    return Meta.label(cls=Wrong)  # error


def star_call() -> str:
    return Meta.label(*(Wrong,))  # error


def mapping_call() -> str:
    return Meta.label(**wrong_keyword)  # error


def partial_bound() -> str:
    return partial(Meta.label, Wrong)()  # error


def partial_unbound() -> str:
    return partial(Meta.label)(Wrong)  # error


def partial_keyword() -> str:
    return partial(Meta.label, cls=Wrong)()  # error


def identity_call() -> str:
    return identity(Meta.label)(Wrong)  # error


def return_callable() -> Callable[[type[Wrong]], str]:
    return Meta.label  # error


def union_call(value: type[Right] | type[Wrong]) -> str:
    return Meta.label(value)  # error
