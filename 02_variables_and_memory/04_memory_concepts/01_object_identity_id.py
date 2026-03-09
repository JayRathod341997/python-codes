# ============================================================
# Object Identity — id()
# ============================================================
# id(obj) returns the MEMORY ADDRESS of an object (as an int).
# Two variables are identical (same object) if id() is equal.
#
# 'is'  → checks identity  (same object in memory)
# '=='  → checks equality  (same value)
# ============================================================

# --- Basic id() usage ---
a = 42
print(f"id(a) = {id(a)}")

b = a
print(f"id(b) = {id(b)}")
print(f"a is b: {a is b}")     # True — both point to same int object

b = 43
print(f"After b=43, id(b) = {id(b)}")
print(f"a is b: {a is b}")     # False — different objects now

# --- id() vs == ---
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"\nlist1 == list2: {list1 == list2}")   # True  (same content)
print(f"list1 is list2: {list1 is list2}")     # False (different objects)
print(f"list1 is list3: {list1 is list3}")     # True  (same object)

print(f"id(list1) = {id(list1)}")
print(f"id(list2) = {id(list2)}")
print(f"id(list3) = {id(list3)}")

# --- CPython small integer cache (-5 to 256) ---
print("\n--- Integer caching ---")
x = 256
y = 256
print(f"x=256, y=256 → x is y: {x is y}")     # True (cached)

x = 257
y = 257
print(f"x=257, y=257 → x is y: {x is y}")     # False (NOT cached) — implementation detail!

# --- String interning ---
print("\n--- String interning ---")
s1 = "hello"
s2 = "hello"
print(f"s1 is s2: {s1 is s2}")     # True — CPython interns short strings

s3 = "hello world"
s4 = "hello world"
print(f"s3 is s4: {s3 is s4}")     # May be True or False — implementation detail

# NOTE: Never rely on 'is' for value comparison. Always use '=='
# 'is' is for identity checks like: `if x is None:`

# --- None identity check (correct usage of 'is') ---
value = None
if value is None:
    print("\nvalue is None — use 'is None', not '== None'")

# --- Object lifecycle: id can be reused ---
temp = [10, 20, 30]
temp_id = id(temp)
del temp                    # object deleted; memory may be freed
new_obj = [99, 88]
print(f"\nOld id: {temp_id}, New obj id: {id(new_obj)}")
# The new object may get the same id as the deleted one
