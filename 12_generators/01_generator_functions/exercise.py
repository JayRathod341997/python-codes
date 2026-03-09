# ─────────────────────────────────────────────
# Exercises — Generator Functions
# ─────────────────────────────────────────────

# ── Exercise 1: First generator ───────────────
# Real-life: generating ticket numbers at a help desk
# Write a generator function ticket_numbers(start, end) that
# yields integers from start to end (inclusive).
# Use it to print ticket numbers 100 to 105.

# --- your code here ---


# Expected output:
# 100
# 101
# 102
# 103
# 104
# 105


# ── Exercise 2: Infinite ID generator ─────────
# Real-life: auto-incrementing primary keys in a database
# Write a generator function auto_id(prefix="ID") that yields
# "ID_1", "ID_2", "ID_3", ... infinitely.
# Use next() to generate the first 4 IDs.

# --- your code here ---


# Expected output:
# ID_1
# ID_2
# ID_3
# ID_4


# ── Exercise 3: Fibonacci generator ───────────
# Real-life: calculating growth ratios (financial modelling)
# Write a generator function fibonacci() that yields the
# Fibonacci sequence infinitely: 0, 1, 1, 2, 3, 5, 8, ...
# Print the first 10 Fibonacci numbers.

# --- your code here ---


# Expected output:
# 0 1 1 2 3 5 8 13 21 34


# ── Exercise 4: File line filter ──────────────
# Real-life: scanning server logs for errors
# Write a generator function error_lines(lines, keyword) that
# takes a list of log strings and yields only lines containing
# the keyword (case-insensitive).

logs = [
    "INFO  2024-01-10 server started",
    "ERROR 2024-01-10 disk full",
    "INFO  2024-01-10 backup complete",
    "ERROR 2024-01-10 connection refused",
    "WARN  2024-01-10 high memory usage",
    "ERROR 2024-01-10 timeout exceeded",
]

# --- your code here ---
# for line in error_lines(logs, "error"):
#     print(line)


# Expected output:
# ERROR 2024-01-10 disk full
# ERROR 2024-01-10 connection refused
# ERROR 2024-01-10 timeout exceeded


# ── Exercise 5: Batch generator ───────────────
# Real-life: sending emails in batches to avoid rate limits
# Write a generator function in_batches(items, batch_size) that
# yields successive sublists of size batch_size.

emails = [f"user{i}@example.com" for i in range(1, 14)]

# --- your code here ---
# for batch in in_batches(emails, 4):
#     print(f"Sending batch: {batch}")


# Expected output:
# Sending batch: ['user1@example.com', 'user2@example.com', 'user3@example.com', 'user4@example.com']
# Sending batch: ['user5@example.com', 'user6@example.com', 'user7@example.com', 'user8@example.com']
# Sending batch: ['user9@example.com', 'user10@example.com', 'user11@example.com', 'user12@example.com']
# Sending batch: ['user13@example.com']


# ─────────────────────────────────────────────
# Self-check:
# Ex1: 6 ticket numbers printed
# Ex2: ID_1 through ID_4
# Ex3: first 10 fibonacci numbers
# Ex4: 3 error lines
# Ex5: 4 batches (sizes 4, 4, 4, 1)
# ─────────────────────────────────────────────
