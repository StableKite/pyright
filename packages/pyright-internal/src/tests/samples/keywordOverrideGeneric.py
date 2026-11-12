# Validate callable parameter kinds without changing diagnostic rules.
class Base[T]:
    def configure(self, *, item: T) -> T:
        return item

class Implementation[T](Base[T]):
    def configure(self, item: T) -> T:
        return item

instance: Base[int] = Implementation[int]()
assert instance.configure(item=7) == 7
