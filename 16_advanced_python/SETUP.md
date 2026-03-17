# Advanced Python Module - Setup Guide

## Quick Start (5 Minutes)

### 1. Prerequisites
```bash
python --version  # Python 3.10+
pip --version
```

### 2. Install Dependencies
```bash
# Navigate to project
cd "d:\Jay Rathod\Tutorials\python-codes\16_advanced_python"

# Install all required packages
pip install pydantic pytest pytest-asyncio httpx dependency-injector line_profiler memory_profiler
```

### 3. Verify Installation
```bash
# Test imports
python -c "import pydantic; import pytest; import httpx; print('All packages installed!')"
```

### 4. Run First Script
```bash
# Test Topic 01
python 01_type_hints/01_basic_annotations.py

# Test Topic 02
python 02_context_managers/01_with_statement_basics.py

# Test Topic 03
python 03_async_await/01_coroutines_basics.py
```

---

## Full Installation

### Step 1: Clone/Navigate to Repository
```bash
cd "d:\Jay Rathod\Tutorials\python-codes\16_advanced_python"
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Upgrade pip
```bash
pip install --upgrade pip
```

### Step 4: Install All Dependencies
```bash
pip install \
  pydantic==2.5.0 \
  pytest==7.4.3 \
  pytest-asyncio==0.21.1 \
  httpx==0.25.0 \
  dependency-injector==4.41.0 \
  line_profiler==4.1.1 \
  memory_profiler==0.61.0
```

### Step 5: Create requirements.txt
```bash
pip freeze > requirements.txt
```

### Step 6: Verify Everything
```bash
python -c "
import pydantic
import pytest
import httpx
import asyncio
from dependency_injector import containers, providers
print('[OK] All packages imported successfully!')
"
```

---

## Running Tests

### Run All Tests
```bash
pytest -v
```

### Run Specific Topic Tests
```bash
pytest 01_type_hints/exercises/ -v
pytest 02_context_managers/exercises/ -v
pytest 05_testing_pytest/ -v
```

### Run with Coverage
```bash
pip install pytest-cov
pytest --cov=. --cov-report=html
```

---

## Running Individual Scripts

### Topic 01: Type Hints
```bash
python 01_type_hints/01_basic_annotations.py
python 01_type_hints/02_collections_typing.py
python 01_type_hints/03_generics_and_typevar.py
python 01_type_hints/04_protocols_and_abc.py
python 01_type_hints/05_advanced_patterns.py
python 01_type_hints/exercises/solutions/solution_01.py
python 01_type_hints/exercises/solutions/solution_02.py
```

### Topic 02: Context Managers
```bash
python 02_context_managers/01_with_statement_basics.py
python 02_context_managers/02_class_based_cm.py
python 02_context_managers/03_contextlib_module.py
python 02_context_managers/04_real_world_examples.py
python 02_context_managers/exercises/solutions/solution_01.py
```

### Topic 03: Async/Await
```bash
python 03_async_await/01_coroutines_basics.py
python 03_async_await/02_tasks_and_concurrency.py
python 03_async_await/03_async_context_managers.py
python 03_async_await/04_real_world_httpx.py
python 03_async_await/exercises/solutions/solution_01.py
python 03_async_await/exercises/solutions/solution_02.py
```

### Topic 04: Pydantic v2
```bash
python 04_data_validation_pydantic/01_basic_models.py
python 04_data_validation_pydantic/02_validation_and_errors.py
python 04_data_validation_pydantic/03_nested_models_config.py
python 04_data_validation_pydantic/04_settings.py
python 04_data_validation_pydantic/exercises/solutions/solution_01.py
python 04_data_validation_pydantic/exercises/solutions/solution_02.py
```

### Topic 05: Pytest
```bash
pytest 05_testing_pytest/ -v
python 05_testing_pytest/01_basics.py
python 05_testing_pytest/02_fixtures.py
python 05_testing_pytest/03_parametrize.py
python 05_testing_pytest/04_mocking.py
```

---

## Troubleshooting

### ImportError: No module named 'pydantic'
```bash
pip install pydantic
```

### ImportError: No module named 'pytest'
```bash
pip install pytest pytest-asyncio
```

### ImportError: No module named 'httpx'
```bash
pip install httpx
```

### Async Runtime Error
```bash
# Make sure Python 3.10+
python --version

# Reinstall asyncio support
pip install pytest-asyncio
```

### Permission Denied (macOS/Linux)
```bash
chmod +x *.py
```

---

## IDE Setup

### VSCode
```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.linting.mypyEnabled": true,
  "[python]": {
    "editor.defaultFormatter": "ms-python.python",
    "editor.formatOnSave": true
  }
}
```

### PyCharm
1. File → Settings → Project → Python Interpreter
2. Click gear → Add
3. Select "Existing Environment"
4. Navigate to venv/bin/python

---

## Verify All Topics Work

```bash
#!/bin/bash
echo "Testing all topics..."

echo "[1/8] Testing Type Hints..."
python 01_type_hints/01_basic_annotations.py > /dev/null && echo "✓ Pass" || echo "✗ Fail"

echo "[2/8] Testing Context Managers..."
python 02_context_managers/01_with_statement_basics.py > /dev/null && echo "✓ Pass" || echo "✗ Fail"

echo "[3/8] Testing Async/Await..."
python 03_async_await/01_coroutines_basics.py > /dev/null && echo "✓ Pass" || echo "✗ Fail"

echo "[4/8] Testing Pydantic..."
python 04_data_validation_pydantic/01_basic_models.py > /dev/null && echo "✓ Pass" || echo "✗ Fail"

echo "[5/8] Testing Pytest..."
pytest 05_testing_pytest/ -q && echo "✓ Pass" || echo "✗ Fail"

echo "Done!"
```

---

## Next Steps After Setup

1. **Read the main README.md** - Understand module structure
2. **Start with Topic 01** - Type Hints foundation
3. **Progress through topics** - Follow recommended learning path
4. **Solve exercises** - Practice each concept
5. **Review solutions** - Compare approaches
6. **Apply to projects** - Use patterns in real code

---

## Package Versions (Recommended)

| Package | Version | Purpose |
|---------|---------|---------|
| Python | 3.10+ | Core language |
| pydantic | 2.5.0 | Data validation |
| pytest | 7.4.3 | Testing framework |
| pytest-asyncio | 0.21.1 | Async test support |
| httpx | 0.25.0 | HTTP client (async) |
| dependency-injector | 4.41.0 | DI container |
| line_profiler | 4.1.1 | Performance profiling |
| memory_profiler | 0.61.0 | Memory profiling |

---

## Files Summary

| File | Purpose |
|------|---------|
| SETUP.md | This file - installation guide |
| README.md | Module overview and learning path |
| 01_type_hints/ | Type hints and static typing |
| 02_context_managers/ | Resource management |
| 03_async_await/ | Async programming |
| 04_data_validation_pydantic/ | Data validation |
| 05_testing_pytest/ | Testing framework |
| 06_code_organization/ | Design patterns |
| 07_performance_tuning/ | Performance optimization |
| 08_dependency_injection/ | Dependency injection |

---

## Getting Help

- **Read notes.md** in each topic for theory
- **Check interview.md** for Q&A explanations
- **Run concept scripts** to see examples
- **Review solutions** for implementation details
- **Modify code** and experiment with changes

---

**Setup complete! Ready to learn advanced Python! 🚀**
