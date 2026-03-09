# ─────────────────────────────────────────────
# Generator vs Iterator
# ─────────────────────────────────────────────

# ── Recap ─────────────────────────────────────
#
# ITERATOR: any object implementing __iter__() and __next__().
#           You build it manually as a class.
#
# GENERATOR: a special kind of iterator created automatically
#            by a generator function or generator expression.
#            Python writes __iter__ and __next__ for you.
#
# Every generator IS an iterator.
# Not every iterator is a generator.

from collections.abc import Iterator, Generator
import sys

# ── Manual iterator (class-based) ─────────────

class CountUp:
    """Iterator class that counts from start to stop."""
    def __init__(self, start, stop):
        self.current = start
        self.stop    = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

# ── Equivalent generator function ─────────────

def count_up_gen(start, stop):
    """Same behaviour — fraction of the code."""
    current = start
    while current <= stop:
        yield current
        current += 1

# ── Both behave identically as iterators ──────

it_class = CountUp(1, 5)
it_gen   = count_up_gen(1, 5)

print("Class iterator :", list(it_class))
print("Generator      :", list(it_gen))

# ── isinstance checks ─────────────────────────

it_class2 = CountUp(1, 3)
it_gen2   = count_up_gen(1, 3)

print(f"\nCountUp  is Iterator : {isinstance(it_class2, Iterator)}")   # True
print(f"CountUp  is Generator: {isinstance(it_class2, Generator)}")   # False — it's a manual iterator

print(f"gen func is Iterator : {isinstance(it_gen2, Iterator)}")      # True  — generators ARE iterators
print(f"gen func is Generator: {isinstance(it_gen2, Generator)}")     # True

# ── Memory comparison ─────────────────────────

N = 100_000

class BigCountUp:
    def __init__(self, n):
        self.n = n
        self.i = 0
    def __iter__(self): return self
    def __next__(self):
        if self.i >= self.n: raise StopIteration
        v = self.i; self.i += 1; return v

class_iter = BigCountUp(N)
gen_iter   = (i for i in range(N))

print(f"\nClass iterator size : {sys.getsizeof(class_iter):>8} bytes")
print(f"Generator expr size : {sys.getsizeof(gen_iter):>8} bytes")
# Both are small — neither stores N values

# ── Code complexity comparison ─────────────────
#
# Task: yield powers of 2 up to a limit
#
# Class-based — boilerplate heavy:

class PowersOfTwo:
    def __init__(self, limit):
        self.limit   = limit
        self.current = 1
    def __iter__(self): return self
    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        val = self.current
        self.current *= 2
        return val

# Generator — clean and concise:
def powers_of_two(limit):
    current = 1
    while current <= limit:
        yield current
        current *= 2

print("\nPowers of 2 up to 64:")
print("Class  :", list(PowersOfTwo(64)))
print("Generator:", list(powers_of_two(64)))

# ── When to use a class iterator instead ──────
#
# Prefer a class iterator when you need:
#   • Multiple methods (reset, peek, skip)
#   • Shared state between methods
#   • Subclassing / inheritance
#   • A public API that users inspect or configure

class ResettableCounter:
    """Class iterator with extra methods a generator can't provide."""
    def __init__(self, start, stop):
        self._start   = start
        self._stop    = stop
        self.current  = start

    def __iter__(self): return self

    def __next__(self):
        if self.current > self._stop:
            raise StopIteration
        v = self.current
        self.current += 1
        return v

    def reset(self):
        self.current = self._start

    def peek(self):
        return self.current if self.current <= self._stop else None

counter = ResettableCounter(1, 5)
print("\nResettable counter:")
print(next(counter), next(counter))     # 1 2
counter.reset()
print("After reset, peek:", counter.peek())  # 1
print(list(counter))                    # [1, 2, 3, 4, 5]

# ── Real-life: log parser — generator wins ────
# Parsing structured log lines is simple enough for a generator.

def parse_logs(raw_lines):
    for line in raw_lines:
        parts = line.split("|")
        if len(parts) == 3:
            yield {
                "timestamp": parts[0].strip(),
                "level":     parts[1].strip(),
                "message":   parts[2].strip(),
            }

raw = [
    "2024-01-10 08:00 | INFO  | Server started",
    "2024-01-10 08:01 | ERROR | Disk full",
    "2024-01-10 08:02 | INFO  | Disk cleared",
    "malformed line without pipes",
    "2024-01-10 08:03 | WARN  | High CPU",
]

print("\nParsed logs:")
for entry in parse_logs(raw):
    print(f"  [{entry['level']}] {entry['message']}")

# ── Key points ────────────────────────────────
# • Generator = iterator created automatically; less boilerplate
# • Use generators for: simple sequences, pipelines, one-pass data
# • Use class iterators for: stateful, resettable, multi-method APIs
# • Both are lazy and one-shot (unless class adds reset)
# • isinstance(x, Generator) is True only for generator objects
