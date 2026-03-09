# ─────────────────────────────────────────────
# Useful Standard Libraries — functools
# ─────────────────────────────────────────────

from functools import (
    reduce, partial, wraps,
    lru_cache, cache,
    total_ordering, cached_property
)

# ══════════════════════════════════════════════
# reduce — fold a sequence into a single value
# ══════════════════════════════════════════════
# (Covered briefly in 07_functions; deeper here)

# Real-life: Order total, pipeline composition
import operator

orders = [1500, 3200, 800, 4500, 2100]
total  = reduce(operator.add, orders)
print(f"Total: ₹{total}")

# Compose a pipeline of functions using reduce
def compose(*fns):
    """Apply functions right-to-left: compose(f, g, h)(x) == f(g(h(x)))"""
    return reduce(lambda f, g: lambda x: f(g(x)), fns)

pipeline = compose(
    lambda s: s.upper(),
    lambda s: s.strip(),
    lambda s: s.replace("  ", " ")
)
print(pipeline("  hello   world  "))    # "HELLO WORLD"


# ══════════════════════════════════════════════
# partial — fix some arguments of a function
# ══════════════════════════════════════════════

# partial(func, *args, **kwargs) → new function with those args pre-filled
# Real-life: Specialise generic functions for a specific context

def send_notification(user, channel, message, priority="normal"):
    print(f"[{priority.upper()}] → {user} via {channel}: {message}")

# Create specialised senders
send_email = partial(send_notification, channel="email")
send_sms   = partial(send_notification, channel="sms",   priority="high")
send_push  = partial(send_notification, channel="push",  priority="low")

send_email("Alice", "Your order shipped!")
send_sms("Bob",     "OTP: 482916")
send_push("Carol",  "New message from Dave")

# Real-life: pre-configure a base URL for API calls
import urllib.parse

def build_url(base, endpoint, **params):
    query = urllib.parse.urlencode(params)
    return f"{base}{endpoint}?{query}" if params else f"{base}{endpoint}"

prod_api = partial(build_url, "https://api.example.com")
dev_api  = partial(build_url, "http://localhost:8000")

print(prod_api("/users", page=1, limit=20))
print(dev_api("/debug"))

# partial + sorted — reusable sort key
from functools import partial

def get_field(record, field):
    return record[field]

sort_by_price  = partial(sorted, key=partial(get_field, field="price"))
sort_by_rating = partial(sorted, key=partial(get_field, field="rating"), reverse=True)

products = [
    {"name": "Mouse",    "price": 799,  "rating": 4.2},
    {"name": "Keyboard", "price": 2499, "rating": 4.7},
    {"name": "Webcam",   "price": 1299, "rating": 4.4},
]
print([p["name"] for p in sort_by_price(products)])
print([p["name"] for p in sort_by_rating(products)])


# ══════════════════════════════════════════════
# wraps — preserve metadata of wrapped functions
# ══════════════════════════════════════════════

# When you write a decorator, the wrapper replaces the original function.
# Without @wraps, the function's __name__ and __doc__ are lost.

# ❌ Without wraps:
def bad_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@bad_logger
def multiply(a, b):
    """Multiply two numbers."""
    return a * b

print(multiply.__name__)    # 'wrapper'  ← wrong!
print(multiply.__doc__)     # None       ← lost!

# ✅ With @wraps:
def logger(func):
    @wraps(func)            # copies __name__, __doc__, __module__, etc.
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def divide(a, b):
    """Divide a by b."""
    return a / b

print(divide.__name__)      # 'divide'   ← correct
print(divide.__doc__)       # 'Divide a by b.'

# Real-life: production decorators always use @wraps
def require_auth(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if not request.get("authenticated"):
            raise PermissionError("Login required")
        return func(request, *args, **kwargs)
    return wrapper


# ══════════════════════════════════════════════
# lru_cache / cache — memoization
# ══════════════════════════════════════════════
# Cache function results; return cached value on repeat calls.
# lru_cache(maxsize=N) keeps N most-recently-used results.
# cache (Python 3.9+) = lru_cache(maxsize=None) — unlimited.

# Real-life: Expensive computation — avoid recalculation
import time

@lru_cache(maxsize=128)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

start = time.perf_counter()
print(fibonacci(40))
print(f"Time: {time.perf_counter() - start:.6f}s")
print(fibonacci.cache_info())   # CacheInfo(hits=38, misses=41, ...)

# Real-life: Cache API/DB lookups
@cache
def get_user_from_db(user_id):
    """Simulate a slow DB call."""
    time.sleep(0.01)    # fake latency
    return {"id": user_id, "name": f"User_{user_id}"}

print(get_user_from_db(42))     # [COMPUTING] 10ms
print(get_user_from_db(42))     # [CACHED]    instant

# ⚠ Only works on HASHABLE arguments (int, str, tuple — not list/dict)
# ⚠ Infinite cache can cause memory issues on long-running servers
#    Use lru_cache(maxsize=256) to limit


# ══════════════════════════════════════════════
# total_ordering — complete comparison from two methods
# ══════════════════════════════════════════════
# Define __eq__ and ONE of __lt__, __le__, __gt__, __ge__
# and @total_ordering fills in the rest.

@total_ordering
class Employee:
    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary
    def __eq__(self, other):
        return self.salary == other.salary
    def __lt__(self, other):
        return self.salary < other.salary
    def __repr__(self):
        return f"Employee({self.name}, ₹{self.salary:,})"

employees = [
    Employee("Alice", 75000),
    Employee("Bob",   92000),
    Employee("Carol", 61000),
]
print(sorted(employees))        # sorts by salary
print(max(employees))           # Bob


# ══════════════════════════════════════════════
# cached_property — compute once, store as attribute
# ══════════════════════════════════════════════
# Like @property but the result is cached after first access.
# Real-life: Expensive derived attributes (stats, parsed data)

class SalesReport:
    def __init__(self, transactions):
        self._transactions = transactions

    @cached_property
    def total_revenue(self):
        print("[computing total_revenue...]")
        return sum(t["amount"] for t in self._transactions)

    @cached_property
    def average_order(self):
        print("[computing average_order...]")
        return self.total_revenue / len(self._transactions)

report = SalesReport([
    {"amount": 1500}, {"amount": 3200}, {"amount": 800},
    {"amount": 4500}, {"amount": 2100},
])
print(report.total_revenue)     # [computing...] 12100
print(report.total_revenue)     # (no recomputation)
print(report.average_order)     # [computing...] 2420.0


# ── Key points ────────────────────────────────
# reduce(f, iter)       — fold sequence to one value
# partial(f, *args)     — pre-fill arguments; create specialised functions
# @wraps(func)          — preserve __name__/__doc__ in decorators
# @lru_cache(maxsize=N) — memoize; limit cache size
# @cache                — unlimited memoize (Python 3.9+)
# @total_ordering       — define __eq__+one comparison, get the rest free
# @cached_property      — compute once on first access, cache result
