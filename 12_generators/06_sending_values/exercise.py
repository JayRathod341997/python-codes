# ─────────────────────────────────────────────
# Exercises — Sending Values to Generators
# ─────────────────────────────────────────────

# ── Exercise 1: Echo coroutine ────────────────
# Real-life: understanding the two-way send protocol
# Write a coroutine echo_upper() that:
#   - receives a string via send()
#   - yields back the string in UPPERCASE
# Test with three sends.

# --- your code here ---

# gen = echo_upper()
# next(gen)                           # prime
# print(gen.send("hello"))            # HELLO
# print(gen.send("world"))            # WORLD
# print(gen.send("python generators")) # PYTHON GENERATORS


# Expected output:
# HELLO
# WORLD
# PYTHON GENERATORS


# ── Exercise 2: Running total coroutine ───────
# Real-life: real-time sales dashboard
# Write a coroutine running_total() that:
#   - receives a number via send()
#   - yields the cumulative total so far
# Test by sending 5 sales amounts.

sales = [150.0, 200.0, 75.50, 310.0, 99.99]

# --- your code here ---


# Expected output:
# 150.00
# 350.00
# 425.50
# 735.50
# 835.49


# ── Exercise 3: .throw() — skipping bad data ──
# Real-life: ETL pipeline that skips corrupted records
# Write a coroutine data_sink() that:
#   - receives records via send() and prints "Saved: <record>"
#   - catches ValueError thrown from outside and prints "Skipped bad record"
#   - continues running after catching the error
# Use .throw(ValueError) to simulate a bad record in the middle.

records = ["order_001", "order_002", "<CORRUPT>", "order_003"]

# --- your code here ---
# sink = data_sink()
# next(sink)
# sink.send(records[0])
# sink.send(records[1])
# sink.throw(ValueError, "corrupt data")
# sink.send(records[3])
# sink.close()


# Expected output:
# Saved: order_001
# Saved: order_002
# Skipped bad record
# Saved: order_003


# ── Exercise 4: .close() with cleanup ─────────
# Real-life: database connection that must be closed properly
# Write a coroutine db_connection(db_name) that:
#   - prints "Connecting to <db_name>"
#   - receives and prints queries via send()
#   - on .close(), prints "Disconnecting from <db_name>"
# Use a try/finally to guarantee the disconnect message.

# --- your code here ---

# conn = db_connection("orders_db")
# next(conn)
# conn.send("SELECT * FROM orders")
# conn.send("UPDATE orders SET status='shipped' WHERE id=5")
# conn.close()


# Expected output:
# Connecting to orders_db
# Executing: SELECT * FROM orders
# Executing: UPDATE orders SET status='shipped' WHERE id=5
# Disconnecting from orders_db


# ── Exercise 5: Stateful coroutine — min/max tracker ──
# Real-life: live metrics dashboard tracking price range
# Write a coroutine price_tracker() that:
#   - receives a price (float) via send()
#   - yields a dict {"min": ..., "max": ..., "latest": ...}
#     updated with each new price
# Test with 6 prices.

prices = [105.5, 98.0, 112.3, 95.7, 108.0, 101.2]

# --- your code here ---


# Expected output:
# {'min': 105.5, 'max': 105.5, 'latest': 105.5}
# {'min':  98.0, 'max': 105.5, 'latest':  98.0}
# {'min':  98.0, 'max': 112.3, 'latest': 112.3}
# {'min':  95.7, 'max': 112.3, 'latest':  95.7}
# {'min':  95.7, 'max': 112.3, 'latest': 108.0}
# {'min':  95.7, 'max': 112.3, 'latest': 101.2}


# ─────────────────────────────────────────────
# Self-check:
# Ex1: 3 uppercase echoes
# Ex2: cumulative totals ending at 835.49
# Ex3: 3 saves + 1 skip message
# Ex4: connect → 2 queries → disconnect
# Ex5: 6 dicts with correct min/max/latest
# ─────────────────────────────────────────────
