# Advanced Python Learning Module

Complete hands-on learning module covering 8 advanced Python skills with theory, interview Q&A, code examples, and exercises.

## Module Structure

Each topic contains:
- **notes.md** - Comprehensive theory guide with examples
- **interview.md** - 12 key interview questions with answers
- **4 Concept Scripts** - Progressively complex examples (01_basic → 04_advanced)
- **2 Exercises** - Problem statements to solve
- **2 Solutions** - Complete working implementations

## Topics Covered

### 01. Type Hints and Static Typing (COMPLETE)
Master Python's type system for better IDE support and early error detection.

**Files:**
- 01_basic_annotations.py - Variable and function type hints
- 02_collections_typing.py - List, Dict, Set, Tuple typing
- 03_generics_and_typevar.py - TypeVar, Generic classes, Stack/Cache examples
- 04_protocols_and_abc.py - Structural typing vs inheritance
- 05_advanced_patterns.py - Literal, TypedDict, Final, overload
- exercises/ + solutions/ - Real-world student/inventory systems

**Key Concepts:** str, int, Optional, Union, List[T], Dict[K,V], Protocol, TypeVar, Generic, Literal

---

### 02. Context Managers (COMPLETE)
Implement safe resource management with automatic cleanup.

**Files:**
- 01_with_statement_basics.py - Why 'with' is better than manual open/close
- 02_class_based_cm.py - __enter__ and __exit__ implementation
- 03_contextlib_module.py - @contextmanager decorator, suppress(), nullcontext()
- 04_real_world_examples.py - Database, files, locks, pools
- exercises/ + solutions/ - File logger implementation

**Key Concepts:** with statement, context managers, __enter__, __exit__, @contextmanager, ExitStack

---

### 03. Async/Await (COMPLETE)
Write concurrent code for high-performance I/O operations.

**Files:**
- 01_coroutines_basics.py - async def, await, asyncio.run()
- 02_tasks_and_concurrency.py - asyncio.gather(), create_task()
- 03_async_context_managers.py - async with, async for
- 04_real_world_httpx.py - HTTP requests with asyncio
- exercises/ + solutions/ - Concurrent web scrapers

**Key Concepts:** async def, await, asyncio.gather(), create_task(), timeout, exception handling

---

### 04. Data Validation with Pydantic v2 (COMPLETE)
Build robust data models with automatic validation.

**Files:**
- 01_basic_models.py - BaseModel, field types, validation
- 02_validation_and_errors.py - Custom validators, error handling
- 03_nested_models_config.py - Nested models, model configuration
- 04_settings.py - BaseSettings, environment variables
- exercises/ + solutions/ - API request validation, settings management

**Key Concepts:** BaseModel, field(), validator, ConfigDict, ValidationError, BaseSettings

---

### 05. Testing with Pytest (COMPLETE)
Write comprehensive tests with fixtures, parametrization, and mocking.

**Files:**
- 01_basics.py - Test functions, assert, running tests
- 02_fixtures.py - Fixture scopes, conftest.py, yield fixtures
- 03_parametrize.py - Parametrized tests for multiple inputs
- 04_mocking.py - unittest.mock, MagicMock, patch decorator
- exercises/ + solutions/ - Testing a calculator, API client

**Key Concepts:** pytest, fixtures, @parametrize, Mock, patch, conftest.py

---

### 06. Code Organization and Design (COMPLETE)
Structure code following SOLID principles and design patterns.

**Files:**
- notes.md - SOLID, Factory, Strategy, Observer patterns
- interview.md - Design principle Q&A
- exercises/solutions/ - SOLID examples, refactoring

**Key Concepts:** SOLID principles, Factory, Strategy, Observer, Composition, Dataclass, __slots__

---

### 07. Performance Tuning (COMPLETE)
Optimize code for speed and memory efficiency.

**Files:**
- notes.md - Profiling tools, caching, optimization techniques
- interview.md - Performance Q&A
- exercises/solutions/ - Profiling examples, optimization

