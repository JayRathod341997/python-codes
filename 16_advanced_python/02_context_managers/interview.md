# Interview Q&A — Context Managers

## Q1. What is a context manager and why use it?

**A:** A context manager ensures proper setup and teardown of resources. Using `with open(file)` automatically closes the file even if an exception occurs, unlike manual `open()` + `close()` which requires try-finally boilerplate.

---

## Q2. What are the two methods a context manager must implement?

**A:** `__enter__()` (called when entering the `with` block) and `__exit__(exc_type, exc_val, exc_tb)` (called when exiting). The `__exit__` parameters contain exception info if one occurred.

---

## Q3. What's the difference between `@contextmanager` and class-based context managers?

**A:** `@contextmanager` is simpler (code before `yield` = setup, after = cleanup). Class-based is more explicit and better for complex logic with multiple methods. Both implement the context manager protocol.

---

## Q4. When should I return `True` in `__exit__`?

**A:** Return `True` to suppress (hide) an exception. This should be rare and intentional (e.g., `contextlib.suppress()`). Usually return `False` to let exceptions propagate normally.

---

## Q5. Can you nest multiple `with` statements?

**A:** Yes, in two ways:
```python
with open("a") as f1, open("b") as f2:
    pass

with ExitStack() as stack:
    f1 = stack.enter_context(open("a"))
    f2 = stack.enter_context(open("b"))
```

---

## Q6. What happens if an exception occurs inside a `with` block?

**A:** The exception is passed to `__exit__()` as `(exc_type, exc_val, exc_tb)`. Your `__exit__` code still runs (cleanup is guaranteed). If `__exit__` returns `False`, the exception propagates.

---

## Q7. What's the difference between `contextmanager` and `suppress`?

**A:** `@contextmanager` creates custom context managers (setup/cleanup pattern). `suppress()` is a built-in context manager that catches and ignores specific exceptions: `with suppress(FileNotFoundError): os.remove(file)`.

---

## Q8. How do you handle multiple resources safely?

**A:** Use `ExitStack()` to dynamically manage any number of context managers:
```python
from contextlib import ExitStack
with ExitStack() as stack:
    files = [stack.enter_context(open(f)) for f in filenames]
```

---

## Q9. What's a good use case for a custom context manager?

**A:** Database transactions, file locking, timing code blocks, thread-safe operations, temporary configuration changes, or cleaning up temporary directories.

---

## Q10. If `__exit__` raises an exception, what happens?

**A:** The new exception replaces the original one (if any). Avoid raising in `__exit__` unless absolutely necessary. Use try-finally to ensure cleanup doesn't break.

---

## Q11. Can you use a context manager with async/await?

**A:** Yes, with async context managers using `async with`:
```python
async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
        data = await response.text()
```

---

## Q12. What's the performance impact of using context managers?

**A:** Negligible. Context managers add minimal overhead. The benefit (safety, readability) far outweighs any tiny performance cost.
