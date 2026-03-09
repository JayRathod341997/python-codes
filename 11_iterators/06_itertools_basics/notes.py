# ─────────────────────────────────────────────
# itertools Basics
# ─────────────────────────────────────────────
import itertools

# ── What is itertools? ────────────────────────
# itertools is a standard library module providing fast,
# memory-efficient iterator building blocks.
# All functions return lazy iterators.
#
# Three categories:
#   Infinite iterators   → count, cycle, repeat
#   Finite iterators     → islice, chain, zip_longest, takewhile, dropwhile,
#                          groupby, starmap, accumulate, compress, pairwise
#   Combinatoric iters   → product, permutations, combinations

# ────────────────────────────────────────────
# INFINITE ITERATORS
# ────────────────────────────────────────────

# ── count(start, step) ────────────────────────
# Real-life: auto-numbering orders, frame IDs in a video stream

counter = itertools.count(1)
print(next(counter))        # 1
print(next(counter))        # 2

# Pair with islice to limit:
print(list(itertools.islice(itertools.count(10, 5), 5)))
# [10, 15, 20, 25, 30]

# ── cycle(iterable) ───────────────────────────
# Real-life: round-robin load balancing, repeating patterns

servers   = itertools.cycle(["server-A", "server-B", "server-C"])
requests  = ["req1", "req2", "req3", "req4", "req5"]
for req in requests:
    print(f"{req} → {next(servers)}")
# req1 → server-A, req2 → server-B, req3 → server-C, req4 → server-A …

# ── repeat(value, times) ─────────────────────
# Real-life: filling default values, padding

print(list(itertools.repeat(0, 5)))     # [0, 0, 0, 0, 0]

# Use with map to apply a constant to many values:
print(list(map(pow, range(1, 6), itertools.repeat(2))))
# [1, 4, 9, 16, 25]

# ────────────────────────────────────────────
# FINITE ITERATORS
# ────────────────────────────────────────────

# ── islice(iterable, stop) ───────────────────
# Real-life: pagination — take page N of results

data = range(1, 101)
page1 = list(itertools.islice(data, 10))            # first 10
page2 = list(itertools.islice(data, 10, 20))        # 10 to 20
print(page1)    # [1..10]
print(page2)    # [11..20]

# ── chain(*iterables) ────────────────────────
# Real-life: merging multiple data sources (log files, API pages)

jan = [101, 102, 103]
feb = [201, 202]
mar = [301, 302, 303, 304]

all_orders = list(itertools.chain(jan, feb, mar))
print(all_orders)   # [101, 102, 103, 201, 202, 301, 302, 303, 304]

# chain.from_iterable — when sources are in a list of lists:
monthly = [jan, feb, mar]
print(list(itertools.chain.from_iterable(monthly)))  # same result

# ── zip_longest(*iterables, fillvalue) ───────
# Real-life: merging survey responses of different lengths

q1 = ["A", "B", "C"]
q2 = ["Yes", "No"]
q3 = ["X", "Y", "Z", "W"]

for row in itertools.zip_longest(q1, q2, q3, fillvalue="-"):
    print(row)
# ('A','Yes','X')  ('B','No','Y')  ('C','-','Z')  ('-','-','W')

# ── takewhile(predicate, iterable) ───────────
# Real-life: read log lines until the first error

log = ["INFO start", "INFO ready", "ERROR crash", "INFO retry"]
before_error = list(itertools.takewhile(lambda l: "ERROR" not in l, log))
print(before_error)     # ['INFO start', 'INFO ready']

# ── dropwhile(predicate, iterable) ───────────
# Real-life: skip header lines until actual data starts

lines = ["# comment", "# generated", "name,age", "Alice,28", "Bob,34"]
data_lines = list(itertools.dropwhile(lambda l: l.startswith("#"), lines))
print(data_lines)       # ['name,age', 'Alice,28', 'Bob,34']

# ── accumulate(iterable, func) ───────────────
# Real-life: running totals in a cashbook, cumulative sales

sales      = [1000, 500, 1500, 800, 200]
cumulative = list(itertools.accumulate(sales))
print(cumulative)       # [1000, 1500, 3000, 3800, 4000]

# Running maximum:
import operator
prices = [5, 3, 8, 2, 9, 1]
running_max = list(itertools.accumulate(prices, max))
print(running_max)      # [5, 5, 8, 8, 9, 9]

# ── pairwise(iterable) (Python 3.10+) ────────
# Real-life: comparing consecutive readings (temperature delta)

temps   = [20.1, 21.3, 19.8, 22.5, 23.0]
deltas  = [(b - a) for a, b in itertools.pairwise(temps)]
print([round(d, 1) for d in deltas])   # [1.2, -1.5, 2.7, 0.5]

# ────────────────────────────────────────────
# COMBINATORIC ITERATORS
# ────────────────────────────────────────────

# ── product(*iterables) ───────────────────────
# Real-life: generating all size × colour combinations for a product

sizes   = ["S", "M", "L"]
colours = ["Red", "Blue"]
variants = list(itertools.product(sizes, colours))
print(variants)
# [('S','Red'),('S','Blue'),('M','Red'),('M','Blue'),('L','Red'),('L','Blue')]

# ── permutations(iterable, r) ────────────────
# Real-life: all possible batting orders for 3 from 5 players

players = ["A", "B", "C"]
print(list(itertools.permutations(players)))
# 6 permutations of all 3

# ── combinations(iterable, r) ────────────────
# Real-life: forming teams — pick 2 from 4 candidates

candidates = ["Alice", "Bob", "Carol", "Dave"]
teams = list(itertools.combinations(candidates, 2))
print(teams)
# [('Alice','Bob'),('Alice','Carol'),('Alice','Dave'),
#  ('Bob','Carol'),('Bob','Dave'),('Carol','Dave')]

# ── Key points ───────────────────────────────
# • All itertools functions are lazy — memory efficient
# • Use islice() to safely sample from infinite iterators
# • chain() is a flat-merge; chain.from_iterable() handles nested lists
# • takewhile / dropwhile are great for header-skip and error-stop patterns
# • accumulate() replaces manual running-total loops
# • product / permutations / combinations avoid nested loops for combinatorics
