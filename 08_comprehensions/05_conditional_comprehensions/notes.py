# ─────────────────────────────────────────────
# Conditional Comprehensions
# ─────────────────────────────────────────────

# Two distinct uses of conditions in comprehensions:
#   1. FILTER  — if at the END     → [expr for x in it if condition]
#   2. TERNARY — if in EXPRESSION  → [a if cond else b for x in it]

# ── 1. Filter (if at the end) ─────────────────
# Keep only items that satisfy a condition
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)    # [2, 4, 6, 8, 10]

# ── Real-life 1: Active users only ───────────
# User management — filter out deactivated accounts
users = [
    {"name": "Alice",   "active": True},
    {"name": "Bob",     "active": False},
    {"name": "Carol",   "active": True},
    {"name": "Dave",    "active": False},
]
active_names = [u["name"] for u in users if u["active"]]
print(active_names)     # ['Alice', 'Carol']

# ── Real-life 2: Out-of-stock filter ──────────
# E-commerce — skip products with zero stock
inventory = [
    {"name": "Laptop",   "stock": 0},
    {"name": "Mouse",    "stock": 45},
    {"name": "Monitor",  "stock": 0},
    {"name": "Keyboard", "stock": 12},
]
available = [p["name"] for p in inventory if p["stock"] > 0]
print(available)        # ['Mouse', 'Keyboard']

# ── 2. Ternary (if-else in expression) ────────
# Transform every item — no filtering, just mapping with a condition
labels = ["pass" if score >= 50 else "fail" for score in [80, 45, 60, 30, 95]]
print(labels)   # ['pass', 'fail', 'pass', 'fail', 'pass']

# ── Real-life 3: Stock status badges ─────────
# Dashboard UI — assign a badge colour per stock level
products = [
    {"name": "Pen",    "stock": 3},
    {"name": "Ruler",  "stock": 50},
    {"name": "Eraser", "stock": 0},
]
badges = [
    {"name": p["name"],
     "badge": "red" if p["stock"] == 0 else "orange" if p["stock"] < 10 else "green"}
    for p in products
]
for b in badges:
    print(b)
# {'name': 'Pen',    'badge': 'orange'}
# {'name': 'Ruler',  'badge': 'green'}
# {'name': 'Eraser', 'badge': 'red'}

# ── Real-life 4: Email validation quick-check ─
# Sign-up form — mark each address valid/invalid
emails = ["alice@gmail.com", "bob-at-mail", "carol@yahoo.com", "nodomain"]
validated = [e if "@" in e else f"INVALID: {e}" for e in emails]
print(validated)
# ['alice@gmail.com', 'INVALID: bob-at-mail', 'carol@yahoo.com', 'INVALID: nodomain']

# ── Combining both filter + ternary ───────────
# Filter adults and then label them by age group
people = [
    {"name": "Alice", "age": 17},
    {"name": "Bob",   "age": 25},
    {"name": "Carol", "age": 34},
    {"name": "Dave",  "age": 15},
    {"name": "Eve",   "age": 62},
]
adult_groups = [
    f"{p['name']} ({'senior' if p['age'] >= 60 else 'adult'})"
    for p in people if p["age"] >= 18
]
print(adult_groups)     # ['Bob (adult)', 'Carol (adult)', 'Eve (senior)']

# ── Real-life 5: Transaction categoriser ──────
# Finance — label transactions as credit/debit
transactions = [500, -200, 1500, -800, 300, -50]
labelled = [f"+{t}" if t > 0 else str(t) for t in transactions]
print(labelled)     # ['+500', '-200', '+1500', '-800', '+300', '-50']

# ── Key points ───────────────────────────────
# • FILTER   : [x for x in it if cond]        — shrinks the list
# • TERNARY  : [a if c else b for x in it]    — keeps same length, maps values
# • BOTH     : [a if c else b for x in it if cond2] — filter, then transform
# • No else  → must go at the END as a filter
# • With else → must go at the FRONT as part of the expression
# • Avoid chaining more than two conditions — extract to a function
