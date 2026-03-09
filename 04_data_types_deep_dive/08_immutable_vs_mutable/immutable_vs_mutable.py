# ─────────────────────────────────────────────
# Immutable vs Mutable Types
# ─────────────────────────────────────────────

# ── Immutable types ───────────────────────────
# int, float, complex, bool, str, tuple, frozenset, bytes
# Cannot be changed after creation

# Strings are immutable
s = "hello"
# s[0] = "H"      # TypeError!
s = s.upper()     # creates a NEW string, rebinds the variable
print(s)

# Tuples are immutable
t = (1, 2, 3)
# t[0] = 99       # TypeError!
t2 = t + (4,)     # creates a NEW tuple
print(t2)

# ── Mutable types ─────────────────────────────
# list, dict, set, bytearray, custom objects
# Can be changed in place

lst = [1, 2, 3]
lst[0] = 99       # works fine — list is mutable
lst.append(4)
print(lst)        # [99, 2, 3, 4]

# ── id() — memory address ─────────────────────
# Immutable: rebinding creates new object (new id)
x = 10
print(id(x))
x += 1            # x now points to a NEW int object
print(id(x))      # different id

# Mutable: modification keeps same object (same id)
lst = [1, 2, 3]
print(id(lst))
lst.append(4)
print(id(lst))    # same id — modified in place

# ── Assignment vs copy ────────────────────────
# This is where mutable types bite beginners!

a = [1, 2, 3]
b = a               # b points to SAME list
b.append(4)
print(a)            # [1, 2, 3, 4]  ← a also changed!

# Fix 1: shallow copy
a = [1, 2, 3]
b = a.copy()        # or list(a) or a[:]
b.append(4)
print(a)            # [1, 2, 3]  ← unchanged

# Fix 2: deep copy (for nested structures)
import copy
nested = [[1, 2], [3, 4]]
shallow = nested.copy()
deep    = copy.deepcopy(nested)

shallow[0].append(99)
print(nested)       # [[1, 2, 99], [3, 4]]  ← shallow copy affected!

deep[0].append(99)
print(nested)       # [[1, 2, 99], [3, 4]]  ← deep copy did NOT affect original

# ── Mutable default argument trap ─────────────
# WRONG — default list is shared across all calls!
def bad_append(item, lst=[]):
    lst.append(item)
    return lst

print(bad_append(1))    # [1]
print(bad_append(2))    # [1, 2]  ← unexpected!

# CORRECT — use None as default
def good_append(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(good_append(1))   # [1]
print(good_append(2))   # [2]  ← fresh list each time

# ── Summary table ─────────────────────────────
print("\n=== Immutable vs Mutable ===")
types = [
    ("int",       "immutable", 42),
    ("float",     "immutable", 3.14),
    ("str",       "immutable", "hi"),
    ("tuple",     "immutable", (1,2)),
    ("frozenset", "immutable", frozenset({1,2})),
    ("list",      "mutable  ", [1,2]),
    ("dict",      "mutable  ", {"a":1}),
    ("set",       "mutable  ", {1,2}),
]
for name, kind, example in types:
    print(f"  {name:<10} {kind}   example: {example}")
