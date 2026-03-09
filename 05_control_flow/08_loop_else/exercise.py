# ─────────────────────────────────────────────
# Exercises — Loop else
# ─────────────────────────────────────────────

# ── Exercise 1: Coupon Code Validator ─────────
# Real-life: E-commerce checkout
# Check if entered_code exists in valid_coupons list.
# If found → "Coupon '{code}' applied! {discount}% off."
# If not found (loop else) → "Invalid coupon code. Please check and retry."

valid_coupons = [
    ("SAVE10", 10),
    ("FLAT20", 20),
    ("WELCOME50", 50),
]
entered_code = "FLAT20"

# --- your for...else loop here ---


# ── Exercise 2: Flight Seat Selector ──────────
# Real-life: Airline booking system
# Search for a window seat (seat_type == "window") that is not reserved.
# If found → "Window seat {seat_id} booked!"
# If no window seat available (loop else) → "No window seats available. Upgrade to business?"

seats = [
    {"id": "12A", "type": "window",  "reserved": True},
    {"id": "14B", "type": "middle",  "reserved": False},
    {"id": "16A", "type": "window",  "reserved": True},
    {"id": "18C", "type": "aisle",   "reserved": False},
    {"id": "20A", "type": "window",  "reserved": False},
]

# --- your for...else loop here ---


# ── Exercise 3: DNS Lookup Simulator ──────────
# Real-life: Network resolver
# Try each DNS server in order (while loop with retries).
# Simulate: server responds True/False (from dns_responses list).
# If a server responds → "Resolved via {server}."
# If all servers fail (while else) → "DNS resolution failed. Check network."

dns_servers   = ["8.8.8.8", "8.8.4.4", "1.1.1.1"]
dns_responses = [False, False, False]   # all fail (change to test success)
idx           = 0

# --- your while...else loop here ---


# ── Exercise 4: Ingredient Checker ────────────
# Real-life: Food allergy app
# Check if any ingredient in the recipe is in the user's allergy list.
# If found → "⚠ Allergy alert: {ingredient} detected! Do not consume."
# If none found (loop else) → "✓ Safe to eat. No allergens detected."

recipe_ingredients = ["flour", "sugar", "eggs", "milk", "vanilla"]
user_allergies     = ["peanuts", "shellfish", "milk"]

# --- your for...else loop here ---


# ── Exercise 5: Warehouse Bin Locator ─────────
# Real-life: Logistics / warehouse management
# Each bin has a location and list of SKUs.
# Search for sku = "SKU-305".
# If found → "SKU-305 located at bin {bin_id}."
# If not found in any bin → "SKU-305 not in warehouse. Initiate restock."

warehouse = [
    {"bin": "A1", "skus": ["SKU-101", "SKU-202"]},
    {"bin": "B3", "skus": ["SKU-305", "SKU-410"]},
    {"bin": "C7", "skus": ["SKU-512", "SKU-613"]},
]
target_sku = "SKU-305"

# --- your for...else loop here ---


# ─────────────────────────────────────────────
# Expected outputs:
# Ex1: Coupon 'FLAT20' applied! 20% off.
# Ex2: Window seat 20A booked!
# Ex3: DNS resolution failed. Check network.
# Ex4: ⚠ Allergy alert: milk detected! Do not consume.
# Ex5: SKU-305 located at bin B3.
# ─────────────────────────────────────────────
