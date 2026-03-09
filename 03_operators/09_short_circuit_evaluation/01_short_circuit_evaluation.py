# ============================================================
# Short-Circuit Evaluation
# ============================================================
# Python's 'and' and 'or' do NOT always evaluate both sides.
# They stop ("short-circuit") as soon as the result is determined.
#
# 'and' short-circuits on the FIRST FALSY value:
#   - If left side is falsy  → return left  (don't evaluate right)
#   - If left side is truthy → return right
#
# 'or' short-circuits on the FIRST TRUTHY value:
#   - If left side is truthy → return left  (don't evaluate right)
#   - If left side is falsy  → return right
#
# KEY INSIGHT: 'and'/'or' return one of the OPERANDS, not True/False.
# ============================================================

# ============================================================
# Observing short-circuit with a function that has side effects
# ============================================================

def check_a():
    print("  check_a called")
    return False

def check_b():
    print("  check_b called")
    return True

print("--- and ---")
result = check_a() and check_b()
# Output: "check_a called"  (check_b is NEVER called — short-circuited)
print(result)               # False

print("--- or ---")
result = check_b() or check_a()
# Output: "check_b called"  (check_a is NEVER called — short-circuited)
print(result)               # True

# ============================================================
# 'and' returns the first falsy or the last value
# ============================================================

print(False and "hello")    # False   (first falsy — stopped here)
print(None and 42)          # None    (first falsy)
print(0 and 99)             # 0       (first falsy)
print(1 and 2)              # 2       (both truthy — returns last)
print("a" and "b" and "c")  # "c"    (all truthy — returns last)

# ============================================================
# 'or' returns the first truthy or the last value
# ============================================================

print(False or "hello")     # "hello" (first is falsy, return right)
print(None or 0 or "")      # ""      (all falsy — returns last)
print(0 or [] or "result")  # "result"(first truthy encountered)
print("user" or "guest")    # "user"  (first truthy — stopped here)
print(42 or crash_here)     # 42      (right side never evaluated!)
# ^ If you uncomment crash_here, it would NameError — but it won't run!

# ============================================================
# Pattern 1: Default value fallback with 'or'
# ============================================================

# If name is empty/None, use "Anonymous" as default
name = ""
display_name = name or "Anonymous"
print(display_name)         # Anonymous

name = "Jay"
display_name = name or "Anonymous"
print(display_name)         # Jay

# ============================================================
# Pattern 2: Guard against None before accessing attribute
# ============================================================

user = None
# This would crash: user.name
# Safe with short-circuit:
username = user and user.get("name")
print(username)             # None  (user is falsy, short-circuited)

user = {"name": "Alice", "age": 30}
username = user and user.get("name")
print(username)             # Alice

# ============================================================
# Pattern 3: Conditional execution without if
# ============================================================

debug = True
debug and print("Debug mode is ON")     # prints

debug = False
debug and print("Debug mode is ON")     # does NOT print

# ============================================================
# Pattern 4: Safe division guard
# ============================================================

denominator = 0
result = denominator != 0 and (100 / denominator)
print(result)               # False  (short-circuited, no ZeroDivisionError)

denominator = 5
result = denominator != 0 and (100 / denominator)
print(result)               # 20.0

# ============================================================
# Important: 'or' fallback breaks for intentionally falsy values
# ============================================================

# Problem: 0 is a valid value, but 'or' treats it as falsy
count = 0
display = count or "N/A"
print(display)              # "N/A"  ← WRONG! 0 is a valid count

# Fix: use explicit None check
count = 0
display = count if count is not None else "N/A"
print(display)              # 0     ← correct
