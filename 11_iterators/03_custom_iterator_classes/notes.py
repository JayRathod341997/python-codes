# ─────────────────────────────────────────────
# Custom Iterator Classes
# ─────────────────────────────────────────────

# ── What you need ────────────────────────────
# To make a class an iterator, implement two methods:
#
#   __iter__(self)   → returns self  (so it can be used in for loops)
#   __next__(self)   → returns next value, raises StopIteration when done
#
# This is called the "iterator protocol".

# ── Example 1: Countdown ──────────────────────
# Real-life: a countdown timer (e.g. OTP expiry, game start)

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self             # the object itself is the iterator

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

timer = Countdown(5)
for tick in timer:
    print(tick)                 # 5, 4, 3, 2, 1

# Can also use next() manually:
timer2 = Countdown(3)
print(next(timer2))             # 3
print(next(timer2))             # 2

# ── Example 2: NumberRange ────────────────────
# Real-life: paginated API — yield page numbers start to end

class NumberRange:
    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop    = stop
        self.step    = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += self.step
        return value

for page in NumberRange(1, 6):
    print(f"Fetching page {page}")
# Fetching page 1 … 5

print(list(NumberRange(0, 20, 5)))  # [0, 5, 10, 15]

# ── Example 3: FileLineIterator ───────────────
# Real-life: reading large log files line by line without
# loading the whole file into memory.

class FileLineIterator:
    def __init__(self, filename):
        self._file = open(filename, "r")

    def __iter__(self):
        return self

    def __next__(self):
        line = self._file.readline()
        if line == "":              # end of file
            self._file.close()
            raise StopIteration
        return line.rstrip("\n")

# Usage (requires an actual file):
# for line in FileLineIterator("app.log"):
#     if "ERROR" in line:
#         print(line)

# ── Example 4: InfiniteCounter ───────────────
# Real-life: generating unique IDs, timestamps, sequence numbers

class InfiniteCounter:
    def __init__(self, start=0, prefix="ID-"):
        self.n      = start
        self.prefix = prefix

    def __iter__(self):
        return self

    def __next__(self):
        uid = f"{self.prefix}{self.n:04d}"
        self.n += 1
        return uid

counter = InfiniteCounter(prefix="ORD-")
print(next(counter))        # ORD-0000
print(next(counter))        # ORD-0001
print(next(counter))        # ORD-0002

# Use itertools.islice to take only N items from infinite iterator:
import itertools
first_five = list(itertools.islice(InfiniteCounter(), 5))
print(first_five)           # ['ID-0000', 'ID-0001', 'ID-0002', 'ID-0003', 'ID-0004']

# ── Example 5: Stateful iterator with reset ──
# Real-life: a circular buffer (e.g. round-robin server selection)

class RoundRobin:
    def __init__(self, items):
        self._items = items
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self._items:
            raise StopIteration
        item = self._items[self._index % len(self._items)]
        self._index += 1
        return item

servers = RoundRobin(["server-A", "server-B", "server-C"])
for _ in range(7):
    print(next(servers))
# server-A, server-B, server-C, server-A, server-B, server-C, server-A

# ── Key points ───────────────────────────────
# • Define __iter__ and __next__ to make any class an iterator
# • __iter__ should return self
# • __next__ must raise StopIteration to signal end
# • Infinite iterators (no StopIteration) are valid — use islice to limit
# • Each iterator instance holds its own state independently
