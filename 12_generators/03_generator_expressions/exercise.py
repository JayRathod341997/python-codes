# ─────────────────────────────────────────────
# Exercises — Generator Expressions
# ─────────────────────────────────────────────

# ── Exercise 1: Memory comparison ─────────────
# Real-life: choosing the right tool for a large dataset
# For n = 500_000, create both a list comprehension and a
# generator expression of cubes (n ** 3).
# Print the size in bytes of each using sys.getsizeof().

import sys

n = 500_000

# --- your code here ---


# Expected output (approximate):
# List size:  ~4,000,056 bytes
# Gen size  :        208 bytes


# ── Exercise 2: Total revenue ─────────────────
# Real-life: daily revenue report from an order system
# Use a generator expression inside sum() to calculate total
# revenue. Revenue per order = price * quantity.

orders = [
    {"product": "Laptop",   "price": 999.99, "qty": 3},
    {"product": "Mouse",    "price":  29.99, "qty": 10},
    {"product": "Monitor",  "price": 349.99, "qty": 5},
    {"product": "Keyboard", "price":  79.99, "qty": 8},
]

# --- your code here ---
# total_revenue = sum(...)
# print(f"Total revenue: ${total_revenue:,.2f}")


# Expected output:
# Total revenue: $4,989.57


# ── Exercise 3: Filter + transform chain ──────
# Real-life: cleaning up a user database export
# Given raw_users below, use a chained generator expression to:
#   1. Strip whitespace from each name
#   2. Keep only names longer than 3 characters
#   3. Convert to UPPERCASE
# Collect results into a list and print.

raw_users = ["  ali", "Bob  ", " Jo", "carol ", "  ed", "DIANA  ", "frank"]

# --- your code here ---


# Expected output:
# ['BOB', 'CAROL', 'DIANA', 'FRANK']


# ── Exercise 4: any() / all() short-circuit ───
# Real-life: security check before processing a batch
# Given a list of uploaded file sizes (in MB), use generator
# expressions to answer:
#   a) Does any file exceed 100 MB?  (flag for manual review)
#   b) Are all files above 0 MB?     (none are empty/corrupt)

file_sizes_mb = [12.5, 0.8, 45.0, 130.2, 22.1, 0.0, 88.4]

# --- your code here ---


# Expected output:
# Any file > 100 MB: True
# All files > 0 MB : False


# ── Exercise 5: CSV column extractor ──────────
# Real-life: reading a specific column from a large CSV
# Given csv_lines, use a generator expression to extract
# the "score" column (index 2, 0-based) as integers,
# filtering out the header row and any row with score < 60.
# Print the passing scores and their count.

csv_lines = [
    "name,subject,score",
    "Alice,Math,88",
    "Bob,Math,52",
    "Carol,Math,76",
    "Dave,Math,45",
    "Eve,Math,91",
    "Frank,Math,60",
]

# --- your code here ---


# Expected output:
# Passing scores: [88, 76, 91, 60]
# Count: 4


# ── Exercise 6: Lazy log scanner ──────────────
# Real-life: real-time anomaly detection on a log stream
# Given the log_stream below, use a single generator expression
# to extract only the numeric status codes (as ints) from lines
# that start with "RESPONSE". Then use max() to find the
# highest status code without building any intermediate list.
#
# Log format: "RESPONSE <status_code> <endpoint>"

log_stream = [
    "REQUEST  GET /api/users",
    "RESPONSE 200 /api/users",
    "REQUEST  POST /api/orders",
    "RESPONSE 422 /api/orders",
    "REQUEST  DELETE /api/item/5",
    "RESPONSE 404 /api/item/5",
    "REQUEST  GET /api/health",
    "RESPONSE 200 /api/health",
    "RESPONSE 500 /api/crash",
]

# --- your code here ---
# highest = max(...)
# print(f"Highest status code: {highest}")


# Expected output:
# Highest status code: 500


# ─────────────────────────────────────────────
# Self-check:
# Ex1: gen is ~200 bytes vs list ~4 MB
# Ex2: $4,989.57
# Ex3: ['BOB', 'CAROL', 'DIANA', 'FRANK']
# Ex4: True, False
# Ex5: [88, 76, 91, 60], count 4
# Ex6: 500
# ─────────────────────────────────────────────
