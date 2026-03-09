# ============================================================
# Mutable vs Immutable — Side-by-Side Comparison
# ============================================================

print("=" * 50)
print("IMMUTABLE (str, int, tuple)")
print("=" * 50)

# Strings
a = "hello"
b = a
b = b + " world"        # creates NEW object; a is untouched
print(f"a = {a!r}")     # 'hello'
print(f"b = {b!r}")     # 'hello world'
print(f"a is b: {a is b}\n")

# Integers — small int caching (-5 to 256)
x = 100
y = 100
print(f"x is y (100): {x is y}")   # True — CPython caches small ints

x = 1000
y = 1000
print(f"x is y (1000): {x is y}")  # False (usually) — not cached

print("\n" + "=" * 50)
print("MUTABLE (list, dict, set)")
print("=" * 50)

# Lists
original = [1, 2, 3]
alias = original        # alias = same object
copy_ = original.copy() # copy_ = different object, same content

alias.append(4)
print(f"original: {original}")  # [1, 2, 3, 4]
print(f"alias:    {alias}")     # [1, 2, 3, 4]  ← same object
print(f"copy_:    {copy_}")     # [1, 2, 3]     ← independent

print(f"original is alias: {original is alias}")  # True
print(f"original is copy_: {original is copy_}")  # False
print(f"original == copy_: {original == copy_}")  # False (different content now)

print("\n" + "=" * 50)
print("PASSING TO FUNCTIONS")
print("=" * 50)

def try_change_int(n):
    n = 999             # local rebind only, caller unaffected
    print("  inside function:", n)

def try_change_list(lst):
    lst.append(999)     # mutates the original list!
    print("  inside function:", lst)

num = 42
my_list = [1, 2, 3]

print(f"Before: num={num}, my_list={my_list}")
try_change_int(num)
try_change_list(my_list)
print(f"After:  num={num}, my_list={my_list}")
# num is unchanged; my_list was mutated!

print("\n" + "=" * 50)
print("QUICK REFERENCE TABLE")
print("=" * 50)
print(f"{'Type':<15} {'Mutable':<10} {'Hashable':<10} {'Example'}")
print("-" * 50)
types = [
    ("int",       "No",  "Yes", "42"),
    ("float",     "No",  "Yes", "3.14"),
    ("str",       "No",  "Yes", "'hello'"),
    ("tuple",     "No",  "Yes*","(1, 2)"),
    ("frozenset", "No",  "Yes", "frozenset({1,2})"),
    ("list",      "Yes", "No",  "[1, 2]"),
    ("dict",      "Yes", "No",  "{'a': 1}"),
    ("set",       "Yes", "No",  "{1, 2}"),
]
for name, mutable, hashable, example in types:
    print(f"{name:<15} {mutable:<10} {hashable:<10} {example}")
print("* only if all elements are immutable")
