# ============================================================
# Bitwise Operators
# ============================================================
# Bitwise operators work directly on the binary (bit-level)
# representation of integers.
#
# Operator  Name            Description
# --------  --------------  ----------------------------------
#   &       AND             1 if BOTH bits are 1
#   |       OR              1 if AT LEAST ONE bit is 1
#   ^       XOR             1 if bits are DIFFERENT
#   ~       NOT             Flips all bits (complement)
#   <<      Left shift      Shift bits left, fill with 0s
#   >>      Right shift     Shift bits right
# ============================================================

# ============================================================
# Binary representation of small integers
# ============================================================
#   5  →  0101
#   3  →  0011
#   9  →  1001

a = 5       # 0101
b = 3       # 0011

# --- Bitwise AND (&) ---
# 0101
# 0011
# ----
# 0001  →  1
print(a & b)        # 1

# --- Bitwise OR (|) ---
# 0101
# 0011
# ----
# 0111  →  7
print(a | b)        # 7

# --- Bitwise XOR (^) ---
# 0101
# 0011
# ----
# 0110  →  6
print(a ^ b)        # 6

# --- Bitwise NOT (~) ---
# Formula: ~x = -(x + 1)
print(~a)           # -6
print(~b)           # -4

# --- Left Shift (<<) ---
# Each left shift = multiply by 2
# 5 = 0000 0101  →  0001 0100 = 20  (shifted 2 positions left)
print(a << 1)       # 10  (5 * 2)
print(a << 2)       # 20  (5 * 4)
print(1 << 3)       # 8   (2^3)

# --- Right Shift (>>) ---
# Each right shift = integer divide by 2
# 20 = 0001 0100  →  0000 0101 = 5  (shifted 2 positions right)
print(20 >> 1)      # 10  (20 // 2)
print(20 >> 2)      # 5   (20 // 4)

# ============================================================
# Viewing binary with bin()
# ============================================================

print(bin(5))       # 0b101
print(bin(3))       # 0b11
print(bin(5 & 3))   # 0b1
print(bin(5 | 3))   # 0b111
print(bin(5 ^ 3))   # 0b110

# ============================================================
# Practical uses
# ============================================================

# 1. Check if a number is even or odd (faster than %)
n = 14
print(n & 1)        # 0  → even (last bit is 0)
n = 7
print(n & 1)        # 1  → odd  (last bit is 1)

# 2. Swap two numbers without a temp variable using XOR
x = 10
y = 25
x = x ^ y
y = x ^ y
x = x ^ y
print(x, y)         # 25 10

# 3. Fast multiply/divide by powers of 2
value = 6
print(value << 3)   # 48  (6 * 8 = 6 * 2^3)
print(48 >> 3)      # 6   (48 / 8)

# 4. Flag / bitmask pattern (permissions)
READ    = 0b001     # 1
WRITE   = 0b010     # 2
EXECUTE = 0b100     # 4

# Give a user read and write permissions
user_perms = READ | WRITE       # 0b011 = 3
print(bin(user_perms))          # 0b11

# Check if user has EXECUTE permission
print(bool(user_perms & EXECUTE))   # False
# Grant execute
user_perms |= EXECUTE
print(bool(user_perms & EXECUTE))   # True
# Revoke write
user_perms &= ~WRITE
print(bool(user_perms & WRITE))     # False
