# Dependency Injection: Building Loosely Coupled Code

## What is it?

Dependency Injection (DI) is a design pattern where objects receive their dependencies instead of creating them. It decouples code and makes it testable.

```python
# Bad - tightly coupled
class Service:
    def __init__(self):
        self.db = PostgreSQL()

# Good - loosely coupled (injection)
class Service:
    def __init__(self, db: Database):
        self.db = db
```

## Why Use DI?

- **Testability** - inject mocks instead of real dependencies
- **Flexibility** - swap implementations easily
- **Reusability** - components don't know about others
- **Maintainability** - clear dependencies

## Dependency Injection Patterns

### 1. Constructor Injection (Most Common)

```python
class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

service = UserService(PostgreSQLRepository())
```

### 2. Setter Injection

```python
class UserService:
    def set_repository(self, repo):
        self.repository = repo
```

Flexible but less clear about dependencies.

### 3. Interface Injection

```python
class Injector:
    def inject(self, service):
        service.set_repository(PostgreSQLRepository())
```

### 4. Factory Pattern

```python
class ServiceFactory:
    @staticmethod
    def create_service():
        db = create_database()
        return UserService(db)
```

## Protocol-Based DI

```python
from typing import Protocol

class Database(Protocol):
    def query(self, sql: str): ...
    def execute(self, sql: str): ...

class UserService:
    def __init__(self, db: Database):
        self.db = db

# Any object with query() and execute() works
class PostgreSQL:
    def query(self, sql): pass
    def execute(self, sql): pass

service = UserService(PostgreSQL())
```

## DI Containers

```python
from dependency_injector import containers, providers

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    db = providers.Singleton(
        Database,
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

## FastAPI-Style DI

```python
from fastapi import Depends

def get_db():
    db = create_database()
    try:
        yield db
    finally:
        db.close()

@app.get("/users/{user_id}")
def get_user(user_id: int, db = Depends(get_db)):
    return db.query(User).filter_by(id=user_id).first()
```

## Testing with DI

```python
class MockRepository:
    def get_user(self, user_id):
        return {"id": user_id, "name": "Test"}

def test_service():
    # Inject mock instead of real DB
    service = UserService(MockRepository())
    result = service.get_user(1)
    assert result["name"] == "Test"
```

## Best Practices

1. **Inject at constructor** - dependencies visible
2. **Use protocols** - define contracts, not implementations
3. **Avoid service locator** - explicit is better
4. **Keep it simple** - don't over-engineer
5. **Use containers for complex graphs** - but not always needed
6. **Test with mocks** - that's the whole point

## Anti-Patterns

- **Service Locator** - hidden dependencies
- **Importing everywhere** - not injectable
- **God Container** - creating everything
- **Circular dependencies** - sign of bad design
