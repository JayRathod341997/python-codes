# Async/Await and Asynchronous Programming in Python

## What is it?

Async/await is Python's syntax for writing asynchronous code that allows concurrent execution of I/O-bound tasks without using threads or multiprocessing. Instead of blocking while waiting for network requests, file operations, or database queries to complete, async code can yield control back to the event loop to handle other tasks.

```python
import asyncio

async def fetch_data():
    await asyncio.sleep(1)  # Simulate I/O wait
    return "data"

result = asyncio.run(fetch_data())
```

---

## Why Use Async/Await?

| Benefit | Example |
|---------|---------|
| **Handle many I/O operations concurrently** | Fetch 1000 URLs in seconds instead of minutes |
| **Single-threaded scalability** | No GIL limitations, one thread handles multiple operations |
| **Cleaner code than callbacks** | Reads like synchronous code but executes asynchronously |
| **Reduced resource overhead** | No thread creation/context switching overhead |
| **Better for web servers** | Handle thousands of concurrent requests efficiently |

---

## Core Concepts

### 1. Understanding Coroutines

A coroutine is a function defined with `async def`. It doesn't execute immediately when called—instead, it returns a coroutine object.

```python
async def greet(name: str) -> str:
    """A coroutine that returns a greeting."""
    return f"Hello, {name}!"

# Calling a coroutine doesn't execute it
coro = greet("Alice")
print(type(coro))  # <class 'coroutine'>

# You must await it or run it with asyncio.run()
result = asyncio.run(coro)  # Runs the coroutine
print(result)  # "Hello, Alice!"
```

**Key points:**
- Functions with `async def` are coroutines
- Calling them returns a coroutine object, not the result
- Must use `await` or `asyncio.run()` to execute
- A coroutine must be awaited before it completes

### 2. The Await Keyword

`await` suspends the current coroutine and allows the event loop to run other tasks. It can only be used inside an `async def` function.

```python
async def example():
    # await pauses execution until the awaited coroutine completes
    result = await some_async_function()
    print(result)

# Attempting to await outside async function raises SyntaxError
# result = await example()  # ✗ SyntaxError: 'await' outside async function
```

### 3. Running Coroutines: asyncio.run()

`asyncio.run()` creates an event loop, runs the coroutine, and closes the loop. Use this as your main entry point.

```python
import asyncio

async def main():
    print("Start")
    await asyncio.sleep(1)
    print("End")

# Best practice: use asyncio.run() in __main__
if __name__ == "__main__":
    asyncio.run(main())
```

### 4. Creating Tasks

Tasks wrap coroutines and schedule them to run on the event loop. Unlike directly awaiting, creating a task allows multiple coroutines to run concurrently.

```python
import asyncio

async def fetch(url: str) -> str:
    await asyncio.sleep(1)  # Simulate network request
    return f"Data from {url}"

async def main():
    # Direct await: runs one at a time (3 seconds total)
    # result1 = await fetch("url1")
    # result2 = await fetch("url2")
    # result3 = await fetch("url3")

    # Using tasks: runs concurrently (1 second total)
    task1 = asyncio.create_task(fetch("url1"))
    task2 = asyncio.create_task(fetch("url2"))
    task3 = asyncio.create_task(fetch("url3"))

    results = await asyncio.gather(task1, task2, task3)
    print(results)

asyncio.run(main())
```

### 5. Common Async Utilities

#### asyncio.gather() — Run multiple coroutines concurrently

```python
async def main():
    # gather() creates tasks and waits for all to complete
    results = await asyncio.gather(
        fetch("url1"),
        fetch("url2"),
        fetch("url3"),
        return_exceptions=True  # Don't stop on first exception
    )
    return results

asyncio.run(main())
```

#### asyncio.wait() — More control over task completion

```python
import asyncio

async def main():
    tasks = [fetch("url1"), fetch("url2"), fetch("url3")]

    # Wait for first task to complete
    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_COMPLETED
    )

    # Cancel remaining tasks
    for task in pending:
        task.cancel()

asyncio.run(main())
```

#### asyncio.sleep() — Async equivalent of time.sleep()

```python
import asyncio
import time

async def example():
    start = time.time()

    # This does NOT block the event loop
    await asyncio.sleep(2)

    elapsed = time.time() - start
    print(f"Elapsed: {elapsed:.1f}s")

asyncio.run(example())
```

### 6. Exception Handling in Async Code

