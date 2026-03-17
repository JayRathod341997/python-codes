"""
============================================================
TOPIC: 03_contextlib_module.py
Real-world context: Using Python's contextlib utilities.
@contextmanager decorator, suppress, nullcontext.
============================================================
"""

from contextlib import contextmanager, suppress, nullcontext
import os
import time

print("=" * 60)
print("SECTION 1: @contextmanager Decorator")
print("=" * 60)

@contextmanager
def timer(name: str):
    """Simple timer using decorator."""
    print(f"  -> Starting {name}")
    start = time.time()
    try:
        yield  # Return control to 'with' block
    finally:
        elapsed = time.time() - start
        print(f"  -> {name} finished in {elapsed:.3f}s")


print("\n1. Using @contextmanager:")
with timer("Operation A"):
    time.sleep(0.2)

with timer("Operation B"):
    time.sleep(0.3)


print("\n" + "=" * 60)
print("SECTION 2: @contextmanager with Return Value")
print("=" * 60)

@contextmanager
def database_connection(db_name: str):
    """Database connection with setup/cleanup."""
    print(f"  -> Connecting to {db_name}")
    connection = f"Connection<{db_name}>"
    try:
        yield connection  # Return value to 'as' variable
    finally:
        print(f"  -> Disconnecting from {db_name}")


print("\n1. Using connection:")
with database_connection("analytics") as conn:
    print(f"  Using {conn}")
    print(f"  Executing query...")


print("\n" + "=" * 60)
print("SECTION 3: @contextmanager with Exception Handling")
print("=" * 60)

@contextmanager
def error_handler(operation_name: str):
    """Context manager that catches exceptions."""
    print(f"  -> Starting {operation_name}")
    try:
        yield
    except ValueError as e:
        print(f"  -> Caught ValueError: {e}")
        print(f"  -> Recovering...")
    except Exception as e:
        print(f"  -> Unexpected error: {type(e).__name__}: {e}")
        raise
    finally:
        print(f"  -> Cleaning up {operation_name}")


print("\n1. Caught exception:")
with error_handler("risky operation"):
    print(f"  Doing something...")
    raise ValueError("Invalid data")
print("  Execution continues after error")

print("\n2. Uncaught exception:")
try:
    with error_handler("another operation"):
        print(f"  Doing something...")
        raise RuntimeError("System error")
except RuntimeError as e:
    print(f"  Exception re-raised: {e}")


print("\n" + "=" * 60)
print("SECTION 4: contextlib.suppress()")
print("=" * 60)

print("\n1. Without suppress (error):")
try:
    os.remove("nonexistent.txt")
except FileNotFoundError:
    print("  -> File not found (caught manually)")

print("\n2. With suppress (cleaner):")
# Silently ignore FileNotFoundError
with suppress(FileNotFoundError):
    os.remove("also_nonexistent.txt")
print("  -> No error message, suppressed automatically")

print("\n3. Suppress multiple exceptions:")
with suppress(FileNotFoundError, PermissionError, OSError):
    os.remove("maybe_exists.txt")
print("  -> Any of these exceptions would be suppressed")


print("\n" + "=" * 60)
print("SECTION 5: contextlib.nullcontext()")
print("=" * 60)

@contextmanager
def optional_context(condition: bool):
    """Return nullcontext if condition is false."""
    if condition:
        print("  -> Using actual context manager")
        yield "real context"
    else:
        print("  -> Using null context (no-op)")
        with nullcontext("dummy") as ctx:
            yield ctx


print("\n1. With condition=True:")
with optional_context(True) as ctx:
    print(f"  Context value: {ctx}")

print("\n2. With condition=False:")
with optional_context(False) as ctx:
    print(f"  Context value: {ctx}")


print("\n" + "=" * 60)
print("SECTION 6: Decorator vs contextlib Comparison")
print("=" * 60)

print("\n1. Using @contextmanager (decorator approach):")
@contextmanager
def simple_setup():
    print("  -> Setup with decorator")
    try:
        yield
    finally:
        print("  -> Cleanup with decorator")


with simple_setup():
    print("  Inside block")

print("\n2. Equivalent class-based:")
class SimpleSetup:
    def __enter__(self):
        print("  -> Setup with class")
        return self

    def __exit__(self, *args):
        print("  -> Cleanup with class")


with SimpleSetup():
    print("  Inside block")


print("\n" + "=" * 60)
print("SECTION 7: Real-World Example - Configuration Override")
print("=" * 60)

class Config:
    """Global configuration."""
    debug_mode = False
    max_retries = 3


@contextmanager
def temporary_config(**kwargs):
    """Temporarily override configuration."""
    old_values = {}
    for key, value in kwargs.items():
        old_values[key] = getattr(Config, key)
        setattr(Config, key, value)
        print(f"  -> Set {key} = {value}")

    try:
        yield
    finally:
        for key, value in old_values.items():
            setattr(Config, key, value)
            print(f"  -> Reset {key} = {value}")


print("\n1. Using temporary config override:")
print(f"Initial debug_mode: {Config.debug_mode}")
print(f"Initial max_retries: {Config.max_retries}")

with temporary_config(debug_mode=True, max_retries=5):
    print(f"Inside context:")
    print(f"  debug_mode: {Config.debug_mode}")
    print(f"  max_retries: {Config.max_retries}")

print(f"After context:")
print(f"  debug_mode: {Config.debug_mode}")
print(f"  max_retries: {Config.max_retries}")


print("\n" + "=" * 60)
print("KEY POINTS")
print("=" * 60)
print("""
1. @contextmanager simplifies context manager creation
   @contextmanager
   def my_context():
       # Setup
       yield resource
       # Cleanup

2. Code before yield = __enter__ logic
   Code after yield = __exit__ logic

3. suppress() ignores specific exceptions
   with suppress(FileNotFoundError):
       os.remove(file)

4. nullcontext() is a no-op context manager
   Used for conditional context managers

5. @contextmanager is shorter than class-based
   Use for simple setup/cleanup
   Use class for complex logic

6. Real-world uses:
   - Timing operations
   - Temporary config overrides
   - Resource acquisition
   - Exception handling
   - Logging context
""")
