# ============================================================
#  SOLUTION 1 — Lists
#  Scenario: Online Food Delivery Order System
# ============================================================

order = ["Burger", "Pizza", "Fries", "Coke", "Salad"]
prices = [5.99, 8.99, 2.49, 1.99, 4.49]

# ---- Task 1: append "Ice Cream" ----
order.append("Ice Cream")
print("Task 1:", order)

# ---- Task 2: insert "Water" at index 4 ----
order.insert(4, "Water")
print("Task 2:", order)

# ---- Task 3: remove "Salad" ----
order.remove("Salad")
print("Task 3:", order)

# ---- Task 4: first and last item ----
print("Task 4 — First:", order[0], "| Last:", order[-1])

# ---- Task 5: 15% discount on prices > 5.0 ----
final_prices = [round(p * 0.85, 2) if p > 5.0 else p for p in prices]
print("Task 5 — Final prices:", final_prices)

# ---- Task 6: 3 most expensive items ----
# Pair items with their prices, sort by price descending, take first 3
paired = list(zip(order[:len(prices)], prices))
paired_sorted = sorted(paired, key=lambda x: x[1], reverse=True)
top3 = [item for item, _ in paired_sorted[:3]]
print("Task 6 — Top 3 expensive:", top3)

# ---- Task 7: count "Pizza" ----
order_history = ["Burger", "Pizza", "Pizza", "Fries", "Pizza", "Coke"]
pizza_count = order_history.count("Pizza")
print("Task 7 — Pizza ordered:", pizza_count, "times")

# ---- Task 8: reverse in-place ----
order.reverse()
print("Task 8 — Reversed:", order)

# ---- Task 9: copy and verify ----
backup_order = order.copy()
backup_order.append("Garlic Bread")
print("Task 9 — Original:", order)
print("Task 9 — Backup  :", backup_order)
print("Task 9 — Same object?", order is backup_order)

# ---- Task 10: sort seating by order_count desc ----
seating = [
    ["Alice", 1, 3],
    ["Bob",   2, 1],
    ["Carol", 3, 5],
    ["Dave",  4, 2],
]
seating.sort(key=lambda x: x[2], reverse=True)
print("Task 10 — Sorted seating:")
for row in seating:
    print(f"  {row[0]:<8} Table {row[1]}  Orders: {row[2]}")
