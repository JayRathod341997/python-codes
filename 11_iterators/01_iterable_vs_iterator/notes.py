# ─────────────────────────────────────────────
# Iterable vs Iterator
# ─────────────────────────────────────────────

# ── Definitions ──────────────────────────────
#
# ITERABLE
#   Any object you can loop over with 'for'.
#   It implements __iter__() which returns an iterator.
#   Examples: list, tuple, str, dict, set, range, file
#
# ITERATOR
#   An object that knows where it is in a sequence.
#   It implements both:
#     __iter__()  → returns itself
#     __next__()  → returns the next value, raises StopIteration when done
#
#   Key difference: an iterator has STATE (it remembers its position).
#   An iterable does NOT — it always starts fresh.

# ── Visual model ─────────────────────────────
#
#   Iterable          Iterator
#   ─────────         ──────────────────────────
#   A book       →    A bookmark inside the book
#   Can be read       Tracks your current page
#   any number        Once finished, it's done
#   of times

# ── Checking with isinstance ──────────────────
from collections.abc import Iterable, Iterator

my_list = [1, 2, 3]

print(isinstance(my_list, Iterable))    # True  — it's an iterable
print(isinstance(my_list, Iterator))    # False — it is NOT an iterator

it = iter(my_list)                      # create an iterator FROM the iterable
print(isinstance(it, Iterable))         # True  — iterators are also iterable
print(isinstance(it, Iterator))         # True  — now it IS an iterator

# ── An iterable can produce multiple independent iterators ──
nums = [10, 20, 30]
it1 = iter(nums)
it2 = iter(nums)            # completely independent

print(next(it1))            # 10
print(next(it1))            # 20
print(next(it2))            # 10  ← starts from beginning, unaffected by it1

# ── Iterators are exhausted (one-shot) ───────
it = iter([1, 2, 3])
print(next(it))             # 1
print(next(it))             # 2
print(next(it))             # 3
# next(it)                  # StopIteration — no more items

# Re-iterating an iterator gives nothing:
for val in it:
    print(val)              # (nothing printed — already exhausted)

# But re-iterating the original list works fine:
for val in [1, 2, 3]:
    print(val)              # 1, 2, 3 — fresh each time

# ── Real-life 1: CSV file processing ─────────
# A file object in Python IS an iterator.
# Reading lines advances its internal pointer.
# Once you reach the end you must re-open the file.

# Simulating with a list to demonstrate the concept:
log_lines = ["INFO: start", "WARNING: slow", "ERROR: crash"]
log_iter  = iter(log_lines)

print(next(log_iter))       # INFO: start
print(next(log_iter))       # WARNING: slow
# At this point log_iter has consumed 2 lines; only 1 remains.

# ── Real-life 2: Streaming data ───────────────
# Sensor readings arrive one at a time.
# Using an iterator means you process each reading on demand
# without loading the entire dataset into memory.

readings = [23.1, 22.8, 24.5, 23.9, 25.0]
sensor   = iter(readings)

first  = next(sensor)       # grab first reading to establish baseline
second = next(sensor)
print(f"Baseline: {first}, Next: {second}")  # Baseline: 23.1, Next: 22.8

# ── Key points ───────────────────────────────
# • All iterators are iterables, but not all iterables are iterators
# • Iterables can be iterated many times; iterators are one-shot
# • 'for' loops call iter() + next() automatically
# • Use iter() to turn an iterable into an iterator
# • Use next() to manually advance an iterator
