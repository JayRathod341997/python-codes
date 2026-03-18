# ─────────────────────────────────────────────────────────────────
# Project 11 — Finance — Risk Pipeline with Generators
# Concepts  : generators, yield, generator chaining, itertools
# Difficulty: Advanced
# ─────────────────────────────────────────────────────────────────

import itertools
from itertools import islice

print("\n" + "="*75)
print("FINANCIAL RISK SCREENING PIPELINE")
print("="*75)

# ── Section 1: Transaction Generator ───────────────────────────────
def generate_transactions(n=10000):
    """Generate n simulated transactions (lazy evaluation)."""
    import random
    for i in range(n):
        yield {
            "id": i + 1,
            "amount": random.uniform(100, 50000),
            "customer_id": random.randint(1000, 5000),
        }

print(f"\nGenerating 10,000 transactions lazily (not all in memory)...")

# ── Section 2: Pipeline Stages (Generators) ────────────────────────

def filter_large_amounts(transactions, threshold=10000):
    """Filter transactions > threshold."""
    for t in transactions:
        if t["amount"] > threshold:
            yield t

def flag_round_numbers(transactions):
    """Flag suspicious round-number amounts (e.g., 5000.00, 10000.00)."""
    for t in transactions:
        amount = t["amount"]
        if amount % 100 == 0:  # Round to nearest 100
            t["is_round"] = True
            yield t
        else:
            t["is_round"] = False
            yield t

def compute_risk_score(transactions):
    """Compute risk score based on patterns."""
    for t in transactions:
        score = 0
        if t["amount"] > 5000:
            score += 20
        if t.get("is_round", False):
            score += 30
        t["risk_score"] = score
        yield t

def filter_high_risk(transactions, threshold=30):
    """Filter only high-risk transactions."""
    for t in transactions:
        if t["risk_score"] >= threshold:
            yield t

# ── Section 3: Assemble the Pipeline ───────────────────────────────
print("Pipeline: Generate → Filter Large → Flag Round → Score Risk → Filter High Risk")
print("─" * 75)

# Chain generators together
raw_transactions = generate_transactions(10000)
large_transactions = filter_large_amounts(raw_transactions, threshold=5000)
flagged = flag_round_numbers(large_transactions)
scored = compute_risk_score(flagged)
high_risk = filter_high_risk(scored, threshold=30)

# Materialize only top 10 using islice
print("\nTop 10 HIGH-RISK transactions:")
print(f"{'ID':<8} {'Amount':>12} {'Round?':>8} {'Risk Score':>12}")
print("─" * 75)

for i, transaction in enumerate(islice(high_risk, 10), start=1):
    is_round = "Yes" if transaction.get("is_round", False) else "No"
    print(f"{transaction['id']:<8} ₹{transaction['amount']:>11,.0f} {is_round:>8} {transaction['risk_score']:>12}")

# ── Section 4: Memory Efficiency Comment ───────────────────────────
print("\n" + "="*75)
print("MEMORY EFFICIENCY:")
print("  Traditional approach: Load 10,000 transactions in memory → ✗ Memory intensive")
print("  Generator pipeline: Process 1 at a time, keep only filtered → ✓ Memory efficient")
print("="*75 + "\n")
