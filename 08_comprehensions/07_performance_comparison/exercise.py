# ─────────────────────────────────────────────
# Exercises — Performance Comparison
# ─────────────────────────────────────────────

import timeit
import sys

# ── Exercise 1: Benchmark Three Approaches ────
# Real-life: You're building an analytics service that processes price data.
# Task: build a list of prices multiplied by 1.18 (add GST) for 500,000 items.
#
# Write THREE versions:
#   a) for loop with append
#   b) list comprehension
#   c) generator expression (converted to list)
# Benchmark each with timeit (number=5) and print results.

prices = list(range(1, 500_001))

# --- your code here ---
# def using_loop(): ...
# def using_list_comp(): ...
# def using_generator(): ...
# print timeit results


# ── Exercise 2: Memory Audit ──────────────────
# Real-life: You're evaluating memory usage for a data pipeline.
# For N = 500_000 items (range), compare sys.getsizeof() of:
#   a) A list comprehension [x*3 for x in range(N)]
#   b) A generator expression (x*3 for x in range(N))
# Print both sizes and the ratio (list_size / gen_size).

N = 500_000

# --- your code here ---


# ── Exercise 3: Choose the Right Tool ─────────
# Real-life: Transaction audit
# You have 1 million transactions. Answer these three questions EFFICIENTLY:
#
#   Q1: What is the total of all "credit" transactions?
#       Use a generator expression with sum() — no intermediate list.
#
#   Q2: Is there ANY transaction with amount > 50,000?
#       Use any() with a generator — short-circuit as soon as found.
#
#   Q3: Are ALL "debit" amounts > 0?
#       Use all() with a generator.

import random
random.seed(0)
transactions = [
    {"type": random.choice(["credit", "debit"]),
     "amount": random.randint(1, 60_000)}
    for _ in range(1_000_000)
]

# --- your code here ---
# total_credits = sum(...)
# any_large     = any(...)
# all_positive  = all(...)


# ── Exercise 4: Exhausted Generator Trap ──────
# Real-life: This is a common bug in production code.
# Run the snippet below and explain (in a comment) WHY the second
# print gives an empty list.

gen = (x ** 2 for x in range(5))
first_pass  = list(gen)
second_pass = list(gen)     # ← why is this []?

print(first_pass)
print(second_pass)

# Your explanation:
# ---


# ── Exercise 5: Refactor for Memory Efficiency ─
# Real-life: ETL pipeline for a large dataset
# The code below uses list comprehensions at every step.
# Refactor using generator expressions so no intermediate list is stored.
# Final output should still be a list.

data = list(range(1, 100_001))

# Original (creates 3 large intermediate lists):
step1 = [x * 2      for x in data]
step2 = [x - 1      for x in step1]
step3 = [x          for x in step2 if x % 3 == 0]
result_original = step3

# --- Refactored version (no intermediate lists) ---
# step1 = (... for x in data)
# step2 = (... for x in step1)
# step3 = (... for x in step2 if ...)
# result_refactored = list(step3)

# Verify both give the same answer:
# print(result_original[:5], result_refactored[:5])
# print(len(result_original) == len(result_refactored))  # True


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: List comp should be fastest; loop slowest
# Ex2: List ~4,000,056 bytes vs generator ~104 bytes; ratio ~38,000×
# Ex3: (values will vary due to random seed, but no errors)
# Ex4: Generator is exhausted after first pass — iterator protocol
# Ex5: result_original == result_refactored (True)
# ─────────────────────────────────────────────
