# ─────────────────────────────────────────────
# float — Floating Point Type
# ─────────────────────────────────────────────

# ── Basics ───────────────────────────────────
x = 3.14
y = -0.001
z = 1.0         # still a float even though whole number

print(type(x))  # <class 'float'>

# Scientific notation
a = 1.5e3       # 1500.0
b = 2.5e-4      # 0.00025
print(a, b)

# ── Float precision problem ───────────────────
print(0.1 + 0.2)            # 0.30000000000000004  ← NOT 0.3!
print(0.1 + 0.2 == 0.3)     # False

# Fix 1: round()
print(round(0.1 + 0.2, 2))  # 0.3

# Fix 2: math.isclose()
import math
print(math.isclose(0.1 + 0.2, 0.3))    # True

# Fix 3: decimal module (for exact decimal arithmetic)
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))  # 0.3 exactly

# ── Special float values ──────────────────────
inf     = float("inf")
neg_inf = float("-inf")
nan     = float("nan")

print(inf, neg_inf, nan)
print(math.isinf(inf))      # True
print(math.isnan(nan))      # True
print(nan == nan)            # False  ← NaN is never equal to itself!

# ── Float methods ─────────────────────────────
f = 3.75
print(f.is_integer())       # False
print((3.0).is_integer())   # True

# as_integer_ratio — exact fraction representation
print((0.5).as_integer_ratio())   # (1, 2)

# ── Rounding ─────────────────────────────────
print(round(3.14159, 2))    # 3.14
print(round(3.5))           # 4  (banker's rounding — rounds to even)
print(round(2.5))           # 2  (banker's rounding)

print(math.floor(3.9))      # 3  — always round down
print(math.ceil(3.1))       # 4  — always round up
print(math.trunc(3.9))      # 3  — truncate (same as int())

# ── Float precision info ──────────────────────
import sys
print(sys.float_info.max)   # max float value
print(sys.float_info.min)   # smallest positive float
