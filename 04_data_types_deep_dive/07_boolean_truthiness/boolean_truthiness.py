# ─────────────────────────────────────────────
# Boolean Truthiness
# Every Python object has a truth value
# ─────────────────────────────────────────────

# ── Falsy values — evaluate to False ─────────
falsy_values = [
    False,      # bool False
    0,          # int zero
    0.0,        # float zero
    0j,         # complex zero
    "",         # empty string
    [],         # empty list
    (),         # empty tuple
    {},         # empty dict
    set(),      # empty set
    None,       # NoneType
]

print("=== Falsy values ===")
for val in falsy_values:
    print(f"  bool({val!r:10}) = {bool(val)}")

# ── Truthy values — everything else ──────────
truthy_values = [
    True, 1, -1, 3.14, "a", [0], (False,), {"key": 0}, {0}
]

print("\n=== Truthy values ===")
for val in truthy_values:
    print(f"  bool({val!r:10}) = {bool(val)}")

# ── Truthiness in conditions ──────────────────
print("\n=== Practical use in conditions ===")

# Instead of: if len(items) > 0:
items = [1, 2, 3]
if items:
    print("List has items")

items = []
if not items:
    print("List is empty")

# Instead of: if name != "":
name = ""
if not name:
    print("Name is empty or None")

# Instead of: if count != 0:
count = 5
if count:
    print(f"Count is {count}")

# ── __bool__ and __len__ ─────────────────────
# Python calls __bool__() first, then __len__() to decide truthiness
class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

ml_empty = MyList([])
ml_full  = MyList([1, 2])
print(bool(ml_empty))   # False — __len__ returns 0
print(bool(ml_full))    # True  — __len__ returns 2

# ── Short-circuit returns non-bool! ──────────
# 'and' returns first falsy value, or last value if all truthy
print(0 and "hello")    # 0         — stops at 0
print(1 and "hello")    # "hello"   — returns last truthy
print([] and [1,2])     # []        — stops at []

# 'or' returns first truthy value, or last value if all falsy
print(0 or "hello")     # "hello"   — skips 0
print("" or 0 or [])    # []        — all falsy, returns last
print("hi" or "bye")    # "hi"      — stops at first truthy

# ── Common idiom: default values ─────────────
user_input = ""
name = user_input or "Anonymous"    # use default if empty
print(name)                         # Anonymous

data = None
result = data or []                 # use empty list if None
print(result)                       # []
