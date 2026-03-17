"""
============================================================
EXERCISE 01 — Pytest: Testing a Calculator Module
============================================================
Problem: Write comprehensive tests for a calculator.

Requirements:
  1. Test basic operations (add, subtract, multiply, divide)
  2. Use @pytest.mark.parametrize for multiple inputs
  3. Test edge cases (zero, negative numbers)
  4. Test exception handling (division by zero)
  5. At least 8 test cases

Hints: Use assert for equality checks
       Use pytest.raises() for exceptions
       Use @pytest.mark.parametrize for multiple cases
============================================================
"""

import pytest


class Calculator:
    """Simple calculator for testing."""
    # TODO: Implement add(), subtract(), multiply(), divide()
    pass


# TODO: Write test functions:
# 1. test_add_positive_numbers
# 2. test_add_negative_numbers
# 3. test_subtract
# 4. test_multiply
# 5. test_divide_positive
# 6. test_divide_by_zero (exception)
# 7. test_with_parametrize (multiple cases)
# 8. test_edge_cases


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
