# Interview Q&A - Performance Tuning

## Q1. How do you identify performance bottlenecks?

**A:** Use profiling tools: cProfile for CPU, tracemalloc for memory, line_profiler for line-by-line analysis. Profile before optimizing.

---

## Q2. What's the difference between cProfile and line_profiler?

**A:** cProfile shows function-level stats. line_profiler shows which specific lines are slow, giving more granular detail.

---

## Q3. When should you use generators instead of lists?

**A:** When you don't need all values at once. Generators are memory-efficient (lazy evaluation) and faster for large datasets.

---

## Q4. Explain @lru_cache and when to use it.

**A:** Decorator that caches function results. Use for expensive computations with limited unique inputs. Avoid for functions with side effects or mutable arguments.

---

## Q5. What are __slots__ and when do you use them?

**A:** __slots__ restricts instance attributes, reducing memory. Use for classes with many instances where memory is critical.

---

## Q6. Why is string concatenation in loops slow?

**A:** Strings are immutable. Each + operation creates a new string. Use "".join() which builds efficiently in one operation.

---

## Q7. What's N+1 query problem and how do you fix it?

**A:** Querying once per item (N+1 queries total). Fix by using joins or eager loading to fetch related data in one query.

---

## Q8. How do you optimize async I/O operations?

**A:** Use asyncio.gather() to run multiple I/O operations concurrently. Don't run them sequentially.

---

## Q9. Why are local variables faster than object attributes?

**A:** Attribute lookups involve dictionary operations. Local variables are direct memory access, much faster.

---

## Q10. When should you use built-in functions like sum() vs manual loops?

**A:** Always. Built-ins are implemented in C and highly optimized. Python loops are much slower.

---

## Q11. What's the impact of repeated imports in loops?

**A:** Major performance hit. Import module once, use many times. Repeated imports re-execute module code.

---

## Q12. How do you balance readability and performance?

**A:** Profile first - don't optimize prematurely. Most code isn't hot. Optimize only clear bottlenecks. Use readable code everywhere else.
