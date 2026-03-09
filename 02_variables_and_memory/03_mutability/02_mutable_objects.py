# ============================================================
# Mutable Objects
# ============================================================
# A mutable object CAN be changed after creation — the object
# is modified IN PLACE at the same memory address.
#
# Mutable types: list, dict, set, bytearray, user-defined classes
# ============================================================

# --- Lists are mutable ---
fruits = ["apple", "banana", "cherry"]
print(id(fruits))

fruits[0] = "avocado"   # modify in place
fruits.append("date")
print(fruits)
print(id(fruits))       # SAME address — same object, changed!

# --- Dicts are mutable ---
person = {"name": "Jay", "age": 22}
print(id(person))

person["age"] = 23      # modify in place
person["city"] = "Mumbai"
print(person)
print(id(person))       # SAME address

# --- Sets are mutable ---
colors = {"red", "green", "blue"}
colors.add("yellow")
colors.discard("green")
print(colors)

# --- Mutability means SHARED references can surprise you ---
list_a = [1, 2, 3]
list_b = list_a         # both point to the SAME object

list_b.append(4)
print("list_a:", list_a)    # [1, 2, 3, 4] ← changed!
print("list_b:", list_b)    # [1, 2, 3, 4]
print(list_a is list_b)     # True — same object

# --- Fix: make a copy instead ---
list_c = [1, 2, 3]
list_d = list_c.copy()  # or list(list_c) or list_c[:]

list_d.append(99)
print("list_c:", list_c)    # [1, 2, 3] — unchanged
print("list_d:", list_d)    # [1, 2, 3, 99]

# --- Mutable default argument gotcha ---
# BAD — the list is created once and shared across calls!
def bad_append(item, result=[]):
    result.append(item)
    return result

print(bad_append("a"))  # ['a']
print(bad_append("b"))  # ['a', 'b'] ← unexpected!

# GOOD — use None as default and create inside function
def good_append(item, result=None):
    if result is None:
        result = []
    result.append(item)
    return result

print(good_append("a")) # ['a']
print(good_append("b")) # ['b'] ← fresh each time
