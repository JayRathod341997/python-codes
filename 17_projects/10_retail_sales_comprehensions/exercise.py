# ───────────────────────────────────────────────────────────────
# Exercises — Project 10: Comprehensions
# ───────────────────────────────────────────────────────────────

# ── Exercise 1: Filter Clothing and Compute Total Revenue ─────────
# Task: Using comprehensions, filter all Clothing transactions and
#       compute total revenue.
#
# Requirements:
#   - Use list/dict comprehension
#   - Filter category == "Clothing"
#   - Calculate revenue = qty * price for each
#   - Sum total revenue
#   - Print results
#
# Hint: List comprehension for filtering, sum() for totaling.

# --- your code here ---




# ── Exercise 2: Revenue by Salesperson (Dict Comprehension) ────────
# Task: Create a dict mapping each salesperson to their total revenue.
#       Use dict comprehension.
#
# Requirements:
#   - Extract unique salespersons
#   - For each, sum their transaction revenues
#   - Use dict comprehension (one-liner if possible)
#   - Sort by revenue (highest first)
#
# Hint: Nested generator expression inside dict comprehension.

# --- your code here ---




# ── Exercise 3: Multi-level Grouping (Nested Comprehension) ───────
# Task: Create nested dict: region → category → total_revenue
#       Using nested dict comprehension.
#
# Requirements:
#   - Outer dict: region as key
#   - Inner dict: category → revenue
#   - Use nested comprehensions
#   - Display result nicely
#
# Hint: Double-nested dict comprehension with sum() inside.

# --- your code here ---




# ───────────────────────────────────────────────────────────────
# Expected outputs (for self-check):
#
# Ex1: Clothing revenue (comprehension)
#      Filter result: 5+ transactions
#      Total: ₹5000+
#
# Ex2: Revenue by salesperson dict
#      Arun: ₹45000
#      Bhavna: ₹30000
#      etc.
#
# Ex3: Nested region-category revenue
#      North:
#        Electronics: ₹80000
#        Food: ₹1500
#      etc.
# ───────────────────────────────────────────────────────────────
