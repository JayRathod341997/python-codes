# ─────────────────────────────────────────────
# Exercises — iter() and next()
# ─────────────────────────────────────────────

# ── Exercise 1: Safe queue drain ──────────────
# Real-life: processing a notification queue
# Use next() with a default so the program doesn't crash
# when the queue runs out.

notifications = ["Order shipped", "Payment received", "Review requested"]
nq = iter(notifications)

# --- your code here ---
# Call next(nq, "No more notifications") 4 times and print each result.

# Expected:
# Order shipped
# Payment received
# Review requested
# No more notifications


# ── Exercise 2: Peek and process ──────────────
# Real-life: reading the header row of a CSV separately,
# then processing the data rows.

csv_rows = [
    "name,age,city",
    "Alice,28,Mumbai",
    "Bob,34,Delhi",
    "Carol,22,Pune",
]

# --- your code here ---
# 1. Create an iterator from csv_rows
# 2. Use next() to extract the header row
# 3. Use a for loop on the remaining rows and print each
# 4. Print the header separately too

# Expected:
# Header: name,age,city
# Data: Alice,28,Mumbai
# Data: Bob,34,Delhi
# Data: Carol,22,Pune


# ── Exercise 3: Two-argument iter() ───────────
# Real-life: reading lines from a text stream until a
# blank line (used as a section separator in config files).

import io

config_text = "host=localhost\nport=8080\nmode=debug\n\nextra=ignored\n"
stream = io.StringIO(config_text)

# --- your code here ---
# Use iter(callable, sentinel) to read lines until the empty line.
# Strip newlines. Print each config line.

# Expected:
# host=localhost
# port=8080
# mode=debug


# ── Exercise 4: Simulate a for loop ───────────
# Real-life: understanding how Python iterates internally
# WITHOUT using a for loop, replicate:
#   for word in ["spam", "eggs", "bacon"]:
#       print(word.upper())
# Use only iter(), next(), while, and try/except StopIteration.

words = ["spam", "eggs", "bacon"]

# --- your code here ---

# Expected:
# SPAM
# EGGS
# BACON


# ── Exercise 5: Rolling until condition ───────
# Real-life: a game mechanic — roll until you hit the target
# Use iter(callable, sentinel) to simulate rolling a 6-sided die
# until a 1 comes up. Count and print how many rolls it took.

import random
random.seed(7)

# --- your code here ---
# rolls = list(iter(..., 1))
# print total rolls + the sequence

# Expected output (with seed=7):
# Rolls before hitting 1: [4, 4, 3, 2, 5, 6, 3, 4, 4, 3]
# Total rolls: 10


# ── Exercise 6: Pairwise iteration ────────────
# Real-life: comparing consecutive sensor readings for a spike
# Given a list of temperature readings, use iter() and next()
# to compare each reading with the next one.
# Print a warning if the difference > 1.5 degrees.

temperatures = [36.5, 36.7, 38.3, 38.1, 36.4, 36.6]

# --- your code here ---
# Hint: create one iterator, call next() to get 'prev',
# then loop calling next() for 'curr', compare, then prev = curr

# Expected:
# Spike detected: 36.7 → 38.3  (diff = 1.6)
# Spike detected: 38.1 → 36.4  (diff = 1.7)


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: 4 lines as shown above
# Ex2: header + 3 data lines
# Ex3: 3 config lines
# Ex4: SPAM, EGGS, BACON
# Ex5: ~10 rolls depending on seed
# Ex6: 2 spike warnings
# ─────────────────────────────────────────────
