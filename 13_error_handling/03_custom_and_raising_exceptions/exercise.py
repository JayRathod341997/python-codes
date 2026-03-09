# ─────────────────────────────────────────────
# Exercises — Custom Exceptions & Raising
# ─────────────────────────────────────────────

# ── Exercise 1: Validated Temperature Sensor ──
# Real-life: IoT device data ingestion
# Create a custom exception SensorReadingError with attributes:
#   sensor_id, reading, reason
# Write set_temperature(sensor_id, value):
#   raise SensorReadingError if value < -50 or value > 150 (unrealistic)
#   raise TypeError if value is not int/float
# Test with values: 36.5, 200, -100, "hot"
# Print sensor_id and reason from the caught exception.

# --- your code here ---


# ── Exercise 2: E-commerce Exception Hierarchy ─
# Real-life: Online store backend
# Build this hierarchy:
#   ShopError (base)
#     ├── ProductError
#     │     ├── OutOfStockError(product, requested, available)
#     │     └── InvalidProductError(product_id)
#     └── CheckoutError
#           ├── CouponExpiredError(code, expired_on)
#           └── MinimumOrderError(minimum, actual)
#
# Write a function checkout(product_id, qty, stock, cart_total,
#                           coupon_code=None, coupon_valid=True):
#   - raise InvalidProductError if product_id not in catalogue
#   - raise OutOfStockError if qty > stock
#   - raise CouponExpiredError if coupon_code given but coupon_valid=False
#   - raise MinimumOrderError if cart_total < 299
#   - else print "Order confirmed!"
#
# CATALOGUE = {"P001", "P002", "P003"}
# Test all five paths (including success).
# Catch ShopError as base in a loop.

CATALOGUE = {"P001", "P002", "P003"}

# --- your code here ---


# ── Exercise 3: raise … from … ────────────────
# Real-life: Data pipeline — wrap low-level errors with context
# Write these functions:
#   read_csv_row(row_str) — splits by comma, raises ValueError on bad format
#   parse_salary(raw)     — converts to float, raises ValueError on bad value
#   load_employee(row_str)— calls the two above; on any ValueError,
#                           raise a DataPipelineError("Failed to load employee")
#                           FROM the original error
#
# In the caller, print both the DataPipelineError message and its __cause__.
#
# Test:
#   load_employee("Alice,25,72500")     → success
#   load_employee("Bob,30")             → pipeline error (wrong columns)
#   load_employee("Carol,28,not_a_num") → pipeline error (bad salary)

class DataPipelineError(Exception):
    pass

# --- your code here ---


# ── Exercise 4: API Key Validator ─────────────
# Real-life: Middleware auth layer
# Create:
#   class APIKeyError(Exception)        — base
#   class MissingAPIKeyError(APIKeyError)
#   class InvalidAPIKeyError(APIKeyError, with attribute key)
#   class RateLimitExceededError(APIKeyError, with attributes key, limit, used)
#
# Write validate_api_key(key, request_count, limit=100):
#   - key is None or ""         → MissingAPIKeyError
#   - key not starting with "sk-" → InvalidAPIKeyError
#   - request_count > limit     → RateLimitExceededError
#   - else                      → print "Authorized"
#
# Test all four paths. Print the extra attributes on each error.

# --- your code here ---


# ── Exercise 5: Re-raise Pattern in Logging ───
# Real-life: Production error logger that must not swallow exceptions
# Write a decorator log_errors(func) that:
#   - wraps func in try/except Exception
#   - on exception: prints a log line with timestamp, function name, error type, message
#   - then RE-RAISES the same exception (so the caller still sees it)
#
# Apply it to two functions:
#   divide(a, b)       — raises ZeroDivisionError when b=0
#   get_item(lst, idx) — raises IndexError when idx out of range
#
# Show that the exception propagates to the outer try/except after logging.

from datetime import datetime

# --- your code here ---


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: SensorReadingError with sensor_id and reason printed
# Ex2: All five paths produce correct exception type messages
# Ex3: First succeeds; second and third show chained errors
# Ex4: Four distinct error messages with custom attributes
# Ex5: Log line printed, then exception caught in outer handler
# ─────────────────────────────────────────────
