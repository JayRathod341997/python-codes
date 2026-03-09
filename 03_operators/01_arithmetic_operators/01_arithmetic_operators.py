# ============================================================
# Arithmetic Operators
# ============================================================
# Arithmetic operators perform mathematical operations on
# numeric values (int, float).
#
# Operator  Name              Example     Result
# --------  ----------------  ----------  ------
#   +       Addition          5 + 3       8
#   -       Subtraction       5 - 3       2
#   *       Multiplication    5 * 3       15
#   /       Division          5 / 3       1.666...
#   //      Floor Division    5 // 3      1
#   %       Modulus           5 % 3       2
#   **      Exponentiation    5 ** 3      125
# ============================================================

a = 10
b = 3

# --- Addition ---
print(a + b)        # 13

# --- Subtraction ---
print(a - b)        # 7

# --- Multiplication ---
print(a * b)        # 30

# --- Division (always returns float) ---
print(a / b)        # 3.3333333333333335

# --- Floor Division (integer part of quotient) ---
print(a // b)       # 3

# --- Modulus (remainder after division) ---
print(a % b)        # 1

# --- Exponentiation ---
print(a ** b)       # 1000

# ============================================================
# Practical uses
# ============================================================

# Check if a number is even or odd using %
number = 17
print(number % 2 == 0)      # False  → odd

# Integer division to find how many groups of 4 fit in 22
students = 22
group_size = 4
groups = students // group_size
leftover = students % group_size
print(groups)       # 5
print(leftover)     # 2

# Compound interest using **
principal = 1000
rate = 1.05         # 5% annual growth
years = 3
amount = principal * (rate ** years)
print(round(amount, 2))     # 1157.63

# ============================================================
# Division quirks
# ============================================================

print(7 / 2)        # 3.5   (float division)
print(7 // 2)       # 3     (floor — rounds toward negative infinity)
print(-7 // 2)      # -4    (floor of -3.5 is -4, NOT -3)
print(7 % 2)        # 1
print(-7 % 2)       # 1     (Python's modulus sign matches divisor sign)


# r = a - (n * {floor}(a / n))   -> a = 7 , n = 2