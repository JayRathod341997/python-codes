# ─────────────────────────────────────────────
# Iterator Protocol
# ─────────────────────────────────────────────

# ── What is the iterator protocol? ───────────
# The iterator protocol is the formal contract Python requires
# for an object to be treated as an iterator.
#
# An object is an iterator if it implements:
#
#   __iter__(self)   → must return self
#   __next__(self)   → must return next value OR raise StopIteration
#
# An object is an iterable (but not necessarily an iterator) if it
# implements only:
#
#   __iter__(self)   → must return an iterator (not necessarily self)

# ── Separation of concerns ────────────────────
# Some objects separate the ITERABLE from its ITERATOR.
# This allows multiple independent iterations over the same data.
#
# Example: list is an iterable, list_iterator is its iterator.

my_list   = [1, 2, 3]
iterator1 = my_list.__iter__()    # same as iter(my_list)
iterator2 = my_list.__iter__()    # independent — fresh state

print(iterator1.__next__())       # 1
print(iterator1.__next__())       # 2
print(iterator2.__next__())       # 1   ← independent

# Confirm iter() on an iterator returns itself:
it = iter([10, 20])
print(iter(it) is it)             # True

# ── Verifying the protocol with hasattr ───────
def is_iterator(obj):
    return hasattr(obj, "__iter__") and hasattr(obj, "__next__")

def is_iterable(obj):
    return hasattr(obj, "__iter__")

print(is_iterable([1, 2, 3]))     # True
print(is_iterator([1, 2, 3]))     # False  (no __next__)
print(is_iterator(iter([1,2,3]))) # True

# ── Two designs: combined vs separate ─────────

# Design 1: COMBINED (iterator IS the iterable)
# Simple, but one-shot — can't restart.
class OnceThroughRange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self             # returns SELF — same object

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        val    = self.i
        self.i += 1
        return val

r = OnceThroughRange(3)
print(list(r))      # [0, 1, 2]
print(list(r))      # []  ← exhausted! second pass gives nothing

# Design 2: SEPARATE (iterable creates fresh iterators)
# More work, but reusable.
class ReusableRange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return ReusableRangeIterator(self.n)  # fresh iterator each time

class ReusableRangeIterator:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        val    = self.i
        self.i += 1
        return val

r = ReusableRange(3)
print(list(r))      # [0, 1, 2]
print(list(r))      # [0, 1, 2]  ← works again! fresh iterator each time

# ── StopIteration must be raised, not returned ─
# This is a common mistake for beginners.

class BadIterator:
    def __init__(self):
        self.done = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.done:
            return StopIteration    # BUG: this RETURNS the exception class
        self.done = True
        return 42

bad = BadIterator()
print(next(bad))    # 42
print(next(bad))    # <class 'StopIteration'>  ← loop will never stop!

class GoodIterator:
    def __init__(self):
        self.done = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.done:
            raise StopIteration     # CORRECT: raise it
        self.done = True
        return 42

good = GoodIterator()
print(list(good))   # [42]

# ── Real-life: reusable database result set ──
class QueryResult:
    """Iterable wrapper around rows — can be iterated multiple times."""
    def __init__(self, rows):
        self._rows = rows           # stores data, never consumed

    def __iter__(self):
        return iter(self._rows)     # creates a fresh list_iterator each time

rows = QueryResult([{"id": 1}, {"id": 2}, {"id": 3}])
print([r["id"] for r in rows])  # [1, 2, 3]
print([r["id"] for r in rows])  # [1, 2, 3]  ← reusable

# ── Key points ───────────────────────────────
# • Iterator protocol = __iter__ + __next__
# • __iter__ on an iterator must return self
# • Always RAISE StopIteration — never return it
# • Combined design is simpler but one-shot
# • Separate design is reusable but requires two classes
# • Use the separate design when users will loop multiple times