```python
import asyncio

async def failing_task():
    await asyncio.sleep(0.5)
    raise ValueError("Task failed!")

async def main():
    try:
        await asyncio.gather(
            failing_task(),
            return_exceptions=False  # Raise on first exception
        )
    except ValueError as e:
        print(f"Caught error: {e}")

asyncio.run(main())
```

### 7. Async Context Managers

Async context managers allow resource management in async code using `async with`.

```python
import asyncio

class AsyncConnection:
    async def __aenter__(self):
        print("Connecting...")
        await asyncio.sleep(0.5)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("Closing...")
        await asyncio.sleep(0.5)

async def main():
    async with AsyncConnection() as conn:
        print("Using connection")

asyncio.run(main())
```

### 8. Async Iterators and Generators

```python
async def async_range(n: int):
    """Async generator that yields values over time."""
    for i in range(n):
        await asyncio.sleep(0.5)
        yield i

async def main():
    async for value in async_range(3):
        print(value)

asyncio.run(main())
```

### 9. Running Blocking Code in Async Functions

For blocking operations (CPU-intensive or using synchronous libraries), use `loop.run_in_executor()`:

```python
import asyncio
import time

def blocking_operation(n: int) -> int:
    """Simulates a blocking CPU-intensive task."""
    time.sleep(1)
    return n * 2

async def main():
    loop = asyncio.get_event_loop()

    # Run blocking operation in thread pool
    result = await loop.run_in_executor(None, blocking_operation, 5)
    print(f"Result: {result}")

asyncio.run(main())
```

### 10. Task Cancellation

```python
import asyncio

async def long_task():
    try:
        for i in range(10):
            print(f"Working... {i}")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Task was cancelled!")
        raise  # Must re-raise

async def main():
    task = asyncio.create_task(long_task())

    await asyncio.sleep(2.5)
    task.cancel()  # Cancel the task

    try:
        await task
    except asyncio.CancelledError:
        print("Caught CancelledError in main")

asyncio.run(main())
```

---

## Real-World Examples

### Example 1: Fetching Multiple APIs Concurrently

```python
import asyncio
import httpx

async def fetch_user(client: httpx.AsyncClient, user_id: int) -> dict:
    """Fetch user data from API."""
    response = await client.get(f"https://api.example.com/users/{user_id}")
    return response.json()

async def main():
    async with httpx.AsyncClient() as client:
        # Fetch 100 users concurrently instead of sequentially
        tasks = [fetch_user(client, i) for i in range(1, 101)]
        users = await asyncio.gather(*tasks)
        return users

results = asyncio.run(main())
```

### Example 2: Async Queue for Task Processing

```python
import asyncio
from asyncio import Queue

async def producer(queue: Queue):
    """Add items to queue."""
    for i in range(5):
        await queue.put(f"item_{i}")
        print(f"Produced: item_{i}")
        await asyncio.sleep(0.5)

    # Signal completion
    await queue.put(None)

async def consumer(queue: Queue, worker_id: int):
    """Process items from queue."""
    while True:
        item = await queue.get()
        if item is None:
            break

        print(f"Worker {worker_id} processing: {item}")
        await asyncio.sleep(1)
        queue.task_done()

async def main():
    queue = Queue()

    await asyncio.gather(
        producer(queue),
        consumer(queue, 1),
        consumer(queue, 2),
    )

asyncio.run(main())
```

### Example 3: Timeout Handling

```python
import asyncio

async def slow_operation():
    await asyncio.sleep(5)
    return "done"

async def main():
    try:
        result = await asyncio.wait_for(
            slow_operation(),
            timeout=2.0  # Timeout after 2 seconds
        )
    except asyncio.TimeoutError:
        print("Operation timed out!")

asyncio.run(main())
```

---

## Common Pitfalls

### Pitfall 1: Forgetting to await a coroutine

```python
async def get_data():
    return "data"

async def main():
    # Wrong: coro object is created but never executed
    result = get_data()  # ✗ This is just a coroutine object
    print(result)  # <coroutine object get_data at 0x...>

    # Right: await executes the coroutine
    result = await get_data()  # OK
    print(result)  # "data"

asyncio.run(main())
```

### Pitfall 2: Blocking the event loop

```python
import asyncio
import time

async def main():
    # Wrong: time.sleep() blocks the entire event loop
    time.sleep(5)  # ✗ Blocks everything for 5 seconds

    # Right: use asyncio.sleep()
    await asyncio.sleep(5)  # OK - Other tasks can run

asyncio.run(main())
```

