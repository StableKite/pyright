# pyright: strict

from metaclassOwnerBoundPositive import A, B, ChildMeta, M, NameMeta

class Plain:
    pass

class OutsideDomain(metaclass=M):
    pass

class IncompatibleMeta(NameMeta):
    def tag(cls: type[A]) -> str:
        return super().tag()

wrong_return: str = B.g2()
M.g1(Plain)
OutsideDomain.g2()
M.tag(Plain)
super(M, Plain).tag()
super(ChildMeta, A).tag()
