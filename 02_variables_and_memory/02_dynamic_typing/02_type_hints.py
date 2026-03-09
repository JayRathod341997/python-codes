# ============================================================
# Type Hints (Optional Static Typing — PEP 484)
# ============================================================
# Python is dynamically typed, but you CAN add optional type
# hints to improve readability and enable static analysis tools
# like mypy. They are NOT enforced at runtime.
# ============================================================

# --- Variable type hints ---
name: str = "Alice"
age: int = 30
salary: float = 75000.0
is_active: bool = True

print(name, age, salary, is_active)

# --- Type hints are just hints — Python doesn't enforce them ---
name: str = 42          # No error! Python still accepts it.
print(name, type(name)) # 42 <class 'int'>

# --- Function with type hints ---
def greet(person: str) -> str:
    return f"Hello, {person}!"

def add(a: int, b: int) -> int:
    return a + b

print(greet("Jay"))
print(add(3, 7))

# --- Complex types using the built-in generics (Python 3.9+) ---
def get_scores(names: list[str]) -> dict[str, int]:
    return {name: len(name) * 10 for name in names}

print(get_scores(["Alice", "Bob", "Charlie"]))

# --- Optional type: value can be the type OR None ---
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)   # returns None if not found

print(find_user(1))     # Alice
print(find_user(99))    # None

# --- Union type (Python 3.10+ syntax: X | Y) ---
def process(value: int | str) -> str:
    return str(value).upper()

print(process(42))
print(process("hello"))
