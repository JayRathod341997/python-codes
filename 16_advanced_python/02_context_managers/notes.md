# Context Managers and the `with` Statement

## What is it?

A context manager is a Python object that defines what happens when you enter and exit a `with` block. It's a way to properly manage resources (files, database connections, locks, etc.) and ensure cleanup happens automatically.

```python
with open("file.txt") as f:
    data = f.read()
# File is automatically closed here
```

---

## Why Use Context Managers?

| Benefit | Example |
|---------|---------|
| **Automatic cleanup** | Files close, connections close, locks release automatically |
| **Error handling** | Cleanup happens even if an exception occurs |
| **Readable code** | Clear entry/exit points without try-finally boilerplate |
| **Resource safety** | Prevents resource leaks and dangling connections |

---

## Core Concepts

### 1. The `with` Statement Basics

```python
# Without context manager (error-prone)
f = open("data.txt")
try:
    data = f.read()
finally:
    f.close()

# With context manager (clean and safe)
with open("data.txt") as f:
    data = f.read()
# File closes automatically
```

### 2. Context Manager Protocol

A context manager must implement two methods:

```python
class MyContextManager:
    def __enter__(self):
        """Called when entering the with block."""
        print("Entering...")
        return self  # or any resource

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting the with block."""
        print("Exiting...")
        return False  # Don't suppress exceptions
```

### 3. Class-Based Context Managers

```python
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        print(f"Opening connection to {self.db_name}")
        self.connection = f"Connected to {self.db_name}"
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection to {self.db_name}")
        self.connection = None
        # Return True to suppress exceptions, False to propagate
        return False

# Usage
with DatabaseConnection("mydb") as conn:
    print(f"Using: {conn}")
    # Connection is closed automatically after
```

### 4. The `@contextmanager` Decorator

Simpler way to create context managers:

```python
from contextlib import contextmanager

@contextmanager
def database_connection(db_name):
    print(f"Opening {db_name}")
    connection = f"Connected to {db_name}"
    try:
        yield connection
    finally:
        print(f"Closing {db_name}")

# Usage
with database_connection("mydb") as conn:
    print(f"Using: {conn}")
```

**Key parts:**
- Code before `yield` = `__enter__` logic
- `yield` = what gets returned to the `with` block
- Code after `yield` = `__exit__` logic

### 5. Exception Handling in Context Managers

```python
class SafeFile:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

        # Return True to suppress the exception
        if exc_type is ValueError:
            print(f"Caught ValueError: {exc_val}")
            return True  # Exception is suppressed

        # Return False (or don't return) to propagate
        return False

# Usage
try:
    with SafeFile("data.txt") as f:
        data = f.read()
        if not data:
            raise ValueError("File is empty")
except ValueError as e:
    print(f"Exception propagated: {e}")
```

### 6. Real-World Examples

#### Timer Context Manager

```python
import time
from contextlib import contextmanager

@contextmanager
def timer(name):
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"{name} took {elapsed:.3f} seconds")

# Usage
with timer("Database query"):
    time.sleep(1)
```

#### Temporary File Handling

```python
from contextlib import contextmanager
import os

@contextmanager
def temp_directory(path):
    os.makedirs(path, exist_ok=True)
    try:
        yield path
    finally:
        import shutil
        shutil.rmtree(path)

# Usage
with temp_directory("/tmp/myapp") as tmpdir:
    # Work with temporary directory
    pass
# Directory is automatically deleted
```

#### Lock Management

```python
from threading import Lock
from contextlib import contextmanager

class SafeCounter:
    def __init__(self):
        self.count = 0
        self.lock = Lock()

    @contextmanager
    def atomic_update(self):
        self.lock.acquire()
        try:
            yield
        finally:
            self.lock.release()

    def increment(self):
        with self.atomic_update():
            self.count += 1

counter = SafeCounter()
counter.increment()  # Lock is acquired and released automatically
```

### 7. Built-in Context Managers

Python provides many useful context managers:

