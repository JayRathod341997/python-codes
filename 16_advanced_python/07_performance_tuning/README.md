# Topic 07: Performance Tuning

## Overview

Identify bottlenecks and optimize code for speed and memory efficiency.

## Quick Start

```bash
# Install profiling tools
pip install line_profiler memory_profiler

# Read theory
cat notes.md
cat interview.md
```

## Key Concepts

### CPU Profiling

```bash
# cProfile
python -m cProfile -s cumulative script.py

# Or in code
import cProfile
cProfile.run('my_function()')
```

### Memory Profiling

```bash
# tracemalloc (built-in)
import tracemalloc
tracemalloc.start()
my_function()
tracemalloc.print_stats()

# Or use memory_profiler
pip install memory_profiler
python -m memory_profiler script.py
```

### Line Profiling

```bash
# line_profiler
pip install line_profiler
kernprof -l -v script.py
```

## Optimization Techniques

### 1. Use Local Variables

```python
# SLOW - repeated lookups
for i in range(1000):
    obj.expensive_attr += i

# FAST - cache in local var
cache = obj.expensive_attr
for i in range(1000):
    cache += i
obj.expensive_attr = cache
```

### 2. Generators vs Lists

```python
# SLOW - creates list in memory
def slow():
    return [i*i for i in range(1000000)]

# FAST - lazy evaluation
def fast():
    return (i*i for i in range(1000000))
```

### 3. Caching

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### 4. __slots__ for Memory

```python
class Point:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Uses much less memory than regular class
```

### 5. Built-in Functions

```python
# SLOW - loops in Python
sum_val = 0
for i in range(1000):
    sum_val += i

# FAST - built-in is optimized
sum_val = sum(range(1000))
```

### 6. String Operations

```python
# SLOW - creates new string each iteration
s = ""
for item in items:
    s += str(item)

# FAST - join is optimized
s = "".join(str(item) for item in items)
```

## Profiling Example

```python
import cProfile
import pstats

def slow_function():
    result = []
    for i in range(10000):
        result.append(i * i)
    return sum(result)

# Profile it
profiler = cProfile.Profile()
profiler.enable()

slow_function()

profiler.disable()
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats()
```

## Async for I/O

```python
# SLOW - sequential requests (30 seconds)
for url in urls:
    response = requests.get(url)
    process(response)

# FAST - concurrent requests (3 seconds)
import asyncio
import httpx

async def fetch_all(urls):
    async with httpx.AsyncClient() as client:
        return await asyncio.gather(*[
            client.get(url) for url in urls
        ])
```

## Database Optimization

```python
# SLOW - N+1 queries
for user in users:
    print(user.posts)  # One query per user!

# FAST - Join query
users_with_posts = User.query.join(Post).all()
```

## Key Metrics

| Metric | Target | Tool |
|--------|--------|------|
| CPU Time | Lowest | cProfile |
| Memory | Lowest | tracemalloc |
| Startup | < 1s | cProfile |
| Response | < 200ms | asyncio |
| Throughput | > 1000 req/s | load test |

## Profiling Workflow

1. **Profile** - Where is time spent?
2. **Identify** - What's the bottleneck?
3. **Optimize** - Make fastest part faster?
4. **Measure** - Did it improve?
5. **Repeat** - Find next bottleneck

## Common Bottlenecks

| Issue | Solution |
|-------|----------|
| Nested loops | Reduce complexity |
| List operations | Use set or dict |
| String concatenation | Use join() |
| Database queries | Add indexes |
| Network calls | Use async |
| Memory leaks | Profile memory |
| Repeated imports | Import once |

## Best Practices

1. **Profile first** - Don't guess
2. **Measure improvements** - Prove it works
3. **Optimize hot paths** - Focus on frequent code
4. **Cache aggressively** - Avoid recomputation
5. **Use async for I/O** - Don't block
6. **Choose data structures** - dict vs list vs set
7. **Batch operations** - Reduce calls
8. **Monitor production** - Real data matters

## Interview Questions

See interview.md for Q1-Q12:
- Profiling tools
- Optimization techniques
- Memory management
- Database optimization
- Async benefits

## Performance Tools

```bash
# Install all tools
pip install \
  line_profiler \
  memory_profiler \
  py_spy \
  scalene
```

## Quick Wins

1. Use `set()` for membership
2. Use dict instead of list lookup
3. Use generators for large data
4. Cache expensive operations
5. Use async for I/O
6. Pre-compile regex
7. Use __slots__ for many objects
8. Batch database operations

## Premature Optimization

DON'T:
- Optimize before profiling
- Optimize readable code into unreadable
- Optimize 1% of code
- Ignore algorithm complexity
- Sacrifice clarity for speed

DO:
- Profile real workloads
- Fix algorithmic issues first
- Measure improvements
- Keep code maintainable
- Test performance changes

## Next Topic

→ [08_dependency_injection](../08_dependency_injection/README.md)

---

**Estimated Time:** 2-3 hours

**Prerequisites:** All previous topics

**Difficulty:** Intermediate-Advanced

**Tools:** cProfile, tracemalloc, line_profiler
