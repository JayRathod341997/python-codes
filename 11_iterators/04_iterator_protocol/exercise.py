# ─────────────────────────────────────────────
# Exercises — Iterator Protocol
# ─────────────────────────────────────────────

# ── Exercise 1: Spot the bugs ─────────────────
# Real-life: debugging a broken data pipeline iterator
# Each class below has a protocol violation. Identify and fix it.

# Bug A: __iter__ doesn't return self
class BugA:
    def __init__(self):
        self.data = [1, 2, 3]
        self.idx  = 0

    def __iter__(self):
        return self.data            # BUG: should return self

    def __next__(self):
        if self.idx >= len(self.data):
            raise StopIteration
        val = self.data[self.idx]
        self.idx += 1
        return val

# Bug B: StopIteration returned instead of raised
class BugB:
    def __init__(self):
        self.items = ["a", "b"]
        self.i     = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= len(self.items):
            return StopIteration    # BUG

        val    = self.items[self.i]
        self.i += 1
        return val

# Bug C: __next__ is missing
class BugC:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self
    # BUG: __next__ not defined

# --- your code here ---
# Fix BugA, BugB, BugC by creating corrected versions FixA, FixB, FixC.
# Then verify:

# print(list(FixA()))       # [1, 2, 3]
# print(list(FixB()))       # ['a', 'b']
# print(list(FixC(4)))      # [0, 1, 2, 3]


# ── Exercise 2: Combined vs Separate design ───
# Real-life: a report that gets printed twice in a workflow
#
# Part A: Implement SalesReport as COMBINED design.
#         Show that iterating twice gives [] on the second pass.
#
# Part B: Implement SalesReport2 as SEPARATE design
#         (iterable + SalesReportIterator).
#         Show that iterating twice gives the same result both times.

sales = [("Jan", 120000), ("Feb", 98000), ("Mar", 145000)]

# --- your code here ---

# Part A test:
# report = SalesReport(sales)
# print(list(report))   # [('Jan', 120000), ('Feb', 98000), ('Mar', 145000)]
# print(list(report))   # []  ← exhausted

# Part B test:
# report2 = SalesReport2(sales)
# print(list(report2))  # full list
# print(list(report2))  # full list again


# ── Exercise 3: Protocol inspection ───────────
# Real-life: writing a utility that tells you about an unknown object
# Write a function describe_object(obj) that prints:
#   - Whether it has __iter__
#   - Whether it has __next__
#   - Whether iter(obj) returns the same object (i.e., it IS an iterator)

def describe_object(obj):
    pass                            # TODO

# --- your code here ---

describe_object([1, 2, 3])
describe_object(iter([1, 2, 3]))
describe_object("hello")
describe_object(42)

# Expected:
# [1, 2, 3]       has __iter__: True  | has __next__: False | is iterator: False
# list_iterator   has __iter__: True  | has __next__: True  | is iterator: True
# hello           has __iter__: True  | has __next__: False | is iterator: False
# 42              has __iter__: False | has __next__: False | is iterator: False


# ── Exercise 4: Reusable ChunkIterator ────────
# Real-life: batch processing — split a list into chunks of size n
# Design: iterable (ChunkList) creates fresh ChunkIterator each time.

class ChunkIterator:
    def __init__(self, data, size):
        pass                        # TODO: store data, size, position

    def __iter__(self):
        pass

    def __next__(self):
        pass                        # TODO: return next slice of length size

class ChunkList:
    def __init__(self, data, size):
        pass                        # TODO: store data and size

    def __iter__(self):
        pass                        # TODO: return a fresh ChunkIterator

# --- your code here ---

records = list(range(1, 11))        # [1..10]
chunks  = ChunkList(records, 3)

print(list(chunks))     # [[1,2,3],[4,5,6],[7,8,9],[10]]
print(list(chunks))     # same again — reusable


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: fixed versions print [1,2,3], ['a','b'], [0,1,2,3]
# Ex2: combined gives [] on second pass; separate gives full list twice
# Ex3: correct flags for each object type
# Ex4: [[1,2,3],[4,5,6],[7,8,9],[10]] twice
# ─────────────────────────────────────────────
