"""
============================================================
TOPIC: 04_real_world_examples.py
Real-world context: Practical context manager examples.
Database connections, file operations, temp directories, locks.
============================================================
"""

from contextlib import contextmanager
from tempfile import TemporaryDirectory
from threading import Lock
import os

print("=" * 60)
print("SECTION 1: Database Transaction Manager")
print("=" * 60)

class Database:
    """Simulated database with transaction support."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.in_transaction = False
        self.data = {}

    @contextmanager
    def transaction(self):
        """Context manager for atomic transactions."""
        print(f"  -> Beginning transaction")
        self.in_transaction = True
        try:
            yield
            print(f"  -> Committing transaction")
        except Exception as e:
            print(f"  -> Rolling back transaction (error: {e})")
            raise
        finally:
            self.in_transaction = False

    def set(self, key: str, value: str) -> None:
        if not self.in_transaction:
            print(f"    Warning: Set outside transaction")
        self.data[key] = value


print("\n1. Successful transaction:")
db = Database("myapp")
try:
    with db.transaction():
        db.set("user:1:name", "Alice")
        db.set("user:1:email", "alice@example.com")
        print(f"    Data set: {db.data}")
except Exception:
    pass

print("\n2. Failed transaction:")
db = Database("myapp")
try:
    with db.transaction():
        db.set("user:2:name", "Bob")
        raise ValueError("Invalid email")
        db.set("user:2:email", "bob@example.com")
except ValueError:
    print(f"    Data after rollback: {db.data}")


print("\n" + "=" * 60)
print("SECTION 2: File Operations with Automatic Cleanup")
print("=" * 60)

@contextmanager
def read_write_files(input_file: str, output_file: str):
    """Context manager for file pair operations."""
    inp = None
    out = None
    try:
        print(f"  -> Opening input: {input_file}")
        inp = open(input_file, "r")
        print(f"  -> Opening output: {output_file}")
        out = open(output_file, "w")
        yield inp, out
    finally:
        if inp:
            inp.close()
            print(f"  -> Closed input")
        if out:
            out.close()
            print(f"  -> Closed output")


print("\n1. Using file pair manager:")
# Create test input
with open("input.txt", "w") as f:
    f.write("Hello\nWorld\nPython\n")

with read_write_files("input.txt", "output.txt") as (inp, out):
    for line in inp:
        out.write(line.upper())
    print(f"    Processed file")

# Verify output
with open("output.txt", "r") as f:
    print(f"    Output: {f.read()}")


print("\n" + "=" * 60)
print("SECTION 3: Temporary Directory Manager")
print("=" * 60)

print("\n1. Using TemporaryDirectory:")
with TemporaryDirectory() as tmpdir:
    print(f"  -> Created temp directory: {tmpdir}")
    test_file = os.path.join(tmpdir, "test.txt")
    with open(test_file, "w") as f:
        f.write("Temporary data")
    print(f"  -> Files in temp dir: {os.listdir(tmpdir)}")
print(f"  -> Temp directory cleaned up automatically")


print("\n" + "=" * 60)
print("SECTION 4: Lock-Based Synchronization")
print("=" * 60)

class Counter:
    """Thread-safe counter with lock."""

    def __init__(self) -> None:
        self.count = 0
        self.lock = Lock()

    def increment(self) -> None:
        with self.lock:
            print(f"    Lock acquired")
            self.count += 1
            print(f"    Count = {self.count}")
            print(f"    Lock released")

    def get_count(self) -> int:
        with self.lock:
            return self.count


print("\n1. Using thread lock:")
counter = Counter()
counter.increment()
counter.increment()
print(f"Final count: {counter.get_count()}")


print("\n" + "=" * 60)
print("SECTION 5: Logging Context Manager")
print("=" * 60)

@contextmanager
def log_operation(operation_name: str, verbose: bool = False):
    """Log entry/exit of an operation."""
    print(f"  [LOG] Starting: {operation_name}")
    try:
        yield
    except Exception as e:
        print(f"  [ERROR] {operation_name} failed: {e}")
        raise
    finally:
        print(f"  [LOG] Finished: {operation_name}")


print("\n1. Normal operation:")
with log_operation("Database query"):
    print(f"    Executing query...")
    # Query result here
    pass

print("\n2. Operation with error:")
try:
    with log_operation("API request"):
        print(f"    Making request...")
        raise ConnectionError("Network timeout")
except ConnectionError:
    print(f"    Error handled")


print("\n" + "=" * 60)
print("SECTION 6: Resource Pool Manager")
print("=" * 60)

class ConnectionPool:
    """Manage a pool of connections."""

    def __init__(self, max_size: int = 5) -> None:
        self.max_size = max_size
        self.available = [f"Conn{i}" for i in range(max_size)]
        self.in_use = []

    @contextmanager
    def get_connection(self):
        """Get a connection from pool."""
        if not self.available:
            raise RuntimeError("No connections available")

        conn = self.available.pop()
        self.in_use.append(conn)
        print(f"  -> Acquired {conn} (available: {len(self.available)})")

        try:
            yield conn
        finally:
            self.in_use.remove(conn)
            self.available.append(conn)
            print(f"  -> Released {conn} (available: {len(self.available)})")


print("\n1. Using connection pool:")
pool = ConnectionPool(max_size=3)

with pool.get_connection() as conn1:
    print(f"    Using {conn1}")

with pool.get_connection() as conn2:
    print(f"    Using {conn2}")

print(f"Available connections: {len(pool.available)}")


print("\n" + "=" * 60)
print("SECTION 7: Timing Decorator as Context Manager")
print("=" * 60)

import time

@contextmanager
def elapsed_time(description: str = "Operation"):
    """Measure and log elapsed time."""
    start = time.time()
    print(f"  -> {description} started")
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"  -> {description} took {elapsed:.3f} seconds")


print("\n1. Timing various operations:")
with elapsed_time("Quick operation"):
    time.sleep(0.1)

with elapsed_time("Slow operation"):
    time.sleep(0.3)


print("\n" + "=" * 60)
print("KEY POINTS")
print("=" * 60)
print("""
1. Context managers are perfect for:
   - Resource cleanup (files, connections, locks)
   - Atomic transactions (commit/rollback)
   - Logging and timing
   - State management (config overrides)

2. Common patterns:
   - Database transactions
   - File pair operations
   - Thread synchronization
   - Connection pools
   - Temporary directories

3. Benefits:
   - Guaranteed cleanup
   - Exception-safe
   - Readable code
   - Less boilerplate

4. Built-in examples:
   - open() for files
   - Lock() for threads
   - TemporaryDirectory()
   - suppress() for errors

5. Custom context managers:
   - Use @contextmanager for simple cases
   - Use class-based for complex logic
   - Both guarantee __exit__ is called
""")

# Cleanup
for f in ["input.txt", "output.txt"]:
    if os.path.exists(f):
        os.remove(f)
print("\nTest files cleaned up.")
