# ─────────────────────────────────────────────
# Exercises — Lazy Evaluation
# ─────────────────────────────────────────────

# ── Exercise 1: Infinite counter with step ────
# Real-life: generating timestamps at fixed intervals
# Write a generator count_by(start, step) that yields values
# starting at 'start', incrementing by 'step' each time (infinite).
# Use it to get the first 6 multiples of 7.

# --- your code here ---


# Expected output:
# [7, 14, 21, 28, 35, 42]


# ── Exercise 2: Lazy vs eager timing ──────────
# Real-life: choosing whether to pre-compute or stream results
# Define heavy(n) that sleeps 0.005s then returns n*n.
# Compare time-to-first-value between:
#   a) building a list of heavy(i) for i in range(20)
#   b) creating a generator of heavy(i) for i in range(20)
# Print time-to-first-value for each approach.

import time

def heavy(n):
    time.sleep(0.005)
    return n * n

# --- your code here ---


# Expected output (approximate):
# Eager  time-to-first: 0.100s
# Lazy   time-to-first: 0.005s


# ── Exercise 3: take() utility ────────────────
# Real-life: paginating results from an infinite stream
# Write a generator take(n, iterable) that yields only the
# first n items from any iterable (including infinite ones).
# Test it by taking the first 8 even numbers from an infinite
# even number generator.

def even_numbers():
    n = 0
    while True:
        yield n
        n += 2

# --- your code here ---
# def take(n, iterable): ...
# print(list(take(8, even_numbers())))


# Expected output:
# [0, 2, 4, 6, 8, 10, 12, 14]


# ── Exercise 4: Short-circuit search ──────────
# Real-life: fraud detection — find the first fraudulent transaction
# Write a generator suspicious_transactions(records) that yields
# a transaction only if amount > 10_000 OR country == "BLOCKED".
# Use next() to get only the FIRST suspicious one without
# scanning the whole list.

transactions = [
    {"id": 1,  "amount": 250,    "country": "US"},
    {"id": 2,  "amount": 8500,   "country": "UK"},
    {"id": 3,  "amount": 150,    "country": "BLOCKED"},
    {"id": 4,  "amount": 15000,  "country": "DE"},
    {"id": 5,  "amount": 99,     "country": "US"},
]

# --- your code here ---


# Expected output:
# First suspicious: {'id': 3, 'amount': 150, 'country': 'BLOCKED'}


# ── Exercise 5: Lazy file line counter ────────
# Real-life: counting lines in a huge log without loading it all
# Simulate a "file" as an iterator of lines (lines_source below).
# Write a generator non_empty_lines(source) that yields only
# lines that are not blank (after stripping).
# Count how many non-empty lines there are using sum() +
# a generator expression — never building a list.

lines_source = iter([
    "Server started\n",
    "\n",
    "Connection accepted\n",
    "  \n",
    "Request received\n",
    "\n",
    "Response sent\n",
    "Connection closed\n",
    "\n",
])

# --- your code here ---


# Expected output:
# Non-empty lines: 5


# ── Exercise 6: Infinite Fibonacci with cutoff ─
# Real-life: financial model — find first Fibonacci number
# that exceeds a given portfolio value
# Write an infinite Fibonacci generator.
# Then use a generator expression + next() to find the
# first Fibonacci number greater than 1000.

# --- your code here ---


# Expected output:
# First Fibonacci > 1000: 1597


# ─────────────────────────────────────────────
# Self-check:
# Ex1: [7, 14, 21, 28, 35, 42]
# Ex2: lazy is ~20x faster to first value
# Ex3: [0, 2, 4, 6, 8, 10, 12, 14]
# Ex4: id=3 (BLOCKED country, not id=4)
# Ex5: 5 non-empty lines
# Ex6: 1597
# ─────────────────────────────────────────────
