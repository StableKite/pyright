# Validate callable parameter kinds without changing diagnostic rules.
class Base:
    def configure(self, *, blocking: bool) -> bool:
        return blocking

class Implementation(Base):
    def configure(self, blocking: bool = False, /, **kwargs: bool) -> bool:
        _ = blocking
        return kwargs['blocking']

instance: Base = Implementation()
assert instance.configure(blocking=True)
