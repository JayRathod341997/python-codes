# ─────────────────────────────────────────────
# Error Handling — Custom Exceptions & Raising
# ─────────────────────────────────────────────

# ── raise — Manually triggering an exception ──
# Use raise to signal that something went wrong in YOUR code.

# Real-life: Age validation for a platform
def set_age(age):
    if not isinstance(age, int):
        raise TypeError(f"Age must be an integer, got {type(age).__name__}")
    if age < 0 or age > 150:
        raise ValueError(f"Age {age} is out of realistic range (0–150)")
    print(f"Age set to {age}")

set_age(25)
try:
    set_age(-5)
except ValueError as e:
    print(e)

try:
    set_age("twenty")
except TypeError as e:
    print(e)


# ── Re-raising an exception ───────────────────
# Use bare `raise` inside an except block to re-raise the current exception
# after logging or partial handling.

def process_payment(amount):
    try:
        if amount <= 0:
            raise ValueError("Payment amount must be positive")
    except ValueError as e:
        print(f"[LOG] Payment validation failed: {e}")
        raise           # re-raises the same ValueError

try:
    process_payment(-100)
except ValueError as e:
    print(f"[HANDLER] Caught: {e}")


# ── raise ... from ... (Exception chaining) ───
# Preserve original exception context when wrapping.

def fetch_user_from_db(user_id):
    raw = {"101": "Alice"}
    try:
        return raw[str(user_id)]
    except KeyError as original:
        raise LookupError(f"User {user_id} not found in DB") from original

try:
    fetch_user_from_db(999)
except LookupError as e:
    print(e)
    print(f"Caused by: {e.__cause__}")


# ── Custom Exception Classes ──────────────────
# Subclass Exception (or a more specific built-in) to create domain errors.

# Minimal custom exception
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(
            f"Cannot withdraw ₹{amount} — balance is ₹{balance}"
        )
    return balance - amount

try:
    withdraw(1000, 2500)
except InsufficientFundsError as e:
    print(e)


# ── Rich custom exceptions with extra data ────
# Add custom attributes to carry context with the error.
# Real-life: E-commerce order validation errors

class OrderError(Exception):
    """Base class for all order-related errors."""

class InvalidQuantityError(OrderError):
    def __init__(self, product, qty, max_stock):
        self.product   = product
        self.qty       = qty
        self.max_stock = max_stock
        super().__init__(
            f"Cannot order {qty}x '{product}' — only {max_stock} in stock"
        )

class PaymentDeclinedError(OrderError):
    def __init__(self, reason, code):
        self.reason = reason
        self.code   = code
        super().__init__(f"Payment declined [{code}]: {reason}")

def place_order(product, qty, stock, pay_ok=True):
    if qty > stock:
        raise InvalidQuantityError(product, qty, stock)
    if not pay_ok:
        raise PaymentDeclinedError("Card limit exceeded", "ERR_4012")
    print(f"Order placed: {qty}x {product}")

try:
    place_order("Laptop", 5, 2)
except InvalidQuantityError as e:
    print(e)
    print(f"  Product: {e.product}, Requested: {e.qty}, Available: {e.max_stock}")

try:
    place_order("Mouse", 1, 10, pay_ok=False)
except PaymentDeclinedError as e:
    print(e)
    print(f"  Error code: {e.code}")


# ── Exception hierarchy for a domain ─────────
# Real-life: Authentication system

class AuthError(Exception):
    """Base for all auth errors."""

class InvalidCredentialsError(AuthError):
    pass

class AccountLockedError(AuthError):
    def __init__(self, username, locked_until):
        self.locked_until = locked_until
        super().__init__(f"Account '{username}' locked until {locked_until}")

class TokenExpiredError(AuthError):
    pass

def authenticate(username, password, failed_attempts):
    if failed_attempts >= 5:
        raise AccountLockedError(username, "2024-01-20 18:00")
    if password != "secret":
        raise InvalidCredentialsError("Wrong username or password")
    print(f"Welcome, {username}!")

def verify_token(token):
    if token == "expired":
        raise TokenExpiredError("Session expired. Please log in again.")

# Catch the base class to handle all auth errors at once
for attempt_count, pwd in [(0, "wrong"), (5, "any"), (0, "secret")]:
    try:
        authenticate("alice", pwd, attempt_count)
    except AuthError as e:          # catches all subclasses
        print(f"[{type(e).__name__}] {e}")

try:
    verify_token("expired")
except TokenExpiredError as e:
    print(e)


# ── Key points ────────────────────────────────
# • raise ExceptionType(msg)  — raise a new exception
# • raise                     — re-raise current exception (inside except)
# • raise NewError() from original — chain: preserves __cause__
# • Custom exceptions: subclass Exception or a domain base class
# • Add __init__ with extra attributes for rich error context
# • Design a hierarchy: BaseAppError → specific errors
#   → catch base class to handle all at once
