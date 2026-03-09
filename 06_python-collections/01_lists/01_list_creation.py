# ============================================================
#  LIST CREATION
#  Real-world context: Building a grocery shopping app
# ============================================================

# --- 1. Empty list (cart starts empty) ---
cart = []
print("Empty cart:", cart)

# --- 2. List with initial items ---
grocery_list = ["milk", "eggs", "bread", "butter", "cheese"]
print("Grocery list:", grocery_list)

# --- 3. List with mixed types (product name, price, in-stock) ---
product = ["Apple", 0.99, True]
print("Product info [name, price, in_stock]:", product)

# --- 4. list() constructor from a string ---
letters = list("PYTHON")
print("Letters:", letters)

# --- 5. list() from range (aisle numbers) ---
aisles = list(range(1, 11))
print("Aisle numbers:", aisles)

# --- 6. List multiplication (default weekly meal plan) ---
default_day = ["salad"]
weekly_plan = default_day * 7
print("Weekly plan:", weekly_plan)

# --- 7. List comprehension (prices after 10% discount) ---
original_prices = [10.0, 25.5, 8.0, 15.75, 30.0]
discounted = [round(p * 0.9, 2) for p in original_prices]
print("Discounted prices:", discounted)

# --- 8. Nested list (store inventory: [product, qty, price]) ---
inventory = [
    ["Apple",  150, 0.99],
    ["Banana",  80, 0.49],
    ["Mango",   40, 1.29],
]
print("\nStore Inventory:")
for item in inventory:
    print(f"  {item[0]:<10} qty={item[1]}  price=${item[2]}")

# --- 9. Checking type and length ---
print("\nType:", type(grocery_list))
print("Number of items:", len(grocery_list))

# ============================================================
#  KEY POINTS
#  - Lists are ordered, mutable, and allow duplicates
#  - Created with [], list(), list comprehension, or range()
#  - Can hold any mix of data types
# ============================================================
