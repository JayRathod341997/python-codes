# ─────────────────────────────────────────────
# Performance Comparison — Loops vs Comprehensions vs Generators
# ─────────────────────────────────────────────

import timeit
import sys

N = 1_000_000   # one million items

# ── 1. Speed comparison ───────────────────────
# Task: build a list of squares from 0 to N-1

# Method A — for loop with append
def using_loop():
    result = []
    for x in range(N):
        result.append(x ** 2)
    return result

# Method B — list comprehension
def using_list_comp():
    return [x ** 2 for x in range(N)]

# Method C — list() wrapping a generator expression
def using_generator():
    return list(x ** 2 for x in range(N))

t_loop = timeit.timeit(using_loop,      number=3)
t_comp = timeit.timeit(using_list_comp, number=3)
t_gen  = timeit.timeit(using_generator, number=3)

print(f"Loop        : {t_loop:.3f}s")
print(f"List comp   : {t_comp:.3f}s")
print(f"Generator   : {t_gen:.3f}s")
# Typical result: list comp ≈ 20-30% faster than loop
# Generator slightly slower than list comp when fully consumed (overhead)

# ── 2. Memory comparison ─────────────────────
loop_result = []
for x in range(N):
    loop_result.append(x ** 2)

list_result = [x ** 2 for x in range(N)]
gen_result  = (x ** 2 for x in range(N))   # not consumed — just the object

print(f"\nMemory (loop list)     : {sys.getsizeof(loop_result):>12,} bytes")
print(f"Memory (list comp)     : {sys.getsizeof(list_result):>12,} bytes")
print(f"Memory (generator obj) : {sys.getsizeof(gen_result):>12,} bytes")
# Generator object is ~104 bytes regardless of N — O(1) memory!

# ── 3. When to choose what ────────────────────
# ┌──────────────────────────────────────────────────────────────────┐
# │ Scenario                              │ Best choice              │
# ├──────────────────────────────────────────────────────────────────┤
# │ Build a list to use multiple times    │ List comprehension       │
# │ Need index access (result[i])         │ List comprehension       │
# │ Need len() of result                  │ List comprehension       │
# │ Large data, iterate once              │ Generator expression     │
# │ Large data, use with sum/any/all/max  │ Generator expression     │
# │ Reading a big file line by line       │ Generator expression     │
# │ Complex multi-step logic              │ Regular for loop         │
# │ Debugging / readability first         │ Regular for loop         │
# └──────────────────────────────────────────────────────────────────┘

# ── 4. Real-life: large CSV processing ───────
# Scenario: sum total sales from a million-row CSV
# Simulate with a list of dicts

import random
random.seed(42)
records = [{"amount": random.randint(100, 10000)} for _ in range(100_000)]

# Bad — builds intermediate list
total_bad  = sum([r["amount"] for r in records])    # list in memory, then sum

# Good — generator passed directly to sum
total_good = sum(r["amount"] for r in records)      # no intermediate list

print(f"\nTotal (list comp) : {total_bad}")
print(f"Total (generator) : {total_good}")
# Results are identical; generator uses far less memory

# ── 5. Pitfall: exhausted generator ───────────
gen = (x * 2 for x in range(5))
print(list(gen))    # [0, 2, 4, 6, 8]
print(list(gen))    # []  ← generator is exhausted after first pass!
# Lesson: if you need to iterate multiple times, use a list comprehension

# ── Key takeaways ─────────────────────────────
# • List comprehension ≈ 20–40% faster than equivalent for+append loop
# • Generator expression ≈ same speed as list comp, but O(1) memory
# • Generator shines when data is huge OR when using lazy built-ins
# • For loop shines when logic is complex or you need multiple statements
# • Profile first (timeit / memory_profiler) — don't optimise blindly
