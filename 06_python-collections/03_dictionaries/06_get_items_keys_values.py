# ============================================================
#  get(), items(), keys(), values() — Deep Dive
#  Real-world context: Inventory & order processing system
# ============================================================

inventory = {
    "laptop"     : {"price": 65000, "stock": 15, "category": "Electronics"},
    "mouse"      : {"price":  1500, "stock": 80, "category": "Electronics"},
    "chair"      : {"price":  8000, "stock": 25, "category": "Furniture"},
    "desk"       : {"price": 12000, "stock": 10, "category": "Furniture"},
    "notebook"   : {"price":    80, "stock": 200,"category": "Stationery"},
    "pen"        : {"price":    20, "stock": 500,"category": "Stationery"},
}

# ============================================================
#  .keys() — all dictionary keys
# ============================================================

print("=== .keys() ===")

all_products = list(inventory.keys())
print("All products:", all_products)

# Check if product exists before processing
def get_product_price(product_name):
    if product_name in inventory.keys():   # same as: if product_name in inventory
        return inventory[product_name]["price"]
    return None

print("Laptop price :", get_product_price("laptop"))
print("TV price     :", get_product_price("tv"))

# keys() is iterable — use directly in loops
print("\nAvailable products:")
for product in inventory.keys():
    print(f"  - {product}")

# ============================================================
#  .values() — all dictionary values
# ============================================================

print("\n=== .values() ===")

# Total inventory value
total_value = sum(
    item["price"] * item["stock"]
    for item in inventory.values()
)
print(f"Total inventory value: ₹{total_value:,}")

# Find categories
all_categories = {item["category"] for item in inventory.values()}
print("Categories:", all_categories)

# Find out-of-stock (stock == 0) — from values
low_stock_items = [
    product
    for product, details in inventory.items()
    if details["stock"] < 20
]
print("Low stock items (<20):", low_stock_items)

# ============================================================
#  .items() — key-value pairs (most powerful for iteration)
# ============================================================

print("\n=== .items() ===")

# Formatted product list
print(f"{'Product':<15} {'Price':>8}  {'Stock':>6}  {'Category'}")
print("-" * 50)
for name, details in inventory.items():
    print(f"{name:<15} ₹{details['price']:>7,}  {details['stock']:>6}  {details['category']}")

# Filter by category
print("\nElectronics only:")
electronics = {k: v for k, v in inventory.items() if v["category"] == "Electronics"}
for name, details in electronics.items():
    print(f"  {name}: ₹{details['price']:,}  (stock: {details['stock']})")

# ============================================================
#  .get() — safe access patterns
# ============================================================

print("\n=== .get() Patterns ===")

order = {"product": "tablet", "quantity": 2}

# Pattern 1: Default for missing config
timeout = order.get("timeout", 30)
print(f"Timeout: {timeout}s (default used)")

# Pattern 2: Conditional processing
def process_order(order, inventory):
    product  = order["product"]
    quantity = order["quantity"]

    # Safe lookup
    item = inventory.get(product)
    if item is None:
        return f"ERROR: '{product}' not found in inventory"

    if item["stock"] < quantity:
        return f"ERROR: Only {item['stock']} units of '{product}' available"

    total = item["price"] * quantity
    return f"ORDER OK: {quantity}x {product} = ₹{total:,}"

print(process_order({"product": "mouse",  "quantity": 3}, inventory))
print(process_order({"product": "tablet", "quantity": 1}, inventory))
print(process_order({"product": "laptop", "quantity": 20}, inventory))

# Pattern 3: Accumulate with get()
word_count = {}
text = "to be or not to be that is the question to be"
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1

print("\nWord count:", dict(sorted(word_count.items(), key=lambda x: -x[1])))

# ============================================================
#  Converting between views and types
# ============================================================

print("\n=== View Conversions ===")

print("list of keys  :", list(inventory.keys()))
print("set of keys   :", set(inventory.keys()))
print("first key     :", next(iter(inventory)))

# Convert items to list of tuples
items_list = list(inventory.items())
print("\nFirst item (as tuple):", items_list[0][0], "→", items_list[0][1])

# ============================================================
#  KEY POINTS
#  .keys()   → view of keys; use 'in' for existence checks
#  .values() → view of values; use for aggregation
#  .items()  → view of (k,v) pairs; best for iteration
#  .get(k, default) → safe; returns default if key missing
#  All three return VIEWS (live), not copies
# ============================================================
