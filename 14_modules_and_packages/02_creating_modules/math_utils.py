# ─────────────────────────────────────────────
# math_utils.py  — a reusable utility module
# ─────────────────────────────────────────────
# This file is imported by notes.py and exercise.py
# to demonstrate how to CREATE and USE a module.

"""Math utility functions for financial and scientific calculations."""

PI = 3.141592653589793

def circle_area(radius):
    """Return the area of a circle given its radius."""
    return PI * radius ** 2

def compound_interest(principal, rate, years, n=12):
    """
    Return amount after compound interest.

    Args:
        principal (float): Initial investment (₹).
        rate      (float): Annual interest rate in % (e.g. 8.5).
        years     (int)  : Investment duration in years.
        n         (int)  : Compounding frequency per year (default 12 = monthly).

    Returns:
        float: Final amount rounded to 2 decimal places.
    """
    r = rate / 100
    amount = principal * (1 + r / n) ** (n * years)
    return round(amount, 2)

def percentage_change(old, new):
    """Return percentage change from old to new value."""
    if old == 0:
        raise ZeroDivisionError("old value cannot be zero")
    return round((new - old) / old * 100, 2)

def clamp(value, minimum, maximum):
    """Clamp value between minimum and maximum."""
    return max(minimum, min(value, maximum))

# Module-level code — runs when the module is imported
_version = "1.0.0"