```python
# File operations
with open("file.txt") as f:
    data = f.read()

# Temporary directory
from tempfile import TemporaryDirectory
with TemporaryDirectory() as tmpdir:
    # Use tmpdir
    pass

# Suppress specific exceptions
from contextlib import suppress
with suppress(FileNotFoundError):
    os.remove("optional_file.txt")

# Redirect stdout
from contextlib import redirect_stdout
import io
f = io.StringIO()
with redirect_stdout(f):
    print("This goes to f, not stdout")
output = f.getvalue()
```

### 8. Multiple Context Managers

```python
# Python 3.10+ (single line)
with open("input.txt") as inp, open("output.txt", "w") as out:
    for line in inp:
        out.write(line.upper())

# Python 3.9 and earlier
from contextlib import ExitStack
with ExitStack() as stack:
    inp = stack.enter_context(open("input.txt"))
    out = stack.enter_context(open("output.txt", "w"))
    for line in inp:
        out.write(line.upper())
```

### 9. ExitStack (Advanced)

Dynamically manage multiple contexts:

```python
from contextlib import ExitStack

def process_files(filenames):
    with ExitStack() as stack:
        # Open all files dynamically
        files = [stack.enter_context(open(fname)) for fname in filenames]
        # All files are available
        for f in files:
            print(f.read())
        # All close automatically
```

---

## Common Patterns

### Resource Acquisition Pattern

```python
class Resource:
    def __enter__(self):
        print("Acquiring resource")
        return self

    def __exit__(self, *args):
        print("Releasing resource")
```

### Connection Pattern

```python
class Connection:
    def __init__(self, host):
        self.host = host

    def __enter__(self):
        print(f"Connecting to {self.host}")
        return self

    def __exit__(self, *args):
        print(f"Disconnecting from {self.host}")
```

### Transaction Pattern

```python
@contextmanager
def transaction(db):
    db.begin()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
```

---

## Common Pitfalls

### 1. **Forgetting Exception Info in `__exit__`**
```python
# Wrong
def __exit__(self):
    self.cleanup()

# Correct
def __exit__(self, exc_type, exc_val, exc_tb):
    self.cleanup()
    return False
```

### 2. **Not Suppressing Exceptions Correctly**
```python
# Wrong - always returns True (suppresses everything)
def __exit__(self, *args):
    self.cleanup()
    return True

# Correct - suppress specific exceptions
def __exit__(self, exc_type, exc_val, exc_tb):
    self.cleanup()
    return exc_type is ValueError  # Only suppress ValueError
```

### 3. **Nested Exceptions**
```python
# If exception happens in __exit__, it overrides the original
def __exit__(self, exc_type, exc_val, exc_tb):
    # Be careful not to raise here unless necessary
    self.cleanup()  # If this raises, original exception is lost
```

---

## Best Practices

1. **Always define `__exit__` with three parameters** (even if you don't use them)
   ```python
   def __exit__(self, exc_type, exc_val, exc_tb):
       pass
   ```

2. **Use `@contextmanager` for simple cases** (less code than class-based)
   ```python
   @contextmanager
   def my_context():
       # setup
       yield resource
       # cleanup
   ```

3. **Use class-based for complex logic** (more readable than decorator)
   ```python
   class MyContext:
       def __enter__(self):
           pass
       def __exit__(self, *args):
           pass
   ```

4. **Don't suppress exceptions unless intentional**
   ```python
   return False  # Let exceptions propagate (default)
   ```

5. **Use `contextlib.suppress()` for optional errors**
   ```python
   from contextlib import suppress
   with suppress(FileNotFoundError):
       os.remove("optional.txt")
   ```

---

## Quick Reference

| Use Case | Tool |
|----------|------|
| File handling | `open()` (built-in) |
| Temporary directory | `tempfile.TemporaryDirectory()` |
| Suppress exceptions | `contextlib.suppress()` |
| Redirect output | `contextlib.redirect_stdout()` |
| Lock/acquire | `threading.Lock()`, `asyncio.Lock()` |
| Custom cleanup | `@contextmanager` or class with `__enter__`/`__exit__` |
| Multiple contexts | `ExitStack()` |

---

## Further Reading

- [PEP 343 — Context Managers](https://www.python.org/dev/peps/pep-0343/)
- [Python `contextlib` Module](https://docs.python.org/3/library/contextlib.html)
- [with Statement Best Practices](https://docs.python.org/3/reference/compound_stmts.html#with)