### Pitfall 3: Mixing sync and async without care

```python
import asyncio

def sync_function():
    return "sync"

async def main():
    # Wrong: Can't await a sync function
    # result = await sync_function()  # ✗ TypeError

    # Right: Call sync function directly (no await)
    result = sync_function()  # OK
    return result

asyncio.run(main())
```

### Pitfall 4: Running async code at module level

```python
import asyncio

async def get_config():
    await asyncio.sleep(1)
    return {"setting": "value"}

# Wrong: This will never work
# config = await get_config()  # ✗ SyntaxError: await outside async

# Right: Use asyncio.run() in main or __main__
if __name__ == "__main__":
    config = asyncio.run(get_config())
```

### Pitfall 5: Not handling CancelledError properly

```python
import asyncio

async def task():
    try:
        while True:
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Cancelled!")
        # Wrong: Don't silently swallow the error
        # return  # ✗ Silently ignores cancellation

        # Right: Re-raise the error
        raise  # OK - Properly propagates cancellation
```

---

## Best Practices

1. **Use asyncio.run() as your main entry point**
   ```python
   if __name__ == "__main__":
       asyncio.run(main())
   ```

2. **Use asyncio.gather() for concurrent execution**
   ```python
   results = await asyncio.gather(task1, task2, task3)
   ```

3. **Always use await with coroutines**
   ```python
   result = await some_async_function()
   ```

4. **Use async context managers for resource management**
   ```python
   async with resource:
       # Use resource
   ```

5. **Handle exceptions in concurrent code**
   ```python
   results = await asyncio.gather(*tasks, return_exceptions=True)
   ```

6. **Avoid blocking operations; use run_in_executor() if needed**
   ```python
   result = await loop.run_in_executor(None, blocking_func, arg)
   ```

7. **Use structured concurrency patterns**
   ```python
   async with asyncio.TaskGroup() as tg:  # Python 3.11+
       await tg.create_task(task1())
       await tg.create_task(task2())
   ```

8. **Set timeouts on I/O operations**
   ```python
   await asyncio.wait_for(operation(), timeout=5.0)
   ```

9. **Use async libraries for I/O (httpx, aiohttp, asyncpg)**
   ```python
   async with httpx.AsyncClient() as client:
       response = await client.get(url)
   ```

10. **Test async code with pytest-asyncio**
    ```python
    @pytest.mark.asyncio
    async def test_async_function():
        result = await my_async_func()
        assert result == expected
    ```

---

## Performance Considerations

### Single-threaded concurrency

Async/await achieves concurrency through a single event loop. This means:
- Only one coroutine runs at a time
- Control switches when `await` is reached
- Ideal for I/O-bound work (network, files, databases)
- Not suitable for CPU-bound work (use multiprocessing instead)

### Event loop switching cost

The event loop overhead is negligible compared to I/O wait times:

```python
import asyncio
import time

async def io_task():
    # I/O wait: ~1 second (event loop can run other tasks)
    await asyncio.sleep(1)

async def main():
    start = time.time()

    # 100 tasks all sleeping simultaneously
    await asyncio.gather(*[io_task() for _ in range(100)])

    elapsed = time.time() - start
    print(f"Time: {elapsed:.2f}s")  # ~1 second, not 100!

asyncio.run(main())
```

### Memory vs Threading

Async uses less memory than threading:
- One coroutine ~1KB
- One thread ~8MB
- One process ~30MB+

You can easily handle 100,000 concurrent coroutines; threads would exhaust memory.

---

## When to Use Async

Use async/await for:
- **Web servers** handling many concurrent requests
- **API clients** making many parallel HTTP requests
- **WebSocket servers** with concurrent connections
- **Database applications** with connection pooling
- **File I/O** operations on many files
- **Any I/O-bound work** where speed matters

Don't use async for:
- **CPU-bound work** (use multiprocessing)
- **Simple scripts** with minimal I/O
- **When thread/process overhead isn't a concern**

---

## Summary

Async/await enables efficient concurrent I/O handling:
- Define coroutines with `async def`
- Use `await` to pause execution
- Use `asyncio.run()` to execute
- Create tasks with `asyncio.create_task()` for concurrency
- Use `asyncio.gather()` to wait for multiple tasks
- Leverage async libraries like httpx for I/O
- Avoid blocking the event loop
- Handle exceptions with try/except
- Test with pytest-asyncio

Master async/await and you'll write highly scalable I/O-bound applications.
