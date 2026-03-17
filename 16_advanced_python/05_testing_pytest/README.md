# Topic 05: Testing with Pytest

## Overview

Write comprehensive test suites with fixtures, parametrization, and mocking.

## Quick Start

```bash
# Run all tests
pytest -v

# Run topic tests
pytest 05_testing_pytest/ -v

# Run with coverage
pip install pytest-cov
pytest --cov=. --cov-report=html
```

## Files

| File | Lines | What You'll Learn |
|------|-------|-------------------|
| notes.md | 400+ | Theory, examples, patterns |
| interview.md | 300+ | 12 Q&A |
| 01_basics.py | 150 | Test functions, assertions |
| 02_fixtures.py | 250+ | Fixtures, scopes, yield |
| 03_parametrize.py | 200+ | Parametrized tests |
| 04_mocking.py | 250+ | unittest.mock, patch |

## Learning Path

1. **Read notes.md** (30 min)
2. **Run pytest 01_basics.py** (10 min)
3. **Run pytest 02_fixtures.py** (10 min)
4. **Run pytest 03_parametrize.py** (10 min)
5. **Run pytest 04_mocking.py** (10 min)
6. **Review interview.md** (10 min)
7. **Write your own tests** (30 min)

## Key Concepts

### Test Functions
```python
def test_addition():
    assert 2 + 2 == 4

def test_string():
    assert "hello".upper() == "HELLO"
```

### Fixtures
```python
import pytest

@pytest.fixture
def db():
    db = Database()
    yield db
    db.close()

def test_query(db):
    result = db.query("SELECT * FROM users")
    assert len(result) > 0
```

### Parametrization
```python
@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
])
def test_square(input, expected):
    assert input ** 2 == expected
```

### Mocking
```python
from unittest.mock import Mock, patch

def test_api_call():
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {"id": 1}
        result = fetch_user(1)
        assert result["id"] == 1
```

### Fixtures with Scope
```python
@pytest.fixture(scope="session")
def db_connection():
    # Create once per session
    conn = connect_db()
    yield conn
    conn.close()

@pytest.fixture(scope="function")
def clean_db(db_connection):
    # Reset before each test
    db_connection.clear()
    yield db_connection
```

## Real-World Example

### Testing Calculator
```python
# calculator.py
def add(a, b):
    return a + b

# test_calculator.py
def test_add():
    assert add(2, 3) == 5

@pytest.mark.parametrize("a,b,expected", [
    (1, 1, 2),
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected
```

### Testing API
```python
@pytest.fixture
def client():
    from fastapi.testclient import TestClient
    from main import app
    return TestClient(app)

def test_get_user(client):
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
```

## Fixture Patterns

| Pattern | Use |
|---------|-----|
| function scope | Default, run per test |
| class scope | Run once per test class |
| module scope | Run once per module |
| session scope | Run once per session |
| autouse=True | Always use, don't pass |
| yield | Cleanup after test |

## Mocking Patterns

```python
# Mock return value
mock.return_value = 42

# Mock method call
mock.method.return_value = "result"

# Check mock was called
mock.assert_called_once()
mock.assert_called_with(arg1, arg2)

# Mock side effects
mock.side_effect = ValueError("Error")
mock.side_effect = [1, 2, 3]  # Multiple calls

# Patch decorator
@patch('module.function')
def test_something(mock_func):
    mock_func.return_value = "mocked"
```

## Test Organization

```
project/
├── main.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Shared fixtures
│   ├── test_models.py
│   ├── test_services.py
│   ├── test_api.py
│   └── fixtures/            # Test data
│       ├── users.json
│       └── products.json
```

## conftest.py Example

```python
# tests/conftest.py
import pytest

@pytest.fixture
def db():
    db = Database()
    db.init()
    yield db
    db.cleanup()

@pytest.fixture
def sample_user():
    return {"id": 1, "name": "Alice"}
```

## Running Tests

```bash
# All tests
pytest

# Specific file
pytest test_models.py

# Specific test
pytest test_models.py::test_user_creation

# Verbose
pytest -v

# Show print statements
pytest -s

# Stop on first failure
pytest -x

# Run N tests
pytest --maxfail=3

# Match test name
pytest -k "test_api"

# Markers
pytest -m "slow"
```

## Coverage

```bash
# Install coverage
pip install pytest-cov

# Run with coverage
pytest --cov=. --cov-report=html

# Check coverage percentage
pytest --cov=. --cov-report=term-missing
```

## Key Takeaways

1. Use pytest for testing
2. One test per function/method
3. Use fixtures for setup/cleanup
4. Parametrize for multiple inputs
5. Mock external dependencies
6. Use conftest.py for shared fixtures
7. Test both happy and sad paths
8. Aim for 80%+ coverage

## Interview Questions

See interview.md for Q1-Q12:
- What is pytest?
- Fixtures and scopes
- Parametrization
- Mocking
- Test organization

## Best Practices

1. Test one thing per test
2. Use descriptive test names
3. Arrange-Act-Assert pattern
4. Don't test implementation
5. Test behavior/contracts
6. Keep tests fast
7. Use fixtures wisely
8. Mock external services

## Common Pitfalls

1. Too many assertions per test
2. Testing implementation details
3. Slow tests (use mocks)
4. Flaky tests (timing issues)
5. Shared state between tests
6. Complex fixtures
7. Not testing errors
8. Low coverage

## Next Topic

→ [06_code_organization](../06_code_organization/README.md)

---

**Estimated Time:** 2-3 hours

**Prerequisites:** None (independent topic)

**Difficulty:** Beginner-Intermediate

**Required Packages:** pytest, pytest-asyncio, pytest-cov
