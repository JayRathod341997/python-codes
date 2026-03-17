# Topic 01: Type Hints and Static Typing

## Overview

Master Python's type system for better IDE support, early error detection, and self-documenting code.

## Quick Start

```bash
# Run all examples
python 01_basic_annotations.py
python 02_collections_typing.py
python 03_generics_and_typevar.py
python 04_protocols_and_abc.py
python 05_advanced_patterns.py

# Run exercises
python exercises/solutions/solution_01.py
python exercises/solutions/solution_02.py
```

## Files

| File | Lines | What You'll Learn |
|------|-------|-------------------|
| notes.md | 400+ | Complete theory, examples, pitfalls |
| interview.md | 300+ | 12 Q&A for interviews |
| 01_basic_annotations.py | 150 | Variable & function type hints |
| 02_collections_typing.py | 260 | List, Dict, Set, Tuple typing |
| 03_generics_and_typevar.py | 300+ | TypeVar, Generic classes |
| 04_protocols_and_abc.py | 250+ | Protocols vs ABC |
| 05_advanced_patterns.py | 330 | Literal, TypedDict, Final, @overload |
| exercises/solution_01.py | 140 | Student grade system |
| exercises/solution_02.py | 200 | Inventory system |

## Learning Path

1. **Read notes.md** (30 min) - Understand type system
2. **Run 01_basic_annotations.py** (10 min) - See basics work
3. **Run 02_collections_typing.py** (10 min) - Collections
4. **Run 03_generics_and_typevar.py** (10 min) - Advanced generics
5. **Run 04_protocols_and_abc.py** (10 min) - Structural typing
6. **Run 05_advanced_patterns.py** (10 min) - Advanced patterns
7. **Review interview.md** (10 min) - Key takeaways
8. **Solve exercises** (20 min) - Practice

## Key Concepts

### Basic Types
```python
name: str = "Alice"
age: int = 25
score: float = 95.5
active: bool = True
```

### Collections
```python
List[str], Dict[str, int], Set[int], Tuple[int, int]
```

### Optional
```python
Optional[str] = str | None
```

### Union
```python
Union[int, str] = int | str
```

### TypeVar
```python
T = TypeVar('T')
def first(items: List[T]) -> T: ...
```

### Protocol
```python
class Drawable(Protocol):
    def draw(self) -> None: ...
```

### Advanced
```python
Literal["red", "green"], TypedDict, Final, @overload
```

## Type Checking

### Install mypy
```bash
pip install mypy
```

### Run Type Checker
```bash
mypy 01_basic_annotations.py
mypy --strict .
```

## Exercises

### Exercise 01: Student Grade Manager
Build a system to:
- Add students with grades
- Get average grade
- Find top student

**Files:**
- exercises/exercise_01.py (template)
- exercises/solutions/solution_01.py (solution)

### Exercise 02: Inventory System
Build a system to:
- Add products to categories
- Calculate inventory value
- Find price range

**Files:**
- exercises/exercise_02.py (template)
- exercises/solutions/solution_02.py (solution)

## Common Patterns

| Pattern | Use Case |
|---------|----------|
| `str`, `int`, `float` | Basic types |
| `List[T]`, `Dict[K,V]` | Collections |
| `Optional[T]` | Nullable values |
| `Union[T1, T2]` | Multiple types |
| `TypeVar('T')` | Generic functions |
| `Protocol` | Duck typing |
| `Final` | Immutable values |
| `Literal` | Specific values |

## Key Takeaways

1. Type hints are documentation + IDE support
2. Don't enforce at runtime (optional)
3. Use type checker (mypy) to verify
4. Optional for nullable values
5. Union for multiple types
6. TypeVar for generic functions
7. Protocol for structural typing
8. Always add return types to functions

## Interview Questions

See interview.md for:
- Q1-Q12: Common interview questions
- Explanations and examples
- Follow-up questions

## Next Topic

→ [02_context_managers](../02_context_managers/README.md)

---

**Estimated Time:** 2-3 hours for complete learning + exercises

**Prerequisites:** Basic Python knowledge

**Difficulty:** Intermediate (builds on basics)
