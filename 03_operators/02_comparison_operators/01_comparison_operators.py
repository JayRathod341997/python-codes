# ============================================================
# Comparison Operators
# ============================================================
# Comparison operators compare two values and always return
# a boolean: True or False.
#
# Operator  Meaning                 Example       Result
# --------  ----------------------  ------------  ------
#   ==      Equal to                5 == 5        True
#   !=      Not equal to            5 != 3        True
#   >       Greater than            5 > 3         True
#   <       Less than               5 < 3         False
#   >=      Greater than or equal   5 >= 5        True
#   <=      Less than or equal      4 <= 3        False
# ============================================================

a = 10
b = 20
c = 10

print(a == c)       # True   (same value)
print(a == b)       # False
print(a != b)       # True
print(a > b)        # False
print(a < b)        # True
print(a >= c)       # True   (10 >= 10)
print(a <= b)       # True

# ============================================================
# Chained comparisons (Python-specific feature)
# ============================================================
# Python allows chaining comparisons — reads like math notation.

x = 15

print(10 < x < 20)          # True   (x is between 10 and 20)
print(10 < x < 15)          # False
print(1 <= x <= 100)        # True

# This is equivalent to:
print(10 < x and x < 20)    # True (same result, less readable)

# ============================================================
# Comparing strings
# ============================================================
# Strings are compared lexicographically (character by character,
# using Unicode code points).

print("apple" == "apple")   # True
print("apple" == "Apple")   # False  (case-sensitive)
print("apple" < "banana")   # True   ('a' < 'b')
print("b" > "a")            # True
print("cat" > "car")        # True   ('t' > 'r' at index 2)

# ============================================================
# Comparing different numeric types
# ============================================================

print(5 == 5.0)             # True   (int vs float, value-equal)
print(5 == "5")             # False  (int vs str — never equal)

# ============================================================
# Practical uses
# ============================================================

age = 18
print(age >= 18)            # True  → eligible to vote

temperature = 37.8
print(temperature > 37.5)   # True  → fever detected

score = 85
grade = "A" if score >= 90 else ("B" if score >= 80 else "C")
print(grade)                # B
