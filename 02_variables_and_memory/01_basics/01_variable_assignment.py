# ============================================================
# Variable Assignment
# ============================================================
# In Python, a variable is a name (label) that points to an
# object stored in memory. Assignment uses the '=' operator.
# ============================================================

# --- Basic assignment ---
name = "Alice"          # str
age = 25                # int
height = 5.6            # float
is_student = True       # bool

print(name)
print(age)
print(height)
print(is_student)

# --- Assigning expressions ---
total = 10 + 5          # result of expression stored in total
greeting = "Hello, " + name

print(total)
print(greeting)

# --- Assigning None (absence of value) ---
result = None
print(result)           # None

# --- Checking the type of a variable ---
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(height))     # <class 'float'>
print(type(is_student)) # <class 'bool'>
print(type(result))     # <class 'NoneType'>
