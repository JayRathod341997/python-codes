# ─────────────────────────────────────────────────────────────────
# Project 10 — Retail — Sales Analysis: Loops vs Comprehensions
# Concepts  : comprehensions, generators, nested structures
# Difficulty: Intermediate/Advanced
# ─────────────────────────────────────────────────────────────────

print("\n" + "="*75)
print("SALES ANALYSIS — ACT 1: Traditional Loops vs ACT 2: Comprehensions")
print("="*75)

# Sample data: 20 transactions
transactions = [
    {"product": "Laptop", "category": "Electronics", "qty": 1, "price": 45000, "region": "North", "salesperson": "Arun"},
    {"product": "Phone", "category": "Electronics", "qty": 2, "price": 15000, "region": "South", "salesperson": "Bhavna"},
    {"product": "Shirt", "category": "Clothing", "qty": 3, "price": 500, "region": "North", "salesperson": "Chirag"},
    {"product": "Snacks", "category": "Food", "qty": 5, "price": 100, "region": "East", "salesperson": "Deepika"},
    {"product": "Watch", "category": "Electronics", "qty": 1, "price": 8000, "region": "West", "salesperson": "Eshan"},
    {"product": "Jeans", "category": "Clothing", "qty": 4, "price": 800, "region": "South", "salesperson": "Fiona"},
    {"product": "Coffee", "category": "Food", "qty": 10, "price": 100, "region": "North", "salesperson": "Ganesh"},
    {"product": "Headphones", "category": "Electronics", "qty": 1, "price": 3000, "region": "East", "salesperson": "Hiral"},
    {"product": "Shoes", "category": "Clothing", "qty": 2, "price": 1500, "region": "West", "salesperson": "Iris"},
    {"product": "Tea", "category": "Food", "qty": 15, "price": 50, "region": "South", "salesperson": "Jatin"},
    {"product": "Monitor", "category": "Electronics", "qty": 1, "price": 12000, "region": "North", "salesperson": "Karan"},
    {"product": "Socks", "category": "Clothing", "qty": 20, "price": 50, "region": "East", "salesperson": "Laxmi"},
    {"product": "Chocolate", "category": "Food", "qty": 8, "price": 100, "region": "West", "salesperson": "Mihir"},
    {"product": "Keyboard", "category": "Electronics", "qty": 2, "price": 2500, "region": "South", "salesperson": "Nina"},
    {"product": "T-Shirt", "category": "Clothing", "qty": 5, "price": 400, "region": "North", "salesperson": "Omkar"},
    {"product": "Biscuits", "category": "Food", "qty": 12, "price": 75, "region": "East", "salesperson": "Priya"},
    {"product": "Tablet", "category": "Electronics", "qty": 1, "price": 20000, "region": "West", "salesperson": "Quentin"},
    {"product": "Hat", "category": "Clothing", "qty": 3, "price": 300, "region": "South", "salesperson": "Raj"},
    {"product": "Milk", "category": "Food", "qty": 20, "price": 50, "region": "North", "salesperson": "Sita"},
    {"product": "Speaker", "category": "Electronics", "qty": 1, "price": 5000, "region": "East", "salesperson": "Tarun"},
]

# ── ACT 1: Traditional for-loops (Like Projects 04 & 05) ──────────
print("\n─── ACT 1: Traditional for-loops ───\n")

# Filter Electronics
electronics_loop = []
for t in transactions:
    if t["category"] == "Electronics":
        electronics_loop.append(t)
print(f"Electronics products (loop): {len(electronics_loop)}")

# Total revenue by region (loop)
revenue_by_region_loop = {}
for t in transactions:
    revenue = t["qty"] * t["price"]
    region = t["region"]
    if region not in revenue_by_region_loop:
        revenue_by_region_loop[region] = 0
    revenue_by_region_loop[region] += revenue

print(f"Revenue by region (loop):")
for region, revenue in sorted(revenue_by_region_loop.items()):
    print(f"  {region}: ₹{revenue:>10,.0f}")

# ── ACT 2: Comprehensions (Pythonic!) ──────────────────────────────
print("\n─── ACT 2: Comprehensions (Pythonic!) ───\n")

# List comprehension: Filter Electronics
electronics_comp = [t for t in transactions if t["category"] == "Electronics"]
print(f"Electronics products (comp): {len(electronics_comp)}")

# Dict comprehension: Revenue by region (more complex)
revenue_by_region_comp = {
    region: sum(t["qty"] * t["price"] for t in transactions if t["region"] == region)
    for region in set(t["region"] for t in transactions)
}

print(f"Revenue by region (comp):")
for region, revenue in sorted(revenue_by_region_comp.items()):
    print(f"  {region}: ₹{revenue:>10,.0f}")

# ── Advanced: Nested Comprehensions ────────────────────────────────
print("\n─── Advanced: Nested Comprehensions ───\n")

# Category and Region revenue matrix (nested)
revenue_matrix = {
    cat: {
        region: sum(t["qty"] * t["price"] for t in transactions if t["category"] == cat and t["region"] == region)
        for region in set(t["region"] for t in transactions)
    }
    for cat in set(t["category"] for t in transactions)
}

print("Revenue by Category and Region:")
for cat, regions in sorted(revenue_matrix.items()):
    print(f"  {cat}:")
    for region, revenue in sorted(regions.items()):
        if revenue > 0:
            print(f"    {region}: ₹{revenue:>10,.0f}")

# Generator expression (lazy evaluation)
print("\n─── Generator: Top 3 Transactions by Revenue ───\n")
top_revenues = sorted((t["qty"] * t["price"], t["product"]) for t in transactions)[-3:]
for revenue, product in reversed(top_revenues):
    print(f"  {product}: ₹{revenue:>10,.0f}")

print("\n" + "="*75)
print("Act 1 is what projects 04 and 05 did; Act 2 is the Pythonic refactor.")
print("="*75 + "\n")