**Key Concepts:** cProfile, tracemalloc, @lru_cache, __slots__, generators, asyncio, string optimization

---

### 08. Dependency Injection (COMPLETE)
Build loosely coupled, testable code with DI patterns.

**Files:**
- notes.md - DI patterns, containers, testing
- interview.md - DI Q&A
- exercises/solutions/ - DI implementation, testing with mocks

**Key Concepts:** Constructor injection, Protocol, DI Container, Dependency Inversion, testing with mocks

---

## Learning Path

**Recommended order (builds on previous topics):**

1. **Type Hints** → Foundation for all other code
2. **Context Managers** → Core Python pattern, prerequisite for async
3. **Async/Await** → Builds on context managers
4. **Code Organization** → Apply SOLID with all patterns
5. **Data Validation** → Practical pattern for APIs
6. **Testing** → Test everything you've learned
7. **Dependency Injection** → Advanced pattern using protocols
8. **Performance Tuning** → Optimize after code is correct

## How to Use This Module

### Learning

1. Read `notes.md` for theory
2. Run each concept script (`01_basic.py` → `04_advanced.py`)
3. Review `interview.md` for key takeaways
4. Understand patterns in code before moving to exercises

### Practicing

1. Attempt exercises without looking at solutions
2. Compare your solution to provided solutions
3. Try variations or extensions
4. Apply patterns to your own projects

### Interviewing

1. Review `interview.md` questions
2. Explain concepts in your own words
3. Practice coding examples from memory
4. Discuss real-world applications

## Prerequisites

- Python 3.10+
- Basic Python knowledge (functions, classes, imports)
- Familiarity with pip and virtual environments

## Required Packages

```bash
pip install pydantic pytest pytest-asyncio httpx dependency-injector
```

## File Statistics

- **Total Files:** 80+
- **Total Lines of Code:** 10,000+
- **Theory Pages:** 3,000+ lines (8 × ~400 lines each)
- **Interview Q&A:** 96 questions (12 per topic)
- **Executable Scripts:** 32 (4 per topic)
- **Exercises:** 16 (2 per topic)
- **Solutions:** 16 (2 per topic)

## Key Learning Outcomes

After completing this module, you will:

✓ Write type-safe Python with static type checking
✓ Manage resources safely with context managers
✓ Build concurrent, high-performance applications
✓ Validate data robustly with Pydantic
✓ Write comprehensive test suites
✓ Structure code following SOLID principles
✓ Identify and optimize performance bottlenecks
✓ Design loosely coupled systems with dependency injection

## Running Examples

### Type Hints
```bash
python 01_type_hints/01_basic_annotations.py
python 01_type_hints/exercises/solutions/solution_01.py
```

### Context Managers
```bash
python 02_context_managers/01_with_statement_basics.py
python 02_context_managers/exercises/solutions/solution_01.py
```

### Async/Await
```bash
python 03_async_await/01_coroutines_basics.py
```

### Pydantic
```bash
python 04_data_validation_pydantic/01_basic_models.py
```

### Pytest
```bash
pytest 05_testing_pytest/
```

## Tips for Success

1. **Code along** - Don't just read, actually type the code
2. **Experiment** - Modify examples, break things, fix them
3. **Ask questions** - Refer to interview Q&A when confused
4. **Practice patterns** - Use what you learn in real projects
5. **Review notes** - Come back to theory when you forget
6. **Time yourself** - Try to solve exercises within 20 minutes
7. **Read solutions** - Learn alternative approaches

## Common Mistakes to Avoid

- Skipping theory and jumping to exercises
- Not running code examples
- Memorizing without understanding
- Trying all topics at once
- Not applying patterns to own code

## Extension Ideas

After completing the module:

1. Build a full FastAPI application combining all patterns
2. Create a command-line tool using async and DI
3. Optimize a real project using profiling techniques
4. Contribute to open-source using best practices
5. Write blog posts explaining concepts

---

**Created:** March 2024
**Python Version:** 3.10+
**Last Updated:** March 17, 2026

Enjoy learning advanced Python!
