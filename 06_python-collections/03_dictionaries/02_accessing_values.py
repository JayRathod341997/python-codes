# ============================================================
#  ACCESSING VALUES
#  Real-world context: E-commerce product catalog
# ============================================================

product = {
    "id"          : "PROD-001",
    "name"        : "Wireless Headphones",
    "brand"       : "SoundMax",
    "price"       : 2999.00,
    "stock"       : 45,
    "rating"      : 4.3,
    "tags"        : ["audio", "wireless", "premium"],
    "in_stock"    : True,
}

# ============================================================
#  Method 1: Square bracket []
# ============================================================

print("=== Square Bracket Access ===")
print("Name  :", product["name"])
print("Price : ₹", product["price"])
print("Tags  :", product["tags"])

# Access first tag
print("Tag[0]:", product["tags"][0])

# KeyError if key doesn't exist
try:
    print(product["discount"])
except KeyError as e:
    print(f"KeyError: {e} — key not found")

# ============================================================
#  Method 2: .get() — SAFE access, returns None or default
# ============================================================

print("\n=== .get() Safe Access ===")

print("Rating   :", product.get("rating"))        # exists
print("Discount :", product.get("discount"))       # missing → None
print("Discount%:", product.get("discount", 0))    # missing → 0 (default)
print("Color    :", product.get("color", "N/A"))   # missing → "N/A"

# ============================================================
#  Checking if a key exists before accessing
# ============================================================

print("\n=== Key Existence Check ===")

# Using 'in' keyword
if "price" in product:
    print(f"Price is ₹{product['price']}")

if "discount" not in product:
    print("No discount available")

# Pattern: get() with default vs if-in check
def get_discounted_price(p):
    discount = p.get("discount_pct", 0)
    return p["price"] * (1 - discount / 100)

print(f"Final price: ₹{get_discounted_price(product):.2f}")

# ============================================================
#  Updating values
# ============================================================

print("\n=== Updating Values ===")

print("Stock before:", product["stock"])
product["stock"] -= 5        # customer bought 5 units
print("Stock after :", product["stock"])

product["price"] = 2749.00   # price change
print("New price   : ₹", product["price"])

product["discount_pct"] = 10  # add new key
print("Added discount:", product["discount_pct"], "%")

# ============================================================
#  update() method — update multiple keys at once
# ============================================================

print("\n=== .update() ===")

updates = {"price": 2499.00, "stock": 100, "rating": 4.5}
product.update(updates)
print("After bulk update:")
print(f"  Price: ₹{product['price']}  Stock: {product['stock']}  Rating: {product['rating']}")

# update() can also use keyword arguments
product.update(brand="SoundMax Pro", in_stock=True)
print(f"  Brand: {product['brand']}")

# ============================================================
#  Deleting keys
# ============================================================

print("\n=== Deleting Keys ===")

# del — raises KeyError if missing
del product["discount_pct"]
print("After del discount_pct:", "discount_pct" in product)

# pop() — returns value, optional default
removed_val = product.pop("rating", "N/A")
print(f"Popped rating: {removed_val}")
print("After pop    :", "rating" in product)

# Safe delete if might not exist
product.pop("non_existent_key", None)   # no error

# ============================================================
#  KEY POINTS
#  - d[key]        → direct access (KeyError if missing)
#  - d.get(key, x) → safe access (returns x if missing)
#  - key in d      → existence check
#  - d[key] = val  → add/update
#  - d.update({})  → bulk update
#  - del d[key]    → remove (error if missing)
#  - d.pop(key, x) → remove and return (safe with default)
# ============================================================
