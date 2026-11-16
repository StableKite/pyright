# These errors must stay errors when instance writes use __get__ result types.

from dataclasses import dataclass
from typing import ClassVar, Final

from nonDataDescriptorAssignment1 import Subject, Value


def wrong_result(amount: int) -> str:
    return str(amount)


def wrong_argument(amount: str) -> int:
    return len(amount)


def invalid_methods(subject: Subject) -> None:
    subject.value = Subject.changed  # error: unbound method
    subject.value = wrong_result  # error: result type
    subject.value = wrong_argument  # error: parameter type
    subject.value = lambda amount: str(amount)  # error: contextual result
    subject.value("wrong")  # error: instance call
    Subject.value(subject, "wrong")  # error: class call
    Subject.value = 1  # error: class write uses descriptor type


class Data:
    def __get__(self, instance: object, owner: type[object] | None = None) -> int:
        return 0

    def __set__(self, instance: object, value: str) -> None:
        pass


class DeleteOnly:
    def __get__(self, instance: object, owner: type[object] | None = None) -> int:
        return 0

    def __delete__(self, instance: object) -> None:
        pass


class Guarded:
    data: Data = Data()
    delete_only: DeleteOnly = DeleteOnly()
    class_value: ClassVar[Value[int]] = Value[int]()
    final_value: Final[Value[int]] = Value[int]()

    def invalid(self) -> None:
        self.data = "accepted by the real setter"
        self.data = 1  # error: actual setter requires str
        self.delete_only = 1  # error: data descriptor, no setter
        self.class_value = 1  # error: ClassVar
        self.final_value = 1  # error: Final


@dataclass(frozen=True)
class Frozen:
    value = Value[int]()


def invalid_frozen(value: Frozen) -> None:
    value.value = 1  # error: frozen dataclass


class Slotted:
    __slots__ = ("spare",)
    value: Value[int] = Value()

    def invalid(self) -> None:
        self.value = 1  # error: slots cannot store a shadow


def invalid_slots(value: Slotted) -> None:
    value.value = 1  # error: external writes also cannot shadow


class WithDictionary:
    __slots__ = ("__dict__",)
    value: Value[int] = Value()

    def valid(self) -> None:
        self.value = 1


class BaseSlot:
    __slots__ = ("value",)


class HiddenSlot(BaseSlot):
    __slots__ = ()
    value: Value[int] = Value()

    def invalid(self) -> None:
        self.value = 1  # error: a non-data descriptor hides the inherited slot


class InstanceMember:
    def __init__(self) -> None:
        self.value: Value[int] = Value()

    def invalid(self) -> None:
        self.value = 1  # error: stored instance value is not a descriptor


class ReadOnlyProperty:
    @property
    def value(self) -> int:
        return 0

    def invalid(self) -> None:
        self.value = 1  # error: properties remain data descriptors
