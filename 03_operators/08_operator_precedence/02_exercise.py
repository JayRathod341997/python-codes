# ============================================================
# Exercise: Operator Precedence
# ============================================================
# For each question, FIRST predict the output using your
# knowledge of precedence, THEN run to verify.
# ============================================================

# ----------------------------------------------------------
# Q1. Predict the output of each expression.
#     Annotate the order of operations in a comment.
# ----------------------------------------------------------

print(2 + 3 * 5 - 1)        # ?
print(100 / 5 ** 2)          # ?
print(2 ** 2 ** 3)           # ?  (right-associative)
print((2 ** 2) ** 3)         # ?
print(10 % 3 + 2 * 4)        # ?


# ----------------------------------------------------------
# Q2. Add parentheses to make each expression evaluate
#     to the TARGET value shown. Do NOT change numbers or operators.
# ----------------------------------------------------------

# Target: 45  (currently evaluates to something else)
print(3 + 6 * 5)             # currently: 33  →  add parens to get 45

# Target: 1
print(10 - 3 * 3)            # currently: 1  →  already correct? verify!

# Target: 100
print(2 + 3 ** 2 * 10)       # currently: ?  →  add parens to get 100


# ----------------------------------------------------------
# Q3. Evaluate these boolean expressions step by step.
#     Write the intermediate steps as comments.
# ----------------------------------------------------------

x = 4

# Step through this:
result = x > 2 and x < 10 or x == 4
print(result)               # ?

# Step through this:
result = not x > 3 and x != 4
print(result)               # ?

# Step through this:
result = not (x > 3 and x != 4)
print(result)               # ?


# ----------------------------------------------------------
# Q4. The following expression has a bug due to wrong
#     assumed precedence. Fix it using parentheses.
# ----------------------------------------------------------

score  = 75
passed = score >= 50
bonus  = True

# Intended: award medal if passed AND (bonus OR score >= 90)
medal = passed and bonus or score >= 90     # BUG: wrong evaluation order
print(medal)                                # True (accidentally correct?)

# TODO: fix by adding parentheses to enforce correct precedence
medal_fixed = None      # write the corrected expression here
print(medal_fixed)      # should match medal when bonus=True


# ----------------------------------------------------------
# Q5. Unary minus trap — predict then verify.
# ----------------------------------------------------------

print(-2 ** 2)          # ?
print((-2) ** 2)        # ?
print(-2 ** 2 + 3)      # ?
print(-(2 ** 2) + 3)    # ?
print((-2) ** 2 + 3)    # ?


# ----------------------------------------------------------
# BONUS: Write a single expression (no if/else) that:
#   - Returns True if n is a positive even number
#   - Use proper parentheses to make precedence explicit
# ----------------------------------------------------------

n = 8
is_positive_even = None     # TODO

print(is_positive_even)     # True

n = -4
is_positive_even = None     # TODO (same expression)

print(is_positive_even)     # False
