# Topic 03: Async/Await and Asynchronous Programming

## Overview

Build high-performance concurrent applications with async/await.

## Quick Start

```bash
python 01_coroutines_basics.py
python 02_tasks_and_concurrency.py
python 03_async_context_managers.py
python 04_real_world_httpx.py
python exercises/solutions/solution_01.py
```

## Files

| File | Lines | What You'll Learn |
|------|-------|-------------------|
| notes.md | 400+ | Theory, patterns, pitfalls |
| interview.md | 300+ | 12 Q&A |
| 01_coroutines_basics.py | 200+ | async def, await, asyncio.run() |
| 02_tasks_and_concurrency.py | 250+ | gather(), create_task() |
| 03_async_context_managers.py | 200+ | async with, async for |
| 04_real_world_httpx.py | 200+ | HTTP with httpx |
| exercises/solution_01.py | 200+ | Web scraper |
| exercises/solution_02.py | 200+ | Concurrent API caller |

## Learning Path

1. **Read notes.md** (30 min) - Understand event loop
2. **Run 01_coroutines_basics.py** (10 min)
3. **Run 02_tasks_and_concurrency.py** (10 min)
4. **Run 03_async_context_managers.py** (10 min)
5. **Run 04_real_world_httpx.py** (10 min)
6. **Review interview.md** (10 min)
7. **Solve exercises** (30 min)

## Key Concepts

### Coroutines
```python
async def fetch():
    await asyncio.sleep(1)
    return "data"

asyncio.run(fetch())
```

### Concurrent Tasks
```python
async def main():
    await asyncio.gather(
        task1(),
        task2(),
        task3()
    )
```

### Creating Tasks
```python
task = asyncio.create_task(slow_operation())
result = await task
```

### Timeout Protection
```python
try:
    await asyncio.wait_for(slow_task(), timeout=5)
except asyncio.TimeoutError:
    print("Too slow!")
```

### Async Context Manager
```python
async with AsyncResource() as res:
    await res.process()
```

### Async Iteration
```python
async for item in async_generator():
    print(item)
```

## Real-World Example

### Concurrent HTTP Requests
```python
import httpx
import asyncio

async def fetch_url(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

async def main():
    urls = ["url1", "url2", "url3"]
    results = await asyncio.gather(*[fetch_url(url) for url in urls])
    return results

asyncio.run(main())
```

### Database Queries
```python
async def get_users():
    async with db.connection() as conn:
        users = await conn.query("SELECT * FROM users")
        return users
```

## Performance Benefits

| Scenario | Sequential | Concurrent |
|----------|-----------|-----------|
| 10 API calls (1s each) | 10 seconds | 1 second |
| 100 DB queries (10ms each) | 1 second | ~10ms |
| 1000 file reads (5ms each) | 5 seconds | ~5ms |

## Exercises

### Exercise 01: Web Scraper
Create async web scraper that:
- Fetches multiple URLs concurrently
- Extracts data from responses
- Handles errors gracefully
- Returns results in order

### Exercise 02: Rate-Limited API Client
Create async client that:
- Makes multiple API requests
- Respects rate limits
- Retries on failure
- Times out after 30s

## Common Patterns

| Pattern | Use |
|---------|-----|
| `async def func()` | Define async function |
| `await func()` | Wait for async result |
| `asyncio.gather()` | Run many in parallel |
| `asyncio.create_task()` | Background task |
| `asyncio.wait_for()` | Add timeout |
| `async with` | Resource management |
| `async for` | Async iteration |

## Testing Async Code

```bash
# Install pytest-asyncio
pip install pytest-asyncio

# Test async function
@pytest.mark.asyncio
async def test_async():
    result = await async_function()
    assert result == expected
```

### Test Example
```python
@pytest.mark.asyncio
async def test_fetch():
    data = await fetch_data()
    assert data is not None
```

## Key Takeaways

1. Use `async def` to define coroutines
2. Use `await` to wait for results
3. Use `asyncio.gather()` for parallel execution
4. Add timeouts with `asyncio.wait_for()`
5. Use async libraries (httpx, aiofiles, etc)
6. Never use time.sleep() in async code
7. Test with pytest-asyncio

## Common Pitfalls

1. **Forgetting await** - task created but doesn't run
2. **Blocking the loop** - time.sleep() blocks everything
3. **Missing timeouts** - request hangs forever
4. **Not handling exceptions** - use return_exceptions=True
5. **Mixing sync/async** - can't call async from sync

## Interview Questions

See interview.md for Q1-Q12:
- What is a coroutine?
- Explain await
- gather() vs create_task()
- Timeout handling
- Exception handling

## Performance Tips

1. Use httpx for async HTTP (not requests)
2. Use aiofiles for async file I/O
3. Use asyncpg for async PostgreSQL
4. Batch operations when possible
5. Add connection pooling
6. Use appropriate timeouts

## Next Topic

→ [04_data_validation_pydantic](../04_data_validation_pydantic/README.md)

---

**Estimated Time:** 2-3 hours

**Prerequisites:** Context managers (Topic 02) helpful

**Difficulty:** Intermediate-Advanced

**Required Packages:** httpx, pytest-asyncio
