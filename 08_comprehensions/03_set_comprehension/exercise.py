# ─────────────────────────────────────────────
# Exercises — Set Comprehension
# ─────────────────────────────────────────────

# ── Exercise 1: Unique Cities ─────────────────
# Real-life: CRM deduplication
# Extract a set of unique cities from the customer list.

customers = [
    {"name": "Alice",   "city": "Mumbai"},
    {"name": "Bob",     "city": "Delhi"},
    {"name": "Carol",   "city": "Mumbai"},
    {"name": "Dave",    "city": "Pune"},
    {"name": "Eve",     "city": "Delhi"},
]

# --- your code here ---


# ── Exercise 2: Unique Error Codes ───────────
# Real-life: Application monitoring
# A log has many repeated error codes. Extract a sorted list of unique codes.

error_log = [500, 404, 200, 500, 403, 404, 200, 500, 301, 403]

# --- your code here ---
# Hint: use sorted() on the set comprehension result


# ── Exercise 3: Common Enrolled Courses ───────
# Real-life: LMS (Learning Management System)
# Find courses that BOTH students are enrolled in (intersection).

alice_courses = ["Python", "Data Science", "Web Dev", "SQL"]
bob_courses   = ["Java",   "Data Science", "SQL",     "DevOps"]

# --- your code here ---
# Hint: build two sets using set comprehension, then use &


# ── Exercise 4: Unique Word Roots ─────────────
# Real-life: Basic text normalisation
# Convert all words to lowercase and collect unique ones.

text = "Python is great and python is easy and PYTHON is powerful"

# --- your code here ---


# ── Exercise 5: Distinct Product Categories ───
# Real-life: Inventory analytics
# Extract a set of unique categories from the product list.

inventory = [
    {"product": "Laptop",   "category": "Electronics"},
    {"product": "Pen",      "category": "Stationery"},
    {"product": "Phone",    "category": "Electronics"},
    {"product": "Notebook", "category": "Stationery"},
    {"product": "Tablet",   "category": "Electronics"},
    {"product": "Desk",     "category": "Furniture"},
]

# --- your code here ---


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: {'Mumbai', 'Delhi', 'Pune'}  (any order)
# Ex2: [200, 301, 403, 404, 500]
# Ex3: {'Data Science', 'SQL'}  (any order)
# Ex4: {'python', 'is', 'great', 'and', 'easy', 'powerful'}  (any order)
# Ex5: {'Electronics', 'Stationery', 'Furniture'}  (any order)
# ─────────────────────────────────────────────
