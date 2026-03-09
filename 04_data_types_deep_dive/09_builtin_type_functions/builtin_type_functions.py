# ─────────────────────────────────────────────
# Built-in Type Functions
# Python's built-ins for inspecting and working with types
# ─────────────────────────────────────────────

# ── Type constructors (also convert types) ────
print(int(3.9))         # 3
print(float("1.5"))     # 1.5
print(str(100))         # '100'
print(bool(0))          # False
print(complex(2, 3))    # (2+3j)
print(list("abc"))      # ['a', 'b', 'c']
print(tuple([1,2,3]))   # (1, 2, 3)
print(set([1,1,2,3]))   # {1, 2, 3}
print(dict(a=1, b=2))   # {'a': 1, 'b': 2}
print(frozenset({1,2})) # frozenset({1, 2})
print(bytes(3))         # b'\x00\x00\x00'
print(bytearray(3))     # bytearray(b'\x00\x00\x00')

# ── type() ───────────────────────────────────
print(type(42))         # <class 'int'>
print(type(42).__name__)# 'int'

# ── isinstance() ─────────────────────────────
print(isinstance(42, int))              # True
print(isinstance(42, (int, float)))     # True

# ── id() — memory address ────────────────────
x = [1, 2, 3]
print(id(x))            # unique integer address

# ── hash() — for hashable (immutable) types ───
print(hash(42))         # deterministic integer
print(hash("hello"))    # deterministic (per session)
print(hash((1, 2, 3)))  # tuples are hashable
# hash([1,2,3])         # TypeError! lists are not hashable

# ── repr() vs str() ──────────────────────────
# str()  — human-readable output
# repr() — unambiguous, developer-friendly
print(str("hello"))     # hello
print(repr("hello"))    # 'hello'  ← includes quotes
print(str(None))        # None
print(repr(None))       # None
print(str([1,2,3]))     # [1, 2, 3]
print(repr([1,2,3]))    # [1, 2, 3]
print(repr("line\nnew"))# 'line\\nnew'  ← shows escape

# ── len() ────────────────────────────────────
print(len("hello"))     # 5
print(len([1,2,3,4]))   # 4
print(len({"a":1}))     # 1
print(len((1,2)))       # 2

# ── dir() — list attributes and methods ───────
print(dir(str))         # all string methods
print([m for m in dir(str) if not m.startswith("_")])  # public only

# ── vars() — object's __dict__ ───────────────
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

p = Person("Jay", 25)
print(vars(p))          # {'name': 'Jay', 'age': 25}

# ── getattr / setattr / hasattr / delattr ─────
print(getattr(p, "name"))           # 'Jay'
print(getattr(p, "email", "N/A"))   # 'N/A'  — default if missing
setattr(p, "email", "jay@mail.com")
print(hasattr(p, "email"))          # True
delattr(p, "email")
print(hasattr(p, "email"))          # False

# ── callable() ───────────────────────────────
print(callable(print))          # True
print(callable(42))             # False
print(callable(lambda x: x))   # True

# ── chr() and ord() ───────────────────────────
print(ord("A"))         # 65  — character → ASCII / Unicode code point
print(chr(65))          # 'A' — code point → character
print(ord("❤"))         # 10084
print(chr(10084))       # ❤

# ── bin() oct() hex() ─────────────────────────
print(bin(255))         # '0b11111111'
print(oct(255))         # '0o377'
print(hex(255))         # '0xff'

# ── format() ─────────────────────────────────
print(format(3.14159, ".2f"))   # '3.14'
print(format(255, "08b"))       # '11111111'
print(format(255, "#010b"))     # '0b11111111'
