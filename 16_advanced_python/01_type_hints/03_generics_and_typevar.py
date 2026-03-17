"""
============================================================
TOPIC: 03_generics_and_typevar.py
Real-world context: Generic utilities that work with any type
while maintaining type consistency (data processing, caching, etc.)
============================================================
"""

from typing import TypeVar, Generic, List, Optional, Dict

# ============================================================
# SECTION 1: TypeVar Basics
# ============================================================
print("=" * 60)
print("SECTION 1: TypeVar Basics")
print("=" * 60)

# TypeVar creates a generic type variable
# It's a placeholder for "any type, but consistent within scope"
T = TypeVar('T')

def get_first_item(items: List[T]) -> T:
    """
    Get first item from a list.
    T must be consistent: if you pass List[str], returns str
    """
    if items:
        return items[0]
    raise ValueError("List is empty")

# Type checker knows get_first_item returns int
first_number = get_first_item([1, 2, 3])
print(f"First number: {first_number}, Type: {type(first_number).__name__}")

# Type checker knows get_first_item returns str
first_word = get_first_item(["hello", "world"])
print(f"First word: {first_word}, Type: {type(first_word).__name__}")

# Type checker knows get_first_item returns bool
first_bool = get_first_item([True, False])
print(f"First boolean: {first_bool}, Type: {type(first_bool).__name__}")


# ============================================================
# SECTION 2: Generic Functions
# ============================================================
print("\n" + "=" * 60)
print("SECTION 2: Generic Functions")
print("=" * 60)

# Function that works with any type
def reverse_list(items: List[T]) -> List[T]:
    """Reverse a list while preserving type."""
    return list(reversed(items))

numbers = [1, 2, 3, 4]
reversed_numbers = reverse_list(numbers)
print(f"Original numbers: {numbers}")
print(f"Reversed numbers: {reversed_numbers}")

words = ["python", "is", "awesome"]
reversed_words = reverse_list(words)
print(f"\nOriginal words: {words}")
print(f"Reversed words: {reversed_words}")


def find_max(items: List[T]) -> Optional[T]:
    """Find maximum value in list (works with comparable types)."""
    if not items:
        return None
    return max(items)

max_number = find_max([45, 23, 67, 12, 89])
print(f"\nMax number: {max_number}, Type: {type(max_number).__name__}")

max_word = find_max(["apple", "zebra", "banana"])
print(f"Max word (alphabetically): {max_word}, Type: {type(max_word).__name__}")


# ============================================================
# SECTION 3: Multiple TypeVars
# ============================================================
print("\n" + "=" * 60)
print("SECTION 3: Multiple TypeVars (Different Types)")
print("=" * 60)

# Use different TypeVars for different parameters
K = TypeVar('K')  # Key type
V = TypeVar('V')  # Value type

def get_dict_value(data: Dict[K, V], key: K, default: V) -> V:
    """Get value from dict with default if key not found."""
    return data.get(key, default)

# Working with string keys and int values
scores = {"Alice": 95, "Bob": 87}
score = get_dict_value(scores, "Alice", 0)
print(f"Alice's score: {score}, Type: {type(score).__name__}")

# Working with int keys and string values
phone_book = {1: "Alice", 2: "Bob"}
name = get_dict_value(phone_book, 1, "Unknown")
print(f"Person 1: {name}, Type: {type(name).__name__}")


# Function that returns different type than input
def pair_items(items1: List[T], items2: List[K]) -> List[tuple]:
    """Pair items from two lists."""
    return list(zip(items1, items2))

paired = pair_items([1, 2, 3], ["a", "b", "c"])
print(f"\nPaired items: {paired}")


# ============================================================
# SECTION 4: Generic Classes
# ============================================================
print("\n" + "=" * 60)
print("SECTION 4: Generic Classes")
print("=" * 60)

# Generic Stack class that works with any type
class Stack(Generic[T]):
    """A generic stack that can store any type."""

    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        """Add item to stack."""
        self._items.append(item)

    def pop(self) -> Optional[T]:
        """Remove and return top item."""
        if self._items:
            return self._items.pop()
        return None

    def peek(self) -> Optional[T]:
        """View top item without removing."""
        if self._items:
            return self._items[-1]
        return None

    def is_empty(self) -> bool:
        """Check if stack is empty."""
        return len(self._items) == 0

    def size(self) -> int:
        """Get number of items in stack."""
        return len(self._items)


# Using Stack with integers
int_stack: Stack[int] = Stack()
int_stack.push(10)
int_stack.push(20)
int_stack.push(30)
print(f"Int stack peek: {int_stack.peek()}")
print(f"Pop from int stack: {int_stack.pop()}")

