# ───────────────────────────────────────────────────────────────
# Exercises — Project 06: Retail Inventory OOP
# ───────────────────────────────────────────────────────────────

# ── Exercise 1: Create Product Objects and Warehouse ──────────────
# Task: Define 3 new products and add them to a warehouse.
#       Then perform 2 sales and 1 restock operation.
#
# Requirements:
#   - Create Product objects: "Tea (500g)", "Coffee (250g)", "Sugar (1kg)"
#   - Create a warehouse and add them
#   - Sell some quantity from each
#   - Restock one product
#   - Print final inventory
#
# Hint: Copy the Product and Warehouse classes from solution.py.

# --- your code here ---




# ── Exercise 2: Property Setter Validation ─────────────────────
# Task: Test that negative stock raises ValueError.
#
# Requirements:
#   - Create a Product
#   - Try to set stock to a negative value
#   - Catch the ValueError and print the error message
#   - Verify that the operation was blocked
#
# Hint: Use try/except to catch the ValueError.

# --- your code here ---




# ── Exercise 3: Low Stock Analysis and Reorder Planning ─────────
# Task: Create a warehouse with 5 products. Simulate some sales.
#       Generate a reorder report showing which items need restocking.
#
# Requirements:
#   - Create 5 products with varying stock levels
#   - Perform multiple sales to deplete stock
#   - Set threshold to 15 and generate reorder report
#   - Calculate total quantity to reorder across all low-stock items
#
# Hint: Use warehouse.get_reorder_report() to get low-stock items.

# --- your code here ---




# ───────────────────────────────────────────────────────────────
# Expected outputs (for self-check):
#
# Ex1: Final inventory with 3 products after sales/restock
#      All 3 items listed with updated stock levels
#
# Ex2: ValueError caught when setting negative stock
#      Error message: "Stock cannot be negative..."
#
# Ex3: Reorder report for 5 products
#      Show items below threshold=15 with needed quantities
# ───────────────────────────────────────────────────────────────
