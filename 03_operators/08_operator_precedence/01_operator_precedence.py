# ============================================================
# Operator Precedence
# ============================================================
# When an expression has multiple operators, Python evaluates
# them in a defined ORDER called operator precedence.
# Higher precedence operators are evaluated FIRST.
#
# Precedence (highest → lowest):
#
#  Level  Operators                         Description
#  -----  --------------------------------  -------------------
#   1     ()                                Parentheses
#   2     **                                Exponentiation
#   3     +x, -x, ~x                        Unary plus/minus/NOT
#   4     *, /, //, %                       Multiply / Divide
#   5     +, -                              Add / Subtract
#   6     <<, >>                            Bitwise Shifts
#   7     &                                 Bitwise AND
#   8     ^                                 Bitwise XOR
#   9     |                                 Bitwise OR
#  10     ==, !=, >, <, >=, <=, is, in ...  Comparisons
#  11     not                               Logical NOT
#  12     and                               Logical AND
#  13     or                                Logical OR
#  14     :=                                Walrus
# ============================================================

# ============================================================
# Arithmetic precedence
# ============================================================

print(2 + 3 * 4)        # 14   (* before +)
print((2 + 3) * 4)      # 20   (parentheses first)
print(2 ** 3 ** 2)      # 512  (** is RIGHT-associative: 3**2=9, 2**9=512)
print((2 ** 3) ** 2)    # 64   (left-to-right with parens: 8**2=64)
print(10 - 3 - 2)       # 5    (- is LEFT-associative: (10-3)-2)

print(10 / 2 + 3 * 4 - 1)   # 16.0
# Step-by-step:
# 10 / 2  = 5.0
# 3 * 4   = 12
# 5.0 + 12 - 1 = 16.0

# ============================================================
# Unary minus and exponentiation
# ============================================================

print(-2 ** 2)          # -4   (** first: 2**2=4, then -4)
print((-2) ** 2)        # 4    (parentheses make -2 the base)

# ============================================================
# Mixing arithmetic and comparisons
# ============================================================

print(3 + 4 > 5 + 1)    # True    (7 > 6)
print(10 - 3 == 4 + 3)  # True    (7 == 7)

# ============================================================
# Mixing comparisons and logical operators
# ============================================================
# Comparisons are evaluated before 'and'/'or'/'not'

x = 5
print(x > 0 and x < 10)            # True
print(not x > 0 or x < 10)         # True
# Evaluation: (not (x > 0)) or (x < 10)
#           = (not True) or True
#           = False or True = True

print(not (x > 0 or x < 10))       # False
# Evaluation: not (True or True) = not True = False

# ============================================================
# Common mistakes
# ============================================================

# MISTAKE: thinking + has higher precedence than ==
result = 1 + 2 == 3
print(result)           # True  (1+2=3, then 3==3)
# NOT: 1 + (2 == 3) → 1 + False → 1

# MISTAKE: unary minus with **
print(-3 ** 2)          # -9  NOT 9  (** first, then negation)

# MISTAKE: or vs and precedence
a, b, c = True, False, True
print(a or b and c)     # True   (and first: b and c = False, then a or False = True)
print((a or b) and c)   # True   (different grouping, same result here)

a, b, c = False, True, False
print(a or b and c)     # False  (and first: True and False = False, then False or False)
print((a or b) and c)   # False  (False or True = True, then True and False = False — same here)

# ============================================================
# Best practice: use parentheses for clarity
# ============================================================
# Even if you know the precedence, parentheses make intent clear.

# Unclear:
if x > 0 and x % 2 == 0 or x == -1:
    pass

# Clear:
if (x > 0 and x % 2 == 0) or (x == -1):
    pass
