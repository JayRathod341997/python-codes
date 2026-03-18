# Solutions — Project 06: Retail Inventory OOP

class Product:
    def __init__(self, sku, name, category, price, initial_stock=0):
        self.sku = sku
        self.name = name
        self.category = category
        self.price = price
        self._stock = initial_stock

    @property
    def stock(self):
        return self._stock

    @property.setter
    def stock(self, value):
        if value < 0:
            raise ValueError(f"Stock cannot be negative. Got {value}")
        self._stock = value

class Warehouse:
    def __init__(self, warehouse_name):
        self.name = warehouse_name
        self.products = {}

    def add_product(self, product):
        self.products[product.sku] = product

    def restock(self, sku, quantity):
        if sku not in self.products:
            raise ValueError(f"Product {sku} not found")
        self.products[sku].stock += quantity

    def sell(self, sku, quantity):
        if sku not in self.products:
            raise ValueError(f"Product {sku} not found")
        if quantity > self.products[sku].stock:
            raise ValueError(f"Insufficient stock")
        self.products[sku].stock -= quantity

    def get_reorder_report(self, threshold=10):
        return [(p.sku, p.name, p.stock, threshold) for p in self.products.values() if p.stock < threshold]

print("\n" + "="*70)
print("EXERCISE 1 SOLUTION: Warehouse with 3 Products")
print("="*70 + "\n")

w = Warehouse("Test Warehouse")
p1 = Product("TEA001", "Tea (500g)", "Beverages", 180, 20)
p2 = Product("COFFEE001", "Coffee (250g)", "Beverages", 350, 15)
p3 = Product("SUGAR001", "Sugar (1kg)", "Groceries", 40, 30)

w.add_product(p1)
w.add_product(p2)
w.add_product(p3)

w.sell("TEA001", 5)
w.sell("COFFEE001", 8)
w.sell("SUGAR001", 10)
w.restock("TEA001", 15)

print("Final Inventory:")
for sku, p in w.products.items():
    print(f"  {sku}: {p.name:<20} ₹{p.price:>6} × {p.stock:>3}")

print("\n" + "="*70)
print("EXERCISE 2 SOLUTION: Negative Stock Validation")
print("="*70 + "\n")

p = Product("TEST001", "Test Product", "Test", 100, 10)
try:
    p.stock = -5
except ValueError as e:
    print(f"✓ ValueError caught: {e}")
    print(f"  Current stock (unchanged): {p.stock}")

print("\n" + "="*70)
print("EXERCISE 3 SOLUTION: Reorder Planning")
print("="*70 + "\n")

w2 = Warehouse("Main Warehouse")
products = [
    Product("P001", "Product A", "Cat1", 100, 25),
    Product("P002", "Product B", "Cat1", 150, 8),
    Product("P003", "Product C", "Cat2", 200, 12),
    Product("P004", "Product D", "Cat2", 120, 3),
    Product("P005", "Product E", "Cat3", 80, 18),
]

for p in products:
    w2.add_product(p)

w2.sell("P001", 10)
w2.sell("P002", 3)
w2.sell("P003", 5)
w2.sell("P004", 1)

report = w2.get_reorder_report(threshold=15)
print(f"Items below threshold (15):")
total_to_reorder = 0
for sku, name, stock, threshold in report:
    needed = threshold - stock
    total_to_reorder += needed
    print(f"  {sku}: {name:<20} Stock: {stock:>2}, Need: {needed:>2}")

print(f"\nTotal quantity to reorder: {total_to_reorder}")
print("\n" + "="*70 + "\n")
