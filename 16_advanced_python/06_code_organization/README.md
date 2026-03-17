# Topic 06: Code Organization and Design Principles

## Overview

Structure code following SOLID principles and design patterns.

## Quick Start

```bash
# Read theory
cat notes.md
cat interview.md

# Review examples in exercises
python exercises/solutions/solution_01.py
python exercises/solutions/solution_02.py
```

## Files

| File | What You'll Learn |
|------|-------------------|
| notes.md | SOLID, patterns, structure |
| interview.md | 12 Q&A on design |
| exercises/solutions/ | Pattern examples |

## Key Concepts

### SOLID Principles

**S - Single Responsibility**
- One reason to change
- One job per class

**O - Open/Closed**
- Open for extension
- Closed for modification

**L - Liskov Substitution**
- Subtype replaces parent type
- Don't break contracts

**I - Interface Segregation**
- Don't depend on unused interfaces
- Specific contracts

**D - Dependency Inversion**
- Depend on abstractions
- Not concrete classes

### Design Patterns

| Pattern | Purpose |
|---------|---------|
| Factory | Create objects |
| Strategy | Encapsulate algorithms |
| Observer | Notify of changes |
| Decorator | Add behavior |
| Adapter | Bridge incompatibility |

### Code Organization

```
myapp/
├── __init__.py
├── models/
│   ├── __init__.py
│   ├── user.py
│   └── product.py
├── services/
│   ├── __init__.py
│   ├── user_service.py
│   └── product_service.py
├── api/
│   ├── __init__.py
│   ├── routes.py
│   └── middleware.py
└── tests/
    ├── test_models.py
    └── test_services.py
```

### Dataclasses

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

## Real-World Example

### Bad Design (Tightly Coupled)
```python
class UserService:
    def __init__(self):
        self.db = PostgreSQLDB()
        self.email = GmailService()

    def create_user(self, name, email):
        self.db.insert(name, email)
        self.email.send(email, "Welcome!")
```

### Good Design (Loosely Coupled)
```python
class UserService:
    def __init__(self, db: Database, email: EmailService):
        self.db = db
        self.email = email

    def create_user(self, name, email):
        self.db.insert(name, email)
        self.email.send(email, "Welcome!")

# Inject implementations
service = UserService(PostgreSQL(), Gmail())
```

## Module Design

### Clear Imports
```python
# BAD - circular imports risk
from myapp.api import something
from myapp.services import something_else

# GOOD - explicit imports
from myapp.services.user_service import UserService
from myapp.models.user import User
```

### Clear Dependencies
```
models → services → api

Each layer only imports from layers below
Never circular (services importing api)
```

## Patterns in Practice

### Factory Pattern
```python
class PaymentFactory:
    @staticmethod
    def create(method):
        if method == "card":
            return CardPayment()
        elif method == "wallet":
            return WalletPayment()
```

### Strategy Pattern
```python
class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def sort(self, data):
        return self.strategy.sort(data)

sorter = Sorter(QuickSort())
```

### Observer Pattern
```python
class Observable:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, event):
        for obs in self.observers:
            obs.update(event)
```

## Key Takeaways

1. Apply SOLID principles
2. One class, one responsibility
3. Depend on abstractions
4. Use design patterns
5. Clear module structure
6. Type hints everywhere
7. Docstrings for public APIs
8. Tests alongside code

## Interview Questions

See interview.md for Q1-Q12:
- What is SOLID?
- Single Responsibility
- Open/Closed Principle
- Design patterns
- Module structure

## Best Practices

1. **SRP** - One reason to change
2. **DIP** - Inject dependencies
3. **Composition** - has-a over is-a
4. **Interfaces** - Program to contracts
5. **Clarity** - Self-documenting code
6. **Testability** - Easy to test
7. **Maintainability** - Easy to change
8. **Scalability** - Grows without pain

## Anti-Patterns to Avoid

1. God Objects (too many responsibilities)
2. Feature Envy (using others' data)
3. Tight Coupling (hard to test)
4. Circular Dependencies (design smell)
5. Deep Inheritance (fragile)
6. Magic Numbers (hardcoded values)
7. Comment Chaos (unclear code)
8. Inconsistent Naming (confusing)

## Exercise Ideas

1. Refactor tightly coupled code
2. Apply SOLID to existing project
3. Implement design patterns
4. Improve module organization
5. Add type hints
6. Create clear abstractions

## Next Topic

→ [07_performance_tuning](../07_performance_tuning/README.md)

---

**Estimated Time:** 2-3 hours (theory-heavy)

**Prerequisites:** All previous topics helpful

**Difficulty:** Intermediate-Advanced
