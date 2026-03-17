# Performance Tuning: Profiling, Memory, and Optimization

## What is it?

Performance tuning is identifying bottlenecks and optimizing code for speed and memory efficiency using profiling tools and optimization techniques.

## Profiling Approaches

### 1. CPU Profiling with cProfile

```python
import cProfile

cProfile.run('my_function()')
```

Identify slow functions.

### 2. Memory Profiling

```python
from tracemalloc import trace_malloc

with trace_malloc():
    my_function()
```

Track memory allocation.

### 3. Line-Level Profiling

```bash
pip install line_profiler
kernprof -l -v script.py
```

See which lines are slow.

## Common Optimizations

### 1. Use Local Variables

```python
# Slower - repeated attribute lookups
def slow():
    for i in range(1000):
        obj.expensive_property += i

# Faster - cache in local variable
def fast():
    cache = obj.expensive_property
    for i in range(1000):
        cache += i
    obj.expensive_property = cache
```

### 2. Generators vs Lists

```python
# Bad - creates list in memory
def bad():
    return [i*i for i in range(1000000)]

# Good - lazy evaluation
def good():
    return (i*i for i in range(1000000))
```

### 3. Caching with functools

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_func(n):
    # computed only once per unique n
    return n * n
```

### 4. __slots__ for Memory Efficiency

```python
class Point:
    __slots__ = ['x', 'y']  # No __dict__
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Uses much less memory than regular class
```

### 5. Use Built-in Functions

```python
# Slower - loops in Python
sum_result = 0
for i in range(1000):
    sum_result += i

# Faster - built-in is optimized
sum_result = sum(range(1000))
```

### 6. Avoid Repeated Imports

```python
# Don't do this in loops
for i in range(1000):
    from module import func  # Import every iteration!

# Do this once
from module import func
for i in range(1000):
    func()
```

### 7. String Operations

```python
# Slower - creates string every iteration
s = ""
for item in items:
    s += str(item)

# Faster - join is optimized
s = "".join(str(item) for item in items)
```

## Async for I/O-Bound Operations

```python
import asyncio

async def concurrent_requests():
    # 10 requests concurrently instead of sequentially
    await asyncio.gather(*[fetch(url) for url in urls])
```

## Database Query Optimization

```python
# Bad - N+1 queries
for user in users:
    print(user.posts)

# Good - join query
users_with_posts = User.query.join(Post)
```

## Memory Profiling Example

```python
from memory_profiler import profile

@profile
def memory_intensive():
    large_list = [i for i in range(1000000)]
    return sum(large_list)
```

## Best Practices

1. **Profile first** - don't guess
2. **Measure improvements** - prove optimizations work
3. **Optimize hot paths** - focus on frequently called code
4. **Use appropriate data structures** - dict vs list vs set
5. **Lazy loading** - load data when needed
6. **Connection pooling** - reuse DB connections
7. **Caching** - avoid redundant computation

## Common Bottlenecks

- Nested loops (O(n²))
- Repeated database queries
- Large list operations
- Inefficient algorithms
- Missing indexes
- Memory leaks
