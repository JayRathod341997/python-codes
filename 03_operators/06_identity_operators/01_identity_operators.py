# ============================================================
# Identity Operators: is, is not
# ============================================================
# Identity operators check whether two variables refer to the
# SAME OBJECT in memory — NOT whether they have equal values.
#
#   is      → True if both variables point to the same object
#   is not  → True if they point to different objects
#
# KEY DISTINCTION:
#   ==  checks VALUE equality    (do they have the same value?)
#   is  checks IDENTITY equality (are they the exact same object?)
# ============================================================

# ============================================================
# id() — returns the memory address of an object
# ============================================================

a = [1, 2, 3]
b = a           # b is an ALIAS — same object
c = [1, 2, 3]   # c is a NEW list with same values

print(id(a))    # e.g. 2345678900
print(id(b))    # same as a
print(id(c))    # DIFFERENT — it's a new list object

print(a is b)           # True   (same object)
print(a is c)           # False  (different objects)
print(a == c)           # True   (same values)
print(a is not c)       # True

# ============================================================
# Why is vs == matters for mutable objects
# ============================================================

a = [1, 2, 3]
b = a

b.append(4)
print(a)        # [1, 2, 3, 4]  ← a was changed too!
# Because b is a is the SAME list.

# ============================================================
# None checks — always use 'is', never '=='
# ============================================================
# None is a singleton: there is only one None object in Python.
# The correct way to check for None is with 'is'.

value = None

print(value is None)        # True   (correct style)
print(value == None)        # True   (works but not idiomatic)
print(value is not None)    # False

# ============================================================
# Integer caching (CPython implementation detail)
# ============================================================
# CPython caches small integers in the range [-5, 256].
# Within that range, the same int object is reused.

x = 100
y = 100
print(x is y)       # True   (cached — same object)

x = 1000
y = 1000
print(x is y)       # False  (outside cache — new objects)
# Note: this behavior is CPython-specific and implementation-
# dependent. Never rely on it in production code.

# ============================================================
# String interning (another CPython detail)
# ============================================================

s1 = "hello"
s2 = "hello"
print(s1 is s2)     # True   (Python interns short strings)

s1 = "hello world"
s2 = "hello world"
print(s1 is s2)     # True or False (depends on CPython interning)
# Again, use == for string comparison in real code.

# ============================================================
# Practical rule of thumb
# ============================================================
# Use 'is' / 'is not' ONLY for:
#   1. Comparing to None
#   2. Comparing to True / False (rare)
#   3. Checking object identity intentionally (e.g., caching, singletons)
#
# Use '==' for all other value comparisons.

result = None

if result is None:
    print("No result yet")      # No result yet

flags = [True, False, True]
for flag in flags:
    if flag is True:            # fine, though `if flag:` is more Pythonic
        print("flag is set")
