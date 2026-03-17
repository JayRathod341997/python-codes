# Topic 08: Dependency Injection

## Overview

Build loosely coupled, testable code using dependency injection patterns.

## Quick Start

```bash
# Read theory
cat notes.md
cat interview.md

# Review examples
python exercises/solutions/solution_01.py
python exercises/solutions/solution_02.py
```

## Key Concepts

### Basic DI

```python
# BAD - tightly coupled
class Service:
    def __init__(self):
        self.db = PostgreSQL()

# GOOD - loosely coupled
class Service:
    def __init__(self, db: Database):
        self.db = db

# Usage
service = Service(PostgreSQL())
```

### Constructor Injection

```python
class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

# Inject real implementation
service = UserService(PostgreSQLRepository())

# Or mock for testing
from unittest.mock import Mock
mock_repo = Mock()
service = UserService(mock_repo)
```

### Protocol-Based DI

```python
from typing import Protocol

class Database(Protocol):
    def query(self, sql: str): ...
    def execute(self, sql: str): ...

class UserService:
    def __init__(self, db: Database):
        self.db = db

# Any object with query/execute works
class PostgreSQL:
    def query(self, sql): pass
    def execute(self, sql): pass

service = UserService(PostgreSQL())
```

### Factory Pattern

```python
class ServiceFactory:
    @staticmethod
    def create_service():
        db = PostgreSQL(host="localhost")
        cache = RedisCache()
        repository = UserRepository(db, cache)
        return UserService(repository)

service = ServiceFactory.create_service()
```

## Real-World Example

### Bad Design - Hard to Test
```python
class PaymentService:
    def __init__(self):
        self.db = MySQLDB()
        self.stripe = StripeAPI()
        self.email = EmailService()

    def process_payment(self, user_id, amount):
        user = self.db.get_user(user_id)
        charge = self.stripe.charge(amount)
        self.email.send_receipt(user.email, charge)
```

### Good Design - Easy to Test
```python
class PaymentService:
    def __init__(self, db: Database, payment_api: PaymentAPI, email: EmailService):
        self.db = db
        self.payment_api = payment_api
        self.email = email

    def process_payment(self, user_id, amount):
        user = self.db.get_user(user_id)
        charge = self.payment_api.charge(amount)
        self.email.send_receipt(user.email, charge)

# For production
service = PaymentService(
    MySQL(),
    StripeAPI(),
    SMTPEmailService()
)

# For testing
from unittest.mock import Mock
service = PaymentService(
    Mock(spec=Database),
    Mock(spec=PaymentAPI),
    Mock(spec=EmailService)
)
```

### FastAPI Dependency

```python
from fastapi import Depends, FastAPI

def get_db():
    db = PostgreSQL()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int, db = Depends(get_db)):
    return db.get_user(user_id)
```

## DI Containers

```bash
pip install dependency-injector
```

```python
from dependency_injector import containers, providers

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    db = providers.Singleton(
        PostgreSQL,
        host=config.db.host,
        password=config.db.password
    )

    repository = providers.Factory(
        UserRepository,
        db=db
    )

    service = providers.Factory(
        UserService,
        repository=repository
    )

# Usage
container = Container()
service = container.service()
```

## Testing with DI

```python
def test_payment_service():
    # Inject mocks
    mock_db = Mock(spec=Database)
    mock_payment = Mock(spec=PaymentAPI)
    mock_email = Mock(spec=EmailService)

    service = PaymentService(mock_db, mock_payment, mock_email)

    # Setup expectations
    mock_db.get_user.return_value = {"id": 1, "email": "test@example.com"}
    mock_payment.charge.return_value = {"id": "charge123"}

    # Test
    result = service.process_payment(1, 100)

    # Assert
    mock_email.send_receipt.assert_called_once()
```

## Patterns

| Pattern | Use |
|---------|-----|
| Constructor | Most common, explicit |
| Setter | Flexible, less clear |
| Factory | Complex creation |
| Container | Many dependencies |
| Service Locator | Hidden (avoid!) |

## Benefits

1. **Testability** - Inject mocks
2. **Flexibility** - Swap implementations
3. **Reusability** - Components independent
4. **Maintainability** - Clear dependencies
5. **Decoupling** - No hard dependencies

## Anti-Patterns

```python
# BAD - Service Locator (hidden dependencies)
class Service:
    def process(self):
        db = ServiceLocator.get_db()
        cache = ServiceLocator.get_cache()

# GOOD - Constructor injection
class Service:
    def __init__(self, db, cache):
        self.db = db
        self.cache = cache
```

## Circular Dependencies

```python
# BAD - A depends on B, B depends on A
class A:
    def __init__(self, b: 'B'):
        self.b = b

class B:
    def __init__(self, a: A):
        self.a = a

# GOOD - Redesign to remove circular dependency
class A:
    def __init__(self):
        pass

class B:
    def process(self, a: A):
        pass
```

## Key Takeaways

1. Inject dependencies, don't create them
2. Use constructor injection
3. Depend on abstractions (protocols)
4. Test with mocks
5. Keep it simple
6. Avoid service locator
7. Watch for circular deps
8. Use containers for complex graphs

## Interview Questions

See interview.md for Q1-Q12:
- What is DI?
- Why use DI?
- Testing with DI
- DI containers
- Anti-patterns

## Best Practices

1. **Constructor injection** - dependencies visible
2. **Type hints** - declare contracts
3. **Protocols** - define interfaces
4. **Testing** - inject mocks freely
5. **Simple** - don't over-engineer
6. **Containers** - for complex apps only
7. **Documentation** - explain dependencies
8. **Verify** - test injected objects work

## When to Use DI

- Building APIs/web apps
- Testing requirements
- Multiple implementations
- Plugin systems
- Microservices

## When NOT to Use DI

- Simple scripts
- Overkill for tiny apps
- When simplicity matters more
- Learning basics first

## Next Topic

This is the final topic! You've completed all 8 advanced Python skills.

---

**Estimated Time:** 2 hours

**Prerequisites:** All previous topics

**Difficulty:** Advanced

**Required Packages:** dependency-injector (optional)
