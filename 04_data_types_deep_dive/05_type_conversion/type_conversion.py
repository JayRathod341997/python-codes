# ─────────────────────────────────────────────
# Type Conversion
# Implicit (automatic) vs Explicit (manual casting)
# ─────────────────────────────────────────────

# ── Implicit conversion (coercion) ───────────
# Python promotes types automatically in expressions
x = 5       # int
y = 2.0     # float
result = x + y
print(result, type(result))     # 7.0 <class 'float'>

# int + float  → float
# int + complex → complex
print(5 + (2+3j))              # (7+3j)

# ── Explicit conversion (casting) ────────────

# → int
print(int(3.9))         # 3     — truncates, does NOT round
print(int("42"))        # 42
print(int("  10  "))    # 10    — strips whitespace
print(int(True))        # 1
print(int(False))       # 0
print(int("0xFF", 16))  # 255   — parse hex string
print(int("0b1010", 2)) # 10    — parse binary string
# int("3.14")           # ValueError! can't convert float-string directly

# → float
print(float(10))        # 10.0
print(float("3.14"))    # 3.14
print(float("inf"))     # inf
print(float(True))      # 1.0

# → str
print(str(42))          # '42'
print(str(3.14))        # '3.14'
print(str(True))        # 'True'
print(str(None))        # 'None'
print(str([1, 2, 3]))   # '[1, 2, 3]'

# → bool
print(bool(0))          # False
print(bool(1))          # True
print(bool(-5))         # True   — any non-zero is True
print(bool(""))         # False
print(bool("hi"))       # True
print(bool(None))       # False
print(bool([]))         # False
print(bool([0]))        # True   — non-empty list

# → list, tuple, set
print(list("abc"))          # ['a', 'b', 'c']
print(tuple([1, 2, 3]))     # (1, 2, 3)
print(set([1, 2, 2, 3]))    # {1, 2, 3}  — removes duplicates

# ── Common conversion errors ─────────────────
conversions = [
    ("int('abc')",       lambda: int("abc")),
    ("int('3.14')",      lambda: int("3.14")),
    ("float('hello')",   lambda: float("hello")),
]

for label, fn in conversions:
    try:
        fn()
    except (ValueError, TypeError) as e:
        print(f"  {label:20} → {type(e).__name__}: {e}")

# ── Safe conversion with fallback ─────────────
def safe_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

print(safe_int("42"))       # 42
print(safe_int("abc"))      # 0
print(safe_int(None, -1))   # -1
