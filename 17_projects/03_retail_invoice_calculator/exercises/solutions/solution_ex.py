# ───────────────────────────────────────────────────────────────
# Solutions — Project 03: Retail GST Invoice Calculator
# ───────────────────────────────────────────────────────────────

print("\n" + "="*75)
print("EXERCISE 1 SOLUTION: Customer Invoice")
print("="*75 + "\n")

def get_gst_rate(category):
    if category == "food":
        return 5
    elif category == "clothing":
        return 5
    elif category == "electronics":
        return 18
    elif category == "luxury":
        return 28
    else:
        return 0

cart_1 = [
    {"name": "Jeans", "qty": 2, "price": 800, "gst_category": "clothing"},
    {"name": "Coffee Beans", "qty": 1, "price": 500, "gst_category": "food"},
    {"name": "Headphones", "qty": 1, "price": 3000, "gst_category": "electronics"},
    {"name": "Luxury Pen Set", "qty": 1, "price": 5000, "gst_category": "luxury"},
]

print(f"{'Item':<20} {'Qty':>6} {'Price':>12} {'Total':>12} {'GST%':>7} {'GST Amt':>12}")
print("─" * 75)

subtotal = 0
total_gst = 0
index = 0

while index < len(cart_1):
    item = cart_1[index]
    item_total = item["qty"] * item["price"]
    gst_rate = get_gst_rate(item["gst_category"])
    gst_amount = (item_total * gst_rate) / 100
    subtotal += item_total
    total_gst += gst_amount
    print(f"{item['name']:<20} {item['qty']:>6} ₹{item['price']:>11,.0f} ₹{item_total:>11,.0f} {gst_rate:>6.0f}% ₹{gst_amount:>11,.0f}")
    index += 1

print("─" * 75)

discount_amount = (subtotal * 5 / 100) if subtotal > 10000 else 0
grand_total = subtotal + total_gst - discount_amount

print(f"\nSubtotal: ₹{subtotal:>15,.0f}")
print(f"Total GST: ₹{total_gst:>15,.0f}")
if discount_amount > 0:
    print(f"Bulk Discount (5%): ₹{discount_amount:>15,.0f}")
print(f"GRAND TOTAL: ₹{grand_total:>15,.0f}")

print("\n" + "="*75)
print("EXERCISE 2 SOLUTION: Medical Supplies Invoice with GST Breakdown")
print("="*75 + "\n")

cart_2 = [
    {"name": "Thermometer", "qty": 10, "price": 200, "gst_category": "electronics"},
    {"name": "Blood Pressure Monitor", "qty": 3, "price": 2000, "gst_category": "electronics"},
    {"name": "Stethoscope", "qty": 5, "price": 800, "gst_category": "electronics"},
    {"name": "Cotton", "qty": 20, "price": 100, "gst_category": "food"},
]

print(f"{'Item':<25} {'Qty':>6} {'Price':>12} {'Total':>12} {'GST%':>7} {'GST Amt':>12}")
print("─" * 75)

subtotal = 0
total_gst = 0
gst_by_category = {}
index = 0

while index < len(cart_2):
    item = cart_2[index]
    item_total = item["qty"] * item["price"]
    gst_rate = get_gst_rate(item["gst_category"])
    gst_amount = (item_total * gst_rate) / 100
    subtotal += item_total
    total_gst += gst_amount

    category = item["gst_category"]
    if category not in gst_by_category:
        gst_by_category[category] = 0
    gst_by_category[category] += gst_amount

    print(f"{item['name']:<25} {item['qty']:>6} ₹{item['price']:>11,.0f} ₹{item_total:>11,.0f} {gst_rate:>6.0f}% ₹{gst_amount:>11,.0f}")
    index += 1

print("─" * 75)

discount_amount = (subtotal * 5 / 100) if subtotal > 10000 else 0
grand_total = subtotal + total_gst - discount_amount

print(f"\nSubtotal: ₹{subtotal:>15,.0f}")
print(f"Total GST: ₹{total_gst:>15,.0f}")
print("\nGST BREAKDOWN BY CATEGORY:")
for cat, gst_amt in gst_by_category.items():
    print(f"  {cat.capitalize()}: ₹{gst_amt:>12,.0f}")

if discount_amount > 0:
    print(f"\nBulk Discount (5%): ₹{discount_amount:>15,.0f}")

print(f"\nGRAND TOTAL: ₹{grand_total:>15,.0f}")
gst_percentage = (total_gst / grand_total * 100) if grand_total > 0 else 0
print(f"GST as % of invoice: {gst_percentage:.1f}%")

print("\n" + "="*75)
print("EXERCISE 3 SOLUTION: Tiered Discount Invoice")
print("="*75 + "\n")

cart_3 = [
    {"name": "Laptop", "qty": 1, "price": 45000, "gst_category": "electronics"},
    {"name": "Mobile Phone", "qty": 2, "price": 15000, "gst_category": "electronics"},
    {"name": "Shirt", "qty": 3, "price": 500, "gst_category": "clothing"},
    {"name": "Snacks", "qty": 5, "price": 100, "gst_category": "food"},
    {"name": "Watch", "qty": 1, "price": 8000, "gst_category": "luxury"},
]

print(f"{'Item':<20} {'Qty':>6} {'Price':>12} {'Total':>12} {'GST%':>7} {'GST Amt':>12}")
print("─" * 75)

subtotal = 0
total_gst = 0
index = 0

while index < len(cart_3):
    item = cart_3[index]
    item_total = item["qty"] * item["price"]
    gst_rate = get_gst_rate(item["gst_category"])
    gst_amount = (item_total * gst_rate) / 100
    subtotal += item_total
    total_gst += gst_amount
    print(f"{item['name']:<20} {item['qty']:>6} ₹{item['price']:>11,.0f} ₹{item_total:>11,.0f} {gst_rate:>6.0f}% ₹{gst_amount:>11,.0f}")
    index += 1

print("─" * 75)

# Tiered discount logic
if subtotal < 5000:
    discount_rate = 0
    tier = "No discount (<₹5,000)"
elif subtotal < 10000:
    discount_rate = 3
    tier = "3% discount (₹5,000–₹10,000)"
elif subtotal < 20000:
    discount_rate = 5
    tier = "5% discount (₹10,000–₹20,000)"
else:
    discount_rate = 8
    tier = "8% discount (>₹20,000)"

discount_amount = (subtotal * discount_rate) / 100
grand_total = subtotal + total_gst - discount_amount

print(f"\nSubtotal: ₹{subtotal:>15,.0f}")
print(f"Total GST: ₹{total_gst:>15,.0f}")
print(f"\nDiscount Tier Applied: {tier}")
print(f"Discount Amount ({discount_rate}%): ₹{discount_amount:>15,.0f}")
print(f"\nGRAND TOTAL: ₹{grand_total:>15,.0f}")

print("\n" + "="*75 + "\n")
