# ─────────────────────────────────────────────
# Lazy Evaluation
# ─────────────────────────────────────────────

# ── What is lazy evaluation? ─────────────────
#
# Lazy evaluation means: compute a value only when it is
# actually needed — not when it is defined.
#
# Eager (lists):  ALL values computed immediately and stored.
# Lazy (generators): values computed ONE AT A TIME, on demand.
#
# Why it matters:
#   • Saves memory — no need to hold the entire sequence
#   • Saves time  — work for values you never reach is skipped
#   • Enables infinite sequences — you can't build an infinite list

import time
import sys

# ── Eager vs lazy: visible timing difference ──

def eager_process(n):
    """Simulates heavy computation — builds entire result list."""
    result = []
    for i in range(n):
        time.sleep(0.001)       # simulate 1ms work per item
        result.append(i * i)
    return result

def lazy_process(n):
    """Produces one result at a time, only when asked."""
    for i in range(n):
        time.sleep(0.001)
        yield i * i

N = 50

# Eager: waits until ALL 50 items are computed before you get anything
t0 = time.perf_counter()
data = eager_process(N)
print(f"Eager: waited {time.perf_counter()-t0:.3f}s to get first value")
print(f"  first value: {data[0]}")

# Lazy: first value is available after computing just ONE item
t0 = time.perf_counter()
gen = lazy_process(N)
first = next(gen)
print(f"\nLazy: waited {time.perf_counter()-t0:.3f}s to get first value")
print(f"  first value: {first}")

# ── Infinite sequences — only possible with lazy eval ──

def natural_numbers():
    """Yields 1, 2, 3, 4, ... forever."""
    n = 1
    while True:
        yield n
        n += 1

def take(n, iterable):
    """Take first n items from an iterable."""
    gen = iter(iterable)
    for _ in range(n):
        yield next(gen)

print("\nFirst 10 natural numbers:")
print(list(take(10, natural_numbers())))

def prime_numbers():
    """Lazily yields prime numbers — infinite sequence."""
    def is_prime(num):
        if num < 2: return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0: return False
        return True

    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

print("First 10 primes:")
print(list(take(10, prime_numbers())))

# ── Short-circuit: stop early without wasted work ──

def find_first(predicate, iterable):
    """Return first item matching predicate — never scans beyond it."""
    for item in iterable:
        if predicate(item):
            return item
    return None

transactions = [45.0, 12.5, 5200.0, 800.0, 99.0, 3400.0]

# Generator produces transactions lazily; find_first stops at 5200.0
suspicious = find_first(
    lambda t: t > 1000,
    (t for t in transactions)
)
print(f"\nFirst suspicious transaction: ${suspicious:,.2f}")

# ── Memory: lazy vs eager on large data ───────

import sys

n = 1_000_000
eager_list = [i * 2 for i in range(n)]
lazy_gen   = (i * 2 for i in range(n))

print(f"\nEager list ({n:,} items): {sys.getsizeof(eager_list):>12,} bytes")
print(f"Lazy  gen  ({n:,} items): {sys.getsizeof(lazy_gen):>12,} bytes")

del eager_list      # release memory

# ── Real-life 1: Streaming large file download ─
# When downloading a large file, process each chunk as it
# arrives instead of waiting for the whole file.

def simulate_download(total_chunks=10, chunk_size_kb=512):
    """Lazily yields chunks as they 'arrive' over the network."""
    for i in range(1, total_chunks + 1):
        # time.sleep(0.1)  # simulate network delay
        chunk = f"<chunk_{i}: {chunk_size_kb}KB of data>"
        yield chunk

downloaded_kb = 0
print("\nStreaming download:")
for chunk in simulate_download(total_chunks=5):
    downloaded_kb += 512
    print(f"  Received {chunk[:20]}...  total: {downloaded_kb} KB")

# ── Real-life 2: Database cursor (lazy rows) ──
# Real DB cursors are lazy — rows fetched one at a time.
# Simulated here with a generator.

def db_cursor(table):
    """Simulate a database cursor — yields rows on demand."""
    # In reality: cursor.execute(query); yield from cursor
    for row in table:
        yield row

employee_table = [
    {"id": 1, "name": "Alice", "dept": "Engineering", "salary": 95000},
    {"id": 2, "name": "Bob",   "dept": "Marketing",   "salary": 62000},
    {"id": 3, "name": "Carol", "dept": "Engineering",  "salary": 105000},
    {"id": 4, "name": "Dave",  "dept": "HR",           "salary": 58000},
    {"id": 5, "name": "Eve",   "dept": "Engineering",  "salary": 88000},
]

# Find first engineering employee earning > 100k — lazy, stops early
result = find_first(
    lambda r: r["dept"] == "Engineering" and r["salary"] > 100_000,
    db_cursor(employee_table)
)
print(f"\nFirst high-earning engineer: {result['name']} (${result['salary']:,})")

# ── Key points ────────────────────────────────
# • Lazy = compute on demand; Eager = compute all upfront
# • Generators enable lazy evaluation in Python
# • Infinite sequences are only possible lazily
# • short-circuit functions (any, all, find_first) benefit most
# • Use lazy when: large data, streaming, early exit patterns
# • Use eager when: you need random access or multiple passes
