# ─────────────────────────────────────────────
# bool — Boolean Type
# ─────────────────────────────────────────────

# ── Basics ───────────────────────────────────
t = True
f = False

print(type(t))          # <class 'bool'>
print(isinstance(t, int))   # True — bool is a subclass of int!
print(int(True))        # 1
print(int(False))       # 0

# ── Comparison operators → produce bools ──────
print(5 > 3)            # True
print(5 == 5)           # True
print(5 != 3)           # True
print(5 >= 10)          # False
print("a" < "b")        # True — compares lexicographically

# ── Logical operators ─────────────────────────
print(True and True)    # True
print(True and False)   # False
print(False or True)    # True
print(not True)         # False

# ── Short-circuit evaluation ──────────────────
# 'and' stops at first False
# 'or'  stops at first True
def say(msg, val):
    print(msg)
    return val

# Only evaluates left side (right is skipped)
result = say("left", False) and say("right", True)
print("Result:", result)    # right side never called

result = say("left", True) or say("right", False)
print("Result:", result)    # right side never called

# ── bool arithmetic ───────────────────────────
print(True + True)      # 2
print(True * 5)         # 5
print(False * 100)      # 0

# Count Trues in a list
flags = [True, False, True, True, False]
print(sum(flags))       # 3  — count of True values

# ── Comparison chaining ───────────────────────
x = 5
print(1 < x < 10)       # True  — Python allows chaining
print(1 < x < 4)        # False
print(1 < 3 < 5 < 10)   # True  — works for any length
