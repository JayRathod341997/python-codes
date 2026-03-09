# ─────────────────────────────────────────────
# Exercises — itertools
# ─────────────────────────────────────────────

import itertools
from itertools import (
    count, cycle, chain, islice, groupby,
    accumulate, product, permutations, combinations,
    compress, takewhile, dropwhile
)

# ── Exercise 1: Round-robin Task Scheduler ────
# Real-life: CPU process scheduler / work queue
# You have 3 workers and a stream of tasks.
# Assign tasks to workers in round-robin using cycle().
# Also add an auto-incrementing task ID using count().
#
# tasks = ["parse_csv", "send_email", "resize_image", "generate_report",
#          "backup_db", "send_sms", "update_index"]
#
# Print:
#   Task-1001  parse_csv      → Worker-A
#   Task-1002  send_email     → Worker-B
#   Task-1003  resize_image   → Worker-C
#   Task-1004  generate_report→ Worker-A
#   ...

tasks   = ["parse_csv", "send_email", "resize_image",
           "generate_report", "backup_db", "send_sms", "update_index"]
workers = ["Worker-A", "Worker-B", "Worker-C"]

# --- your code here ---


# ── Exercise 2: Paginated Data Fetcher ────────
# Real-life: API pagination / DB cursor
# Write a function paginate(iterable, page_size) that yields one
# page (list) at a time using islice().
#
# Simulate a large product catalogue (1000 items) and print only
# pages 1, 2, and the last page (page 200).
# Show the first and last item on each page.

def paginate(iterable, page_size):
    pass    # your code here — use islice

def product_stream(n):
    """Yield n fake product dicts."""
    for i in count(1):
        if i > n:
            return
        yield {"id": f"P{i:04d}", "name": f"Product {i}", "price": i * 9.99}

# --- your code here ---


# ── Exercise 3: Sales Report with groupby ─────
# Real-life: Monthly sales breakdown by region/category
# Given the transactions below:
#   a) Group by region, print total sales per region
#   b) Group by category within each region (nested groupby)
#   c) Use accumulate to show running total across all transactions
#      (sort by date first)
#
# Print a formatted report.

transactions = [
    {"date": "2024-01-05", "region": "North", "category": "Electronics", "amount": 15000},
    {"date": "2024-01-07", "region": "South", "category": "Clothing",    "amount": 4500},
    {"date": "2024-01-10", "region": "North", "category": "Clothing",    "amount": 3200},
    {"date": "2024-01-12", "region": "East",  "category": "Electronics", "amount": 8700},
    {"date": "2024-01-15", "region": "South", "category": "Electronics", "amount": 22000},
    {"date": "2024-01-18", "region": "North", "category": "Electronics", "amount": 11500},
    {"date": "2024-01-20", "region": "East",  "category": "Clothing",    "amount": 2100},
    {"date": "2024-01-22", "region": "South", "category": "Clothing",    "amount": 5600},
]

# --- your code here ---


# ── Exercise 4: Combinatorics — Menu Combos ───
# Real-life: Restaurant combo meal builder / A-B test variants
#
# a) Use product() to generate all possible meals:
#    starter = ["Soup", "Salad"]
#    main    = ["Pasta", "Burger", "Rice Bowl"]
#    drink   = ["Juice", "Coffee", "Water"]
#    Print all combos and count them.
#
# b) A team of 10 developers must form pairs for code review.
#    Use combinations() to list all pairs.
#    Print total pair count.
#
# c) A password uses 4 characters from "ABCD" with repetition allowed.
#    Use product("ABCD", repeat=4) to count possibilities.
#    Print first 5 and last 5 passwords.

starter = ["Soup", "Salad"]
main    = ["Pasta", "Burger", "Rice Bowl"]
drink   = ["Juice", "Coffee", "Water"]
devs    = ["Alice","Bob","Carol","Dave","Eve","Frank","Grace","Hank","Ivy","Jay"]

# --- your code here ---


# ── Exercise 5: Feature Flag System (compress) ─
# Real-life: A/B testing and feature rollout
# You have a feature registry and a per-user flag mask.
# Use compress() and takewhile() to:
#   a) Given user flags (list of 0/1), show which features are ON for a user
#   b) Use takewhile() to process log entries only until "CRITICAL" level
#   c) Use dropwhile() to skip the CSV header rows and process data rows

features = [
    "dark_mode", "ai_assistant", "analytics_v2",
    "export_pdf", "live_chat", "beta_dashboard",
    "notification_v3", "offline_mode"
]
user_flags = [1, 0, 1, 1, 0, 0, 1, 1]     # user A's feature access

log_entries = [
    ("INFO",     "Server started"),
    ("DEBUG",    "Config loaded"),
    ("INFO",     "Listening on :8080"),
    ("WARNING",  "Slow query detected"),
    ("CRITICAL", "DB connection lost"),
    ("INFO",     "Retrying connection"),
]

csv_lines = [
    "# Auto-generated report",
    "# Date: 2024-01-15",
    "name,score,grade",           # ← actual data starts here
    "Alice,91,A",
    "Bob,55,C",
    "Carol,78,B",
]

# --- your code here ---


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: Task-1001..1007 assigned round-robin to workers
# Ex2: First item of pages 1, 2 and last page shown
# Ex3: Regional totals, nested category breakdown, running total
# Ex4: a) 18 combos | b) 45 pairs | c) 256 passwords, first/last 5
# Ex5: Active features for user | log before CRITICAL | CSV data rows
# ─────────────────────────────────────────────
