# ─────────────────────────────────────────────────────────────────
# Project 06 — Retail — Inventory Management with OOP
# Concepts  : classes, @property, @property.setter, raise ValueError
# Difficulty: Intermediate
# ─────────────────────────────────────────────────────────────────

# ── Section 1: Product Class ───────────────────────────────────────
class Product:
    """Represents a product in inventory."""

    def __init__(self, sku, name, category, price, initial_stock=0):
        self.sku = sku
        self.name = name
        self.category = category
        self.price = price
        self._stock = initial_stock  # Use underscore to indicate "private"

    # ── CONCEPT: @property decorator ───────────────────────────
    # Allows us to access _stock as product.stock (read-only getter)
    @property
    def stock(self):
        return self._stock

    # ── CONCEPT: @property.setter ────────────────────────────
    # Allows us to set stock with validation: product.stock = 100
    # If stock is negative, we raise ValueError (no silent failures)
    @property.setter
    def stock(self, value):
        if value < 0:
            raise ValueError(f"Stock cannot be negative. Got {value}")
        self._stock = value

    def __repr__(self):
        return f"Product(sku={self.sku}, name={self.name}, stock={self.stock})"


# ── Section 2: Warehouse Class ─────────────────────────────────────
class Warehouse:
    """Manages a collection of products."""

    def __init__(self, warehouse_name):
        self.name = warehouse_name
        self.products = {}  # Dict: sku -> Product object

    def add_product(self, product):
        """Add a product to the warehouse."""
        if product.sku in self.products:
            print(f"  Warning: Product {product.sku} already exists. Overwriting.")
        self.products[product.sku] = product

    def restock(self, sku, quantity):
        """Add quantity to stock for a product."""
        if sku not in self.products:
            raise ValueError(f"Product {sku} not found in warehouse")
        if quantity < 0:
            raise ValueError(f"Restock quantity must be non-negative. Got {quantity}")

        current = self.products[sku].stock
        self.products[sku].stock = current + quantity
        print(f"  Restocked {sku} ({self.products[sku].name}): +{quantity} → {self.products[sku].stock}")

    def sell(self, sku, quantity):
        """Reduce stock when a product is sold."""
        if sku not in self.products:
            raise ValueError(f"Product {sku} not found in warehouse")
        if quantity < 0:
            raise ValueError(f"Sell quantity must be non-negative. Got {quantity}")
        if quantity > self.products[sku].stock:
            raise ValueError(f"Cannot sell {quantity} of {sku}. Only {self.products[sku].stock} in stock.")

        current = self.products[sku].stock
        self.products[sku].stock = current - quantity
        print(f"  Sold {sku} ({self.products[sku].name}): -{quantity} → {self.products[sku].stock}")

    def get_reorder_report(self, threshold=10):
        """Return products below reorder threshold."""
        low_stock = []
        for sku, product in self.products.items():
            if product.stock < threshold:
                low_stock.append((product.sku, product.name, product.stock, threshold))
        return low_stock


# ── Section 3: Demo Usage ──────────────────────────────────────────
print("\n" + "="*70)
print("SUPERMARKET INVENTORY SYSTEM")
print("="*70)

# Create warehouse
warehouse = Warehouse("Delhi Central Warehouse")

# Create products
p1 = Product("SKU001", "Milk (1L)", "Dairy", 80, initial_stock=50)
p2 = Product("SKU002", "Bread", "Bakery", 40, initial_stock=30)
p3 = Product("SKU003", "Rice (5kg)", "Groceries", 250, initial_stock=8)
p4 = Product("SKU004", "Eggs (dozen)", "Dairy", 120, initial_stock=25)

# Add to warehouse
print("\n--- Adding products to warehouse ---")
warehouse.add_product(p1)
warehouse.add_product(p2)
warehouse.add_product(p3)
warehouse.add_product(p4)

# Display inventory
print("\n--- Initial Inventory ---")
for sku, product in warehouse.products.items():
    print(f"  {sku}: {product.name:<20} ₹{product.price:>6} × {product.stock:>3} = ₹{product.price * product.stock:>8,.0f}")

# ── Section 4: Operations ──────────────────────────────────────────
print("\n--- Sales Transactions ---")
warehouse.sell("SKU001", 15)  # Sell 15 milk
warehouse.sell("SKU002", 10)  # Sell 10 bread
warehouse.sell("SKU003", 2)   # Sell 2 rice
warehouse.sell("SKU004", 5)   # Sell 5 eggs

print("\n--- Restock Operations ---")
warehouse.restock("SKU001", 20)  # Restock milk
warehouse.restock("SKU003", 12)  # Restock rice

# ── Section 5: Reorder Report ──────────────────────────────────────
print("\n--- Low Stock Report (threshold: 10) ---")
low_stock_items = warehouse.get_reorder_report(threshold=10)
if low_stock_items:
    print(f"\n{'SKU':<10} {'Product':<20} {'Current Stock':>15} {'Threshold':>10} {'Action':>20}")
    print("─" * 75)
    for sku, name, stock, threshold in low_stock_items:
        needed = threshold - stock
        print(f"{sku:<10} {name:<20} {stock:>15} {threshold:>10} Order {needed:>10}")
else:
    print("  No items below reorder threshold.")

# ── Section 6: Final Inventory Value ───────────────────────────────
print("\n--- Final Inventory Value ---")
total_value = 0
for sku, product in warehouse.products.items():
    item_value = product.price * product.stock
    total_value += item_value
    print(f"  {sku}: {product.name:<20} ₹{product.price:>6} × {product.stock:>3} = ₹{item_value:>10,.0f}")

print(f"\n{'Total Inventory Value:':<40} ₹{total_value:>20,.0f}")

# ── Section 7: Error Handling ──────────────────────────────────────
print("\n--- Testing Error Handling ---")
try:
    warehouse.sell("SKU001", 100)  # Try to sell more than in stock
except ValueError as e:
    print(f"  Error caught: {e}")

try:
    warehouse.restock("SKU999", 50)  # Try to restock non-existent product
except ValueError as e:
    print(f"  Error caught: {e}")

try:
    p1.stock = -5  # Try to set negative stock via property
except ValueError as e:
    print(f"  Error caught: {e}")

print("\n" + "="*70 + "\n")

# ── KEY POINTS ──────────────────────────────────────────────────────
# 1. Classes model real-world entities (Product, Warehouse)
# 2. @property provides controlled access to internal state (_stock)
# 3. @property.setter enables validation (no negative stock)
# 4. Instance methods (restock, sell) bundle related operations
# 5. Raising exceptions ensures errors don't go unnoticed
# 6. Dict of objects (products dict) replaces parallel lists
# ────────────────────────────────────────────────────────────────────
