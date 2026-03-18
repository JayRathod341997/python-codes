# ─────────────────────────────────────────────────────────────────
# Project 12 — IT — API Monitoring with Decorators
# Concepts  : decorators, @functools.wraps, decorator factories
# Difficulty: Advanced
# ─────────────────────────────────────────────────────────────────

import functools
import time

print("\n" + "="*75)
print("API MONITORING — DECORATORS IN ACTION")
print("="*75)

# ── Section 1: @timer Decorator ────────────────────────────────────
def timer(func):
    """Measure function execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"  ⏱ {func.__name__} took {duration:.4f}s")
        return result
    return wrapper

# ── Section 2: @log_call Decorator ────────────────────────────────
def log_call(func):
    """Log function calls with args and return value."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  📝 Calling {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"  ✓ {func.__name__} returned {result}")
        return result
    return wrapper

# ── Section 3: @retry Decorator (Decorator Factory) ────────────────
def retry(max_attempts=3, delay=0.5):
    """Retry decorator factory."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt < max_attempts:
                        print(f"  ⚠ Attempt {attempt} failed: {e}. Retrying...")
                        time.sleep(delay)
                    else:
                        print(f"  ✗ All {max_attempts} attempts failed.")
                        raise
        return wrapper
    return decorator

# ── Section 4: @cache_result Decorator ────────────────────────────
def cache_result(func):
    """Simple memoization decorator."""
    cache = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache:
            print(f"  💾 Returning cached result for {func.__name__}")
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper

# ── Section 5: Stacked Decorators ──────────────────────────────────
@timer
@log_call
@cache_result
def fetch_user_data(user_id):
    """Simulated API call (with caching + logging + timing)."""
    time.sleep(0.1)
    return {"user_id": user_id, "name": "Arun Kumar"}

@retry(max_attempts=3, delay=0.2)
@timer
def fetch_with_retry():
    """Simulated flaky API that succeeds on 2nd try."""
    import random
    if random.random() < 0.5:
        raise Exception("Network timeout")
    return "Data received"

# ── Section 6: Demo ────────────────────────────────────────────────
print("\n--- Test 1: Cached call ---")
result1 = fetch_user_data(101)

print("\n--- Test 2: Same call (should use cache) ---")
result2 = fetch_user_data(101)

print("\n--- Test 3: Retry with flaky API ---")
try:
    result3 = fetch_with_retry()
except Exception as e:
    print(f"  Failed: {e}")

print("\n" + "="*75 + "\n")
