# ============================================================
#  LIST COPYING — Shallow vs Deep Copy
#  Real-world context: School timetable scheduling system
# ============================================================

import copy

# ============================================================
#  THE PROBLEM: Direct Assignment is NOT a copy
# ============================================================

print("=== Direct Assignment (NOT a copy) ===")

monday_schedule = ["Math", "English", "Science", "PE"]
tuesday_schedule = monday_schedule   # SAME object, not a copy!

tuesday_schedule[2] = "Art"   # intend to change only Tuesday
print("Monday :", monday_schedule)    # Monday also changed! BUG
print("Tuesday:", tuesday_schedule)
print("Same object?", monday_schedule is tuesday_schedule)

# ============================================================
#  SHALLOW COPY — Three ways
# ============================================================

print("\n=== Shallow Copy ===")

monday_schedule = ["Math", "English", "Science", "PE"]

# Method 1: .copy()
tue1 = monday_schedule.copy()

# Method 2: list()
tue2 = list(monday_schedule)

# Method 3: slicing
tue3 = monday_schedule[:]

tue1[2] = "Art"
tue2[0] = "History"
tue3[3] = "Music"

print("Monday (unchanged):", monday_schedule)
print("Tuesday (copy)    :", tue1)
print("Tuesday (list())  :", tue2)
print("Tuesday (slice)   :", tue3)

# ============================================================
#  SHALLOW COPY LIMITATION with nested lists
# ============================================================

print("\n=== Shallow Copy Limitation ===")

# Each week has [Monday, Tuesday, Wednesday] schedules
week1 = [["Math", "PE"], ["English", "Art"], ["Science", "Music"]]
week2 = week1.copy()      # shallow copy

# Modifying a NESTED list affects BOTH
week2[0][0] = "CHANGED"
print("Week1 after modifying week2[0][0]:", week1)   # Also changed!
print("Week2                            :", week2)

# ============================================================
#  DEEP COPY — copies everything recursively
# ============================================================

print("\n=== Deep Copy ===")

week1 = [["Math", "PE"], ["English", "Art"], ["Science", "Music"]]
week2 = copy.deepcopy(week1)

week2[0][0] = "CHANGED"
print("Week1 (unaffected):", week1)
print("Week2             :", week2)

# ============================================================
#  PRACTICAL SUMMARY TABLE
# ============================================================

print("\n=== When to Use What ===")

summary = [
    ["Method",          "Syntax",                "New obj?", "Nested safe?"],
    ["Assignment",      "b = a",                 "No",       "No"         ],
    ["copy()",          "b = a.copy()",           "Yes",      "No"         ],
    ["list()",          "b = list(a)",            "Yes",      "No"         ],
    ["Slice",           "b = a[:]",               "Yes",      "No"         ],
    ["deepcopy()",      "b = copy.deepcopy(a)",   "Yes",      "Yes"        ],
]

col_widths = [14, 26, 10, 12]
for row in summary:
    print(" | ".join(str(v).ljust(w) for v, w in zip(row, col_widths)))

# ============================================================
#  KEY POINTS
#  - a = b        → same object (not a copy)
#  - .copy(), list(), [:] → shallow copy (safe for flat lists)
#  - copy.deepcopy() → full independent copy (safe for nested)
# ============================================================
