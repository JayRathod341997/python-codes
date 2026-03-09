# ============================================================
# Assignment Operators
# ============================================================
# Assignment operators assign a value to a variable.
# Compound assignment operators combine an arithmetic/bitwise
# operation with assignment — a shorthand for updating a variable.
#
# Operator  Equivalent to      Example      Result (x starts at 10)
# --------  -----------------  -----------  -----------------------
#   =       x = value          x = 10       x = 10
#   +=      x = x + value      x += 3       x = 13
#   -=      x = x - value      x -= 3       x = 7
#   *=      x = x * value      x *= 3       x = 30
#   /=      x = x / value      x /= 3       x = 3.333...
#   //=     x = x // value     x //= 3      x = 3
#   %=      x = x % value      x %= 3       x = 1
#   **=     x = x ** value     x **= 3      x = 1000
#   &=      x = x & value      (bitwise)
#   |=      x = x | value      (bitwise)
#   ^=      x = x ^ value      (bitwise)
#   >>=     x = x >> value     (bitwise)
#   <<=     x = x << value     (bitwise)
# ============================================================

# --- Basic assignment ---
x = 10
print(x)        # 10

# --- += ---
x += 5
print(x)        # 15

# --- -= ---
x -= 3
print(x)        # 12

# --- *= ---
x *= 2
print(x)        # 24

# --- /= (result is always float) ---
x /= 4
print(x)        # 6.0

# --- //= ---
x //= 2
print(x)        # 3.0

# --- %= ---
x = 10
x %= 3
print(x)        # 1

# --- **= ---
x = 2
x **= 8
print(x)        # 256

# ============================================================
# Walrus operator := (Python 3.8+)
# ============================================================
# Assigns AND returns a value inside an expression.
# Also called the "assignment expression" operator.

import random
numbers = [4, 15, 7, 23, 2, 18]

# Without walrus:
for n in numbers:
    doubled = n * 2
    if doubled > 20:
        print(doubled)      # 30, 46, 36

# With walrus (compute and test in one step):
for n in numbers:
    if (doubled := n * 2) > 20:
        print(doubled)      # same result

# Common use: avoiding repeated function calls
data = "hello world"
if (length := len(data)) > 5:
    print(f"String is {length} chars long")   # String is 11 chars long

# ============================================================
# Multiple assignment and augmented assignment patterns
# ============================================================

# Accumulator pattern
total = 0
for i in range(1, 6):
    total += i
print(total)        # 15  (1+2+3+4+5)

# Counter pattern
count = 0
items = [1, -2, 3, -4, 5]
for item in items:
    if item > 0:
        count += 1
print(count)        # 3  (positive numbers)
