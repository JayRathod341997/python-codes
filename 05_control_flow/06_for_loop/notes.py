# ─────────────────────────────────────────────
# for Loop
# ─────────────────────────────────────────────

# ── Syntax ───────────────────────────────────
# for <variable> in <iterable>:
#     <block>
#
# Iterates over ANY iterable: list, tuple, string, range, dict, file...

# ── Iterating a list ─────────────────────────
# Real-life: E-commerce order processing
orders = ["ORD001", "ORD002", "ORD003", "ORD004"]

for order in orders:
    print(f"Processing order: {order}")

# ── range() — numeric iteration ──────────────
# range(stop)         → 0 to stop-1
# range(start, stop)  → start to stop-1
# range(start, stop, step)

# Real-life: Generate invoice numbers
print("\nInvoice Numbers:")
for num in range(1001, 1006):
    print(f"  INV-{num}")

# Countdown using negative step
print("\nCountdown:")
for i in range(10, 0, -2):
    print(f"  {i}")

# ── enumerate() — index + value ───────────────
# Real-life: Leaderboard display
scores = [("Alice", 9850), ("Bob", 9720), ("Charlie", 9540)]

print("\nLeaderboard:")
for rank, (player, score) in enumerate(scores, start=1):
    print(f"  #{rank}  {player:<10} {score} pts")

# ── zip() — parallel iteration ───────────────
# Real-life: Matching students with their marks
students = ["Jay",   "Priya", "Rohan"]
marks    = [88,       92,      76]

print("\nReport:")
for student, mark in zip(students, marks):
    grade = "Pass" if mark >= 40 else "Fail"
    print(f"  {student}: {mark} → {grade}")

# ── Iterating a string ───────────────────────
# Real-life: Password strength — count special chars
password = "Hello@World#2024"
special  = 0

for char in password:
    if char in "!@#$%^&*":
        special += 1

print(f"\nSpecial characters in password: {special}")

# ── Iterating a dict ─────────────────────────
# Real-life: Shopping cart total
cart = {"Laptop": 55000, "Mouse": 1200, "Keyboard": 2500, "USB Hub": 899}

total = 0
print("\nCart:")
for item, price in cart.items():
    print(f"  {item:<12} ₹{price:>7,}")
    total += price

print(f"  {'─'*22}")
print(f"  {'Total':<12} ₹{total:>7,}")

# ── List comprehension (compact for loop) ─────
# Real-life: Price list after applying 18% GST
prices_excl_gst = [1000, 2500, 750, 4200]
prices_incl_gst = [round(p * 1.18, 2) for p in prices_excl_gst]
print(f"\nPrices incl. GST: {prices_incl_gst}")

# ── Nested comprehension ─────────────────────
# 3x3 multiplication table as a 2D list
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
for row in table:
    print(row)

# ── Key points ───────────────────────────────
# • for loop is preferred over while when the iterable is known
# • enumerate() when you need both index and value
# • zip() to iterate over two+ sequences in lockstep
# • dict.items() to iterate key-value pairs
# • List comprehensions replace simple for+append patterns
