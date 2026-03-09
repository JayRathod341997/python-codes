# ============================================================
# Exercise: Comparison Operators
# ============================================================

# ----------------------------------------------------------
# Q1. Given two exam scores, write comparisons to check:
#     a) Are the scores equal?
#     b) Is score_a higher than score_b?
#     c) Did score_b fail? (passing mark is 50)
# ----------------------------------------------------------

score_a = 78
score_b = 45

equal   = None      # TODO
a_wins  = None      # TODO
b_fails = None      # TODO

print(equal)        # False
print(a_wins)       # True
print(b_fails)      # True


# ----------------------------------------------------------
# Q2. A speed limit is 60 km/h. A car is travelling at
#     85 km/h. Check if the car is overspeeding.
# ----------------------------------------------------------

speed_limit = 60
car_speed   = 85

overspeeding = None     # TODO

print(overspeeding)     # True


# ----------------------------------------------------------
# Q3. Use a chained comparison to check if a number is
#     in the valid range [1, 100] (inclusive on both ends).
# ----------------------------------------------------------

number = 73

in_range = None         # TODO: use chained comparison

print(in_range)         # True


# ----------------------------------------------------------
# Q4. Compare strings: check if "Python" comes before
#     "Ruby" alphabetically.
# ----------------------------------------------------------

lang1 = "Python"
lang2 = "Ruby"

py_first = None         # TODO: use <

print(py_first)         # True


# ----------------------------------------------------------
# Q5. Predict the output WITHOUT running, then verify.
# ----------------------------------------------------------

print("z" > "a")                    # ?
print("abc" == "ABC")               # ?
print(100 == 100.0)                 # ?
print(0 == False)                   # ?  (hint: bool is subclass of int)
print(1 == True)                    # ?


# ----------------------------------------------------------
# Q6. A cinema gives discount if age < 12 OR age >= 60.
#     Check for age = 8 and age = 45 separately.
# ----------------------------------------------------------

age1 = 8
age2 = 45

discount1 = None        # TODO: age1 < 12 or age1 >= 60
discount2 = None        # TODO: age2 < 12 or age2 >= 60

print(discount1)        # True
print(discount2)        # False
