# Solutions — Project 12: Decorators

import functools
import time

print("\n" + "="*70)
print("EXERCISE 1 SOLUTION: Timer + Logger (Stacked)")
print("="*70 + "\n")

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"  ⏱ {func.__name__} took {duration:.4f}s")
        return result
    return wrapper

def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  📝 Calling {func.__name__}({args})")
        result = func(*args, **kwargs)
        print(f"  ✓ Returned {result}")
        return result
    return wrapper

@timer
@log_call
def square(x):
    time.sleep(0.1)
    return x * x

result = square(5)

print("\n" + "="*70)
print("EXERCISE 2 SOLUTION: Cache Decorator")
print("="*70 + "\n")

def cache(func):
    cache_dict = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache_dict:
            print(f"  💾 Cache hit for {func.__name__}{args}")
            return cache_dict[args]
        result = func(*args)
        cache_dict[args] = result
        return result
    return wrapper

@cache
def fibonacci(n):
    time.sleep(0.5)
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("1st call to fibonacci(5):")
fib1 = fibonacci(5)
print(f"  Result: {fib1}")

print("2nd call to fibonacci(5) (from cache):")
fib2 = fibonacci(5)
print(f"  Result: {fib2}")

print("\n" + "="*70 + "\n")
