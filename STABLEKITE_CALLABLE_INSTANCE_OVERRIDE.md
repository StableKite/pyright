# Callable instance attributes overriding concrete methods

Engine version `1.1.414-stablekite.4` retains all preceding StableKite fixes.
This change addresses a Pyright limitation (test-policy classification B): a
callback Protocol instance attribute was rejected as an override before its
call signature was compared with the inherited method.

An annotation-only class declaration or an instance member assignment leaves
the inherited class descriptor intact. Its instance call signature is checked
against the actual bound base method using the existing `assignType` relation.
This preserves keyword names, parameter kinds, defaults, parameter
contravariance, result covariance, generics, and complete overload coverage.
`Self` is compared as the same rigid subclass type variable on both sides;
returning a concrete child class cannot satisfy a polymorphic `Self` result.
Class-scoped type variables are likewise rigid on both sides, so an open
`Child[T]` cannot narrow the inherited contract to `int`. Method-scoped
parameters likewise describe every supported call and remain rigid in the
base signature; a callback may rename its own generic parameters while
preserving that universal contract.

The new path requires genuine method declarations in the base and instance
variable declarations in the subclass. It retains existing errors for final
and abstract methods, special methods, class variables, class-body defaults,
slot descriptors, non-callable values, and mutable callable base variables.
Class-body callable values can replace the inherited descriptor, and Python
special-method lookup can bypass an instance value, so these require separate
reasoning and receive no exemption here.

The independent regression suite adds twelve valid and twenty-three invalid cases.
No existing sample, expected diagnostic, snapshot, rule setting, or test
assertion is changed. No `Any`, `Unknown`, cast, per-project exemption, or
diagnostic suppression is introduced. Typeshed is unchanged. The intended
precision change is the removal of false override diagnostics for compatible
instance callables; invalid call signatures keep their original diagnostic.

Primary specifications:

- https://typing.python.org/en/latest/spec/callables.html
- https://typing.python.org/en/latest/spec/protocol.html
- https://typing.python.org/en/latest/spec/class-compat.html

Implementation and initial tests were prepared with AI assistance. Full
original checks, CI, packaging, and clean consumer qualification are separate
release gates; the presence of this file is not a readiness declaration.
