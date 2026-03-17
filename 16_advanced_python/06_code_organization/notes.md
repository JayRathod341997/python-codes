# Code Organization and Design Principles

## What is it?

Code organization involves structuring your codebase following SOLID principles, design patterns, and modular design to create maintainable, scalable, and testable code.

## SOLID Principles

### S - Single Responsibility Principle

Each class should have ONE reason to change.

```python
# Bad
class User:
    def save_to_db(self): pass
    def send_email(self): pass
    def validate_email(self): pass

# Good
class User:
    pass

class UserRepository:
    def save(self, user): pass

class EmailService:
    def send(self, email): pass

class EmailValidator:
    def validate(self, email): pass
```

### O - Open/Closed Principle

Open for extension, closed for modification.

```python
# Bad
def calculate_discount(user_type):
    if user_type == "regular":
        return 0.05
    elif user_type == "premium":
        return 0.10

# Good
class DiscountStrategy:
    def get_discount(self): pass

class RegularDiscount(DiscountStrategy):
    def get_discount(self): return 0.05

class PremiumDiscount(DiscountStrategy):
    def get_discount(self): return 0.10
```

### L - Liskov Substitution Principle

Subtypes must be substitutable for their base types.

```python
class Bird:
    def fly(self): pass

class Penguin(Bird):
    def fly(self):  # Can't actually fly!
        raise NotImplementedError

# Bad design - Penguin breaks Bird contract
```

### I - Interface Segregation Principle

Clients shouldn't depend on interfaces they don't use.

```python
# Bad
class Worker:
    def work(self): pass
    def eat_lunch(self): pass

# Good
class Workable:
    def work(self): pass

class Eatable:
    def eat_lunch(self): pass
```

### D - Dependency Inversion Principle

Depend on abstractions, not concretions.

```python
# Bad
class Repository:
    def __init__(self):
        self.db = PostgreSQLDB()

# Good
class Repository:
    def __init__(self, db: DatabaseInterface):
        self.db = db
```

## Design Patterns

### Factory Pattern

Create objects without specifying exact classes.

```python
class PaymentFactory:
    @staticmethod
    def create_processor(method):
        if method == "card":
            return CardPayment()
        elif method == "wallet":
            return WalletPayment()
```

### Strategy Pattern

Encapsulate algorithm families.

```python
class SortingStrategy:
    def sort(self, data): pass

class QuickSort(SortingStrategy):
    def sort(self, data): pass

class Sorter:
    def __init__(self, strategy: SortingStrategy):
        self.strategy = strategy
```

### Observer Pattern

Notify multiple objects of state changes.

```python
class Observable:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self):
        for obs in self.observers:
            obs.update()
```

## Module Design

### Package Structure

```
myapp/
  __init__.py
  core/
    __init__.py
    models.py
    services.py
  api/
    __init__.py
    routes.py
    middleware.py
  tests/
    __init__.py
    test_services.py
```

### Import Best Practices

```python
# Bad - circular imports risk
from myapp.api import something
from myapp.core import something_else

# Good - explicit imports
from myapp.core.services import UserService
from myapp.core.models import User
```

## Dataclasses

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    age: int = 0

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")
```

## Best Practices

1. **One class per file** (for small classes)
2. **Group related classes** in modules
3. **Use __all__** to control exports
4. **Clear dependency flow** (models -> services -> api)
5. **Type hints** for all functions
6. **Docstrings** for public APIs
7. **Tests co-located** with code

## Common Pitfalls

- God objects (too many responsibilities)
- Tight coupling (hard to change)
- Deep inheritance hierarchies
- Circular imports
- Inconsistent naming conventions
