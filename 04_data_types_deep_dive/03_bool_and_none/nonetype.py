# ─────────────────────────────────────────────
# NoneType — The Null / Absence of Value
# ─────────────────────────────────────────────

# ── Basics ───────────────────────────────────
x = None
print(x)                    # None
print(type(x))              # <class 'NoneType'>

# There is only ONE None object in Python
a = None
b = None
print(a is b)               # True — same object in memory
print(id(a) == id(b))       # True

# ── Checking for None ─────────────────────────
# ALWAYS use 'is' / 'is not', never == / !=
value = None

if value is None:
    print("value is None")

if value is not None:
    print("value has something")
else:
    print("still None")

# Avoid this (works but not idiomatic):
# if value == None: ...

# ── Common uses ───────────────────────────────

# 1. Default return value of functions
def do_nothing():
    pass    # implicit return None

result = do_nothing()
print(result)           # None

# 2. Optional / sentinel arguments
def greet(name, greeting=None):
    if greeting is None:
        greeting = "Hello"
    return f"{greeting}, {name}!"

print(greet("Jay"))             # Hello, Jay!
print(greet("Jay", "Hi"))       # Hi, Jay!

# 3. Initializing a variable before assignment
user = None
# ... later in code ...
user = "Jay"
print(user)

# 4. Clearing a reference
data = [1, 2, 3]
data = None             # release the list from memory

# ── None is falsy ─────────────────────────────
print(bool(None))       # False

items = None
if not items:
    print("No items yet")  # prints this

# ── None vs 0 vs empty string vs False ────────
for val in [None, 0, "", [], False]:
    print(f"  bool({val!r:6}) = {bool(val)}")
