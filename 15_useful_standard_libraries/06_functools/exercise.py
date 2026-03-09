# ─────────────────────────────────────────────
# Exercises — functools
# ─────────────────────────────────────────────

from functools import reduce, partial, wraps, lru_cache, cache, total_ordering
import time, operator

# ── Exercise 1: reduce — Data Aggregation ────
# Real-life: Analytics engine
# Using ONLY reduce (no sum/min/max/sorted builtins):
#
# Given the sales data, compute:
#   a) Total revenue
#   b) Maximum single sale
#   c) Minimum single sale
#   d) Concatenate all region names into one comma-separated string
#   e) Merge all product dicts into a single dict
#      (later values overwrite earlier ones on conflict)
#
# Print all five results.

sales = [
    {"region": "North", "product": "Laptop",   "revenue": 150000},
    {"region": "South", "product": "Mouse",    "revenue": 8500},
    {"region": "East",  "product": "Keyboard", "revenue": 22000},
    {"region": "West",  "product": "Monitor",  "revenue": 88000},
    {"region": "North", "product": "Webcam",   "revenue": 15000},
]

# --- your code here ---


# ── Exercise 2: partial — Notification System ─
# Real-life: Multi-channel notification service
# Define a generic function:
#   notify(user, channel, message, *, priority="normal", retry=0)
#   that prints: "[PRIORITY | CHANNEL | retry=N] user: message"
#
# Use partial to create:
#   urgent_sms(user, message)   → channel="sms",   priority="urgent", retry=3
#   info_email(user, message)   → channel="email",  priority="low",    retry=0
#   push_alert(user, message)   → channel="push",   priority="high",   retry=1
#
# Also use partial to create:
#   round2(x) = round(x, 2)
#   format_inr(amount) = f"₹{amount:,.2f}"  (partial of a format function)
#
# Test all functions.

# --- your code here ---


# ── Exercise 3: @wraps — Decorator Library ────
# Real-life: A reusable decorator toolkit for a web framework
# Write THREE decorators, each using @wraps:
#
# a) @timer — prints execution time of the function
#    "[TIMER] function_name took 0.0023s"
#
# b) @retry(max_attempts=3, delay=0) — retries the function on Exception
#    Prints attempt number on each failure, raises after max_attempts.
#    (delay is seconds to sleep between retries — use time.sleep)
#
# c) @validate_types(**expected) — checks that kwargs match expected types
#    @validate_types(amount=float, name=str)
#    def process(amount, name): ...
#    Raises TypeError with a clear message on mismatch.
#
# Test each decorator:
#   timer: on a slow function (time.sleep(0.1))
#   retry: on a function that fails 2× then succeeds
#   validate_types: with correct and incorrect types

# --- your code here ---


# ── Exercise 4: lru_cache — Performance ───────
# Real-life: Caching expensive lookups (tax rates, exchange rates, permissions)
#
# a) Write a recursive function count_ways(n) that counts the number
#    of ways to climb n stairs (1 or 2 steps at a time).
#    Without cache: count_ways(35) is slow.
#    Add @lru_cache(maxsize=64). Compare timing with and without.
#
# b) Write @cache on get_tax_rate(country_code) that simulates a slow
#    DB/API call (sleep 0.05s). Show cache hits are instant.
#    Call it 3 times for "IN", 2 times for "US", then print cache_info().
#
# c) Demonstrate the limitation: try calling a cached function with
#    an unhashable argument (like a list) and handle the TypeError.

import time

# --- your code here ---


# ── Exercise 5: total_ordering — Product Sorting ─
# Real-life: E-commerce search — sort by multiple criteria
# Create a class Product with:
#   name, price, rating, stock
#
# Use @total_ordering where ordering is by (rating DESC, price ASC).
# That is: higher rating = better; on equal rating, lower price = better.
#
# Define __eq__ (same rating AND same price) and __lt__ (worse product).
#
# Create 6 products, sort them, and print in ranked order:
#
#   Rank 1: Keyboard   rating=4.8  price=₹2,499
#   Rank 2: Monitor    rating=4.7  price=₹22,000
#   Rank 3: Webcam     rating=4.7  price=₹25,000
#   ...

# --- your code here ---


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: ₹2,83,500 | ₹1,50,000 | ₹8,500 | "North, South, East, West, North"
#      merged dict with all 5 product/region/revenue keys
# Ex2: Formatted notification lines | 1234.57 | ₹12,345.68
# Ex3: Timer output | retry counts then success | type error message
# Ex4: cached fib fast | tax_rate cache_info shows hits | TypeError caught
# Ex5: Products sorted by rating↓, price↑
# ─────────────────────────────────────────────
