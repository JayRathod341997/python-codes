# ============================================================
# Dynamic Typing
# ============================================================
# Python is dynamically typed: the TYPE of a variable is
# determined at RUNTIME, not at declaration time.
# You don't declare types — Python figures it out on the fly.
# ============================================================

# --- Same variable, different types at different times ---
data = 42
print(type(data))       # <class 'int'>

data = "hello"
print(type(data))       # <class 'str'>

data = [1, 2, 3]
print(type(data))       # <class 'list'>

data = {"key": "value"}
print(type(data))       # <class 'dict'>

# --- The variable is just a label; the object has the type ---
# Think of it as: variable → points to → object (which has a type)

# --- isinstance(): safer than type() for checks ---
value = 3.14
if isinstance(value, float):
    print("It's a float!")

if isinstance(value, (int, float)):     # check multiple types
    print("It's a number!")

# --- Duck typing: "if it walks like a duck, it's a duck" ---
# Python doesn't care about the exact type, just whether the
# object supports the operation you're trying to perform.

def double(x):
    return x * 2

print(double(5))        # 10
print(double("hi"))     # hihi      ← works on strings too!
print(double([1, 2]))   # [1, 2, 1, 2] ← and lists!

# --- Type errors happen at runtime, not compile time ---
# Uncomment to see the error:
# result = "hello" + 5   # TypeError: can only concatenate str (not "int") to str
