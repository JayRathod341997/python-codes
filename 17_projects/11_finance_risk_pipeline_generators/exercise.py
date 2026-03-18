# ───────────────────────────────────────────────────────────────
# Exercises — Project 11: Generators & Pipelines
# ───────────────────────────────────────────────────────────────

# ── Exercise 1: Create Custom Generator & Filter ──────────────────
# Task: Create a generator that yields transactions from a list.
#       Filter only those with amount > ₹5000.
#
# Requirements:
#   - Define transaction_generator(transactions) that yields each one
#   - Define filter_by_amount(generator, threshold) that filters
#   - Chain them together
#   - Consume using islice() or list()
#
# Hint: Use yield to make a generator. Chain with another generator.

# --- your code here ---




# ── Exercise 2: Risk Score Pipeline ────────────────────────────────
# Task: Build a pipeline: generate → add_risk_score → filter_high_risk
#
# Requirements:
#   - Generator that yields transactions
#   - Compute risk_score based on amount (>1000: +10pts, >5000: +20pts)
#   - Filter only risk_score >= 20
#   - Materialize top 5 with islice()
#
# Hint: Risk score should be cumulative. Use islice for top N.

# --- your code here ---




# ── Exercise 3: Memory Efficiency Comparison ──────────────────────
# Task: Simulate processing 100,000 transactions.
#       Compare memory usage: list vs generator.
#
# Requirements:
#   - Generate 100,000 transactions using generator
#   - Process them through a filter pipeline
#   - Compare memory: loading all vs lazy
#   - Print memory estimate (rough calculation)
#
# Hint: sys.getsizeof() can estimate object size. Generators don't
#       store all data, so memory should be minimal.

# --- your code here ---




# ───────────────────────────────────────────────────────────────
# Expected outputs (for self-check):
#
# Ex1: Filtered transactions
#      Only show those > ₹5000
#      Count should be reasonable subset
#
# Ex2: Risk pipeline top 5
#      All have risk_score >= 20
#      Sorted by score (descending)
#
# Ex3: Memory comparison
#      Estimate: list ≈ 50MB, generator ≈ 0.5KB
#      Generator is ~100x more memory-efficient
# ───────────────────────────────────────────────────────────────
