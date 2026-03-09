# ============================================================
#  ITERATING DICTIONARIES
#  Real-world context: Sales analytics dashboard
# ============================================================

monthly_sales = {
    "Jan": 125000,
    "Feb":  98000,
    "Mar": 145000,
    "Apr": 132000,
    "May": 167000,
    "Jun": 112000,
}

# ============================================================
#  1. Iterate over KEYS (default)
# ============================================================

print("=== Iterating Keys ===")
for month in monthly_sales:
    print(f"  {month}", end="  ")
print()

# Explicitly using .keys()
for month in monthly_sales.keys():
    print(f"  Month: {month}")

# ============================================================
#  2. Iterate over VALUES
# ============================================================

print("\n=== Iterating Values ===")
total = 0
for revenue in monthly_sales.values():
    total += revenue
print(f"  Total annual revenue: ₹{total:,}")
print(f"  Monthly average     : ₹{total // len(monthly_sales):,}")

# ============================================================
#  3. Iterate over KEY-VALUE pairs with .items()
# ============================================================

print("\n=== Iterating Items ===")
print(f"  {'Month':<6}  {'Revenue':>12}  {'Bar'}")
print("  " + "-" * 40)
for month, revenue in monthly_sales.items():
    bar = "█" * (revenue // 10000)
    print(f"  {month:<6}  ₹{revenue:>10,}  {bar}")

# ============================================================
#  4. Enumerate with dict (adding position/rank)
# ============================================================

print("\n=== enumerate() with dict ===")
for i, (month, revenue) in enumerate(monthly_sales.items(), 1):
    print(f"  Q{i}  {month}: ₹{revenue:,}")

# ============================================================
#  5. Filter while iterating — DO NOT modify size during loop
# ============================================================

print("\n=== Safe Filtering ===")

inventory = {"Apple": 50, "Banana": 0, "Mango": 30, "Grapes": 0, "Kiwi": 15}

# WRONG: modifying dict size during iteration → RuntimeError
# for k, v in inventory.items():
#     if v == 0:
#         del inventory[k]  ← DON'T DO THIS

# CORRECT: iterate over a copy, or use dict comprehension
in_stock = {k: v for k, v in inventory.items() if v > 0}
print("In-stock items:", in_stock)

# Remove out-of-stock from original
out_of_stock = [k for k, v in inventory.items() if v == 0]
for k in out_of_stock:
    del inventory[k]
print("After cleanup  :", inventory)

# ============================================================
#  6. Sorted iteration
# ============================================================

print("\n=== Sorted Iteration ===")

# By key alphabetically
print("By month (alpha):")
for month in sorted(monthly_sales):
    print(f"  {month}: ₹{monthly_sales[month]:,}")

# By value descending (best sales first)
print("\nBy revenue (highest first):")
for month, rev in sorted(monthly_sales.items(), key=lambda x: x[1], reverse=True):
    print(f"  {month}: ₹{rev:,}")

# ============================================================
#  7. Dictionary comprehension (transform)
# ============================================================

print("\n=== Dict Comprehension ===")

# Convert revenue from absolute to % of total
total_rev = sum(monthly_sales.values())
revenue_pct = {
    month: round((rev / total_rev) * 100, 1)
    for month, rev in monthly_sales.items()
}
print("Revenue share (%):", revenue_pct)

# Convert all keys to uppercase
upper_keys = {k.upper(): v for k, v in monthly_sales.items()}
print("Uppercase keys   :", upper_keys)

# ============================================================
#  8. zip() two dicts together
# ============================================================

print("\n=== Comparing Two Periods ===")

last_year = {"Jan": 110000, "Feb": 95000, "Mar": 130000}
this_year = {"Jan": 125000, "Feb":  98000, "Mar": 145000}

print(f"  {'Month':<6}  {'Last Year':>12}  {'This Year':>12}  {'Growth':>8}")
print("  " + "-" * 46)
for month in last_year:
    ly = last_year[month]
    ty = this_year.get(month, 0)
    growth = ((ty - ly) / ly) * 100
    arrow = "▲" if growth > 0 else "▼"
    print(f"  {month:<6}  ₹{ly:>10,}  ₹{ty:>10,}  {arrow}{abs(growth):>5.1f}%")

# ============================================================
#  KEY POINTS
#  for k in d         → iterates keys
#  for v in d.values()→ iterates values
#  for k,v in d.items()→ key-value pairs (most common)
#  sorted(d.items(), key=...) → sorted iteration
#  {k:v for k,v in d.items() if condition} → filter/transform
# ============================================================
