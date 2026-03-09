# ─────────────────────────────────────────────
# Useful Standard Libraries — itertools
# ─────────────────────────────────────────────

import itertools

# itertools provides fast, memory-efficient "iterator building blocks".
# All functions return lazy iterators — wrap in list() to materialise.


# ══════════════════════════════════════════════
# Infinite iterators
# ══════════════════════════════════════════════

# ── count(start, step) — endless counter ─────
counter = itertools.count(1, 2)         # 1, 3, 5, 7, ...
print([next(counter) for _ in range(5)])   # [1, 3, 5, 7, 9]

# Real-life: Auto-incrementing ID generator
def id_generator(prefix="ID", start=1000):
    for n in itertools.count(start):
        yield f"{prefix}-{n}"

gen = id_generator("ORD")
print(next(gen))    # ORD-1000
print(next(gen))    # ORD-1001
print(next(gen))    # ORD-1002


# ── cycle(iterable) — repeat endlessly ───────
# Real-life: Round-robin load balancing
servers = itertools.cycle(["server1", "server2", "server3"])
requests = ["req1", "req2", "req3", "req4", "req5", "req6", "req7"]
assignments = [(req, next(servers)) for req in requests]
for req, srv in assignments:
    print(f"  {req} → {srv}")


# ── repeat(obj, times) — repeat N times ──────
print(list(itertools.repeat("*", 5)))       # ['*','*','*','*','*']
# Used with map() to pass a fixed argument
squares = list(map(pow, range(1, 6), itertools.repeat(2)))
print(squares)      # [1, 4, 9, 16, 25]


# ══════════════════════════════════════════════
# Finite iterators
# ══════════════════════════════════════════════

# ── chain(*iterables) — flatten iterables ─────
# Real-life: Combine multiple query results
q1 = [1, 2, 3]
q2 = [4, 5]
q3 = [6, 7, 8, 9]
all_results = list(itertools.chain(q1, q2, q3))
print(all_results)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# chain.from_iterable — flatten a list of lists
nested = [["Alice", "Bob"], ["Carol"], ["Dave", "Eve", "Frank"]]
flat   = list(itertools.chain.from_iterable(nested))
print(flat)


# ── islice(iterable, stop) — lazy slicing ────
# Real-life: Paginate through a large dataset without loading it all
def big_dataset():
    """Simulate a database cursor yielding millions of rows."""
    for i in itertools.count(1):
        yield {"id": i, "value": i * 10}

page1 = list(itertools.islice(big_dataset(), 5))        # first 5
page2 = list(itertools.islice(big_dataset(), 5, 10))    # rows 5–9
print(page1)
print(page2)


# ── compress(data, selectors) — filter by mask ─
# Real-life: Feature flags — keep items where flag is True
features  = ["dark_mode", "beta_ui", "analytics", "export", "ai_assist"]
enabled   = [True, False, True, True, False]
active    = list(itertools.compress(features, enabled))
print(f"Active features: {active}")


# ── takewhile / dropwhile ─────────────────────
# Real-life: Process log entries until an error appears
log_levels = ["INFO", "INFO", "DEBUG", "WARNING", "ERROR", "INFO"]
before_error = list(itertools.takewhile(lambda x: x != "ERROR", log_levels))
print(f"Before first ERROR: {before_error}")

# dropwhile — skip leading items while condition is True
after_header = list(itertools.dropwhile(lambda x: x != "DATA",
                                         ["HEADER", "META", "DATA", "1", "2", "3"]))
print(f"After header: {after_header}")


# ── groupby — group consecutive identical elements ─
# Real-life: Group transactions by date, group sorted employees by dept
# ⚠ Data MUST be sorted by the key first!

employees = [
    {"name": "Alice", "dept": "Engineering"},
    {"name": "Bob",   "dept": "Engineering"},
    {"name": "Carol", "dept": "Marketing"},
    {"name": "Dave",  "dept": "Marketing"},
    {"name": "Eve",   "dept": "Sales"},
]
employees.sort(key=lambda e: e["dept"])

for dept, members in itertools.groupby(employees, key=lambda e: e["dept"]):
    names = [m["name"] for m in members]
    print(f"  {dept}: {', '.join(names)}")


# ── accumulate — running total ────────────────
# Real-life: Running sales total, cumulative rainfall
from itertools import accumulate
import operator

daily_sales = [1200, 3400, 800, 5600, 2100, 4300]
running_total = list(accumulate(daily_sales))
print(f"Daily   : {daily_sales}")
print(f"Running : {running_total}")

# Running maximum
running_max = list(accumulate(daily_sales, func=max))
print(f"Run max : {running_max}")


# ══════════════════════════════════════════════
# Combinatoric iterators
# ══════════════════════════════════════════════

# ── product — cartesian product ───────────────
# Real-life: Generate all size × color combinations for a product
sizes  = ["S", "M", "L", "XL"]
colors = ["Red", "Blue"]
variants = list(itertools.product(sizes, colors))
print(f"Variants ({len(variants)}): {variants}")

# Repeated product
print(list(itertools.product("AB", repeat=3)))   # all 3-char strings from A,B


# ── permutations — all orderings ─────────────
# Real-life: All possible orderings of a delivery route
stops = ["A", "B", "C"]
routes = list(itertools.permutations(stops))
print(f"Routes: {routes}")      # 6 permutations


# ── combinations — subsets without repeat ────
# Real-life: Lottery ticket, team selection
players = ["Alice", "Bob", "Carol", "Dave"]
teams = list(itertools.combinations(players, 2))
print(f"Possible teams of 2: {teams}")

# combinations_with_replacement — sampling with replacement
dice_outcomes = list(itertools.combinations_with_replacement([1,2,3,4,5,6], 2))
print(f"Dice pairs: {len(dice_outcomes)}")   # 21


# ── Key points ────────────────────────────────
# Infinite:   count, cycle, repeat
# Finite:     chain, islice, compress, takewhile, dropwhile, groupby, accumulate
# Combinator: product, permutations, combinations, combinations_with_replacement
# All return lazy iterators — memory efficient for large data
# groupby requires pre-sorted data to work correctly
