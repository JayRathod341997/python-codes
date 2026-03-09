# ─────────────────────────────────────────────
# Exercises — Generator vs Iterator
# ─────────────────────────────────────────────
from collections.abc import Iterator, Generator

# ── Exercise 1: Identify the type ─────────────
# Real-life: debugging an "object is not a generator" error
# For each object below, print whether it is an Iterator,
# a Generator, both, or neither.

class MyIter:
    def __init__(self): self.n = 0
    def __iter__(self): return self
    def __next__(self):
        if self.n >= 3: raise StopIteration
        self.n += 1; return self.n

def my_gen():
    yield 1; yield 2; yield 3

objects = {
    "list [1,2,3]"      : [1, 2, 3],
    "iter([1,2,3])"     : iter([1, 2, 3]),
    "MyIter()"          : MyIter(),
    "my_gen()"          : my_gen(),
    "(x for x in [])"  : (x for x in []),
    "range(5)"          : range(5),
}

# --- your code here ---
# for name, obj in objects.items():
#     print(...)


# Expected output:
# list [1,2,3]       → Iterator: False | Generator: False
# iter([1,2,3])      → Iterator: True  | Generator: False
# MyIter()           → Iterator: True  | Generator: False
# my_gen()           → Iterator: True  | Generator: True
# (x for x in [])   → Iterator: True  | Generator: True
# range(5)           → Iterator: False | Generator: False


# ── Exercise 2: Rewrite class as generator ────
# Real-life: simplifying legacy code
# The class below works but is verbose. Rewrite it as a
# generator function called even_range_gen(start, stop).

class EvenRange:
    def __init__(self, start, stop):
        self.n    = start if start % 2 == 0 else start + 1
        self.stop = stop
    def __iter__(self): return self
    def __next__(self):
        if self.n >= self.stop: raise StopIteration
        v = self.n; self.n += 2; return v

# Verify both produce the same output:
print("Class  :", list(EvenRange(1, 12)))

# --- your code here ---
# def even_range_gen(start, stop): ...
# print("Generator:", list(even_range_gen(1, 12)))


# Expected output:
# Class  : [2, 4, 6, 8, 10]
# Generator: [2, 4, 6, 8, 10]


# ── Exercise 3: Build a resettable iterator ───
# Real-life: replaying a sensor stream for testing
# Build a class ReplaySensor(readings) where readings is a list.
# It must support:
#   - iteration (yield each reading once)
#   - .reset() method to restart from the beginning
# Demonstrate: iterate, reset, iterate again.

readings = [23.1, 22.8, 24.5, 23.9]

# --- your code here ---


# Expected output:
# First pass : [23.1, 22.8, 24.5, 23.9]
# After reset: [23.1, 22.8, 24.5, 23.9]


# ── Exercise 4: Generator vs class — add method ──
# Real-life: understanding where generators fall short
# Below is a generator that yields stock prices.
# You need a "peek" feature — see the next price without
# consuming it. Generators can't do this natively.
# Wrap the generator in a class PeekableIterator(iterable)
# that adds a .peek() method.

def stock_prices():
    for price in [102.5, 105.0, 103.8, 108.2, 107.1]:
        yield price

# --- your code here ---
# class PeekableIterator: ...

# stream = PeekableIterator(stock_prices())
# print("Peek :", stream.peek())   # 102.5 (not consumed)
# print("Next :", next(stream))    # 102.5 (now consumed)
# print("Peek :", stream.peek())   # 105.0
# print("Next :", next(stream))    # 105.0


# Expected output:
# Peek : 102.5
# Next : 102.5
# Peek : 105.0
# Next : 105.0


# ── Exercise 5: Performance comparison ────────
# Real-life: deciding between class iterator and generator for
# a high-throughput data pipeline
# Time consuming 500_000 items from:
#   a) A class-based counter iterator
#   b) A generator function counter
# Print elapsed time for each.

import time

class ClassCounter:
    def __init__(self, n): self.i = 0; self.n = n
    def __iter__(self): return self
    def __next__(self):
        if self.i >= self.n: raise StopIteration
        v = self.i; self.i += 1; return v

def gen_counter(n):
    for i in range(n): yield i

N = 500_000

# --- your code here ---


# Expected output (approximate):
# Class iterator: 0.045s
# Generator     : 0.020s
# (Generator is roughly 2x faster due to less overhead)


# ─────────────────────────────────────────────
# Self-check:
# Ex1: correct Iterator/Generator flags per object
# Ex2: [2, 4, 6, 8, 10] from both
# Ex3: same list printed twice
# Ex4: peek doesn't consume; next does
# Ex5: generator typically faster
# ─────────────────────────────────────────────
