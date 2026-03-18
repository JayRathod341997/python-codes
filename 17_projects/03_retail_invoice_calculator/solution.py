# ─────────────────────────────────────────────────────────────────
# Project 03 — Retail — GST Invoice Calculator
# Concepts  : while loop, if/elif, ternary operator, f-string alignment
# Difficulty: Beginner/Intermediate
# ─────────────────────────────────────────────────────────────────

# ── Section 1: Shopping Cart Data ──────────────────────────────────
# Hardcoded 5-item shopping cart from Pradeep's store
# Each item: name, quantity, price per unit, GST category
# In production, you'd read this from a database or POS system

print("\n" + "="*75)
print("RETAIL INVOICE CALCULATOR — PRADEEP'S ELECTRONICS STORE")
print("="*75)

shopping_cart = [
    {"name": "Laptop", "qty": 1, "price": 45000, "gst_category": "electronics"},
    {"name": "Mobile Phone", "qty": 2, "price": 15000, "gst_category": "electronics"},
    {"name": "Shirt", "qty": 3, "price": 500, "gst_category": "clothing"},
    {"name": "Snacks", "qty": 5, "price": 100, "gst_category": "food"},
    {"name": "Watch", "qty": 1, "price": 8000, "gst_category": "luxury"},
]

# ── Section 2: GST Rate Lookup ─────────────────────────────────────
# Different product categories have different GST rates in India
# This is a real-world constraint from the Indian tax system

def get_gst_rate(category):
    """Return GST rate (%) for a product category."""
    # Using if/elif to match the category and return the corresponding rate
    if category == "food":
        return 5
    elif category == "clothing":
        return 5
    elif category == "electronics":
        return 18
    elif category == "luxury":
        return 28
    else:
        return 0  # Unknown category, no GST

# ── Section 3: Invoice Computation with while loop ────────────────
# We use a while loop to iterate through the shopping cart
# This allows us to control the iteration and index manually

print("\n" + "ITEMIZED DETAILS:")
print("─" * 75)
print(f"{'Item':<20} {'Qty':>6} {'Price':>12} {'Total':>12} {'GST%':>7} {'GST Amt':>12}")
print("─" * 75)

item_index = 0
subtotal = 0
total_gst = 0

# ── CONCEPT: while loop ────────────────────────────────────────────
# We use while instead of for to have explicit index control
# This is useful when we need to access multiple items or skip items

while item_index < len(shopping_cart):
    item = shopping_cart[item_index]
    item_name = item["name"]
    qty = item["qty"]
    price_per_unit = item["price"]
    gst_category = item["gst_category"]

    # Compute item total (before GST)
    item_total = qty * price_per_unit

    # Get GST rate for this category
    gst_rate = get_gst_rate(gst_category)

    # Compute GST amount
    gst_amount = (item_total * gst_rate) / 100

    # Add to invoice totals
    subtotal += item_total
    total_gst += gst_amount

    # Format and print this item
    print(f"{item_name:<20} {qty:>6} ₹{price_per_unit:>11,.0f} ₹{item_total:>11,.0f} {gst_rate:>6.0f}% ₹{gst_amount:>11,.0f}")

    item_index += 1

print("─" * 75)

# ── Section 4: Bulk Discount Logic ────────────────────────────────
# ── CONCEPT: Ternary Operator ──────────────────────────────────────
# A ternary operator is a concise if/else: value = a if condition else b
# Here we use it to decide discount based on subtotal

# Check if subtotal exceeds ₹10,000 for bulk discount
bulk_discount_threshold = 10000
bulk_discount_rate = 5  # 5% discount if threshold crossed

# Ternary operator: if subtotal > threshold, apply discount, else 0
discount_amount = (subtotal * bulk_discount_rate / 100) if subtotal > bulk_discount_threshold else 0

print(f"\nSubtotal (before GST and discount): ₹{subtotal:>15,.0f}")
print(f"Total GST Amount:                   ₹{total_gst:>15,.0f}")
if discount_amount > 0:
    print(f"Bulk Discount (5%, >₹10,000):       ₹{discount_amount:>15,.0f}")
else:
    print(f"Bulk Discount:                      ₹{discount_amount:>15,.0f} (not eligible)")

# ── Section 5: Grand Total Computation ─────────────────────────────
# Grand Total = Subtotal + GST - Discount
grand_total = subtotal + total_gst - discount_amount

print("─" * 75)
print(f"GRAND TOTAL (₹):                    ₹{grand_total:>15,.0f}")
print("="*75)

# ── Section 6: Invoice Footer ──────────────────────────────────────
# In production, you'd write this to a PDF or email to customer
print("\nInvoice Breakdown Summary:")
print(f"  • Subtotal (all items):     ₹{subtotal:>15,.0f}")
print(f"  • GST (by category):        ₹{total_gst:>15,.0f}")
print(f"  • Bulk Discount Applied:    ₹{discount_amount:>15,.0f}")
print(f"  • TOTAL PAYABLE:            ₹{grand_total:>15,.0f}")

# Calculate effective tax rate
effective_tax_rate = (total_gst / subtotal * 100) if subtotal > 0 else 0
print(f"\nEffective GST rate on this invoice: {effective_tax_rate:.2f}%")
print("(This varies because different items have different GST rates)")

print("\n" + "="*75 + "\n")

# ── KEY POINTS ──────────────────────────────────────────────────────
# 1. while loop gives explicit control over iteration with an index
#    (useful when we need to conditionally skip or modify items)
# 2. if/elif chains help categorize products into tax buckets
# 3. Ternary operator makes the discount logic concise and readable
# 4. f-string alignment ({:>15,.0f}) ensures clean invoice formatting
# 5. GST computation is REAL-WORLD: India has tiered GST by category
# 6. In production, you'd save this invoice to a file, email it, or
#    integrate with accounting software like Tally for GST compliance
# ────────────────────────────────────────────────────────────────────
