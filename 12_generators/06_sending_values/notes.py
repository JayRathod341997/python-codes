# ─────────────────────────────────────────────
# Sending Values to Generators — .send() / .throw() / .close()
# ─────────────────────────────────────────────

# ── Beyond one-way generators ─────────────────
#
# So far generators only pushed values OUT to the caller.
# Python's generator protocol also supports two-way communication:
#
#   gen.send(value)   → resumes the generator AND passes 'value'
#                       in as the result of the yield expression
#   gen.throw(exc)    → injects an exception at the yield point
#   gen.close()       → injects GeneratorExit, shutting it down
#
# A generator that uses send() is sometimes called a "coroutine"
# (though modern Python uses async/await for that role).

# ── How yield becomes an expression ───────────
#
# received = yield produced_value
#
#   produced_value → sent to caller (via next / send)
#   received       → value the caller sends back (via .send())
#
# First call MUST be next(gen) or gen.send(None) to advance
# to the first yield — you cannot send a non-None value before
# the generator reaches a yield.

# ── Minimal example ───────────────────────────

def accumulator():
    """Yield running total; accept new numbers via send()."""
    total = 0
    while True:
        value = yield total     # yield current total, receive next number
        if value is None:
            break
        total += value

gen = accumulator()
next(gen)           # prime: advance to first yield (total=0)

print(gen.send(10))     # 10
print(gen.send(25))     # 35
print(gen.send(5))      # 40

gen.close()             # clean shutdown

# ── .send() step-by-step ──────────────────────

def echo():
    """Receive a value and yield it back doubled."""
    while True:
        received = yield
        if received is None:
            return
        print(f"  generator received: {received!r}, echoing: {received * 2!r}")
        yield received * 2

e = echo()
next(e)                     # prime
result = e.send("hello")    # send → generator echoes "hellohello"
print("caller got:", result)

next(e)                     # prime for next iteration
result = e.send(7)
print("caller got:", result)

# ── .throw() — inject an exception ────────────

def safe_processor():
    while True:
        try:
            data = yield
        except ValueError as exc:
            print(f"  [generator] bad data: {exc} — skipping")
        else:
            print(f"  [generator] processed: {data}")

proc = safe_processor()
next(proc)

proc.send("record_A")
proc.throw(ValueError, "corrupted row")
proc.send("record_B")
proc.close()

# ── .close() — graceful shutdown ──────────────

def resource_holder():
    print("  [gen] acquiring resource")
    try:
        while True:
            item = yield
            print(f"  [gen] handling: {item}")
    except GeneratorExit:
        print("  [gen] GeneratorExit caught — releasing resource")
    finally:
        print("  [gen] cleanup done")

print("\nResource holder:")
rh = resource_holder()
next(rh)
rh.send("job_1")
rh.send("job_2")
rh.close()          # triggers GeneratorExit inside the generator

# ── Real-life 1: Stateful moving average ──────
# A data pipeline stage that maintains a sliding window
# and accepts new data points via send().

def moving_average(window_size):
    """Coroutine: receive values, yield moving average."""
    window = []
    avg    = None
    while True:
        value = yield avg
        if value is None:
            return
        window.append(value)
        if len(window) > window_size:
            window.pop(0)
        avg = sum(window) / len(window)

print("\nMoving average (window=3):")
ma = moving_average(3)
next(ma)                            # prime

stock_prices = [10, 12, 11, 13, 15, 14, 16]
for price in stock_prices:
    avg = ma.send(price)
    print(f"  price={price:5.1f}  moving_avg={avg:.2f}")

ma.close()

# ── Real-life 2: Interactive form validator ───
# A coroutine that validates form fields one at a time,
# telling the caller which field it's waiting for next.

def form_validator():
    errors = []

    name = yield "Enter name"
    if not name or len(name) < 2:
        errors.append("Name too short")

    email = yield "Enter email"
    if "@" not in (email or ""):
        errors.append("Invalid email")

    age_str = yield "Enter age"
    try:
        age = int(age_str)
        if not (18 <= age <= 120):
            errors.append("Age must be 18-120")
    except (TypeError, ValueError):
        errors.append("Age must be a number")

    yield errors    # final yield: hand back validation result

print("\nForm validation:")
validator = form_validator()
prompt = next(validator)

# Simulate a user filling in the form
responses = {"Enter name": "J", "Enter email": "not-an-email", "Enter age": "25"}

while True:
    try:
        result = validator.send(responses.get(prompt))
        if isinstance(result, list):
            print("  Validation errors:", result)
            break
        prompt = result
    except StopIteration:
        break

# ── Key points ────────────────────────────────
# • yield is an EXPRESSION when used with .send()
# • Prime the generator with next() or .send(None) first
# • .send(value) resumes AND injects value at the yield point
# • .throw(exc)  injects an exception — generator can catch it
# • .close()     injects GeneratorExit — use finally to clean up
# • Useful for: stateful pipelines, coroutines, protocol machines