# Using Stack with strings
str_stack: Stack[str] = Stack()
str_stack.push("Hello")
str_stack.push("World")
print(f"\nStr stack peek: {str_stack.peek()}")
print(f"Pop from str stack: {str_stack.pop()}")


# Generic Cache class
class Cache(Generic[K, V]):
    """A generic cache that maps keys to values."""

    def __init__(self) -> None:
        self._data: Dict[K, V] = {}

    def set(self, key: K, value: V) -> None:
        """Store key-value pair."""
        self._data[key] = value

    def get(self, key: K, default: Optional[V] = None) -> Optional[V]:
        """Retrieve value by key."""
        return self._data.get(key, default)

    def exists(self, key: K) -> bool:
        """Check if key exists."""
        return key in self._data

    def clear(self) -> None:
        """Clear all cache."""
        self._data.clear()


# Using Cache with string keys and integer values
user_cache: Cache[str, int] = Cache()
user_cache.set("user1", 101)
user_cache.set("user2", 102)
print(f"\nUser cache get 'user1': {user_cache.get('user1')}")

# Using Cache with integer keys and string values
product_cache: Cache[int, str] = Cache()
product_cache.set(1, "Laptop")
product_cache.set(2, "Mouse")
print(f"Product cache get 1: {product_cache.get(1)}")


# ============================================================
# SECTION 5: Bounded TypeVar
# ============================================================
print("\n" + "=" * 60)
print("SECTION 5: Bounded TypeVar (Constrained Types)")
print("=" * 60)

# TypeVar that only accepts certain types (bounded)
# Useful for numeric operations
Number = TypeVar('Number', int, float)

def add_numbers(a: Number, b: Number) -> Number:
    """
    Add two numbers. Works with int or float, but not strings.
    Number = TypeVar('Number', int, float) restricts to these types.
    """
    return a + b

print(f"Add ints: {add_numbers(10, 20)}")
print(f"Add floats: {add_numbers(3.5, 2.5)}")
# add_numbers("10", "20")  # ✗ Type checker error! strings not allowed


# ============================================================
# SECTION 6: Real-World Example - Generic Repository
# ============================================================
print("\n" + "=" * 60)
print("SECTION 6: Real-World Example - Generic Repository")
print("=" * 60)

ID = TypeVar('ID')  # ID type
Entity = TypeVar('Entity')  # Entity type


class Repository(Generic[ID, Entity]):
    """
    Generic repository for any entity type.
    Real-world: Database access layer that works with any model.
    """

    def __init__(self) -> None:
        self._data: Dict[ID, Entity] = {}
        self._next_id: ID = 1  # Simplified ID generation

    def add(self, entity: Entity) -> ID:
        """Add entity and return its ID."""
        entity_id = self._next_id  # type: ignore
        self._data[entity_id] = entity
        self._next_id = entity_id + 1  # type: ignore
        return entity_id

    def get(self, entity_id: ID) -> Optional[Entity]:
        """Get entity by ID."""
        return self._data.get(entity_id)

    def get_all(self) -> List[Entity]:
        """Get all entities."""
        return list(self._data.values())

    def delete(self, entity_id: ID) -> bool:
        """Delete entity by ID."""
        if entity_id in self._data:
            del self._data[entity_id]
            return True
        return False


# Using Repository with User entities
class User:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        return f"User(name='{self.name}', email='{self.email}')"


user_repo: Repository[int, User] = Repository()
user_repo.add(User("Alice", "alice@example.com"))
user_repo.add(User("Bob", "bob@example.com"))

print(f"All users: {user_repo.get_all()}")
print(f"Get user 1: {user_repo.get(1)}")


# ============================================================
# KEY POINTS
# ============================================================
print("\n" + "=" * 60)
print("KEY POINTS")
print("=" * 60)
print("""
1. TypeVar(name) creates a generic type variable
   T = TypeVar('T')

2. Use TypeVar in functions when you work with any type
   def process(items: List[T]) -> T:
   Type checker remembers the type through the function

3. Multiple TypeVars for different type parameters
   K = TypeVar('K')  # Key type
   V = TypeVar('V')  # Value type

4. Generic[T] allows you to create type-safe generic classes
   class Stack(Generic[T]):
       def push(self, item: T) -> None

5. Bounded TypeVar restricts to specific types
   Number = TypeVar('Number', int, float)

6. Real-world use cases:
   - Collections (Stack, Queue, Cache)
   - Repositories and DAOs
   - Generic processing pipelines
   - API response wrappers

7. TypeVar ONLY helps type checkers and IDEs
   It doesn't affect runtime behavior
""")
