# Testing with Pytest: Building Reliable Test Suites

## What is it?

Pytest is Python's most popular testing framework. It simplifies test writing with simple function-based tests, powerful fixtures for setup/teardown, parametrization for multiple inputs, and excellent reporting. It's the industry standard for Python testing.

```python
import pytest

def test_addition():
    assert 2 + 2 == 4

def test_string_contains():
    assert "hello" in "hello world"

# Run with: pytest test_file.py
```

---

## Why Use Pytest?

| Benefit | Example |
|---------|---------|
| **Simple syntax** | Use plain assert instead of self.assertEqual |
| **Powerful fixtures** | Reusable setup/teardown code |
| **Parametrization** | Test multiple inputs with one function |
| **Plugins** | Extend functionality (coverage, mocking, etc.) |
| **Clear output** | Shows exactly what failed and why |
| **Marks** | Tag and run specific test subsets |
| **Async support** | Test async code with pytest-asyncio |
| **Mocking** | pytest-mock integrates unittest.mock |

---

## Core Concepts

### 1. Basic Test Functions

```python
def test_addition():
    result = 2 + 2
    assert result == 4

def test_string_upper():
    text = "hello"
    assert text.upper() == "HELLO"

def test_list_append():
    lst = [1, 2, 3]
    lst.append(4)
    assert lst == [1, 2, 3, 4]
    assert len(lst) == 4
```

### 2. Fixtures (Setup and Teardown)

```python
import pytest

@pytest.fixture
def sample_database():
    # Setup
    db = {"users": []}
    print("Creating test database")

    yield db  # Test uses this value

    # Teardown
    db.clear()
    print("Cleaning up test database")

def test_add_user(sample_database):
    sample_database["users"].append({"id": 1, "name": "Alice"})
    assert len(sample_database["users"]) == 1
```

### 3. Parametrization (Test Multiple Inputs)

```python
import pytest

@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
    (-2, 4),
])
def test_square(input, expected):
    assert input ** 2 == expected

# This creates 4 separate tests automatically
```

### 4. Markers (Tagging Tests)

```python
import pytest

@pytest.mark.slow
def test_slow_operation():
    time.sleep(10)
    assert True

@pytest.mark.skip(reason="Not implemented yet")
def test_not_ready():
    assert False

@pytest.mark.xfail
def test_known_bug():
    assert False  # Expected to fail

# Run only fast tests: pytest -m "not slow"
```

### 5. Exception Testing

```python
import pytest

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_value_error_message():
    with pytest.raises(ValueError, match="invalid value"):
        raise ValueError("invalid value provided")
```

### 6. Mocking

```python
from unittest.mock import Mock, patch

def test_with_mock():
    mock_api = Mock()
    mock_api.get_user.return_value = {"id": 1, "name": "Alice"}

    result = mock_api.get_user(1)

    assert result == {"id": 1, "name": "Alice"}
    mock_api.get_user.assert_called_once_with(1)

def test_with_patch():
    with patch('module.function', return_value=42):
        import module
        result = module.function()
        assert result == 42
```

### 7. Fixtures with Scope

```python
import pytest

@pytest.fixture(scope="module")
def shared_resource():
    # Created once per module
    return "shared data"

@pytest.fixture(scope="function")
def fresh_resource():
    # Created fresh for each test (default)
    return "fresh data"

@pytest.fixture(scope="session")
def expensive_resource():
    # Created once per test session
    return "expensive data"
```

### 8. Testing Async Code

```python
import pytest
import asyncio

@pytest.mark.asyncio
async def test_async_function():
    result = await some_async_function()
    assert result == expected_value
```

---

## Best Practices

1. **Use descriptive test names**
   ```python
   # Good
   def test_user_cannot_register_with_empty_email():
       pass

   # Bad
   def test_user():
       pass
   ```

2. **One assertion per test (when possible)**
   ```python
   # Better: Each test is focused
   def test_user_is_created_with_name():
       user = User(name="Alice")
       assert user.name == "Alice"

   def test_user_has_email():
       user = User(email="alice@example.com")
       assert user.email == "alice@example.com"
   ```

3. **Use fixtures for common setup**
   ```python
   @pytest.fixture
   def user():
       return User(name="Alice", email="alice@example.com")

   def test_user_name(user):
       assert user.name == "Alice"
   ```

4. **Parametrize for multiple inputs**
   ```python
   @pytest.mark.parametrize("value,expected", [(1, True), (0, False)])
   def test_is_valid(value, expected):
       assert is_valid(value) == expected
   ```

5. **Mock external dependencies**
   ```python
   @patch('requests.get')
   def test_api_call(mock_get):
       mock_get.return_value.json.return_value = {"data": "value"}
       result = fetch_api()
       assert result == {"data": "value"}
   ```

---

## Summary

Pytest provides:
- Simple assert-based syntax
- Powerful fixtures for setup/teardown
- Parametrization for multiple test cases
- Clear failure messages
- Markers for test organization
- Mocking capabilities
- Async test support
- Plugin ecosystem

Master pytest to write fast, reliable tests and deploy with confidence.
