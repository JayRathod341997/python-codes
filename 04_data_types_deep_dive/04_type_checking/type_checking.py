# ─────────────────────────────────────────────
# Type Checking — type() and isinstance()
# ─────────────────────────────────────────────

# ── type() ───────────────────────────────────
# Returns the exact type of an object

x = 42
print(type(x))              # <class 'int'>
print(type("hello"))        # <class 'str'>
print(type([1, 2, 3]))      # <class 'list'>
print(type(None))           # <class 'NoneType'>
print(type(lambda: None))   # <class 'function'>

# Using type() for exact comparison
print(type(x) is int)       # True
print(type(x) is float)     # False

# ── isinstance() ─────────────────────────────
# Preferred for type checking — handles inheritance

print(isinstance(x, int))           # True
print(isinstance(x, (int, float)))  # True  — check against multiple types
print(isinstance(True, int))        # True  — bool IS an int
print(isinstance(True, bool))       # True
print(isinstance(3.14, (int, float)))  # True

# ── type() vs isinstance() ───────────────────
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

print(type(dog) is Dog)         # True
print(type(dog) is Animal)      # False — exact type only

print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True  — accounts for inheritance

# RULE: Use isinstance() in production code.
#       Use type() only when you need the exact type.

# ── Practical type guard ──────────────────────
def process(value):
    if isinstance(value, str):
        return value.upper()
    elif isinstance(value, (int, float)):
        return value * 2
    elif isinstance(value, list):
        return [process(item) for item in value]
    else:
        raise TypeError(f"Unsupported type: {type(value).__name__}")

print(process("hello"))         # HELLO
print(process(21))              # 42
print(process([1, "hi", 3.5]))  # [2, 'HI', 7.0]

# ── __class__ attribute ───────────────────────
print(x.__class__)          # <class 'int'>
print(x.__class__.__name__) # 'int'

# ── Type annotations (not enforcement) ────────
# Python type hints are hints only — not enforced at runtime
def add(a: int, b: int) -> int:
    return a + b

print(add(1, 2))        # 3
print(add("a", "b"))    # 'ab' — no error! annotations are not checked
