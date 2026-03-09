# ============================================================
#  SORTING — sort() vs sorted()
#  Real-world context: E-commerce product listing
# ============================================================

# ============================================================
#  sort() vs sorted()  — key difference
# ============================================================

prices = [299.99, 49.99, 150.0, 999.0, 75.5, 12.0]

# sort()   — modifies IN PLACE, returns None
prices.sort()
print("sort() ascending :", prices)

prices.sort(reverse=True)
print("sort() descending:", prices)

# sorted() — returns NEW list, original UNCHANGED
original = [299.99, 49.99, 150.0, 999.0, 75.5, 12.0]
cheap_first = sorted(original)
print("\nOriginal     :", original)
print("sorted() asc :", cheap_first)

# ============================================================
#  Sorting STRINGS — product names alphabetically
# ============================================================

print("\n--- Sorting Strings ---")

products = ["Laptop", "headphones", "Tablet", "mouse", "Keyboard"]

# Default: case-sensitive (uppercase before lowercase in ASCII)
print("Default sort   :", sorted(products))

# Case-insensitive using key=str.lower
print("Ignore case    :", sorted(products, key=str.lower))

# By length (shortest product name first)
print("By name length :", sorted(products, key=len))

# ============================================================
#  Sorting with KEY function — by attribute
# ============================================================

print("\n--- key= parameter ---")

# List of (product, price, rating) tuples
catalog = [
    ("Laptop",       999.0,  4.5),
    ("Headphones",    49.99, 4.8),
    ("Tablet",       299.0,  4.2),
    ("Mouse",         25.0,  4.6),
    ("Keyboard",      75.5,  4.7),
]

# Sort by price (index 1)
by_price = sorted(catalog, key=lambda x: x[1])
print("By price (asc) :")
for item in by_price:
    print(f"  {item[0]:<15} ${item[1]:<8} ★{item[2]}")

# Sort by rating descending
by_rating = sorted(catalog, key=lambda x: x[2], reverse=True)
print("\nBy rating (desc):")
for item in by_rating:
    print(f"  {item[0]:<15} ${item[1]:<8} ★{item[2]}")

# ============================================================
#  Multi-key sorting — primary & secondary sort
# ============================================================

print("\n--- Multi-key sort (primary + secondary) ---")

# Sort by category first, then by price within each category
items = [
    ("Electronics", "Laptop",       999.0),
    ("Electronics", "Mouse",         25.0),
    ("Clothing",    "T-Shirt",       19.99),
    ("Clothing",    "Jacket",        89.99),
    ("Electronics", "Headphones",   49.99),
    ("Clothing",    "Jeans",         59.99),
]

items.sort(key=lambda x: (x[0], x[2]))  # category then price
print("Sorted by category, then price:")
for item in items:
    print(f"  [{item[0]:<12}] {item[1]:<15} ${item[2]}")

# ============================================================
#  Sorting with operator.itemgetter (faster than lambda)
# ============================================================

from operator import itemgetter

students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob",   "grade": 75},
    {"name": "Carol", "grade": 92},
    {"name": "Dave",  "grade": 88},
]

# Sort by grade desc, then name asc for ties
students.sort(key=lambda s: (-s["grade"], s["name"]))
print("\nLeaderboard:")
for i, s in enumerate(students, 1):
    print(f"  {i}. {s['name']:<8} {s['grade']}")

# ============================================================
#  KEY POINTS
#  - sort()   modifies in-place | sorted() returns new list
#  - key=     transform each element before comparing
#  - reverse= True for descending
#  - Tuple as key → multi-level sorting
# ============================================================
