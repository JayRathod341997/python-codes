# ============================================================
#  DICTIONARY METHODS
#  Real-world context: Student grade management
# ============================================================

grades = {
    "Alice" : 88,
    "Bob"   : 75,
    "Carol" : 92,
    "Dave"  : 61,
    "Eve"   : 78,
}

# ============================================================
#  keys(), values(), items()
# ============================================================

print("=== View Objects ===")
print("keys()  :", list(grades.keys()))
print("values():", list(grades.values()))
print("items() :", list(grades.items()))

# These are VIEWS — live, reflect changes
keys_view = grades.keys()
grades["Frank"] = 83
print("\nAfter adding Frank — keys view (live):", keys_view)

# ============================================================
#  get() — safe retrieval
# ============================================================

print("\n=== get() ===")
print("Alice's grade :", grades.get("Alice"))
print("Unknown student:", grades.get("Zara", "Not enrolled"))

# ============================================================
#  pop() — remove and return
# ============================================================

print("\n=== pop() ===")
dropped = grades.pop("Dave")
print(f"Dave dropped the course, grade was: {dropped}")
print("Grades now:", grades)

# pop with default (won't raise KeyError)
result = grades.pop("NonExistent", None)
print("Pop missing key:", result)

# ============================================================
#  popitem() — remove and return the LAST inserted item
# ============================================================

print("\n=== popitem() ===")
last_item = grades.popitem()
print(f"Removed last item: {last_item}")
print("Grades now:", grades)

# ============================================================
#  update() — merge / bulk update
# ============================================================

print("\n=== update() ===")

# Add new students
new_students = {"Grace": 95, "Hank": 70, "Ivy": 88}
grades.update(new_students)
print("After adding new students:", grades)

# Update existing grades (re-evaluation)
grades.update({"Alice": 91, "Bob": 79})
print("After re-evaluation:", grades)

# ============================================================
#  setdefault() — get value, insert with default if missing
# ============================================================

print("\n=== setdefault() ===")

attendance = {}
students = ["Alice", "Bob", "Alice", "Carol", "Bob", "Alice"]

# Count attendance using setdefault
for student in students:
    attendance.setdefault(student, 0)
    attendance[student] += 1

print("Attendance:", attendance)

# Contrast with get() — setdefault also INSERTS, get() doesn't
d = {"a": 1}
d.setdefault("b", 99)   # inserts "b": 99
d.setdefault("a", 99)   # "a" already exists, doesn't change
print("After setdefault:", d)

# ============================================================
#  copy() — shallow copy
# ============================================================

print("\n=== copy() ===")
grades_backup = grades.copy()
grades_backup["Alice"] = 0   # modify backup
print("Original Alice:", grades["Alice"])       # unchanged
print("Backup Alice  :", grades_backup["Alice"])

# ============================================================
#  clear() — empty the dict
# ============================================================

print("\n=== clear() ===")
temp = {"x": 1, "y": 2}
temp.clear()
print("After clear():", temp)

# ============================================================
#  len(), sorted(), min(), max()  on dicts
# ============================================================

print("\n=== Aggregate Operations ===")
print("Number of students:", len(grades))
print("Highest grade     :", max(grades.values()))
print("Lowest grade      :", min(grades.values()))
print("Average grade     :", round(sum(grades.values()) / len(grades), 2))

# Top student
top = max(grades, key=grades.get)
print(f"Top student       : {top} ({grades[top]})")

# Sorted by grade descending
ranked = sorted(grades.items(), key=lambda x: x[1], reverse=True)
print("\nRankings:")
for rank, (name, score) in enumerate(ranked, 1):
    print(f"  {rank}. {name:<8} {score}")

# ============================================================
#  KEY POINTS
#  keys() / values() / items() → live view objects
#  get(k, default)   → safe retrieval
#  pop(k, default)   → remove & return
#  popitem()         → remove last inserted item
#  update({})        → merge / bulk update
#  setdefault(k, v)  → get or insert default
#  copy()            → shallow copy
#  clear()           → empty the dict
# ============================================================
