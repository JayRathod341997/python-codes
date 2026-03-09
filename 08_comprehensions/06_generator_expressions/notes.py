# ─────────────────────────────────────────────
# Generator Expressions
# ─────────────────────────────────────────────

# ── What is a generator expression? ──────────
# Syntax:  (expression  for  item  in  iterable  [if condition])
# Looks like a list comprehension but uses () instead of []
# Returns a GENERATOR OBJECT — values are produced lazily (one at a time).
# Does NOT build the full list in memory.

# ── List vs Generator ─────────────────────────
list_comp = [x ** 2 for x in range(10)]      # builds all 10 items in memory
gen_expr  = (x ** 2 for x in range(10))      # iterator — nothing computed yet

print(type(list_comp))  # <class 'list'>
print(type(gen_expr))   # <class 'generator'>

print(list_comp)        # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] — all at once
print(next(gen_expr))   # 0  — compute one value on demand
print(next(gen_expr))   # 1
print(next(gen_expr))   # 4

# ── Memory comparison ─────────────────────────
import sys

big_list = [x * 2 for x in range(1_000_000)]
big_gen  = (x * 2 for x in range(1_000_000))

print(f"List size : {sys.getsizeof(big_list):>10,} bytes")
print(f"Gen size  : {sys.getsizeof(big_gen):>10,} bytes")
# List: ~8,000,056 bytes  |  Generator: ~104 bytes

# ── Real-life 1: Processing a large log file ──
# DevOps — scan millions of log lines without loading all into RAM
# Simulate with a list; in reality this would be open("app.log")
log_lines = [
    "ERROR: disk full",
    "INFO: user login",
    "ERROR: timeout",
    "INFO: request ok",
    "ERROR: null pointer",
]
errors = (line for line in log_lines if line.startswith("ERROR"))
for e in errors:
    print(e)
# Reads one line at a time — no full list stored

# ── Real-life 2: Sum without building a list ──
# Finance — sum large numbers on the fly
transactions = [100, -50, 200, -30, 400, -20]
total = sum(t for t in transactions if t > 0)   # sum of credits only
print(f"Total credits: {total}")    # 700

# ── Real-life 3: First match (short-circuit) ──
# Search — stop as soon as the first out-of-stock item is found
products = [
    {"name": "Laptop",   "stock": 10},
    {"name": "Mouse",    "stock": 0},
    {"name": "Monitor",  "stock": 5},
]
first_oos = next((p["name"] for p in products if p["stock"] == 0), "All in stock")
print(first_oos)    # 'Mouse' — stops scanning after finding it

# ── Generator inside built-ins ────────────────
# any(), all(), sum(), min(), max() all accept generators directly
scores = [85, 90, 78, 92, 88]
print(all(s >= 75 for s in scores))     # True  — all passed
print(any(s >= 90 for s in scores))     # True  — at least one A-grade
print(max(s for s in scores))           # 92
print(sum(s for s in scores) / len(scores))  # average = 86.6

# ── Real-life 4: Pipeline-style processing ───
# ETL — chain generators like Unix pipes; nothing computed until consumed
raw_data   = ["  alice@gmail.com ", "BOB@YAHOO.COM", "  carol@outlook.com"]
stripped   = (s.strip()      for s in raw_data)
lowered    = (s.lower()      for s in stripped)
gmail_only = (s              for s in lowered if "gmail" in s)

print(list(gmail_only))     # ['alice@gmail.com']
# Each stage is lazy — processes one item at a time through the whole pipeline

# ── Key points ───────────────────────────────
# • () → generator  |  [] → list  |  {} → set or dict
# • Generator expression: lazy — values produced on demand
# • Cannot reuse a generator — once exhausted it's empty
# • Use generators when: data is large, you iterate once, or you use any/all/sum
# • Use list comprehension when: you need indexing, len(), or multiple passes
# • Passing a generator as the sole arg to a function: can omit extra ()
#   e.g.  sum(x*2 for x in range(10))  ← valid — no double parentheses needed
