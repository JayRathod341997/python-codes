# Python Learning Repository — 13 Real-World Projects

All 13 projects have been created with complete structure: **storyline.md**, **solution.py**, **exercise.py**, and **exercises/solutions/solution_ex.py**.

## Project Overview

### Beginner Level (01-03)

1. **01_finance_expense_tracker** — Month-End Budget Report
   - Concepts: Variables, operators, if/elif/else, f-string formatting
   - Domain: Personal Finance
   - Difficulty: Beginner

2. **02_health_bmi_vitals_checker** — Patient Vitals Screening
   - Concepts: Arithmetic, match/case, nested if/elif, boolean logic
   - Domain: Healthcare
   - Difficulty: Beginner/Intermediate

3. **03_retail_invoice_calculator** — GST Invoice with Discounts
   - Concepts: While loop, if/elif, ternary operator, f-string alignment
   - Domain: Retail/E-commerce
   - Difficulty: Beginner/Intermediate

### Intermediate Level (04-06)

4. **04_hr_employee_directory** — Employee Lookup & Salary Analysis
   - Concepts: List of dicts, functions, for loops, sorted(), enumerate(), max/min
   - Domain: Human Resources
   - Difficulty: Intermediate
   - Note: Includes comment about refactoring in Project 10

5. **05_it_log_analyzer** — DevOps Log Parsing
   - Concepts: String methods, tuples, sets, dicts, sorted+lambda
   - Domain: DevOps/IT
   - Difficulty: Intermediate
   - Note: Includes comment about refactoring in Project 10

6. **06_retail_inventory_oop** — Supermarket Inventory Management
   - Concepts: Classes, @property with setter, @classmethod, two-class design
   - Domain: Retail
   - Difficulty: Intermediate

### Intermediate/Advanced Level (07-09)

7. **07_finance_bank_oop** — Banking with Inheritance
   - Concepts: Inheritance, super().__init__(), method overriding, polymorphism
   - Domain: Banking/Finance
   - Difficulty: Intermediate

8. **08_hr_payroll_files** — Payroll CSV to JSON Processing
   - Concepts: CSV module, JSON module, pathlib, with statement, exception handling
   - Domain: HR/Payroll
   - Difficulty: Intermediate

9. **09_it_config_manager** — Application Configuration with JSON
   - Concepts: JSON I/O, OOP, dot-notation access, datetime logging
   - Domain: DevOps/Cloud
   - Difficulty: Intermediate

### Advanced Level (10-13)

10. **10_retail_sales_comprehensions** — Sales Analysis: Loops vs Comprehensions
    - Concepts: List/dict/set comprehensions, generator expressions, nested comprehensions
    - Domain: Retail/Analytics
    - Difficulty: Intermediate/Advanced
    - REFACTOR edition: Act 1 (traditional for-loops) vs Act 2 (Pythonic comprehensions)
    - References Projects 04 & 05

11. **11_finance_risk_pipeline_generators** — Risk Screening Pipeline
    - Concepts: Generator functions, yield, generator chaining, itertools, lazy evaluation
    - Domain: FinTech/AML
    - Difficulty: Advanced
    - Memory efficiency comparison included

12. **12_it_api_monitor_decorators** — API Endpoint Monitoring
    - Concepts: Decorators, @functools.wraps, decorator factories, stacking
    - Domain: DevOps/Microservices
    - Difficulty: Advanced
    - Includes: @timer, @log_call, @retry, @cache_result

13. **13_health_async_data_fetcher** — Concurrent Patient Data Aggregation
    - Concepts: async/await, asyncio.gather, dataclasses, type hints
    - Domain: Healthcare/Telemedicine
    - Difficulty: Advanced
    - Concurrency vs serial comparison included

## Project Structure (per project)

Each project directory contains:

```
0X_project_name/
├── storyline.md                     # Real-world context & motivation
├── solution.py                      # Complete working solution
├── exercise.py                      # 3 exercises with hints
└── exercises/solutions/
    └── solution_ex.py              # Full solutions to exercises
```

## Key Features

- **Real-world domains**: Finance, Healthcare, Retail, HR, DevOps, E-commerce
- **Progressive difficulty**: Beginner → Advanced
- **Heavy inline comments**: Explaining WHY, not just WHAT
- **Consistent code style**: Matching existing project standards
- **Section dividers**: `# ── Section N ──` (beginner), `# ══ SECTION N: Title ══` (advanced)
- **Concept callouts**: `# ── CONCEPT: X ────` for new features
- **Rupee symbol**: ₹ in all financial outputs
- **F-string formatting**: Alignment and thousands separators
- **No external libraries**: Standard library only
- **No `if __name__ == "__main__"`**: Direct execution
- **Production notes**: "In production, you'd use..." comments
- **Comprehensive exercises**: 3 exercises per project with expected outputs

## How to Use

1. Read the **storyline.md** for context and domain understanding
2. Run **solution.py** to see the complete solution in action
3. Study the code structure and patterns
4. Attempt the 3 exercises in **exercise.py** without looking at solutions
5. Compare your approach with **exercises/solutions/solution_ex.py**
6. Observe the progression from procedural (Projects 01-06) to advanced patterns (Projects 07-13)

## Learning Path

- **Projects 01-03**: Core Python fundamentals
- **Projects 04-05**: Loops, functions, and data structures (for-loop heavy)
- **Projects 06-07**: Object-Oriented Programming basics
- **Projects 08-09**: File I/O and configuration management
- **Project 10**: Refactoring 04-05 using comprehensions (Pythonic alternative)
- **Projects 11-13**: Advanced patterns (generators, decorators, async)

## Notes

- Project 04 and 05 include comments about refactoring in Project 10
- Project 10 explicitly contrasts "Act 1: Loops" with "Act 2: Comprehensions"
- All projects use hardcoded or simulated data (no real databases)
- Focus is on Python language features, not production infrastructure
- Code is optimized for learning clarity, not performance

Total: **52 files** across **13 projects**
