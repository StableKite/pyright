# pyright: strict
# Incompatible instance replacements and class writes remain errors.

from nonDataDescriptorAssignment1 import Value


class Row:
    declared: Value[str] = Value()
    inferred = Value[str]()


def invalid_instance(row: Row) -> None:
    row.declared = 1  # error: declared instance-read type is str
    row.inferred = 1  # error: inferred instance-read type is str


def invalid_class() -> None:
    Row.declared = "replacement"  # error: class write requires descriptor type
    Row.inferred = "replacement"  # error: class write requires descriptor type
