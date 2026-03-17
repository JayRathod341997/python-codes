# Topic 02: Context Managers and the `with` Statement

## Overview

Master resource management with automatic cleanup using context managers.

## Quick Start

```bash
python 01_with_statement_basics.py
python 02_class_based_cm.py
python 03_contextlib_module.py
python 04_real_world_examples.py
python exercises/solutions/solution_01.py
```

## Files

| File | Lines | What You'll Learn |
|------|-------|-------------------|
| notes.md | 350+ | Theory, patterns, best practices |
| interview.md | 300+ | 12 Q&A |
| 01_with_statement_basics.py | 150 | Why with is better |
| 02_class_based_cm.py | 280 | __enter__ and __exit__ |
| 03_contextlib_module.py | 260 | @contextmanager decorator |
| 04_real_world_examples.py | 300+ | DB, files, locks, pools |
| exercises/solution_01.py | 100+ | File logger |

## Learning Path

1. **Read notes.md** (20 min)
2. **Run 01_with_statement_basics.py** (10 min)
3. **Run 02_class_based_cm.py** (10 min)
4. **Run 03_contextlib_module.py** (10 min)
5. **Run 04_real_world_examples.py** (10 min)
6. **Review interview.md** (10 min)
7. **Solve exercises** (20 min)

## Key Concepts

### with Statement
```python
with open("file.txt") as f:
    data = f.read()
# File closes automatically
```

### Class-Based
```python
class MyContext:
    def __enter__(self):
        return resource
    def __exit__(self, exc_type, exc_val, exc_tb):
        cleanup()
```

### Decorator-Based
```python
@contextmanager
def my_context():
    setup()
    try:
        yield resource
    finally:
        cleanup()
```

### suppress() - Ignore Exceptions
```python
from contextlib import suppress
with suppress(FileNotFoundError):
    os.remove(file)
```

### ExitStack - Multiple Resources
```python
from contextlib import ExitStack
with ExitStack() as stack:
    f1 = stack.enter_context(open("a"))
    f2 = stack.enter_context(open("b"))
```

## Real-World Examples

### Database Transactions
```python
with db.transaction():
    db.insert(user)
    db.update(account)
# Auto commit/rollback
```

### File Operations
```python
with open("input") as inp, open("output", "w") as out:
    for line in inp:
        out.write(line.upper())
```

### Timing
```python
@contextmanager
def timer(name):
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"{name}: {elapsed:.3f}s")
```

### Thread Locks
```python
with lock:
    shared_resource += 1
```

## Exercises

### Exercise 01: File Logger
Create a FileLogger context manager that:
- Opens log file automatically
- Writes timestamped messages
- Closes file on exit
- Handles exceptions gracefully

**Files:**
- exercises/exercise_01.py (template)
- exercises/solutions/solution_01.py (solution)

## Pattern Comparison

| Pattern | When to Use |
|---------|------------|
| `with` | All resource management |
| Class-based | Complex logic, multiple methods |
| @contextmanager | Simple setup/cleanup |
| suppress() | Ignore optional errors |
| ExitStack | Multiple resources |

## Common Use Cases

1. **Files** - open(), read, close
2. **Databases** - connection, transaction, close
3. **Locks** - acquire, use, release
4. **Timing** - start, measure, report
5. **Temporary resources** - create, use, delete
6. **Logging** - start scope, log, end scope

## Key Takeaways

1. Always use `with` for resource management
2. `__enter__` = setup, `__exit__` = cleanup
3. Exceptions are passed to `__exit__`
4. Return False to propagate exception
5. Use @contextmanager for simple cases
6. ExitStack for dynamic resource management
7. Cleanup is guaranteed (even on error)

## Interview Questions

See interview.md for Q1-Q12:
- What is a context manager?
- Explain __enter__ and __exit__
- Decorator vs class-based
- Exception handling in __exit__
- Multiple context managers

## Performance Tip

Context managers have negligible overhead. Use them everywhere for safety without concern for performance.

## Next Topic

→ [03_async_await](../03_async_await/README.md)

---

**Estimated Time:** 1.5-2 hours

**Prerequisites:** Type hints (Topic 01) helpful but not required

**Difficulty:** Beginner-Intermediate
