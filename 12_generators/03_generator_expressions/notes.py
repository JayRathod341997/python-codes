# ─────────────────────────────────────────────
# Generator Expressions
# ─────────────────────────────────────────────

# ── What is a generator expression? ──────────
#
# A generator expression is a one-line shorthand for a simple
# generator function. Syntax is identical to a list
# comprehension, but uses () instead of [].
#
#   List comprehension:   [expr for item in iterable if cond]
#   Generator expression: (expr for item in iterable if cond)
#
# The key difference: list comp builds the entire list NOW.
# Generator expression produces values LAZILY, one at a time.

import sys

# ── Side-by-side comparison ───────────────────

numbers = range(1, 1_000_001)

list_comp = [n * n for n in numbers]        # builds 1M items immediately
gen_expr  = (n * n for n in numbers)        # creates a tiny generator object

print(f"List comp size : {sys.getsizeof(list_comp):>10,} bytes")
print(f"Gen expr size  : {sys.getsizeof(gen_expr):>10,} bytes")
print(f"Type of gen_expr: {type(gen_expr)}")

# ── Consuming a generator expression ─────────

squares = (x ** 2 for x in range(1, 6))

print("\nSquares (via next):")
print(next(squares))        # 1
print(next(squares))        # 4

print("Remaining (via for loop):")
for s in squares:           # continues from where next() left off
    print(s)                # 9, 16, 25

# ── Passing directly to functions ─────────────
# When a generator expression is the ONLY argument, the outer
# parentheses can be omitted — no double brackets needed.

total   = sum(x ** 2 for x in range(1, 11))
maximum = max(len(word) for word in ["Python", "is", "awesome"])
joined  = ", ".join(str(x) for x in [1, 2, 3, 4, 5])

print(f"\nSum of squares 1-10 : {total}")
print(f"Longest word length : {maximum}")
print(f"Joined string       : {joined}")

# ── Filtering with if ─────────────────────────

prices = [9.99, 24.99, 4.50, 99.00, 14.99, 0.99, 49.99]

expensive = (p for p in prices if p > 20)
print("\nExpensive items (>$20):")
for p in expensive:
    print(f"  ${p:.2f}")

# ── Chaining generator expressions ────────────
# Each gen expr wraps the previous — fully lazy chain

raw_data = ["  42 ", "hello", " 17", "100 ", "NaN", " 8  "]

cleaned    = (s.strip() for s in raw_data)
only_nums  = (s for s in cleaned if s.lstrip("-").isdigit())
as_ints    = (int(s) for s in only_nums)
above_ten  = (n for n in as_ints if n > 10)

print("\nValid numbers above 10:", list(above_ten))

# ── Real-life 1: Processing CSV-like data ─────
# A typical data pipeline: read rows, filter, transform — all lazy.

csv_rows = [
    "Alice,Engineering,95000",
    "Bob,Marketing,62000",
    "Carol,Engineering,105000",
    "Dave,HR,58000",
    "Eve,Engineering,88000",
]

engineers = (
    row.split(",")
    for row in csv_rows
    if "Engineering" in row
)

salaries = (int(parts[2]) for parts in engineers)

avg_salary = sum(salaries) / 3   # we know there are 3 engineers
print(f"\nEngineering avg salary: ${avg_salary:,.0f}")

# ── Real-life 2: Log file scanning ────────────
# Find unique error codes from a large stream of log entries.

log_entries = [
    "ERR-404 page not found",
    "ERR-500 internal server error",
    "INFO heartbeat ok",
    "ERR-404 page not found",
    "ERR-403 forbidden",
    "INFO user login",
    "ERR-500 internal server error",
]

error_codes = set(
    line.split()[0]
    for line in log_entries
    if line.startswith("ERR")
)
print(f"\nUnique error codes: {sorted(error_codes)}")

# ── Real-life 3: any() / all() with gen exprs ─
# These short-circuit — stop as soon as result is known.
# Using a list would build all items even if the first is enough.

transactions = [250.0, 800.0, 1500.0, 300.0, 99.0]

has_large   = any(t > 1000 for t in transactions)   # stops at 1500
all_positive = all(t > 0   for t in transactions)

print(f"\nAny transaction > $1000: {has_large}")
print(f"All transactions positive: {all_positive}")

# ── Key points ────────────────────────────────
# • () → generator expression (lazy)
# • [] → list comprehension  (eager)
# • Generator expressions use almost no memory
# • They are one-shot — cannot be restarted or reused
# • Ideal as arguments to sum(), max(), min(), any(), all(), join()
# • Can be chained to build lazy data pipelines in one expression
