# Type Hints and Static Typing Best Practices

## What is it?

Type hints (also called "type annotations") are a way to explicitly declare the expected data types of variables, function parameters, and return values in Python. They don't enforce types at runtime but provide documentation and enable static type checkers like `mypy`, `pyright`, and IDE autocompletion.

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

Here, `name: str` means the parameter `name` should be a string, and `-> str` means the function returns a string.

---

## Why Use Type Hints?

| Benefit | Example |
|---------|---------|
| **Self-documenting code** | Function signatures are clearer; less need for comments |
| **IDE autocompletion** | IDEs know what methods/attributes are available |
| **Catch bugs early** | Static type checkers find type mismatches before runtime |
| **Refactoring safety** | Renaming a type helps the checker catch all usages |
| **Better onboarding** | New developers understand function contracts immediately |

---

## Core Concepts

### 1. Basic Type Annotations

```python
name: str = "Alice"              # Variable annotation
age: int = 25
is_active: bool = True
score: float = 95.5
```

### 2. Collection Types (from `typing` module)

```python
from typing import List, Dict, Set, Tuple, Optional

# Lists with type of elements
users: List[str] = ["Alice", "Bob"]

# Dictionaries with key and value types
scores: Dict[str, int] = {"Alice": 95, "Bob": 87}

# Sets
tags: Set[str] = {"python", "typing"}

# Tuples (fixed length, specific types)
coordinates: Tuple[int, int] = (10, 20)
mixed_tuple: Tuple[str, int, bool] = ("data", 42, True)
```

### 3. Optional Types

Use `Optional[Type]` when a value can be `None`:

```python
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    # Returns either a string (username) or None
    if user_id == 1:
        return "Alice"
    return None
```

**Alternative (Python 3.10+):**
```python
def find_user(user_id: int) -> str | None:
    # Same meaning, cleaner syntax
    return "Alice" if user_id == 1 else None
```

### 4. Union Types (Multiple Possible Types)

```python
from typing import Union

# Value can be either int or str
def process(value: Union[int, str]) -> None:
    if isinstance(value, int):
        print(f"Number: {value}")
    else:
        print(f"Text: {value}")

# Python 3.10+ alternative:
def process(value: int | str) -> None:
    pass
```

### 5. Function Type Hints

```python
from typing import Callable

# Function that takes two ints and returns an int
add: Callable[[int, int], int] = lambda x, y: x + y

# Function as parameter
def apply_operation(x: int, y: int, op: Callable[[int, int], int]) -> int:
    return op(x, y)

result = apply_operation(5, 3, add)  # result = 8
```

### 6. Generics and TypeVar

Use `TypeVar` when a function works with any type but must be consistent:

```python
from typing import TypeVar, List

T = TypeVar('T')  # Generic type variable

def get_first(items: List[T]) -> T:
    """Returns the first item of any list."""
    return items[0]

first_str = get_first(["a", "b"])     # Type of first_str is str
first_int = get_first([1, 2])         # Type of first_int is int
```

### 7. Protocols (Structural Typing)

Define what methods an object should have without inheritance:

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

class Circle:
    def draw(self) -> None:
        print("Drawing circle")

def render(obj: Drawable) -> None:
    obj.draw()

render(Circle())  # ✓ Works because Circle has draw()
```

### 8. Literal Types (Specific Values)

```python
from typing import Literal

def set_status(status: Literal["active", "inactive", "pending"]) -> None:
    # status can ONLY be one of these three strings
    pass

set_status("active")    # ✓ OK
set_status("pending")   # ✓ OK
set_status("unknown")   # ✗ Type checker error
```

### 9. TypedDict (Typed Dictionaries)

```python
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int
    email: str

user: User = {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com"
}
```

### 10. Final (Prevent Reassignment)

```python
from typing import Final

MAX_RETRIES: Final[int] = 3
# MAX_RETRIES = 5  # ✗ Type checker error: cannot reassign Final

class Config:
    VERSION: Final = "1.0"
    # VERSION = "2.0"  # ✗ Error
```

---

## Common Pitfalls

### 1. **Forgetting `None` in Optional**
```python
# ✗ Wrong: doesn't document that None is possible
def get_user(user_id: int) -> str:
    if user_id == 1:
        return "Alice"
    return None  # Runtime error! Expected str, got None

# ✓ Correct
from typing import Optional
def get_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Alice"
    return None
```

### 2. **Mutable Default Arguments**
```python
# ✗ Wrong: list is shared across all calls
def add_user(name: str, users: List[str] = []) -> None:
    users.append(name)

add_user("Alice")
add_user("Bob")
print(users)  # ["Alice", "Bob"] -- unexpected!

# ✓ Correct
def add_user(name: str, users: Optional[List[str]] = None) -> None:
    if users is None:
        users = []
    users.append(name)
```

### 3. **Covariance/Contravariance Confusion**
```python
# ✗ This is tricky with inheritance
# A function expecting List[Animal] can't accept List[Dog]
# (even though Dog is a subclass of Animal)

# Use Sequence[Animal] for read-only operations instead
from typing import Sequence

def print_animals(animals: Sequence[Animal]) -> None:
    for animal in animals:
        print(animal.name)
```

### 4. **Not Using Type Checkers**
Type hints are only useful if you **actually run a type checker**:

```bash
# Install mypy
pip install mypy

# Check your code
mypy your_file.py
```

---

## Quick Reference Cheatsheet

| Type | Syntax | Example |
|------|--------|---------|
| String | `str` | `name: str = "Alice"` |
| Integer | `int` | `age: int = 25` |
| Float | `float` | `price: float = 19.99` |
| Boolean | `bool` | `is_active: bool = True` |
| List | `List[T]` | `items: List[int] = [1, 2, 3]` |
| Dict | `Dict[K, V]` | `data: Dict[str, int] = {}` |
| Tuple | `Tuple[T, ...]` | `point: Tuple[int, int] = (0, 0)` |
| Optional | `Optional[T]` or `T \| None` | `result: Optional[str] = None` |
| Union | `Union[T1, T2]` or `T1 \| T2` | `value: int \| str` |
| Function | `Callable[[Args], Return]` | `fn: Callable[[int], str]` |
| Any | `Any` | `data: Any` (use sparingly!) |
| No return | `None` | `def log(): -> None` |

---

## Type Hints Best Practices

1. **Always use return type hints** — helps catch bugs
   ```python
   def calculate(x: int, y: int) -> int:  # ✓ Good
       return x + y
   ```

2. **Use `Optional[T]` for potentially `None` values**
   ```python
   def get_user(uid: int) -> Optional[str]:  # ✓ Clear
       pass
   ```

3. **Avoid `Any` — be specific**
   ```python
   # ✗ Too vague
   def process(data: Any) -> Any:
       pass

   # ✓ Better
   def process(data: List[Dict[str, int]]) -> Dict[str, int]:
       pass
   ```

4. **Use type checkers in your workflow** (CI/CD)
   ```bash
   mypy . --strict
   ```

5. **Document why, not what** (types show the "what")
   ```python
   def exponential_backoff(attempt: int) -> int:
       """Wait longer after each failed attempt (2^attempt seconds)."""
       return 2 ** attempt
   ```

---

## Further Reading

- [PEP 484 — Type Hints](https://www.python.org/dev/peps/pep-0484/)
- [Python `typing` Module](https://docs.python.org/3/library/typing.html)
- [MyPy Documentation](https://mypy.readthedocs.io/)
- [Pyright (VSCode Type Checker)](https://github.com/microsoft/pyright)
