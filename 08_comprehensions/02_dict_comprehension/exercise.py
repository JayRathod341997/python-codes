# ─────────────────────────────────────────────
# Exercises — Dictionary Comprehension
# ─────────────────────────────────────────────

# ── Exercise 1: Student Report Card ──────────
# Real-life: School management system
# Given two parallel lists, build a dict: {student_name: marks}

students = ["Riya", "Arjun", "Meera", "Kabir"]
marks    = [88, 72, 95, 60]

# --- your code here ---


# ── Exercise 2: URL Slug Generator ───────────
# Real-life: CMS / Blog platform
# Convert page titles to URL-friendly slugs:
#   "About Us" → "about-us"
# Build a dict: {original_title: slug}

titles = ["About Us", "Contact Page", "Privacy Policy", "Terms Of Service"]

# --- your code here ---


# ── Exercise 3: Apply Discount ────────────────
# Real-life: Flash sale — reduce every price by 10%
# Build a new dict with discounted prices (round to 2 decimal places).

prices = {"Apple": 120.0, "Mango": 80.0, "Grapes": 200.0, "Orange": 50.0}

# --- your code here ---


# ── Exercise 4: Phone Book Inversion ─────────
# Real-life: Reverse lookup system
# Given {name: phone}, build {phone: name}

phone_book = {
    "Alice":   "9876543210",
    "Bob":     "9123456789",
    "Charlie": "9988776655",
}

# --- your code here ---


# ── Exercise 5: JSON Response Flattener ───────
# Real-life: API response processing
# Each record has "symbol" and "price".
# Build a dict: {symbol: price} for easy ticker lookup.

api_data = [
    {"symbol": "AAPL", "price": 182.5},
    {"symbol": "GOOG", "price": 140.3},
    {"symbol": "MSFT", "price": 378.9},
    {"symbol": "TSLA", "price": 245.0},
]

# --- your code here ---


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: {'Riya': 88, 'Arjun': 72, 'Meera': 95, 'Kabir': 60}
# Ex2: {'About Us': 'about-us', 'Contact Page': 'contact-page',
#       'Privacy Policy': 'privacy-policy', 'Terms Of Service': 'terms-of-service'}
# Ex3: {'Apple': 108.0, 'Mango': 72.0, 'Grapes': 180.0, 'Orange': 45.0}
# Ex4: {'9876543210': 'Alice', '9123456789': 'Bob', '9988776655': 'Charlie'}
# Ex5: {'AAPL': 182.5, 'GOOG': 140.3, 'MSFT': 378.9, 'TSLA': 245.0}
# ─────────────────────────────────────────────
