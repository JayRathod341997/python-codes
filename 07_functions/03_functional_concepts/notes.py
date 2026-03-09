# ─────────────────────────────────────────────
# Functions — Functional Concepts
# ─────────────────────────────────────────────

# ── 1. Lambda Functions ───────────────────────
# Anonymous (nameless) single-expression functions.
# Syntax: lambda parameters: expression

# Real-life: Quick inline calculation
tax = lambda amount, rate: amount * rate / 100
print(tax(10_000, 18))          # 1800.0

# Real-life: Sorting a list of dicts by a field
employees = [
    {"name": "Alice", "salary": 75000},
    {"name": "Bob",   "salary": 92000},
    {"name": "Carol", "salary": 61000},
]
# Sort by salary without defining a full function
by_salary = sorted(employees, key=lambda e: e["salary"])
for emp in by_salary:
    print(f"  {emp['name']:10s} ₹{emp['salary']:,}")

# Lambda with conditional expression
classify = lambda score: "Pass" if score >= 40 else "Fail"
print(classify(72))     # Pass
print(classify(35))     # Fail

# ⚠ When NOT to use lambda:
# If the expression is complex or needs a docstring, use def instead.


# ── 2. Higher-order Functions ─────────────────
# A function that:
#   a) takes another function as an argument, OR
#   b) returns a function as its result.

# ── a) Functions as Arguments ─────────────────
# Real-life: Payment processor — apply different fee strategies

def apply_fee(amount, fee_fn):
    """Apply a fee strategy function to the amount."""
    return amount + fee_fn(amount)

def flat_fee(amount):
    return 25                   # ₹25 flat

def percentage_fee(amount):
    return amount * 0.02        # 2%

def tiered_fee(amount):
    return 50 if amount >= 10_000 else 15

print(apply_fee(5_000, flat_fee))           # 5025
print(apply_fee(5_000, percentage_fee))     # 5100.0
print(apply_fee(5_000, tiered_fee))         # 5015

# Lambda inline as the fee strategy
print(apply_fee(8_000, lambda a: a * 0.015))  # 2% = 8120


# ── b) Returning Functions (Function Factories) ─
# Real-life: Configurable discount coupon generator

def make_discount(percent):
    """Return a discount function for the given percentage."""
    def apply_discount(price):
        return price * (1 - percent / 100)
    return apply_discount       # returns the inner function

diwali_sale  = make_discount(20)   # 20% off
clearance    = make_discount(50)   # 50% off

print(f"Diwali price: ₹{diwali_sale(2000)}")    # ₹1600.0
print(f"Clearance   : ₹{clearance(2000)}")      # ₹1000.0


# ── 3. Closures ───────────────────────────────
# A closure is a function that "remembers" variables from its
# enclosing scope even after that scope has finished executing.

# Real-life: Request counter — track how many times a user hits an API endpoint

def make_counter(label="hits"):
    count = 0                   # enclosed variable
    def increment():
        nonlocal count
        count += 1
        print(f"{label}: {count}")
    return increment

api_counter  = make_counter("API calls")
page_counter = make_counter("Page views")

api_counter()   # API calls: 1
api_counter()   # API calls: 2
api_counter()   # API calls: 3
page_counter()  # Page views: 1  ← independent counter


# Real-life: Multiplier factory — unit conversion utilities
def make_multiplier(factor):
    return lambda x: x * factor    # lambda is the closure

km_to_miles  = make_multiplier(0.621371)
kg_to_lbs    = make_multiplier(2.20462)
usd_to_inr   = make_multiplier(83.5)

print(f"100 km  = {km_to_miles(100):.2f} miles")
print(f"70 kg   = {kg_to_lbs(70):.2f} lbs")
print(f"$500    = ₹{usd_to_inr(500):.2f}")


# ── Inspecting closures ───────────────────────
def outer(msg):
    def inner():
        print(msg)          # msg is a free variable (closed over)
    return inner

say_hi = outer("Hi there!")
say_hi()                                        # Hi there!
print(say_hi.__closure__[0].cell_contents)      # Hi there!


# ── 4. Decorators (Bonus — built on closures) ─
# Real-life: Logging every function call automatically

def logger(func):
    """Decorator: print function name and args before calling."""
    def wrapper(*args, **kwargs):
        print(f"[CALL] {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"[DONE] {func.__name__} → {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

@logger
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

add(3, 7)
greet("Alice", greeting="Hi")


# ── Key points ────────────────────────────────
# • lambda: single expression, no docstring, use for short inline logic
# • Higher-order functions enable flexible, reusable code
# • Closures remember enclosing scope via cell objects
# • nonlocal keyword lets inner functions modify enclosing variables
# • Decorators = higher-order functions + closures combined
