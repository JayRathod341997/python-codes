# Solutions — Project 10: Comprehensions

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
]

print("\n" + "="*70)
print("EXERCISE 1 SOLUTION: Clothing Revenue (Comprehension)")
print("="*70 + "\n")

clothing = [t for t in transactions if t["category"] == "Clothing"]
clothing_revenue = sum(t["qty"] * t["price"] for t in clothing)

print(f"Clothing transactions: {len(clothing)}")
print(f"Total clothing revenue: ₹{clothing_revenue:,.0f}")

print("\n" + "="*70)
print("EXERCISE 2 SOLUTION: Revenue by Salesperson")
print("="*70 + "\n")

salesperson_revenue = {
    sp: sum(t["qty"] * t["price"] for t in transactions if t["salesperson"] == sp)
    for sp in set(t["salesperson"] for t in transactions)
}

print("Revenue by Salesperson (top 5):")
for sp, rev in sorted(salesperson_revenue.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(f"  {sp}: ₹{rev:>10,.0f}")

print("\n" + "="*70)
print("EXERCISE 3 SOLUTION: Nested Region-Category Revenue")
print("="*70 + "\n")

revenue_matrix = {
    region: {
        cat: sum(t["qty"] * t["price"] for t in transactions if t["region"] == region and t["category"] == cat)
        for cat in set(t["category"] for t in transactions)
    }
    for region in set(t["region"] for t in transactions)
}

print("Revenue Matrix (Region x Category):")
for region in sorted(revenue_matrix.keys()):
    print(f"  {region}:")
    for cat, rev in sorted(revenue_matrix[region].items()):
        if rev > 0:
            print(f"    {cat}: ₹{rev:>10,.0f}")

print("\n" + "="*70 + "\n")
