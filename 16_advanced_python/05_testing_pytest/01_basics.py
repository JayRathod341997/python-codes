"""
============================================================
TOPIC: 01_basics.py
Real-world context: Testing e-commerce functions
============================================================
"""

import pytest

def add_numbers(a, b):
    return a + b

def get_user_email(users_dict, user_id):
    return users_dict.get(user_id, {}).get("email")

def validate_email(email):
    return "@" in email and "." in email.split("@")[1]

def process_order(order):
    if order["quantity"] <= 0:
        raise ValueError("Quantity must be positive")
    if order["price"] <= 0:
        raise ValueError("Price must be positive")
    return {"total": order["quantity"] * order["price"]}


# ============================================================
# SECTION 1: Basic Assertions
# ============================================================

def test_addition():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_string_operations():
    text = "hello"
    assert text.upper() == "HELLO"
    assert len(text) == 5
    assert "h" in text

def test_list_operations():
    lst = [1, 2, 3, 4, 5]
    assert len(lst) == 5
    assert 3 in lst
    assert lst[0] == 1


# ============================================================
# SECTION 2: Testing with Dictionaries
# ============================================================

def test_get_user_email():
    users = {
        1: {"name": "Alice", "email": "alice@example.com"},
        2: {"name": "Bob", "email": "bob@example.com"}
    }

    assert get_user_email(users, 1) == "alice@example.com"
    assert get_user_email(users, 2) == "bob@example.com"
    assert get_user_email(users, 999) is None

def test_email_validation():
    assert validate_email("alice@example.com") is True
    assert validate_email("bob@test.co.uk") is True
    assert validate_email("invalid_email") is False
    assert validate_email("no_at_sign.com") is False


# ============================================================
# SECTION 3: Exception Testing
# ============================================================

def test_process_order_with_invalid_quantity():
    with pytest.raises(ValueError):
        process_order({"quantity": 0, "price": 10})

def test_process_order_with_invalid_price():
    with pytest.raises(ValueError):
        process_order({"quantity": 5, "price": -10})

def test_process_order_error_message():
    with pytest.raises(ValueError, match="Quantity must be positive"):
        process_order({"quantity": -1, "price": 10})

def test_process_order_success():
    result = process_order({"quantity": 5, "price": 10})
    assert result["total"] == 50


# ============================================================
# SECTION 4: Multiple Assertions
# ============================================================

def test_user_dictionary_structure():
    user = {"id": 1, "name": "Alice", "email": "alice@example.com"}

    assert user["id"] == 1
    assert user["name"] == "Alice"
    assert user["email"] == "alice@example.com"
    assert len(user) == 3

def test_order_calculation():
    order = {"items": 3, "unit_price": 25}
    total = order["items"] * order["unit_price"]

    assert total == 75
    assert total > 0
    assert isinstance(total, int)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
