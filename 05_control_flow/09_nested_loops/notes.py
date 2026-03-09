# ─────────────────────────────────────────────
# Nested Loops
# ─────────────────────────────────────────────

# A nested loop is a loop INSIDE another loop.
# The inner loop runs COMPLETELY for each iteration of the outer loop.

# ── Syntax ───────────────────────────────────
# for outer in outer_iterable:
#     for inner in inner_iterable:
#         <block>

# ── Real-life: Multiplication table ──────────
print("Multiplication Table (1–5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:4}", end="")   # end="" stays on same line
    print()                         # newline after each row

# ── Real-life: Seating chart ─────────────────
# Cinema hall — rows A-E, seats 1-8
print("\nCinema Seating Chart:")
rows  = ["A", "B", "C", "D", "E"]
seats = range(1, 9)

for row in rows:
    for seat in seats:
        print(f"{row}{seat}", end="  ")
    print()

# ── Real-life: Order × Product inventory ─────
# Checking which items in multiple orders are out of stock
orders = [
    {"order_id": "O1", "items": ["Laptop", "Mouse"]},
    {"order_id": "O2", "items": ["Phone", "Charger", "Headphones"]},
    {"order_id": "O3", "items": ["Tablet", "Keyboard"]},
]
out_of_stock = {"Charger", "Keyboard"}

print("\nOrder Fulfillment Check:")
for order in orders:
    print(f"  Order {order['order_id']}:")
    for item in order["items"]:
        status = "⛔ OUT OF STOCK" if item in out_of_stock else "✓ Available"
        print(f"    {item:<15} {status}")

# ── Real-life: Matrix operations ─────────────
# 2D data grid (e.g., spreadsheet, sensor grid)
sensor_grid = [
    [22.1, 21.8, 23.0],
    [19.5, 20.2, 21.0],
    [25.3, 24.8, 26.1],
]

print("\nSensor Grid (row, col) readings:")
for row_idx, row in enumerate(sensor_grid):
    for col_idx, temp in enumerate(row):
        alert = " ← HIGH!" if temp > 25 else ""
        print(f"  [{row_idx},{col_idx}] = {temp:.1f}°C{alert}")

# ── Real-life: Timetable generator ───────────
days    = ["Mon", "Tue", "Wed", "Thu", "Fri"]
periods = ["9–10 AM", "10–11 AM", "11–12 PM", "2–3 PM"]
subjects = ["Math", "Science", "English", "History"]

print("\nWeekly Timetable:")
header = f"{'Period':<12}" + "".join(f"{d:<10}" for d in days)
print(header)
print("─" * len(header))

for period, subject in zip(periods, subjects):
    row = f"{period:<12}"
    for day in days:
        row += f"{subject:<10}"
    print(row)

# ── break in nested loops — inner only ───────
# break only exits the INNER loop, not the outer!
print("\nSearching grid for value 20.2:")
target = 20.2
found  = False

for r, row in enumerate(sensor_grid):
    for c, val in enumerate(row):
        if val == target:
            print(f"  Found {target} at position [{r},{c}]")
            found = True
            break           # exits inner loop only
    if found:
        break               # exits outer loop

# ── Pattern printing (classic nested loop problem) ──
# Real-life concept: understanding iteration order
print("\nRight-angle triangle pattern:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# ── Time complexity note ─────────────────────
# Nested loops: O(n * m) — for n=outer size, m=inner size
# Three levels: O(n * m * k) — use only when necessary
# Prefer flattening data or using list comprehensions for performance

# ── Key points ───────────────────────────────
# • Inner loop runs completely for each outer iteration
# • break only exits the INNERMOST loop it's in
# • Nested loops are natural for 2D data (grids, matrices, tables)
# • Beyond 2–3 levels, extract inner loops into functions for clarity
