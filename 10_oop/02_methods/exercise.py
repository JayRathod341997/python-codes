# ─────────────────────────────────────────────
# Exercises — Instance, Class & Static Methods
# ─────────────────────────────────────────────

# ── Exercise 1: Coupon System ─────────────────
# Real-life: E-commerce discount engine
# Create a class Coupon with:
#   class variable  : active_coupons = {}  (code → discount%)
#   __init__(self, code, discount_pct, min_order)
#   instance method apply(cart_total) →
#       if cart_total >= min_order: return discounted total
#       else: print "Minimum order ₹X required"
#   class method    register(cls, code, discount_pct, min_order) →
#       creates a Coupon and stores it in active_coupons
#   class method    get(cls, code) →
#       returns the Coupon object from active_coupons or None
#   static method   is_valid_code(code) →
#       returns True if code is exactly 8 uppercase letters/digits
#
# Register coupons: "SAVE20PC"(20%, ₹500), "FLAT50RS"(10%, ₹300)
# Validate codes, retrieve and apply them.

# --- your code here ---


# ── Exercise 2: Temperature Converter ────────
# Real-life: Weather / IoT sensor utility
# Create a class Temperature with:
#   __init__(self, value, unit)   unit ∈ "C", "F", "K"
#   instance method display()    → prints "37.0 °C"
#   class method from_fahrenheit(cls, f) → creates Temperature in Celsius
#   class method from_kelvin(cls, k)     → creates Temperature in Celsius
#   static method c_to_f(c)  → returns Fahrenheit value
#   static method c_to_k(c)  → returns Kelvin value
#   static method is_fever(c) → returns True if c > 37.5
#
# Demonstrate all methods with realistic values (body temp, water boiling, etc.)

# --- your code here ---


# ── Exercise 3: User Account Factory ─────────
# Real-life: SaaS app — different signup flows
# Create a class UserAccount with:
#   class variable : user_count = 0
#   __init__(self, username, email, role)
#   instance method profile() → prints formatted user card
#   class method from_google(cls, google_email) →
#       username = email prefix, role = "member"
#   class method create_admin(cls, username, email) →
#       role = "admin"
#   static method validate_email(email) →
#       returns True if "@" and "." are in email (basic check)
#   static method generate_username(full_name) →
#       returns first_name.last_name in lowercase
#
# Create one regular, one google, one admin user and print their profiles.

# --- your code here ---


# ── Exercise 4: Invoice Calculator ───────────
# Real-life: Billing software
# Create a class Invoice with:
#   class variable : invoice_count = 0
#   __init__(self, client_name)
#     auto-generate invoice_id like "INV-001", "INV-002" ...
#   instance method add_line(description, qty, unit_price)
#   instance method subtotal()  → sum of all line totals
#   instance method tax_amount(rate=0.18) → subtotal * rate
#   instance method grand_total(rate=0.18) → subtotal + tax
#   instance method print_invoice()  → full formatted invoice
#   static method  round_currency(amount) → rounds to 2 decimal places
#   class method   reset_count(cls) → resets invoice_count to 0
#
# Create 2 invoices for different clients, print both.

# --- your code here ---


# ── Exercise 5: Geometry Toolkit ─────────────
# Real-life: CAD / architecture software utility
# Create a class Shape with:
#   class variable : PI = 3.14159
#   __init__(self, color="white")
#   instance method describe() → prints "A white shape"
#   static method circle_area(r)       → π r²
#   static method rectangle_area(l, w) → l × w
#   static method triangle_area(b, h)  → 0.5 × b × h
#   static method hypotenuse(a, b)     → √(a²+b²)
#   class method  colored_circle(cls, r, color) →
#       creates a Shape(color) and returns its area + the object
#
# Use static methods to calculate areas for a floor plan:
#   circular fountain r=3.5, rectangular room 12×8, triangular garden b=10 h=6

# --- your code here ---


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: Coupon applied with discount; invalid code rejected; min order warning
# Ex2: Conversions correct: 37°C = 98.6°F = 310.15K; is_fever(38) = True
# Ex3: 3 user profiles printed; user_count = 3
# Ex4: 2 formatted invoices with line items, subtotal, tax, grand total
# Ex5: Areas printed; colored_circle returns both area and Shape object
# ─────────────────────────────────────────────
