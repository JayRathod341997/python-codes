# ─────────────────────────────────────────────
# Generator Pipelines
# ─────────────────────────────────────────────

# ── What is a generator pipeline? ────────────
#
# A generator pipeline is a chain of generators where:
#   - each generator takes the previous one as its input
#   - data flows lazily through the entire chain
#   - NO intermediate lists are created at any stage
#
# Think of it like Unix pipes:
#   cat file.log | grep ERROR | awk '{print $3}' | sort | uniq
#
# In Python:
#   source → filter → transform → aggregate
#
# Key properties:
#   • Memory: only ONE item exists in the pipeline at a time
#   • Composable: each stage is a reusable generator function
#   • Lazy: nothing runs until the consumer (for loop / list()) pulls

# ── Building a simple pipeline ────────────────

# Stage 1: source
def read_numbers(numbers):
    for n in numbers:
        yield n

# Stage 2: filter
def only_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n

# Stage 3: transform
def square(numbers):
    for n in numbers:
        yield n * n

# Stage 4: consumer (pulls data through the pipeline)
source   = read_numbers(range(1, 11))
filtered = only_even(source)
squared  = square(filtered)

print("Even squares 1-10:", list(squared))

# ── Inline with generator expressions ─────────
# The same pipeline in one expression — even more concise:

result = (
    n * n
    for n in range(1, 11)
    if n % 2 == 0
)
print("Same result (gen expr):", list(result))

# ── Real-life 1: Log processing pipeline ──────
# Classic ETL on a server log:
#   read → parse → filter errors → extract fields → format report

raw_logs = [
    "2024-01-10 08:00:01 INFO  user=alice action=login",
    "2024-01-10 08:00:05 ERROR user=bob   action=payment  code=402",
    "2024-01-10 08:00:09 INFO  user=carol action=view",
    "2024-01-10 08:00:12 ERROR user=alice action=checkout code=500",
    "2024-01-10 08:00:15 WARN  user=dave  action=login",
    "2024-01-10 08:00:18 ERROR user=carol action=payment  code=402",
    "2024-01-10 08:01:00 INFO  user=eve   action=logout",
]

def parse_log_lines(lines):
    """Stage 1: parse each raw line into a dict."""
    for line in lines:
        parts = line.split()
        record = {"date": parts[0], "time": parts[1], "level": parts[2]}
        for kv in parts[3:]:
            if "=" in kv:
                k, v = kv.split("=", 1)
                record[k] = v
        yield record

def filter_level(records, level):
    """Stage 2: keep only records matching level."""
    for r in records:
        if r["level"] == level:
            yield r

def add_severity(records):
    """Stage 3: enrich record with a human-readable severity label."""
    labels = {"ERROR": "🔴 CRITICAL", "WARN": "🟡 WARNING", "INFO": "🟢 INFO"}
    for r in records:
        r["severity"] = labels.get(r["level"], r["level"])
        yield r

def format_report(records):
    """Stage 4: format for display."""
    for r in records:
        code = r.get("code", "N/A")
        yield f"[{r['time']}] {r['severity']} — user={r['user']} action={r['action']} code={code}"

# Assemble the pipeline — nothing runs yet
stage1 = parse_log_lines(raw_logs)
stage2 = filter_level(stage1, "ERROR")
stage3 = add_severity(stage2)
stage4 = format_report(stage3)

# Consumer pulls data through all 4 stages lazily:
print("\n=== Error Report ===")
for line in stage4:
    print(" ", line)

# ── Real-life 2: Data import pipeline ─────────
# Transform raw CSV rows into validated, enriched order records.

csv_data = [
    "order_id,customer,amount,currency",
    "ORD-001,Alice,  1200.50 ,USD",
    "ORD-002,Bob,   -50.00  ,USD",
    "ORD-003,Carol, 340.00  ,EUR",
    "ORD-004,,      200.00  ,USD",
    "ORD-005,Dave,  88.75   ,GBP",
]

def skip_header(rows):
    it = iter(rows)
    next(it)            # discard header
    yield from it

def parse_csv(rows):
    for row in rows:
        parts = [p.strip() for p in row.split(",")]
        yield {"order_id": parts[0], "customer": parts[1],
               "amount": parts[2], "currency": parts[3]}

def validate(records):
    for r in records:
        try:
            amount = float(r["amount"])
        except ValueError:
            continue                    # skip unparseable
        if not r["customer"]:
            continue                    # skip missing customer
        if amount <= 0:
            continue                    # skip negative/zero amounts
        r["amount"] = amount
        yield r

def convert_to_usd(records):
    rates = {"USD": 1.0, "EUR": 1.08, "GBP": 1.27}
    for r in records:
        rate = rates.get(r["currency"], 1.0)
        r["amount_usd"] = round(r["amount"] * rate, 2)
        yield r

# Pipeline
pipeline = convert_to_usd(
    validate(
        parse_csv(
            skip_header(csv_data)
            )
        )
    )

print("\n=== Valid Orders (USD) ===")
total_usd = 0
for order in pipeline:
    print(f"  {order['order_id']}  {order['customer']:6s}  ${order['amount_usd']:>8.2f}")
    total_usd += order["amount_usd"]
print(f"  {'TOTAL':>18}  ${total_usd:>8.2f}")

# ── Pipeline with itertools ────────────────────
import itertools

def generate_orders(n):
    statuses = itertools.cycle(["pending", "shipped", "delivered"])
    for i in range(1, n + 1):
        yield {"id": i, "status": next(statuses), "amount": i * 10.0}

def shipped_only(orders):
    return (o for o in orders if o["status"] == "shipped")

orders_pipeline = shipped_only(generate_orders(12))
print("\nShipped orders:")
for o in orders_pipeline:
    print(f"  #{o['id']:02d}  ${o['amount']:.2f}")

# ── Key points ────────────────────────────────
# • Each stage is a generator that wraps the previous one
# • Data flows on demand — no intermediate lists created
# • Stages are independently testable and reusable
# • Can combine generator functions AND generator expressions
# • itertools provides ready-made pipeline stages (chain, islice, etc.)
# • The pipeline only runs when the consumer (for/list/sum) pulls
