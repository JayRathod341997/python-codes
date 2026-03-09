# ============================================================
# Exercise: Logical Operators
# ============================================================

# ----------------------------------------------------------
# Q1. A user can log in if they have a valid username AND
#     a valid password. Fill in the condition.
# ----------------------------------------------------------

username_valid = True
password_valid = False

can_login = None        # TODO

print(can_login)        # False


# ----------------------------------------------------------
# Q2. A movie is available to watch if it is NOT censored
#     OR if the user is an adult.
# ----------------------------------------------------------

is_censored   = True
is_adult_user = True

can_watch = None        # TODO: not is_censored or is_adult_user

print(can_watch)        # True


# ----------------------------------------------------------
# Q3. A student passes the year if they pass BOTH subjects.
#     Subject pass mark = 40.
# ----------------------------------------------------------

math_score    = 55
science_score = 38

passed_year = None      # TODO

print(passed_year)      # False


# ----------------------------------------------------------
# Q4. Predict the output WITHOUT running, then verify.
# ----------------------------------------------------------

x = 5
y = 0
z = -3

print(x > 0 and y > 0)             # ?
print(x > 0 or y > 0)              # ?
print(not (z < 0))                  # ?
print(x > 0 and y == 0 and z < 0)  # ?


# ----------------------------------------------------------
# Q5. Using truthy/falsy, write a single expression that
#     returns name if it is non-empty, otherwise "Anonymous".
#     (Do not use if/else — use 'or'.)
# ----------------------------------------------------------

name = ""

display_name = None     # TODO: use 'or'

print(display_name)     # Anonymous


# ----------------------------------------------------------
# Q6. Apply De Morgan's Law manually.
#     Rewrite `not (a and b)` using only `not` and `or`.
#     Verify both expressions give the same result.
# ----------------------------------------------------------

a = True
b = False

original  = not (a and b)
demorgan  = None            # TODO: (not a) or (not b)

print(original)             # True
print(demorgan)             # True
print(original == demorgan) # True


# ----------------------------------------------------------
# BONUS: What does this print? Explain WHY.
# ----------------------------------------------------------

print([] or {} or "hello" or 0)     # ?
print(1 and 2 and 3)                # ?
print(0 and 99)                     # ?
