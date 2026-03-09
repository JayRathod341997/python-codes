# ============================================================
# Exercise: Short-Circuit Evaluation
# ============================================================

# ----------------------------------------------------------
# Q1. Predict what each expression returns (the actual value,
#     not just True/False). Then run to verify.
# ----------------------------------------------------------

print(0 or "hello")             # ?
print("" or [] or 42)           # ?
print(None and "value")         # ?
print("first" and "second")     # ?
print([] or {} or () or "last") # ?
print(1 and 2 and 0 and 4)      # ?


# ----------------------------------------------------------
# Q2. Use 'or' to write a default-value expression.
#     If user_city is empty, fall back to "Unknown City".
# ----------------------------------------------------------

user_city = ""

city = None         # TODO: use 'or' for default

print(city)         # Unknown City

user_city = "Mumbai"
city = None         # TODO: same expression

print(city)         # Mumbai


# ----------------------------------------------------------
# Q3. Use short-circuit 'and' to safely access a nested
#     dictionary without raising a KeyError or TypeError.
# ----------------------------------------------------------

profiles = {
    "alice": {"age": 25, "email": "alice@example.com"},
    "bob":   None,
}

# Safe access for alice
alice_email = profiles.get("alice") and profiles["alice"].get("email")
print(alice_email)              # alice@example.com

# Safe access for bob (profile is None)
bob_email = profiles.get("bob") and profiles["bob"].get("email")
print(bob_email)                # None  (short-circuited)

# Safe access for charlie (not in dict)
charlie_email = profiles.get("charlie") and profiles["charlie"].get("email")
print(charlie_email)            # None  (short-circuited)


# ----------------------------------------------------------
# Q4. Which side is NOT evaluated? Use a helper function
#     to prove it.
# ----------------------------------------------------------

call_log = []

def left():
    call_log.append("left")
    return False

def right():
    call_log.append("right")
    return True

call_log.clear()
result = left() and right()
print(call_log)     # ['left']  — right() was never called

call_log.clear()
result = right() or left()
print(call_log)     # ['right'] — left() was never called


# ----------------------------------------------------------
# Q5. Safe division: use short-circuit to avoid ZeroDivisionError.
#     Return the division result, or 0 if denominator is zero.
# ----------------------------------------------------------

def safe_divide(a, b):
    return None     # TODO: use short-circuit with 'and'/'or'
                    # Hint: b != 0 and a / b or 0

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # 0


# ----------------------------------------------------------
# Q6. Spot the bug: the programmer uses 'or' for a default
#     but the value 0 is a valid input.
#     Rewrite it correctly.
# ----------------------------------------------------------

items_in_cart = 0

# Buggy code:
display = items_in_cart or "Cart is empty"
print(display)      # "Cart is empty"  ← BUG: 0 is a valid value!

# TODO: fix using an explicit None check so that 0 prints as 0
# items_in_cart might genuinely be None when cart hasn't loaded
items_in_cart = None

display_fixed = None    # TODO: items_in_cart if items_in_cart is not None else "Cart is empty"

print(display_fixed)    # Cart is empty

items_in_cart = 0
display_fixed = None    # TODO: same expression

print(display_fixed)    # 0


# ----------------------------------------------------------
# BONUS: Write a one-liner using short-circuit that prints
#        a greeting only when the user is logged in and
#        the user's name is non-empty.
# ----------------------------------------------------------

is_logged_in = True
user_name    = "Jay"

# TODO: single line using 'and' — print "Welcome, Jay!" only if both are truthy
