# Class-object bounds in metaclass methods

Version 1.1.414-stablekite.3 preserves the preceding StableKite ctypes, HID,
pickle, and precise-sentinel changes and adds nominal metaclass owner checks.

An explicitly annotated class-object self bound is accepted in a metaclass
instance method only when that bound has a known metaclass whose MRO contains
the method owner. A broader bound with a different metaclass is not accepted.
This does not make an arbitrary metaclass instance assignable to the bound.

Zero-argument and explicit super(M, cls) select the metaclass MRO when cls is
an instance of M rather than an ordinary subclass of M. Member binding retains
the actual class object. The ordinary MRO retains precedence if it contains M.
An existing custom metaclass index method that fails binding reports an index
error instead of falling through to generic or enum indexing.

The real EnumMeta implementation can keep
return super().**getitem**(key.upper()) with Member bounded to its actual
CaseInsensitiveEnum base. The return remains the concrete enum subclass.
Member bounded only to Enum does not guarantee the custom metaclass and
remains rejected. No producer body change, Any, cast, ignore, or rule change
is used.

An independent test file adds precise positive and negative examples with
real EnumMeta and ordinary metaclasses, inherited metaclasses, explicit and
implicit super, incompatible owners, wrong keys and returns, and enum classes
outside the declared bound. Existing test files and assertions are unchanged.
