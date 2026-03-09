# ─────────────────────────────────────────────
# Exercises — yield
# ─────────────────────────────────────────────

# ── Exercise 1: Running average ───────────────
# Real-life: monitoring a live sensor dashboard
# Write a generator running_average(numbers) that yields the
# cumulative average after each new number is consumed.

readings = [10, 20, 30, 40, 50]

# --- your code here ---
# for avg in running_average(readings):
#     print(f"{avg:.1f}")


# Expected output:
# 10.0
# 15.0
# 20.0
# 25.0
# 30.0


# ── Exercise 2: yield from — flatten nested list ──
# Real-life: normalising nested JSON arrays from an API response
# Write a generator deep_flatten(nested) that yields every
# non-list value from an arbitrarily nested list.

nested = [1, [2, 3], [4, [5, 6]], [[7], 8], 9]

# --- your code here ---
# print(list(deep_flatten(nested)))


# Expected output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


# ── Exercise 3: Countdown with side effects ───
# Real-life: launch sequence controller
# Write a generator launch_sequence(n) that:
#   - yields each number from n down to 1
#   - after yielding 1, prints "Liftoff!" (no more yields)

# --- your code here ---
# for step in launch_sequence(5):
#     print(step)


# Expected output:
# 5
# 4
# 3
# 2
# 1
# Liftoff!


# ── Exercise 4: yield from for merging sources ─
# Real-life: consolidating reports from multiple departments
# Write a generator all_reports(*departments) where each
# department is a list of report strings.
# Use yield from to yield every report across all departments.

engineering = ["ENG-001: API latency report", "ENG-002: DB index report"]
marketing   = ["MKT-001: Q1 campaign results"]
finance     = ["FIN-001: Monthly P&L", "FIN-002: Budget forecast", "FIN-003: Tax summary"]

# --- your code here ---
# for report in all_reports(engineering, marketing, finance):
#     print(report)


# Expected output:
# ENG-001: API latency report
# ENG-002: DB index report
# MKT-001: Q1 campaign results
# FIN-001: Monthly P&L
# FIN-002: Budget forecast
# FIN-003: Tax summary


# ── Exercise 5: Branching yield — order status ─
# Real-life: order fulfilment pipeline status messages
# Write a generator order_status(order) where order is a dict
# with keys: "paid", "in_stock", "shipped".
# Yield status messages based on the order's state:
#   - if not paid:       yield "Awaiting payment"
#   - if paid but no stock: yield "Payment received", "Out of stock — on backorder"
#   - if paid + stock but not shipped: yield "Payment received", "Packed", "Awaiting dispatch"
#   - if all True:       yield "Payment received", "Packed", "Shipped", "Complete"

orders = [
    {"paid": False, "in_stock": True,  "shipped": False},
    {"paid": True,  "in_stock": False, "shipped": False},
    {"paid": True,  "in_stock": True,  "shipped": False},
    {"paid": True,  "in_stock": True,  "shipped": True},
]

# --- your code here ---
# for i, order in enumerate(orders, 1):
#     print(f"\nOrder {i}:")
#     for status in order_status(order):
#         print(f"  → {status}")


# Expected output:
# Order 1:
#   → Awaiting payment
# Order 2:
#   → Payment received
#   → Out of stock — on backorder
# Order 3:
#   → Payment received
#   → Packed
#   → Awaiting dispatch
# Order 4:
#   → Payment received
#   → Packed
#   → Shipped
#   → Complete


# ─────────────────────────────────────────────
# Self-check:
# Ex1: 5 averages printed
# Ex2: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Ex3: 5 down to 1 then "Liftoff!"
# Ex4: 6 report lines in order
# Ex5: 4 order statuses, varying lengths
# ─────────────────────────────────────────────
