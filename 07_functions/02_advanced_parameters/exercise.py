# ─────────────────────────────────────────────
# Exercises — Advanced Parameters
# ─────────────────────────────────────────────

# ── Exercise 1: Flexible Greeting ────────────
# Real-life: Notification system
# Write a function notify(user, *channels, priority="normal", **options)
# that prints:
#
#   Notifying: alice  via: email, sms  priority: HIGH
#   Options  : retry=3, sound=True
#
# Call it with at least 2 channels and 2 extra options.
# Uppercase the priority in output.

# --- your code here ---


# ── Exercise 2: Restaurant Order Builder ─────
# Real-life: POS (point of sale) system
# Write a function place_order(table_no, *dishes, discount=0, **extras)
# that prints a receipt:
#
#   Table #5 Order
#   ─────────────────────────
#   Dishes  : Paneer Tikka, Naan, Lassi
#   Extras  : spice=extra, no_onion=True
#   Discount: 10%
#
# Test with table 5, 3 dishes, 10% discount, and 2 extra preferences.

# --- your code here ---


# ── Exercise 3: Safe Config Loader ───────────
# Real-life: App configuration system
# Write a function load_config(filepath, *, encoding="utf-8",
#                              strict=False, timeout=5)
# The parameters encoding, strict, timeout must be keyword-only.
# The function should just print what it would do (no actual file read):
#
#   Loading 'config.yaml'  encoding=utf-8  strict=False  timeout=5s
#
# Try calling it without keyword names for encoding — expect a TypeError.
# (Comment out the bad call after observing the error.)

# --- your code here ---


# ── Exercise 4: Statistics Calculator ────────
# Real-life: Analytics dashboard
# Write a function stats(*numbers) that accepts any count of numbers
# and returns a dict with keys: count, total, mean, minimum, maximum.
# Do NOT use built-in min/max/sum for the main logic —
# compute them with a loop to practice *args.
#
# Test with: stats(10, 20, 30, 40, 50)
# Output:
#   {'count': 5, 'total': 150, 'mean': 30.0, 'minimum': 10, 'maximum': 50}

# --- your code here ---


# ── Exercise 5: URL Query Builder ────────────
# Real-life: REST API client
# Write a function build_url(base, endpoint, **params) that builds a URL:
#
#   build_url("https://api.example.com", "/search",
#             q="python functions", page=2, limit=10)
#   → "https://api.example.com/search?q=python+functions&page=2&limit=10"
#
# Hint: encode spaces in values as '+'.
# Use str(v).replace(" ", "+") for each value.

# --- your code here ---


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: Notifying: alice  via: email, sms  priority: NORMAL  Options: ...
# Ex2: Formatted receipt block
# Ex3: Loading line printed; TypeError on positional encoding call
# Ex4: {'count': 5, 'total': 150, 'mean': 30.0, 'minimum': 10, 'maximum': 50}
# Ex5: https://api.example.com/search?q=python+functions&page=2&limit=10
# ─────────────────────────────────────────────
