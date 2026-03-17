"""
============================================================
TOPIC: 04_mocking.py
Real-world context: Testing code that calls external APIs
and services using mocks
============================================================
"""

import pytest
from unittest.mock import Mock, patch, MagicMock


class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_user(self, user_id):
        # In real code, this would make HTTP request
        pass

    def create_user(self, user_data):
        # In real code, this would make HTTP request
        pass

def fetch_user_from_api(api, user_id):
    """Function that calls API."""
    user = api.get_user(user_id)
    return user

def process_user_data(api, user_id):
    """Complex function using API."""
    user = api.get_user(user_id)
    if user:
        user["processed"] = True
        return user
    return None


# ============================================================
# SECTION 1: Basic Mocking
# ============================================================

def test_fetch_user_with_mock():
    mock_api = Mock()
    mock_api.get_user.return_value = {"id": 1, "name": "Alice"}

    user = fetch_user_from_api(mock_api, 1)

    assert user["name"] == "Alice"
    mock_api.get_user.assert_called_once_with(1)

def test_fetch_user_not_found():
    mock_api = Mock()
    mock_api.get_user.return_value = None

    user = fetch_user_from_api(mock_api, 999)

    assert user is None


# ============================================================
# SECTION 2: Mock Assertions
# ============================================================

def test_api_called_with_correct_arguments():
    mock_api = Mock()
    mock_api.get_user.return_value = {"id": 1}

    fetch_user_from_api(mock_api, 123)

    # Verify how mock was called
    mock_api.get_user.assert_called_once_with(123)
    assert mock_api.get_user.call_count == 1

def test_api_called_multiple_times():
    mock_api = Mock()
    mock_api.get_user.return_value = {"id": 1}

    fetch_user_from_api(mock_api, 1)
    fetch_user_from_api(mock_api, 2)
    fetch_user_from_api(mock_api, 3)

    assert mock_api.get_user.call_count == 3


# ============================================================
# SECTION 3: Mocking with Side Effects
# ============================================================

def test_api_raises_exception():
    mock_api = Mock()
    mock_api.get_user.side_effect = Exception("API Error")

    with pytest.raises(Exception):
        fetch_user_from_api(mock_api, 1)

def test_multiple_return_values():
    mock_api = Mock()
    # Return different values for different calls
    mock_api.get_user.side_effect = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        Exception("API Error")
    ]

    user1 = fetch_user_from_api(mock_api, 1)
    user2 = fetch_user_from_api(mock_api, 2)

    assert user1["name"] == "Alice"
    assert user2["name"] == "Bob"

    with pytest.raises(Exception):
        fetch_user_from_api(mock_api, 3)


# ============================================================
# SECTION 4: Using patch Decorator
# ============================================================

@patch('requests.get')
def test_with_patch_decorator(mock_get):
    mock_get.return_value.json.return_value = {"data": "value"}

    # Code using requests.get would work here
    assert mock_get is not None


# ============================================================
# SECTION 5: Complex Mock Scenarios
# ============================================================

def test_process_user_data_with_mock():
    mock_api = Mock()
    mock_api.get_user.return_value = {"id": 1, "name": "Alice"}

    result = process_user_data(mock_api, 1)

    assert result["processed"] is True
    assert result["name"] == "Alice"
    mock_api.get_user.assert_called_once_with(1)

def test_mock_attributes():
    mock_api = Mock()
    mock_api.host = "api.example.com"
    mock_api.port = 443

    assert mock_api.host == "api.example.com"
    assert mock_api.port == 443


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
