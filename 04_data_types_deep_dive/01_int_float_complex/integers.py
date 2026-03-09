# ─────────────────────────────────────────────
# int — Integer Type
# ─────────────────────────────────────────────

# ── Basics ───────────────────────────────────
x = 10
y = -5
z = 0

print(type(x))          # <class 'int'>
print(x, y, z)

# Python integers have unlimited precision
big = 10 ** 100         # googol — no overflow!
print(big)

# ── Different bases ──────────────────────────
binary  = 0b1010        # base 2  → 10
octal   = 0o12          # base 8  → 10
hexa    = 0x0A          # base 16 → 10

print(binary, octal, hexa)      # all print 10

# Convert to different base strings
num = 255
print(bin(num))         # '0b11111111'
print(oct(num))         # '0o377'
print(hex(num))         # '0xff'

# ── Underscores for readability ───────────────
million   = 1_000_000
pi_digits = 3_141_592_653

print(million)          # 1000000
print(pi_digits)

# ── Integer methods ──────────────────────────
n = -42
print(abs(n))           # 42         — absolute value
print(pow(2, 10))       # 1024       — 2^10
print(pow(2, 10, 100))  # 24         — (2^10) % 100  (fast modular exponentiation)
print(divmod(17, 5))    # (3, 2)     — quotient and remainder

# ── Integer limits (sys) ─────────────────────
import sys
print("Max int size:", sys.maxsize)   # platform max (not a hard limit)
