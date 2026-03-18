# ───────────────────────────────────────────────────────────────
# Exercises — Project 12: Decorators
# ───────────────────────────────────────────────────────────────

# ── Exercise 1: Combine Timer + Logger Decorators ───────────────────
# Task: Create two decorators: @timer and @log_call.
#       Apply both to a function (stacked).
#       Observe execution order.
#
# Requirements:
#   - Define @timer (measure execution time)
#   - Define @log_call (print function name, args, return value)
#   - Stack both: @timer @log_call def my_function(x)
#   - Call function and observe output
#   - Verify @functools.wraps is used
#
# Hint: Stacking order matters! Bottom decorator runs first.

# --- your code here ---




# ── Exercise 2: Caching Decorator with Performance Gain ────────────
# Task: Create @cache decorator. Show performance improvement on
#       repeated calls.
#
# Requirements:
#   - Define @cache that stores results
#   - Define expensive_operation(n) that takes time to compute
#   - Call with same arg twice: show 2nd is faster
#   - Print cache hit message on 2nd call
#
# Hint: Cache is a dict mapping args to results. Check if args exist.

# --- your code here ---




# ── Exercise 3: Retry Decorator with Exponential Backoff ──────────
# Task: Create @retry(max_attempts, delay) that retries with increasing delay.
#
# Requirements:
#   - Define @retry decorator factory
#   - On failure, delay should increase (exponential backoff)
#   - Retry up to max_attempts times
#   - On final failure, raise exception
#   - Test with a function that fails 1st time, succeeds 2nd
#
# Hint: Use delay * attempt for exponential backoff. Sleep between retries.

# --- your code here ---




# ───────────────────────────────────────────────────────────────
# Expected outputs (for self-check):
#
# Ex1: Stacked decorators output
#      📝 Calling my_function(5)
#      ⏱ my_function took 0.1s
#      ✓ my_function returned 25
#
# Ex2: Cache performance
#      1st call: 1.0s
#      2nd call (cached): 0.001s
#      Cache hit message displayed
#
# Ex3: Retry with backoff
#      Attempt 1: failed
#      Attempt 2: success
#      Total time: sum of backoff delays
# ───────────────────────────────────────────────────────────────
