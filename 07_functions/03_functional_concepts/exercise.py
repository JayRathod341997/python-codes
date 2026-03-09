# ─────────────────────────────────────────────
# Exercises — Functional Concepts
# ─────────────────────────────────────────────

# ── Exercise 1: Lambda Sorting ────────────────
# Real-life: E-commerce product listing
# Given the list below, use lambda + sorted() to produce:
#   a) products sorted by price ascending
#   b) products sorted by rating descending
#   c) products sorted by name alphabetically
# Print each sorted list (just product names + the sort value).

products = [
    {"name": "Wireless Mouse",  "price": 799,  "rating": 4.3},
    {"name": "Mechanical KB",   "price": 3499, "rating": 4.7},
    {"name": "USB Hub",         "price": 499,  "rating": 4.1},
    {"name": "Monitor Stand",   "price": 1299, "rating": 4.5},
    {"name": "Webcam HD",       "price": 2199, "rating": 4.2},
]

# --- your code here ---


# ── Exercise 2: Function Factory — Tax Calculator
# Real-life: Multi-country tax system
# Write a function make_tax_calculator(rate, currency="₹")
# that returns a function calculate(amount) → prints:
#
#   Amount : ₹10,000.00
#   Tax 18%: ₹1,800.00
#   Total  : ₹11,800.00
#
# Create calculators for: India GST 18%, UK VAT 20%, US Sales Tax 8.5%
# Call each with 10,000 units of their currency.

# --- your code here ---


# ── Exercise 3: Retry Closure ─────────────────
# Real-life: Network request with retry limit
# Write make_retry(max_attempts) that returns a function
# attempt(success=False) which:
#   - Tracks how many times it has been called (closure variable)
#   - If success=True  → prints "Success on attempt N" and resets count
#   - If success=False → prints "Attempt N failed (X left)"
#                        where X = remaining attempts
#   - If max_attempts exhausted → prints "Max retries reached. Aborting."
#                                  and does nothing further
#
# Test:
#   retry = make_retry(3)
#   retry()            # Attempt 1 failed (2 left)
#   retry()            # Attempt 2 failed (1 left)
#   retry(success=True)# Success on attempt 3
#   retry()            # Attempt 1 failed (2 left)  ← reset after success

# --- your code here ---


# ── Exercise 4: Higher-order — Pipeline ───────
# Real-life: Data processing pipeline (ETL)
# Write a function pipeline(data, *transforms) that applies
# each transform function to the data in sequence and returns
# the final result.
#
# Create these transform functions:
#   strip_spaces(s)    → s.strip()
#   to_uppercase(s)    → s.upper()
#   remove_dots(s)     → s.replace(".", "")
#   add_prefix(s)      → "ID_" + s
#
# Then run:
#   pipeline("  abc.def.ghi  ", strip_spaces, to_uppercase, remove_dots, add_prefix)
# Expected: "ID_ABCDEFGHI"

# --- your code here ---


# ── Exercise 5: Memoization Closure ──────────
# Real-life: Caching expensive API/DB calls
# Write a function memoize(func) — a higher-order function that
# wraps func and caches its results in a dict keyed by arguments.
# On a cache hit it prints "[CACHE HIT]" and returns stored result.
# On a cache miss it prints "[COMPUTING]", calls func, stores & returns result.
#
# Test with a slow fibonacci (use time.sleep(0.1) to simulate cost):
#   def slow_square(n):
#       time.sleep(0.1)
#       return n * n
#
#   fast_square = memoize(slow_square)
#   fast_square(5)   → [COMPUTING]  25
#   fast_square(5)   → [CACHE HIT]  25
#   fast_square(9)   → [COMPUTING]  81
#   fast_square(5)   → [CACHE HIT]  25

import time

# --- your code here ---


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: Three sorted lists printed
# Ex2: Three formatted tax summaries
# Ex3: Attempt 1 failed (2 left) / Attempt 2 failed (1 left) /
#      Success on attempt 3 / Attempt 1 failed (2 left)
# Ex4: ID_ABCDEFGHI
# Ex5: [COMPUTING] then [CACHE HIT] on repeated calls
# ─────────────────────────────────────────────
