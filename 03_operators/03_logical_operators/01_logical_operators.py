# ============================================================
# Logical Operators
# ============================================================
# Logical operators combine boolean expressions.
#
# Operator  Description                         Example
# --------  ----------------------------------  ---------------
#   and     True if BOTH sides are True         True and False  → False
#   or      True if AT LEAST ONE side is True   True or False   → True
#   not     Inverts the boolean value           not True        → False
# ============================================================

# --- and ---
print(True and True)        # True
print(True and False)       # False
print(False and True)       # False
print(False and False)      # False

# --- or ---
print(True or True)         # True
print(True or False)        # True
print(False or True)        # True
print(False or False)       # False

# --- not ---
print(not True)             # False
print(not False)            # True

# ============================================================
# Truth tables (quick reference)
# ============================================================
#
# A      B      A and B    A or B
# -----  -----  ---------  ------
# True   True   True       True
# True   False  False      True
# False  True   False      True
# False  False  False      False
#
# A      not A
# -----  -----
# True   False
# False  True

# ============================================================
# Using logical operators with comparisons
# ============================================================

age    = 25
income = 50000

# Both conditions must be true
eligible_loan = age >= 18 and income >= 30000
print(eligible_loan)        # True

# At least one condition must be true
gets_discount = age < 12 or age >= 65
print(gets_discount)        # False

# Negation
is_weekday = True
is_holiday = False
is_working_day = is_weekday and not is_holiday
print(is_working_day)       # True

# ============================================================
# Truthy and falsy values
# ============================================================
# In Python, non-boolean values are evaluated as True/False
# in a boolean context.
#
# Falsy: 0, 0.0, "", [], {}, (), None, False
# Truthy: everything else

print(bool(0))              # False
print(bool(""))             # False
print(bool([]))             # False
print(bool(None))           # False
print(bool(42))             # True
print(bool("hello"))        # True
print(bool([1, 2]))         # True

# Logical operators return one of the OPERANDS (not just True/False)
# (This ties into short-circuit evaluation — covered in topic 09)

print(0 or "default")       # "default"  (0 is falsy, returns right side)
print("user" or "guest")    # "user"     ("user" is truthy, returns left side)
print(None and "value")     # None       (None is falsy, short-circuits)

# ============================================================
# De Morgan's Laws
# ============================================================
# not (A and B)  ==  (not A) or  (not B)
# not (A or  B)  ==  (not A) and (not B)

a = True
b = False
print(not (a and b))            # True
print((not a) or (not b))       # True   (same result)

print(not (a or b))             # False
print((not a) and (not b))      # False  (same result)
