# ─────────────────────────────────────────────
# Exercises — Iterable vs Iterator
# ─────────────────────────────────────────────
from collections.abc import Iterable, Iterator

# ── Exercise 1: Classification ────────────────
# Real-life: debugging a "object is not iterable" error
# For each object below, print whether it is an Iterable,
# an Iterator, both, or neither.

objects = [
    [1, 2, 3],          # list
    iter([1, 2, 3]),    # list_iterator
    "hello",            # str
    42,                 # int
    range(5),           # range
    (x for x in []),   # generator
]

# --- your code here ---


# Expected output format:
# [1, 2, 3]          → Iterable: True  | Iterator: False
# <list_iterator>    → Iterable: True  | Iterator: True
# hello              → Iterable: True  | Iterator: False
# 42                 → Iterable: False | Iterator: False
# range(0, 5)        → Iterable: True  | Iterator: False
# <generator>        → Iterable: True  | Iterator: True


# ── Exercise 2: One-shot vs reusable ──────────
# Real-life: processing a task queue
# Demonstrate that a list can be iterated multiple times
# but an iterator can only be consumed once.

tasks = ["send_email", "generate_report", "backup_db"]

# --- your code here ---
# 1. Iterate tasks with a for loop — print each task
# 2. Iterate tasks AGAIN — confirm it still works (print each)
# 3. Create an iterator from tasks
# 4. Iterate the iterator with a for loop — print each task
# 5. Iterate the SAME iterator again — show it prints nothing


# ── Exercise 3: Independent iterators ─────────
# Real-life: two workers processing the same product list
# Create two independent iterators from the same list.
# Advance it1 twice, then show it2 still starts at the beginning.

products = ["laptop", "mouse", "keyboard", "monitor"]

# --- your code here ---
# it1 = ...
# it2 = ...
# advance it1 twice (use next())
# print next(it2) → should print "laptop"


# ── Exercise 4: Manual for loop ───────────────
# Real-life: understanding what Python's 'for' loop does internally
# Replicate the behavior of:
#   for item in [10, 20, 30]:
#       print(item)
# Using ONLY iter() and next() inside a while loop.

data = [10, 20, 30]

# --- your code here ---
# Hint: catch StopIteration to know when to stop


# ── Exercise 5: Exhaustion check ──────────────
# Real-life: reading a sensor stream exactly once
# A batch of temperature readings is delivered as an iterator.
# Read all readings and compute the average.
# Then try to iterate again and show nothing is returned.

readings_iter = iter([36.5, 37.1, 36.8, 38.2, 37.5])

# --- your code here ---
# Collect all values using next() in a loop into a list
# Compute and print the average
# Then use a for loop on readings_iter — show it's exhausted

# Expected average: 37.22


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex2: tasks prints 3 items, then 3 items again; iterator prints 3 then 0
# Ex3: next(it2) → "laptop"  (independent of it1)
# Ex4: prints 10, 20, 30
# Ex5: average = 37.22, second loop prints nothing
# ─────────────────────────────────────────────
