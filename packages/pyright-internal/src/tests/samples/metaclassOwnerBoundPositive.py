# pyright: strict

from typing import assert_type

class NameMeta(type):
    def tag(cls) -> str:
        return cls.__name__

class M(NameMeta):
    def g1(cls: type[A]) -> A:
        return cls()

    def g2[T: A](cls: type[T]) -> T:
        return cls()

    def tag(cls: type[A]) -> str:
        return super().tag()

    def explicit_tag(cls: type[A]) -> str:
        return super(M, cls).tag()

    def explicit_generic_tag[T: A](cls: type[T]) -> str:
        return super(M, cls).tag()

class A(metaclass=M):
    pass

class ChildMeta(M):
    pass

class B(A, metaclass=ChildMeta):
    pass

assert_type(A.g1(), A)
assert_type(A.g2(), A)
assert_type(B.g2(), B)
assert_type(M.g2(B), B)
assert_type(A.tag(), str)
assert_type(B.tag(), str)
assert type(A.g1()) is A
assert type(B.g2()) is B
assert A.tag() == 'A'
assert B.tag() == 'B'
assert_type(A.explicit_tag(), str)
assert_type(B.explicit_generic_tag(), str)
assert A.explicit_tag() == 'A'
assert B.explicit_generic_tag() == 'B'
