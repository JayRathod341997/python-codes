# ─────────────────────────────────────────────
# Built-in Iterators
# ─────────────────────────────────────────────

# ── Overview ──────────────────────────────────
# Python provides many built-in functions and types that
# return iterators (lazy — they compute values on demand).
#
# Function/Type      Returns iterator of…
# ─────────────────  ────────────────────────────────────────
# range()            integers in a range
# enumerate()        (index, value) pairs
# zip()              tuples of elements from multiple iterables
# map()              results of applying a function
# filter()           items passing a condition
# reversed()         items in reverse order
# dict.items()       (key, value) pairs
# dict.keys()        keys
# dict.values()      values
# open()  / file     lines of a file

# ── range() ──────────────────────────────────
# Does NOT store all numbers in memory — generates on demand.

r = range(1, 6)
print(type(r))              # <class 'range'>
print(list(r))              # [1, 2, 3, 4, 5]

# range is an iterable, not an iterator — you can iterate it multiple times
r_iter = iter(r)
print(next(r_iter))         # 1
print(next(r_iter))         # 2

# ── enumerate() ──────────────────────────────
# Real-life: numbered receipts, line numbers in an editor

products = ["apple", "banana", "cherry"]
for i, name in enumerate(products, start=1):
    print(f"{i}. {name}")
# 1. apple  2. banana  3. cherry

# enumerate returns an iterator:
en = enumerate(["a", "b"])
print(next(en))             # (0, 'a')
print(next(en))             # (1, 'b')

# ── zip() ────────────────────────────────────
# Real-life: pairing names with scores, merging two data streams

names  = ["Alice", "Bob", "Carol"]
scores = [88, 72, 95]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Alice: 88  Bob: 72  Carol: 95

# zip stops at the shortest iterable:
print(list(zip([1, 2, 3], ["a", "b"])))    # [(1,'a'), (2,'b')]

# zip returns an iterator:
z = zip([1, 2], ["x", "y"])
print(next(z))              # (1, 'x')

# ── map() ────────────────────────────────────
# Real-life: applying a transformation to every item (prices, temps, etc.)

prices   = [100, 250, 499]
with_gst = list(map(lambda p: round(p * 1.18, 2), prices))
print(with_gst)             # [118.0, 295.0, 588.82]

# map is lazy — values computed on demand:
m = map(str.upper, ["hello", "world"])
print(next(m))              # HELLO

# map with multiple iterables:
a = [1, 2, 3]
b = [10, 20, 30]
print(list(map(lambda x, y: x + y, a, b)))   # [11, 22, 33]

# ── filter() ─────────────────────────────────
# Real-life: filtering active users, valid transactions

numbers  = [1, -2, 3, -4, 5, -6]
positives = list(filter(lambda x: x > 0, numbers))
print(positives)            # [1, 3, 5]

# filter is lazy:
f = filter(None, [0, 1, "", "hello", None, True])
print(list(f))              # [1, 'hello', True]  (filter(None,...) keeps truthy)

# ── reversed() ───────────────────────────────
# Real-life: displaying items newest-first, undo stack

history = ["open", "edit", "save", "close"]
for action in reversed(history):
    print(action)
# close, save, edit, open

rev = reversed([10, 20, 30])
print(next(rev))            # 30

# ── dict views ───────────────────────────────
# Real-life: iterating config keys, serialising settings

config = {"host": "localhost", "port": 8080, "debug": True}

for key in config.keys():
    print(key)              # host  port  debug

for val in config.values():
    print(val)              # localhost  8080  True

for key, val in config.items():
    print(f"{key} = {val}") # host = localhost  …

# views are iterables (not iterators):
kv = iter(config.items())
print(next(kv))             # ('host', 'localhost')

# ── Key points ───────────────────────────────
# • All these return LAZY iterators — no memory wasted until consumed
# • Wrap with list() / tuple() to materialise all values at once
# • They all support next() and for loops
# • map() and filter() are often replaced by comprehensions — both are fine
# • zip() stops at the shortest input; use itertools.zip_longest for full
