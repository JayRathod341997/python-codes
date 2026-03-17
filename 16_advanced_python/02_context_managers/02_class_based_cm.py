"""
============================================================
TOPIC: 02_class_based_cm.py
Real-world context: Creating custom context managers using classes.
Example: Database connection manager.
============================================================
"""

print("=" * 60)
print("SECTION 1: Basic Context Manager Class")
print("=" * 60)

class SimpleContext:
    """Simplest possible context manager."""

    def __enter__(self):
        print("  -> __enter__ called: setup")
        return self  # Return what 'as' variable gets

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("  -> __exit__ called: cleanup")
        return False  # Don't suppress exceptions


print("\n1. Using simple context manager:")
with SimpleContext() as ctx:
    print("  In the with block")
print("  Exited with block\n")


print("\n" + "=" * 60)
print("SECTION 2: Database Connection Manager")
print("=" * 60)

class DatabaseConnection:
    """Manage database connection lifecycle."""

    def __init__(self, db_name: str) -> None:
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        print(f"  -> Opening connection to {self.db_name}")
        self.connection = f"Connection<{self.db_name}>"
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"  -> Closing connection to {self.db_name}")
        self.connection = None
        return False


print("\n1. Using database context manager:")
with DatabaseConnection("mydb") as conn:
    print(f"  Using connection: {conn}")
    print(f"  Connection active: {conn is not None}")
print("  Connection closed\n")


print("\n" + "=" * 60)
print("SECTION 3: Exception Handling in __exit__")
print("=" * 60)

class SafeConnection:
    """Connection that handles exceptions gracefully."""

    def __init__(self, db_name: str) -> None:
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        print(f"  -> Opening {self.db_name}")
        self.connection = f"Connection<{self.db_name}>"
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"  -> Closing {self.db_name}")

        if exc_type is not None:
            print(f"  -> Exception occurred: {exc_type.__name__}: {exc_val}")

        self.connection = None

        # Return False to propagate exception
        # Return True to suppress exception
        return False


print("\n1. Normal execution:")
with SafeConnection("db1") as conn:
    print(f"  Working with: {conn}")

print("\n2. Exception occurs:")
try:
    with SafeConnection("db2") as conn:
        print(f"  Working with: {conn}")
        raise ValueError("Invalid query")
except ValueError as e:
    print(f"  Caught exception: {e}")


print("\n" + "=" * 60)
print("SECTION 4: Timer Context Manager")
print("=" * 60)

import time

class Timer:
    """Measure execution time of code block."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()
        print(f"  -> Starting timer: {self.name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start_time
        print(f"  -> {self.name} took {elapsed:.3f} seconds")
        return False


print("\n1. Using timer:")
with Timer("Sleep operation") as timer:
    time.sleep(0.5)

print("\n2. Measuring function call:")
def slow_function():
    time.sleep(0.2)
    print("    Function completed")

with Timer("Slow function") as timer:
    slow_function()


print("\n" + "=" * 60)
print("SECTION 5: File Wrapper Context Manager")
print("=" * 60)

class FileWrapper:
    """Wrapper around file with logging."""

    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"  -> Opening file: {self.filename} (mode={self.mode})")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"  -> Closing file: {self.filename}")
        if self.file:
            self.file.close()
        return False


print("\n1. Using file wrapper:")
# Create a test file
test_file = "wrapper_test.txt"

with FileWrapper(test_file, "w") as f:
    f.write("Hello from wrapper!\n")
    print(f"    Wrote to file")

with FileWrapper(test_file, "r") as f:
    content = f.read()
    print(f"    Read: {content.strip()}")


print("\n" + "=" * 60)
print("SECTION 6: Lock/Semaphore Context Manager")
print("=" * 60)

from threading import Lock

class SafeCounter:
    """Thread-safe counter using context manager for locks."""

    def __init__(self) -> None:
        self.count = 0
        self.lock = Lock()

    def increment(self) -> None:
        with self.lock:
            # Lock is acquired here
            self.count += 1
            print(f"    Count incremented to {self.count}")
            # Lock is released here


print("\n1. Using lock context manager:")
counter = SafeCounter()
counter.increment()
counter.increment()
counter.increment()
print(f"Final count: {counter.count}")


print("\n" + "=" * 60)
print("KEY POINTS")
print("=" * 60)
print("""
1. Context manager protocol:
   def __enter__(self): ...
   def __exit__(self, exc_type, exc_val, exc_tb): ...

2. __enter__:
   - Called when entering 'with' block
   - Should set up resources
   - Can return any value (accessed as 'as' variable)

3. __exit__:
   - Always called on exit (even on exception)
   - exc_type, exc_val, exc_tb = exception info (None if no error)
   - Return True to suppress exception, False to propagate

4. Exception handling:
   - Code in __exit__ runs even if exception occurred
   - Cleanup is guaranteed
   - Can decide whether to suppress exception

5. Real-world uses:
   - File/database connections
   - Thread locks/semaphores
   - Timing code blocks
   - Resource allocation (memory, connections, etc.)

6. Class-based vs @contextmanager:
   Use class when: complex logic, multiple methods
   Use decorator when: simple setup/cleanup
""")

# Cleanup
import os
os.remove(test_file)
print("\nTest file cleaned up.")
