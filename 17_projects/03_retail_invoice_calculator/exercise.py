# ───────────────────────────────────────────────────────────────
# Exercises — Project 03: Retail GST Invoice Calculator
# ───────────────────────────────────────────────────────────────

# ── Exercise 1: Create Invoice for Different Cart ────────────────
# Real-life: A customer buys a different set of items.
#
# Cart:
#   - Jeans (qty 2, ₹800 each) — clothing
#   - Coffee beans (qty 1, ₹500) — food
#   - Headphones (qty 1, ₹3000) — electronics
#   - Luxury pen set (qty 1, ₹5000) — luxury
#
# Task: Compute itemized invoice with GST rates, subtotal, discount (if >10k),
#       and grand total. Use the same logic from solution.py.
#
# Requirements:
#   - Use a while loop to iterate through items
#   - Compute GST for each item based on category
#   - Apply 5% bulk discount if subtotal > ₹10,000
#   - Print formatted invoice with alignment
#
# Hint: Copy the functions from solution.py and adapt the cart.

# --- your code here ---




# ── Exercise 2: Multi-Category Cart and GST Breakdown ────────────
# Real-life: Dr. Sharma wants to buy medical equipment for her clinic.
#            She needs a detailed invoice showing GST breakdown by category.
#
# Cart (assume all medical equipment is "electronics"):
#   - Thermometer (qty 10, ₹200) — electronics
#   - Blood pressure monitor (qty 3, ₹2000) — electronics
#   - Stethoscope (qty 5, ₹800) — electronics
#   - Cotton (qty 20 packets, ₹100) — food (assume basic supplies)
#
# Task: Generate invoice and also print "GST Breakdown by Category"
#       showing total GST collected per category.
#
# Requirements:
#   - Compute GST for each item
#   - Group GST totals by category (e.g., "Electronics: ₹X", "Food: ₹Y")
#   - Show percentage of total invoice that comes from GST
#   - Apply bulk discount if subtotal > ₹10,000
#
# Hint: Use a dictionary to track GST totals by category, or print them
#       as you iterate through the cart.

# --- your code here ---




# ── Exercise 3: Dynamic Discount Tier ──────────────────────────────
# Real-life: Pradeep decides to add a tiered discount structure:
#            - No discount if subtotal < ₹5,000
#            - 3% discount if subtotal ₹5,000–₹10,000
#            - 5% discount if subtotal ₹10,000–₹20,000
#            - 8% discount if subtotal > ₹20,000
#
# Cart (same as solution.py):
#   - Laptop (qty 1, ₹45,000) — electronics
#   - Mobile Phone (qty 2, ₹15,000) — electronics
#   - Shirt (qty 3, ₹500) — clothing
#   - Snacks (qty 5, ₹100) — food
#   - Watch (qty 1, ₹8,000) — luxury
#
# Task: Compute invoice with the new tiered discount logic.
#       Display which discount tier applies.
#
# Requirements:
#   - Use if/elif/else to determine discount tier (or nested ternary)
#   - Print which tier the customer qualifies for
#   - Show discount amount and final total
#   - Reuse the GST computation logic
#
# Hint: Apply discount based on subtotal value ranges. You can use
#       multiple ternary operators or a straightforward if/elif chain.

# --- your code here ---




# ───────────────────────────────────────────────────────────────
# Expected outputs (for self-check):
#
# Ex1: Customer cart invoice
#      Subtotal: ₹11,600 (2*800 + 500 + 3000 + 5000)
#      GST: Electronics 18% on 3000+5000 = ₹1,440
#           Clothing 5% on 1600 = ₹80
#           Food 5% on 500 = ₹25
#      Total GST: ₹1,545
#      Bulk discount (5%): ₹580
#      Grand total: ₹12,565
#
# Ex2: Medical supplies invoice (multiple items, grouped GST)
#      Subtotal: ₹12,800
#      GST by category: Electronics = ₹2,772, Food = ₹20
#      Total GST: ₹2,792
#      Bulk discount: ₹640
#      Grand total: ₹14,952
#      GST % of invoice: 18.7%
#
# Ex3: Tiered discount invoice
#      Subtotal: ₹91,500 (same as solution.py)
#      Total GST: ₹14,860
#      Tier applied: 8% (>₹20,000)
#      Discount amount: ₹7,320
#      Grand total: ₹99,040
# ───────────────────────────────────────────────────────────────
