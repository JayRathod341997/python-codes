# ─────────────────────────────────────────────
# Exercises — Debugging Basics
# ─────────────────────────────────────────────
# Each exercise contains BUGGY code.
# Your job: identify the bug, fix it, and explain it in a comment.

# ── Exercise 1: Fix the NameError ────────────
# Real-life: Shipping cost calculator
# The function below crashes. Fix it.

def calculate_shipping(weight_kg, distance_km):
    base_rate  = 10          # ₹ per kg
    dist_rate  = 0.5         # ₹ per km
    cost = weight * base_rate + distance_km * dist_rate   # ← bug here
    return cost

# print(calculate_shipping(5, 200))   # uncomment after fix
# Expected: 150.0

# Bug explanation: ___________________________________________________


# ── Exercise 2: Fix the TypeError ────────────
# Real-life: Invoice formatter
# The function crashes with a TypeError on some inputs. Fix it.

def format_invoice(order_id, total, discount):
    net = total - discount
    line = "Order #" + order_id + " | Net: ₹" + net    # ← bug here
    return line

# print(format_invoice("1042", 5000, 500))   # uncomment after fix
# Expected: "Order #1042 | Net: ₹4500"

# Bug explanation: ___________________________________________________


# ── Exercise 3: Fix the IndexError ───────────
# Real-life: Leaderboard display
# Shows top-3 from a scores list — crashes when fewer than 3 entries.

def show_top3(scores):
    scores_sorted = sorted(scores, reverse=True)
    print("🥇", scores_sorted[0])
    print("🥈", scores_sorted[1])
    print("🥉", scores_sorted[2])   # ← crashes on short list

# show_top3([9500, 8700, 7100, 6300])  # works
# show_top3([9500, 8700])              # crashes — fix this

# Fix: handle fewer than 3 entries gracefully.
# Expected for [9500, 8700]: show only 2 places, no crash.

# --- your fix here ---


# ── Exercise 4: Fix the Logic Bug with assert ─
# Real-life: Percentage-off discount function
# The function produces wrong results. Add assert statements to
# catch the bug, then fix the calculation.

def apply_discount(price, pct_off):
    # Bug: pct_off of 20 should mean 20%, not 20x
    discounted = price - (price * pct_off)   # ← wrong
    return discounted

# Clue: apply_discount(1000, 20) returns -19000, expected 800.
# Step 1: Add asserts to catch unrealistic results.
# Step 2: Fix the formula.

# --- your fix here ---

# print(apply_discount(1000, 20))   # Expected: 800.0


# ── Exercise 5: Add Logging to a Pipeline ────
# Real-life: ETL data processing
# Replace all print() calls with proper logging at the right levels.
# Rules:
#   - "Starting ..." → logging.info
#   - "Skipping ..."  → logging.warning
#   - "Error ..."     → logging.error
#   - "Processed ..." → logging.info
#   - "Done ..."      → logging.info
#   - Value details   → logging.debug

import logging

# Configure logging format: "LEVEL | message"
# --- configure logging here ---

def etl_pipeline(records):
    print("Starting ETL pipeline")                           # → info
    processed = 0
    for i, record in enumerate(records):
        print(f"  Record {i}: {record}")                    # → debug
        if not isinstance(record.get("value"), (int, float)):
            print(f"  Skipping record {i}: invalid value")  # → warning
            continue
        if record["value"] < 0:
            print(f"  Error in record {i}: negative value") # → error
            continue
        processed += 1
    print(f"Done. Processed {processed}/{len(records)} records")  # → info

records = [
    {"id": 1, "value": 100},
    {"id": 2, "value": "bad"},
    {"id": 3, "value": -50},
    {"id": 4, "value": 250},
]

# Replace print() with logging calls, then run:
# etl_pipeline(records)


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: 150.0
# Ex2: "Order #1042 | Net: ₹4500"
# Ex3: Shows only available places, no crash
# Ex4: 800.0 (with assert verifying 0 ≤ discounted ≤ price)
# Ex5: Proper log lines at correct levels
# ─────────────────────────────────────────────
