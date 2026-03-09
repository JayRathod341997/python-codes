# ─────────────────────────────────────────────
# Functions — Basics
# ─────────────────────────────────────────────

# ── What is a function? ───────────────────────
# A function is a reusable block of code that performs a specific task.
# Real-life analogy: A TV remote "volume up" button — same action, every press.

# ── Defining a function ───────────────────────
# Syntax:
#   def function_name(parameters):
#       """docstring"""
#       body
#       return value        ← optional

def greet():
    print("Hello, World!")

greet()         # calling the function → Hello, World!
greet()         # reusable — call as many times as needed


# ── Function with arguments ───────────────────
# Real-life: Personalized email greeting
def greet_user(name):
    print(f"Hello, {name}! Welcome to our platform.")

greet_user("Alice")
greet_user("Bob")


# ── Multiple arguments ────────────────────────
# Real-life: Invoice line item
def print_invoice_item(product, qty, price):
    total = qty * price
    print(f"{product:20s} x{qty}  ₹{price:.2f}  →  ₹{total:.2f}")

print_invoice_item("Laptop Stand", 2, 899.00)
print_invoice_item("USB-C Cable",  5, 199.00)


# ── Return values ─────────────────────────────
# return sends a value back to the caller; execution stops there.

# Real-life: Tax calculator
def calculate_gst(amount, rate=18):
    return amount * rate / 100

gst = calculate_gst(10_000)
print(f"GST: ₹{gst}")          # ₹1800.0


# ── Returning multiple values ─────────────────
# Python returns a tuple — unpack with multiple variables
# Real-life: Currency converter
def convert_inr_to_usd(inr, rate=83.5):
    usd   = inr / rate
    cents = round((usd % 1) * 100)
    return round(usd, 2), cents

dollars, cents = convert_inr_to_usd(10_000)
print(f"$10,000 INR = ${dollars} ({cents} cents)")


# ── Functions that return None ────────────────
# If no return statement, Python implicitly returns None.
def log_event(message):
    print(f"[LOG] {message}")          # side-effect only

result = log_event("User logged in")
print(result)                          # None


# ── Early return ──────────────────────────────
# Real-life: API key validation
def validate_api_key(key):
    if not key:
        return "Error: API key is empty."
    if len(key) < 32:
        return "Error: API key too short."
    return "Valid key."

print(validate_api_key(""))
print(validate_api_key("abc123"))
print(validate_api_key("a" * 32))


# ── Docstrings ────────────────────────────────
# A string literal right after def — documents purpose, args, return value.

# Single-line docstring (short functions)
def square(n):
    """Return the square of n."""
    return n ** 2

# Multi-line docstring (complex functions)
def calculate_emi(principal, annual_rate, months):
    """
    Calculate monthly EMI for a loan.

    Args:
        principal   (float): Loan amount in ₹.
        annual_rate (float): Annual interest rate in % (e.g. 8.5).
        months      (int)  : Loan tenure in months.

    Returns:
        float: Monthly EMI rounded to 2 decimal places.
    """
    r = annual_rate / 12 / 100          # monthly rate
    emi = principal * r * (1 + r)**months / ((1 + r)**months - 1)
    return round(emi, 2)

# Access the docstring
print(calculate_emi.__doc__)
print(f"EMI: ₹{calculate_emi(500_000, 8.5, 60)}")   # ₹10,245.64


# ── Functions are first-class objects ─────────
# You can assign a function to a variable.
say_hello = greet_user
say_hello("Charlie")        # same as greet_user("Charlie")


# ── Key points ────────────────────────────────
# • def creates a function object and binds it to a name
# • Parameters are local variables inside the function
# • return exits immediately; the value travels to the caller
# • No return → None
# • Docstrings show up in help() and IDE tooltips
