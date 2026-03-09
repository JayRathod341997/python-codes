# ─────────────────────────────────────────────
# iter() and next()
# ─────────────────────────────────────────────

# ── iter() ───────────────────────────────────
# iter(iterable)       → calls iterable.__iter__(), returns an iterator
# iter(callable, sentinel) → calls callable() until it returns sentinel value

# ── next() ───────────────────────────────────
# next(iterator)              → calls iterator.__next__()
# next(iterator, default)     → returns default instead of raising StopIteration

# ── Basic usage ──────────────────────────────
colors = ["red", "green", "blue"]
it = iter(colors)

print(next(it))         # red
print(next(it))         # green
print(next(it))         # blue
# next(it)              # StopIteration

# ── next() with default ───────────────────────
# Real-life: safely peek at a queue — don't crash if it's empty
queue = iter([])
item  = next(queue, "EMPTY")
print(item)             # EMPTY  (no StopIteration raised)

notifications = iter(["You have 1 new message"])
msg = next(notifications, "No new notifications")
print(msg)              # You have 1 new message

# ── iter() two-argument form ──────────────────
# iter(callable, sentinel)
# Calls callable() repeatedly; stops when the return value == sentinel.
# Real-life 1: reading lines from a simulated stream until empty string

import io
stream = io.StringIO("line1\nline2\nline3\n")

# readline() returns "" at end-of-file
for line in iter(stream.readline, ""):
    print(line.strip())
# line1
# line2
# line3

# Real-life 2: rolling a die until you get a 6
import random
random.seed(42)

rolls = list(iter(lambda: random.randint(1, 6), 6))
print(rolls)            # e.g. [1, 5, 5, 2, ...] — all rolls before first 6

# ── Manually simulating a for loop ───────────
# Python's 'for item in iterable:' is exactly:
#
#   _it = iter(iterable)
#   while True:
#       try:
#           item = next(_it)
#           <loop body>
#       except StopIteration:
#           break

items = [10, 20, 30]
_it = iter(items)
while True:
    try:
        item = next(_it)
        print(item)     # 10, 20, 30
    except StopIteration:
        break

# ── Real-life 1: Processing a data pipeline step ──
# Imagine reading records from a database cursor one by one.

class FakeDBCursor:
    def __init__(self, rows):
        self._rows = iter(rows)

    def fetchone(self):
        return next(self._rows, None)

cursor = FakeDBCursor([
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
])

while (row := cursor.fetchone()) is not None:
    print(row)
# {'id': 1, 'name': 'Alice'}
# {'id': 2, 'name': 'Bob'}

# ── Real-life 2: Peeking ahead in a stream ────
# Read the first item to inspect, then continue iterating the rest.

prices = [299, 499, 149, 999, 59]
price_iter = iter(prices)

first_price = next(price_iter)
print(f"First item costs ₹{first_price}")   # First item costs ₹299

print("Remaining prices:")
for p in price_iter:                         # continues from 499 onwards
    print(f"  ₹{p}")

# ── Key points ───────────────────────────────
# • iter() converts any iterable into an iterator
# • next() advances the iterator by one step
# • next(it, default) is the safe version — no crash on exhaustion
# • iter(callable, sentinel) is great for reading streams until a stop marker
# • Behind the scenes, every 'for' loop is iter() + next()
