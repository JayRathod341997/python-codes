"""
============================================================
TOPIC: 03_parametrize.py
Real-world context: Testing mathematical and validation functions
with multiple inputs
============================================================
"""

import pytest


def calculate_discount(price, discount_percent):
    """Calculate price after discount."""
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be 0-100")
    return price * (1 - discount_percent / 100)

def is_valid_age(age):
    """Check if age is valid."""
    return 0 < age < 150

def get_shipping_cost(weight, destination):
    """Calculate shipping cost."""
    base_rates = {"local": 5, "national": 10, "international": 25}
    rate = base_rates.get(destination, 0)
    return rate + (weight * 2)


# ============================================================
# SECTION 1: Simple Parametrize
# ============================================================

@pytest.mark.parametrize("price,discount,expected", [
    (100, 10, 90),
    (100, 0, 100),
    (100, 50, 50),
    (200, 25, 150),
])
def test_calculate_discount(price, discount, expected):
    assert calculate_discount(price, discount) == expected


# ============================================================
# SECTION 2: Parametrize with Names
# ============================================================

@pytest.mark.parametrize("age,expected", [
    (5, True),
    (18, True),
    (65, True),
    (0, False),
    (-1, False),
    (150, False),
])
def test_is_valid_age(age, expected):
    assert is_valid_age(age) == expected


# ============================================================
# SECTION 3: Parametrize Multiple Arguments
# ============================================================

@pytest.mark.parametrize("weight,destination,expected", [
    (1, "local", 7),
    (5, "local", 15),
    (1, "national", 12),
    (5, "national", 20),
    (2, "international", 29),
])
def test_shipping_cost(weight, destination, expected):
    assert get_shipping_cost(weight, destination) == expected


# ============================================================
# SECTION 4: Indirect Parametrization
# ============================================================

@pytest.fixture
def user(request):
    """Fixture that uses parametrized values."""
    return {"name": request.param["name"], "age": request.param["age"]}

@pytest.mark.parametrize("user", [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
], indirect=True)
def test_user_names(user):
    assert user["name"] in ["Alice", "Bob", "Charlie"]
    assert user["age"] >= 25


# ============================================================
# SECTION 5: Exception Testing with Parametrize
# ============================================================

@pytest.mark.parametrize("discount", [-1, 101, 150])
def test_discount_out_of_range(discount):
    with pytest.raises(ValueError):
        calculate_discount(100, discount)


# ============================================================
# SECTION 6: Parametrize with IDs
# ============================================================

@pytest.mark.parametrize("price,tip_percent,expected", [
    (100, 15, 115),
    (50, 20, 60),
    (200, 10, 220),
], ids=["standard", "generous", "large_bill"])
def test_bill_with_tip(price, tip_percent, expected):
    result = price * (1 + tip_percent / 100)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
