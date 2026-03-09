# ─────────────────────────────────────────────
# yield — The Heart of Generators
# ─────────────────────────────────────────────

# ── What yield does ───────────────────────────
#
# yield does THREE things at once:
#   1. Produces a value to the caller (like return)
#   2. Suspends the function — freezing all local state
#   3. Resumes from the SAME line on the next next() call
#
# Unlike return (which exits forever), yield is a pause button.

# ── yield vs return ───────────────────────────

def using_return():
    print("  start")
    return 1            # exits; everything below is unreachable
    print("  never runs")
    return 2

def using_yield():
    print("  start")
    yield 1             # pause; caller gets 1
    print("  resumed")
    yield 2             # pause again; caller gets 2
    print("  done")

print("=== return ===")
val = using_return()
print(val)              # 1

print("\n=== yield ===")
gen = using_yield()
print(next(gen))        # start → 1
print(next(gen))        # resumed → 2
# next(gen)             # would raise StopIteration after "done"

# ── yield preserves local state ───────────────

def running_total(numbers):
    total = 0
    for n in numbers:
        total += n
        yield total     # local variable 'total' lives between yields

sales = [200, 150, 300, 100, 250]
print("\nRunning sales total:")
for cumulative in running_total(sales):
    print(f"  ${cumulative}")

# ── yield from — delegating to a sub-generator ─

def inner():
    yield "a"
    yield "b"
    yield "c"

def outer():
    yield "start"
    yield from inner()  # delegate to inner; equivalent to looping and yielding each
    yield "end"

print("\nyield from demo:")
for val in outer():
    print(" ", val)

# 'yield from' also works with any iterable:
def flatten(nested):
    for sublist in nested:
        yield from sublist  # yield every element of each sublist

data = [[1, 2], [3, 4, 5], [6]]
print("\nFlatten:", list(flatten(data)))

# ── Multiple yield paths (branching) ──────────

def classify_transaction(amount):
    if amount < 0:
        yield "debit"
        yield f"amount: ${abs(amount):.2f}"
    elif amount == 0:
        yield "zero transaction"
    else:
        yield "credit"
        yield f"amount: ${amount:.2f}"

print("\nTransaction classifier:")
for msg in classify_transaction(-49.99):
    print(" ", msg)
for msg in classify_transaction(200.00):
    print(" ", msg)

# ── Real-life 1: ETL — transform rows one at a time ──
# In data pipelines, each row is read, transformed, and
# passed downstream without materialising the full dataset.

raw_orders = [
    {"id": 1, "item": "  Laptop ", "price": "999.99", "qty": "2"},
    {"id": 2, "item": "Mouse",     "price": "29.99",  "qty": "5"},
    {"id": 3, "item": " Keyboard", "price": "79.99",  "qty": "3"},
]

def clean_orders(orders):
    for order in orders:
        yield {
            "id":    order["id"],
            "item":  order["item"].strip().title(),
            "price": float(order["price"]),
            "qty":   int(order["qty"]),
            "total": float(order["price"]) * int(order["qty"]),
        }

print("\nCleaned orders:")
for order in clean_orders(raw_orders):
    print(f"  [{order['id']}] {order['item']:10s}  qty={order['qty']}  total=${order['total']:.2f}")

# ── Real-life 2: yield from for tree traversal ──
# Recursively walk a nested category tree (e.g., e-commerce).

category_tree = {
    "Electronics": {
        "Phones": {},
        "Laptops": {"Gaming": {}, "Business": {}},
    },
    "Books": {
        "Fiction": {},
        "Non-Fiction": {"Tech": {}, "Science": {}},
    },
}

def walk_categories(tree, prefix=""):
    for name, subtree in tree.items():
        path = f"{prefix}/{name}" if prefix else name
        yield path
        yield from walk_categories(subtree, path)

print("\nAll categories:")
for cat in walk_categories(category_tree):
    print(" ", cat)

# ── Key points ────────────────────────────────
# • yield pauses; return exits
# • Local variables survive across yields
# • yield from delegates to any iterable or sub-generator
# • Multiple yields in one function are perfectly fine
# • A generator without a yield never yields anything
