# ─────────────────────────────────────────────
# Numeric Operations
# ─────────────────────────────────────────────

import math
import statistics

# ── Basic arithmetic operators ────────────────
print(10 + 3)       # 13   — addition
print(10 - 3)       # 7    — subtraction
print(10 * 3)       # 30   — multiplication
print(10 / 3)       # 3.333...  — true division (always float)
print(10 // 3)      # 3    — floor division (integer result)
print(10 % 3)       # 1    — modulo (remainder)
print(10 ** 3)      # 1000 — exponentiation

# ── Augmented assignment ──────────────────────
x = 10
x += 3;  print(x)   # 13
x -= 3;  print(x)   # 10
x *= 2;  print(x)   # 20
x //= 3; print(x)   # 6
x **= 2; print(x)   # 36
x %= 10; print(x)   # 6

# ── Operator precedence (PEMDAS / BODMAS) ─────
print(2 + 3 * 4)        # 14  — * before +
print((2 + 3) * 4)      # 20  — parentheses first
print(2 ** 3 ** 2)      # 512 — ** is right-associative: 2**(3**2)=2**9
print(-2 ** 2)          # -4  — -(2**2), not (-2)**2!
print((-2) ** 2)        # 4

# ── Bitwise operators ─────────────────────────
a, b = 0b1100, 0b1010   # 12 and 10
print(f"{a & b:04b}")   # 1000  — AND
print(f"{a | b:04b}")   # 1110  — OR
print(f"{a ^ b:04b}")   # 0110  — XOR
print(f"{~a}")          # -13   — NOT (bitwise complement)
print(f"{a << 1:04b}")  # 11000 — left shift (multiply by 2)
print(f"{a >> 1:04b}")  # 0110  — right shift (divide by 2)

# ── math module ───────────────────────────────
print(math.sqrt(144))       # 12.0
print(math.cbrt(27))        # 3.0  — cube root (Python 3.11+)
print(math.log(100, 10))    # 2.0  — log base 10
print(math.log(math.e))     # 1.0  — natural log
print(math.log2(8))         # 3.0
print(math.factorial(5))    # 120
print(math.gcd(48, 18))     # 6    — greatest common divisor
print(math.lcm(4, 6))       # 12   — least common multiple
print(math.comb(10, 3))     # 120  — combinations (nCr)
print(math.perm(10, 3))     # 720  — permutations (nPr)
print(math.isqrt(17))       # 4    — integer square root

# ── Trig ─────────────────────────────────────
print(math.sin(math.pi / 2))    # 1.0
print(math.cos(0))              # 1.0
print(math.tan(math.pi / 4))    # ~1.0
print(math.degrees(math.pi))    # 180.0
print(math.radians(180))        # pi

# ── Built-in numeric functions ────────────────
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(min(nums))            # 1
print(max(nums))            # 9
print(sum(nums))            # 31
print(abs(-7))              # 7
print(round(3.567, 2))      # 3.57
print(divmod(17, 5))        # (3, 2)  — (quotient, remainder)

# ── statistics module ─────────────────────────
data = [10, 20, 30, 40, 50]
print(statistics.mean(data))        # 30
print(statistics.median(data))      # 30
print(statistics.mode([1,1,2,3]))   # 1
print(statistics.stdev(data))       # standard deviation
print(statistics.variance(data))    # variance
