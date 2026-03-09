# ============================================================
# Exercise: Identity Operators (is, is not)
# ============================================================

# ----------------------------------------------------------
# Q1. Predict whether each pair of variables refer to the
#     SAME object (is → True) or different objects.
#     Then verify using 'is' and id().
# ----------------------------------------------------------

a = [10, 20]
b = a
c = [10, 20]

# Predict first, then fill in:
print(a is b)       # ?  True or False
print(a is c)       # ?  True or False
print(id(a) == id(b))   # ?


# ----------------------------------------------------------
# Q2. The function below receives a list and appends 99.
#     After calling it, does the original list change?
#     Explain using 'is'.
# ----------------------------------------------------------

def append_value(lst):
    lst.append(99)
    return lst

original = [1, 2, 3]
returned = append_value(original)

print(original)             # ?  Does it have 99?
print(returned is original) # ?  True or False — same object?


# ----------------------------------------------------------
# Q3. Check if the following variables are None using 'is'.
# ----------------------------------------------------------

def find_user(users, name):
    for user in users:
        if user == name:
            return user
    return None

users = ["Alice", "Bob", "Charlie"]

result1 = find_user(users, "Bob")
result2 = find_user(users, "Dave")

# TODO: check if result1 is None
found1 = None       # use 'is not None'
found2 = None       # use 'is None'

print(found1)       # True  (Bob was found)
print(found2)       # True  (Dave not found)


# ----------------------------------------------------------
# Q4. Integer caching puzzle.
#     Predict True/False for each, then run to verify.
# ----------------------------------------------------------

x = 5
y = 5
print(x is y)       # ?  (small int — cached)

x = 500
y = 500
print(x is y)       # ?  (large int — may not be cached)

# Explanation: write a comment here


# ----------------------------------------------------------
# Q5. Spot the bug: the programmer uses == to check for None.
#     Rewrite the check using 'is not None'.
# ----------------------------------------------------------

data = None

# Bug:
if data == None:
    print("data is missing")

# TODO: rewrite using 'is not None' to check when data HAS a value


# ----------------------------------------------------------
# BONUS: Create two variables pointing to the same dict.
#        Modify via one variable and show that both are affected.
# ----------------------------------------------------------

config = {"debug": False, "version": 1}
settings = config   # alias

# TODO: set settings["debug"] = True

print(config["debug"])  # True (changed through settings)
print(config is settings)  # True
