# Interview Q&A — Async/Await and Asynchronous Programming

## Q1. What's the difference between asyncio.run() and loop.run_until_complete()?

**A:** `asyncio.run()` (Python 3.7+) creates a fresh event loop, runs the coroutine, and closes the loop. It's simpler and preferred for main entry points. `loop.run_until_complete()` requires manually creating and managing the event loop. `asyncio.run()` is the modern approach.

```python
# asyncio.run() — Modern, preferred
asyncio.run(main())

# loop.run_until_complete() — Legacy, more control
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

---

## Q2. If I call an async function without await, what happens?

**A:** It returns a coroutine object that does nothing. The function body never executes. This is a common bug:

```python
async def fetch():
    return "data"

# Wrong: Creates coroutine but doesn't run it
coro = fetch()  # No execution, just a coroutine object
print(coro)  # <coroutine object fetch at 0x...>

# Right: await executes it
result = await fetch()
```

---

## Q3. Can I use threads and async together?

**A:** Yes, but carefully. Use `asyncio.to_thread()` (Python 3.9+) or `loop.run_in_executor()` to run blocking code in a thread pool without blocking the event loop:

```python
import asyncio

def blocking_io():
    import time
    time.sleep(1)  # Blocks, but in a separate thread
    return "done"

async def main():
    # Doesn't block event loop
    result = await asyncio.to_thread(blocking_io)
    return result

asyncio.run(main())
```

---

## Q4. What happens if an async task raises an exception and isn't awaited?

**A:** The exception is stored in the task. If you never await it, you get a warning at garbage collection, but the exception is lost. Always await tasks or handle exceptions:

```python
import asyncio

async def failing_task():
    raise ValueError("Failed!")

async def main():
    # Wrong: Exception lost, warning printed
    task = asyncio.create_task(failing_task())
    # (never await task)

    # Right: Exception is raised
    task = asyncio.create_task(failing_task())
    try:
        await task
    except ValueError:
        print("Caught!")

asyncio.run(main())
```

---

## Q5. How is asyncio different from threading?

**A:** Key differences:

| Feature | Asyncio | Threading |
|---------|---------|-----------|
| **Concurrency model** | Single-threaded, cooperative | Multi-threaded, preemptive |
| **Context switching** | Manual (at await) | Automatic (OS scheduler) |
| **GIL impact** | Not affected | Blocked by GIL |
| **Memory per task** | ~1KB | ~8MB |
| **Scalability** | 100,000s of tasks | Hundreds of threads |
| **Suitable for** | I/O-bound | I/O or CPU-bound |

Async is better for I/O-heavy services; threading for mixed workloads.

---

## Q6. What's asyncio.gather() vs asyncio.wait()?

**A:** `gather()` is simpler and returns results directly. `wait()` is more flexible and returns done/pending sets:

```python
import asyncio

async def task(n):
    await asyncio.sleep(n)
    return n

async def main():
    # gather: Simple, returns list of results
    results = await asyncio.gather(task(1), task(2), task(3))
    print(results)  # [1, 2, 3]

    # wait: More control, returns (done, pending) sets
    done, pending = await asyncio.wait(
        {task(1), task(2), task(3)},
        return_when=asyncio.FIRST_COMPLETED
    )
    print(f"Done: {len(done)}, Pending: {len(pending)}")

asyncio.run(main())
```

Use `gather()` for simple cases; `wait()` when you need FIRST_COMPLETED or other strategies.

---

## Q7. Can I run sync code in an async function?

**A:** Yes, sync code runs fine in async functions. However, blocking operations freeze the event loop:

```python
import asyncio
import time

async def main():
    # Sync code runs fine (and blocks)
    result = "hello".upper()

    # Blocking I/O freezes event loop
    time.sleep(1)  # ✗ Blocks event loop (bad)
    await asyncio.sleep(1)  # OK - Doesn't block

asyncio.run(main())
```

If you must call blocking code, use `run_in_executor()`.

---

## Q8. What's the difference between async for and regular for?

**A:** `async for` works with async iterators that yield values asynchronously. Regular `for` works with regular iterables:

```python
import asyncio

async def async_range(n):
    """Async generator."""
    for i in range(n):
        await asyncio.sleep(0.5)
        yield i

async def main():
    # Regular for with sync iterator
    for i in range(3):
        print(i)  # Runs synchronously, fast

    # Async for with async iterator
    async for i in async_range(3):
        print(i)  # Waits at each iteration

asyncio.run(main())
```

Use `async for` with async iterators; regular `for` for sync data.

---

## Q9. How do I timeout an async operation?

**A:** Use `asyncio.wait_for()` with a timeout parameter:

```python
import asyncio

async def slow_api_call():
    await asyncio.sleep(10)
    return "data"

async def main():
    try:
        result = await asyncio.wait_for(
            slow_api_call(),
            timeout=2.0  # Timeout after 2 seconds
        )
    except asyncio.TimeoutError:
        print("API call timed out!")
        return None

asyncio.run(main())
```

The task is cancelled if it exceeds the timeout.

---

## Q10. What's an async context manager, and why use it?

**A:** An async context manager (implements `__aenter__` and `__aexit__`) manages resources asynchronously. Used for connections that require async setup/cleanup:

```python
import asyncio

class AsyncDB:
    async def __aenter__(self):
        await asyncio.sleep(0.5)  # Connect asynchronously
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await asyncio.sleep(0.5)  # Disconnect asynchronously

    async def query(self, sql):
        await asyncio.sleep(0.1)
        return f"Result of: {sql}"

async def main():
    async with AsyncDB() as db:
        result = await db.query("SELECT * FROM users")
        print(result)

asyncio.run(main())
```

Use when resource setup/cleanup requires I/O operations.

---

## Q11. How do I cancel an async task?

**A:** Call `task.cancel()` to request cancellation. The task raises `asyncio.CancelledError`. You must catch and re-raise it for proper cleanup:

```python
import asyncio

async def long_task():
    try:
        while True:
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Cleaning up...")
        raise  # Must re-raise to signal cancellation

async def main():
    task = asyncio.create_task(long_task())
    await asyncio.sleep(2.5)
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Task cancelled")

asyncio.run(main())
```

---

## Q12. Should I use asyncio for CPU-bound work?

**A:** No. Asyncio provides concurrency through cooperative multitasking, not parallelism. For CPU-bound work (CPU-intensive calculations), use multiprocessing. Asyncio is for I/O-bound work (network, files, databases).

```python
import asyncio
import time
from multiprocessing import Pool

# CPU-bound: Use multiprocessing
def cpu_task(n):
    total = 0
    for i in range(n):
        total += i
    return total

# I/O-bound: Use asyncio
async def io_task():
    await asyncio.sleep(1)
    return "data"

# For CPU-bound, multiprocessing is better
if __name__ == "__main__":
    with Pool(4) as pool:
        results = pool.map(cpu_task, [10000000] * 4)
```

Use asyncio for I/O; multiprocessing for CPU.
