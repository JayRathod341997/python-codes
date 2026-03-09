# ─────────────────────────────────────────────
# Generator Functions
# ─────────────────────────────────────────────

# ── What is a generator function? ────────────
#
# A generator function looks like a regular function but uses
# 'yield' instead of 'return'.
#
# Calling it does NOT execute the body. Instead, it returns a
# generator object — a special iterator that runs the body
# lazily, one yield at a time.
#
# Key behaviours:
#   • Execution pauses at each 'yield' and resumes on next()
#   • Local variables and execution state are preserved between calls
#   • Raises StopIteration automatically when the function body ends
#   • Memory-efficient: values produced one at a time, not all at once

# ── Minimal example ───────────────────────────

def count_up(start, stop):
    current = start
    while current <= stop:
        yield current       # pause here, hand value to caller
        current += 1        # resume from here on next call

gen = count_up(1, 5)
print(type(gen))            # <class 'generator'>

print(next(gen))            # 1
print(next(gen))            # 2

for n in gen:               # consumes remaining values
    print(n)                # 3, 4, 5

# ── Regular function vs generator function ────

def squares_list(n):        # regular — builds entire list in memory
    result = []
    for i in range(1, n + 1):
        result.append(i * i)
    return result

def squares_gen(n):         # generator — one value at a time
    for i in range(1, n + 1):
        yield i * i

print(squares_list(5))      # [1, 4, 9, 16, 25]  — all in memory

for sq in squares_gen(5):   # values produced lazily
    print(sq, end=" ")      # 1 4 9 16 25
print()

# ── Generator state is preserved ─────────────

def step_tracker():
    print("  [step] starting run...")
    yield "warm-up"
    print("  [step] cardio phase")
    yield "cardio"
    print("  [step] cool-down phase")
    yield "cool-down"
    print("  [step] done!")

tracker = step_tracker()
phase = next(tracker)
print(f"Current phase: {phase}")

phase = next(tracker)
print(f"Current phase: {phase}")

phase = next(tracker)
print(f"Current phase: {phase}")

# ── Real-life 1: Reading a large log file ─────
# Loading a 2 GB log file into a list crashes memory.
# A generator reads it one line at a time.

def read_log_lines(filename):
    """Yield one log line at a time — file never fully loaded."""
    try:
        with open(filename) as f:
            for line in f:
                yield line.rstrip()
    except FileNotFoundError:
        # Simulate for demo
        sample = [
            "2024-01-01 ERROR: disk full",
            "2024-01-01 INFO:  backup started",
            "2024-01-01 ERROR: timeout",
            "2024-01-01 INFO:  backup done",
        ]
        yield from sample

error_count = 0
for line in read_log_lines("app.log"):
    if "ERROR" in line:
        error_count += 1

print(f"\nErrors found in log: {error_count}")

# ── Real-life 2: Paginated API results ────────
# APIs return data in pages. A generator abstracts the paging
# so callers just iterate over results naturally.

def fetch_users(total=50, page_size=10):
    """Simulate paginated API — yield one user at a time."""
    fetched = 0
    page = 1
    while fetched < total:
        # In reality: response = requests.get(url, params={"page": page})
        batch = [f"user_{i}" for i in range(fetched, min(fetched + page_size, total))]
        print(f"  [API] fetched page {page} ({len(batch)} users)")
        for user in batch:
            yield user
        fetched += page_size
        page += 1

print("\nFirst 3 users from API:")
user_gen = fetch_users(total=25, page_size=10)
for _ in range(3):
    print(" ", next(user_gen))

# ── Key points ────────────────────────────────
# • A generator function body doesn't run until you call next()
# • 'yield' suspends and resumes — 'return' ends forever
# • Generators implement the iterator protocol automatically
# • Perfect for large data, streams, or infinite sequences
