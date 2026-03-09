# ─────────────────────────────────────────────
# List Comprehension
# ─────────────────────────────────────────────

# ── Syntax ───────────────────────────────────
# [expression  for  item  in  iterable]
# Short for:
#   result = []
#   for item in iterable:
#       result.append(expression)

# ── Basic example ─────────────────────────────
squares = [x ** 2 for x in range(1, 6)]
print(squares)      # [1, 4, 9, 16, 25]

# ── Real-life 1: Price list with tax ─────────
# E-commerce — add 18% GST to every product price
prices    = [100, 250, 499, 1200, 3000]
with_gst  = [round(p * 1.18, 2) for p in prices]
print(with_gst)     # [118.0, 295.0, 588.82, 1416.0, 3540.0]

# ── Real-life 2: Clean user input ────────────
# Form submission — strip whitespace from every field
raw_inputs = ["  Alice ", "bob@email.com ", "  +91-9876543210"]
cleaned    = [s.strip() for s in raw_inputs]
print(cleaned)      # ['Alice', 'bob@email.com', '+91-9876543210']

# ── Real-life 3: Celsius → Fahrenheit ────────
# Weather app unit conversion
celsius     = [0, 20, 37, 100]
fahrenheit  = [round((c * 9/5) + 32, 1) for c in celsius]
print(fahrenheit)   # [32.0, 68.0, 98.6, 212.0]

# ── Real-life 4: Extract field from records ──
# Database — get only usernames from a list of user dicts
users = [
    {"name": "Alice", "age": 28, "active": True},
    {"name": "Bob",   "age": 34, "active": False},
    {"name": "Carol", "age": 22, "active": True},
]
names = [u["name"] for u in users]
print(names)        # ['Alice', 'Bob', 'Carol']

# ── Real-life 5: String processing ───────────
# Log parser — extract HTTP status codes from log lines
logs = [
    "GET /home 200",
    "POST /login 401",
    "GET /dashboard 200",
    "DELETE /post/5 403",
]
status_codes = [int(line.split()[-1]) for line in logs]
print(status_codes)     # [200, 401, 200, 403]

# ── Equivalent loop (for comparison) ─────────
# The list comprehension:
#   [x**2 for x in range(5)]
# is exactly:
#   result = []
#   for x in range(5):
#       result.append(x**2)

# ── Key points ───────────────────────────────
# • Returns a NEW list — original is untouched
# • Single line, readable, and faster than a manual loop
# • expression can be any valid Python expression
# • iterable can be list, tuple, string, range, dict, set, file…
# • Avoid putting too much logic inside — keep it readable
