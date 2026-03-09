# ─────────────────────────────────────────────
# Functions — Built-in Functional Tools
# ─────────────────────────────────────────────

from functools import reduce

# ── 1. map() ─────────────────────────────────
# Apply a function to every item in an iterable.
# Returns a map object (lazy iterator) — wrap in list() to materialise.
#
# Syntax: map(function, iterable)

# Real-life: Convert product prices from USD to INR
usd_prices = [9.99, 19.99, 4.49, 14.99, 7.99]
usd_to_inr = lambda p: round(p * 83.5, 2)

inr_prices = list(map(usd_to_inr, usd_prices))
print("INR prices:", inr_prices)
# [834.17, 1669.17, 374.92, 1251.67, 667.17]

# Real-life: Normalise usernames from a sign-up form
raw_names = ["  alice ", "BOB", "Charlie  ", "  dave"]
clean_names = list(map(str.strip, map(str.lower, raw_names)))
print("Clean names:", clean_names)
# ['alice', 'bob', 'charlie', 'dave']

# map() with a named function
def apply_gst(price, rate=18):
    return round(price * (1 + rate / 100), 2)

menu_prices = [120, 250, 80, 340]
gst_prices  = list(map(apply_gst, menu_prices))
print("After GST:", gst_prices)

# map() over multiple iterables (stops at shortest)
quantities = [2, 3, 1, 4]
line_totals = list(map(lambda q, p: q * p, quantities, menu_prices))
print("Line totals:", line_totals)


# ── 2. filter() ──────────────────────────────
# Keep only items for which function returns True.
# Returns a filter object (lazy iterator).
#
# Syntax: filter(function, iterable)

# Real-life: Show only in-stock products
inventory = [
    {"name": "Laptop",  "stock": 0},
    {"name": "Mouse",   "stock": 15},
    {"name": "Keyboard","stock": 0},
    {"name": "Monitor", "stock": 4},
    {"name": "Webcam",  "stock": 9},
]

in_stock = list(filter(lambda p: p["stock"] > 0, inventory))
print("In stock:")
for p in in_stock:
    print(f"  {p['name']:12s} — {p['stock']} units")

# Real-life: Filter valid email addresses
emails = ["user@gmail.com", "bad-email", "admin@corp.in", "noreply", "dev@x.io"]
valid_emails = list(filter(lambda e: "@" in e and "." in e.split("@")[-1], emails))
print("Valid emails:", valid_emails)

# filter() with None — removes all falsy values
raw_data = [0, "hello", None, 42, "", False, 3.14, [], "world"]
truthy   = list(filter(None, raw_data))
print("Truthy values:", truthy)
# ['hello', 42, 3.14, 'world']


# ── 3. reduce() ──────────────────────────────
# Cumulatively apply a function to collapse an iterable to ONE value.
# Lives in functools — not a built-in since Python 3.
#
# Syntax: reduce(function, iterable[, initializer])

# How it works:
#   reduce(f, [a, b, c, d]) == f(f(f(a, b), c), d)

# Real-life: Total cart value
cart = [499, 1299, 799, 249, 1099]
total = reduce(lambda acc, price: acc + price, cart)
print(f"Cart total: ₹{total}")          # ₹3945

# Real-life: Find the largest transaction from a day's log
transactions = [2300, 8750, 450, 12000, 6800, 3200]
largest = reduce(lambda a, b: a if a > b else b, transactions)
print(f"Largest transaction: ₹{largest}")   # ₹12000

# Real-life: Build a sentence from words (log aggregation)
log_parts = ["[ERROR]", "2024-01-15", "DB", "connection", "refused"]
message   = reduce(lambda a, b: a + " " + b, log_parts)
print(message)      # [ERROR] 2024-01-15 DB connection refused

# reduce() with initializer — useful to start with a base value
orders = [150, 300, 200, 450]
total_with_service = reduce(lambda acc, o: acc + o, orders, 100)   # ₹100 base charge
print(f"Total with service fee: ₹{total_with_service}")            # ₹1200


# ── Combining map + filter + reduce ──────────
# Real-life: Sales report — total revenue from completed orders only

orders_data = [
    {"id": 1, "status": "completed", "amount": 1500},
    {"id": 2, "status": "cancelled", "amount": 800},
    {"id": 3, "status": "completed", "amount": 3200},
    {"id": 4, "status": "pending",   "amount": 950},
    {"id": 5, "status": "completed", "amount": 2100},
]

revenue = reduce(
    lambda acc, amt: acc + amt,
    map(
        lambda o: o["amount"],
        filter(lambda o: o["status"] == "completed", orders_data)
    ),
    0
)
print(f"Total revenue (completed): ₹{revenue}")    # ₹6800

# Same pipeline — step by step for clarity
completed = filter(lambda o: o["status"] == "completed", orders_data)
amounts   = map(lambda o: o["amount"], completed)
total_rev = reduce(lambda acc, a: acc + a, amounts, 0)
print(f"Revenue (step-by-step): ₹{total_rev}")


# ── map / filter vs list comprehensions ──────
# Both are valid; list comprehensions are often more readable in Python.
# map/filter shine when passing pre-defined functions or chaining.

prices = [100, 250, 80, 500, 320]

# Using map + filter
discounted_map = list(map(lambda p: p * 0.9,
                          filter(lambda p: p >= 100, prices)))

# Using list comprehension (equivalent)
discounted_comp = [p * 0.9 for p in prices if p >= 100]

print(discounted_map)
print(discounted_comp)  # identical output


# ── Key points ────────────────────────────────
# • map()    → transform every element  (1-to-1)
# • filter() → keep elements that pass a test (subset)
# • reduce() → collapse all elements to a single value (N-to-1)
# • All three return lazy iterators; wrap in list() to evaluate
# • reduce() needs: from functools import reduce
# • Combine them for expressive data processing pipelines
