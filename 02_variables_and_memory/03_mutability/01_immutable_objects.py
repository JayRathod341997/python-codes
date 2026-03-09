# ============================================================
# Immutable Objects
# ============================================================
# An immutable object CANNOT be changed after it is created.
# Any "modification" creates a NEW object in memory.
#
# Immutable types: int, float, complex, bool, str, tuple,
#                  frozenset, bytes, NoneType
# ============================================================

# --- Integers are immutable ---
x = 10
print(id(x))            # memory address of the object 10

x = x + 1              # creates a NEW int object (11)
print(id(x))            # different address!

# --- Strings are immutable ---
s = "hello"
print(id(s))

# s[0] = "H"           # TypeError: 'str' object does not support item assignment

s = s.upper()           # creates a NEW string object
print(s)
print(id(s))            # different address

# --- String methods always return new strings ---
original = "  python  "
stripped = original.strip()
upper = stripped.upper()
print(repr(original))   # still "  python  " — unchanged
print(repr(stripped))   # "python"
print(repr(upper))      # "PYTHON"

# --- Tuples are immutable ---
point = (3, 4)
# point[0] = 10         # TypeError: 'tuple' object does not support item assignment

# To "change" a tuple, create a new one:
point = (10, point[1])
print(point)

# --- Immutable objects are hashable → can be dict keys or set elements ---
coords = {(0, 0): "origin", (1, 1): "point A"}
print(coords[(0, 0)])

valid_set = {1, 2, "hello", (3, 4)}    # all immutable ✓
print(valid_set)

# --- Why immutability matters ---
# 1. Thread-safe: multiple threads can read the same object safely.
# 2. Hashable: can use as dictionary keys.
# 3. Predictable: no surprise side effects.
