# Interview Q&A — Testing with Pytest

## Q1. What's the difference between fixtures and setup/teardown methods?

**A:** Fixtures are Pytest's way of managing setup/teardown. They're functions decorated with @pytest.fixture, reusable across tests, and injectable as parameters. They're cleaner and more flexible than unittest's setUp/tearDown methods.

```python
# Pytest fixture (preferred)
@pytest.fixture
def database():
    db = create_db()
    yield db
    db.close()

def test_query(database):
    result = database.query()
    assert result is not None
```

---

## Q2. How do I parametrize tests for multiple inputs?

**A:** Use @pytest.mark.parametrize to run the same test with different inputs. It creates separate test cases for each input tuple.

```python
@pytest.mark.parametrize("input,expected", [
    (2, 4), (3, 9), (4, 16)
])
def test_square(input, expected):
    assert input ** 2 == expected
# Creates 3 tests: test_square[2-4], test_square[3-9], test_square[4-16]
```

---

## Q3. How do I mock external API calls in tests?

**A:** Use `unittest.mock.patch` to replace external dependencies. Mock the function/class, set return values, and verify calls.

```python
from unittest.mock import patch

@patch('module.requests.get')
def test_fetch_user(mock_get):
    mock_get.return_value.json.return_value = {"id": 1, "name": "Alice"}

    user = fetch_user(1)

    assert user["name"] == "Alice"
    mock_get.assert_called_once()
```

---

## Q4. What's the difference between @pytest.mark.skip and @pytest.mark.xfail?

**A:** `skip` completely skips the test (not run). `xfail` (expected fail) runs the test but expects it to fail; if it passes, Pytest reports it as "XPASS" (unexpectedly passed).

```python
@pytest.mark.skip(reason="Not ready")
def test_not_ready():
    pass  # Won't run

@pytest.mark.xfail(reason="Known bug")
def test_known_bug():
    assert False  # Runs, expected to fail
```

---

## Q5. How do I test exceptions?

**A:** Use `pytest.raises()` to assert that an exception is raised. You can also check the exception message.

```python
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_exception_message():
    with pytest.raises(ValueError, match="invalid"):
        raise ValueError("invalid input")
```

---

## Q6. What's a fixture scope, and why does it matter?

**A:** Fixture scope controls when fixtures are created/destroyed: "function" (fresh per test), "class" (per class), "module" (per module), "session" (once per test run). Affects performance and isolation.

```python
@pytest.fixture(scope="session")
def expensive_db():
    # Created once, reused across all tests
    return create_database()

@pytest.fixture(scope="function")
def fresh_data():
    # Created fresh for each test
    return []
```

---

## Q7. How do I test async code with Pytest?

**A:** Use `@pytest.mark.asyncio` and `pytest-asyncio` plugin. Write async test functions and await async code.

```python
import pytest

@pytest.mark.asyncio
async def test_async_function():
    result = await fetch_data()
    assert result is not None
```

---

## Q8. How do I run only specific tests?

**A:** Use pytest command-line options: `-k` for keyword matching, `-m` for markers, or specify files/directories.

```bash
# Run tests matching pattern
pytest -k "test_user"

# Run tests with specific marker
pytest -m "slow"

# Run single file
pytest test_users.py

# Run single test
pytest test_file.py::test_function
```

---

## Q9. How do I capture print statements in tests?

**A:** Pytest automatically captures stdout. Use `capsys` fixture to access captured output.

```python
def test_output(capsys):
    print("Hello")
    captured = capsys.readouterr()
    assert "Hello" in captured.out
```

---

## Q10. What's conftest.py and how do I use it?

**A:** conftest.py is a special file where you define fixtures and hooks shared across multiple test files. Pytest auto-discovers it.

```python
# conftest.py
import pytest

@pytest.fixture
def database():
    db = create_db()
    yield db
    db.close()

# Now all tests in this directory can use 'database' fixture
```

---

## Q11. How do I measure test coverage?

**A:** Use pytest-cov plugin: `pip install pytest-cov` then `pytest --cov=module_name`.

```bash
# Run tests with coverage report
pytest --cov=myapp --cov-report=html

# Shows percentage of code covered by tests
```

---

## Q12. How do I organize test files?

**A:** Use directory structure matching your code. Name test files `test_*.py` or `*_test.py`. Pytest auto-discovers them.

```
project/
├── myapp/
│   ├── user.py
│   └── api.py
├── tests/
│   ├── conftest.py
│   ├── test_user.py
│   └── test_api.py
```
