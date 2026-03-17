# Interview Q&A — Type Hints and Static Typing

## Q1. What's the difference between type hints and runtime type enforcement?

**A:** Type hints are **purely documentation** — Python doesn't enforce them at runtime. They're for static type checkers (mypy, pyright) and IDEs. Runtime type checking requires explicit checks: `if not isinstance(x, int): raise TypeError()`.

---

## Q2. When should I use `Optional[T]` vs `T | None`?

**A:** Both are equivalent. `Optional[T]` is the pre-Python 3.10 syntax; `T | None` is the modern PEP 604 syntax (Python 3.10+). Use `T | None` for new code if your project supports Python 3.10+.

---

## Q3. Can type hints improve performance?

**A:** Not directly — they don't run at runtime. However, they enable better IDE optimization and help you write more efficient code by catching type mismatches early.

---

## Q4. What's the difference between `List[int]` and `list[int]`?

**A:** `List[int]` (from `typing` module) works in Python 3.8 and earlier. `list[int]` (built-in) works in Python 3.9+. Both mean "a list of integers." Use `list[int]` for new code.

---

## Q5. How do I type a function that accepts a function as a parameter?

**A:** Use `Callable`:
```python
from typing import Callable
def apply(fn: Callable[[int, int], int], x: int, y: int) -> int:
    return fn(x, y)
```
`Callable[[int, int], int]` means a function taking two ints, returning an int.

---

## Q6. What's a Protocol, and why would I use it instead of inheritance?

**A:** A Protocol defines a structural type ("if it has these methods, it matches"). It's duck typing with explicit documentation. Use it when you don't want to force inheritance:
```python
class Drawable(Protocol):
    def draw(self) -> None: ...

class Circle:
    def draw(self) -> None: pass  # No inheritance needed!
```

---

## Q7. What does `TypeVar` do, and when do I use it?

**A:** `TypeVar` creates a generic type that must be consistent within a function scope:
```python
T = TypeVar('T')
def first(items: List[T]) -> T:
    return items[0]  # Returns same type as list element
```
Use it when a function works with any type but needs type consistency.

---

## Q8. How do I type a variable that could be a string OR an integer?

**A:** Use `Union`:
```python
from typing import Union
value: Union[str, int] = "hello"  # or 42
# In Python 3.10+: value: str | int
```

---

## Q9. What's the point of `Literal` types?

**A:** `Literal` restricts a value to specific constants. Useful for functions that accept only certain values:
```python
from typing import Literal
def log_level(level: Literal["DEBUG", "INFO", "ERROR"]) -> None:
    pass  # Only these three strings allowed
```

---

## Q10. Should I use type hints everywhere, or only on public APIs?

**A:** Start with function signatures (especially public APIs and complex functions). For simple internal functions and variable assignments, type hints are optional. Always use them in:
- Public function signatures
- Class methods
- Anything that interacts with external code
- Complex logic where types aren't obvious

---

## Q11. What's the difference between `@overload` and `Union`?

**A:** `@overload` defines multiple function signatures for different input types (for type checkers only). Use it when behavior differs by type:
```python
from typing import overload

@overload
def process(data: int) -> str: ...
@overload
def process(data: str) -> int: ...

def process(data):
    if isinstance(data, int):
        return str(data)
    return int(data)
```

---

## Q12. Why is `Any` considered bad practice?

**A:** `Any` disables type checking, defeating the purpose of type hints. It's a type escape hatch. Use it only when you genuinely can't determine the type (e.g., working with untyped external libraries).

---

## Bonus: How do I run a type checker on my project?

```bash
# Install mypy (most popular)
pip install mypy

# Check a file
mypy your_file.py

# Check entire directory with strict mode
mypy . --strict

# For VSCode, install Pylance extension (uses Pyright)
```
