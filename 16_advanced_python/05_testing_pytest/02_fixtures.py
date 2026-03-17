"""
============================================================
TOPIC: 02_fixtures.py
Real-world context: Testing database operations with fixtures
============================================================
"""

import pytest


class SimpleDatabase:
    def __init__(self):
        self.data = {}

    def add_user(self, user_id, user_data):
        self.data[user_id] = user_data

    def get_user(self, user_id):
        return self.data.get(user_id)

    def delete_user(self, user_id):
        if user_id in self.data:
            del self.data[user_id]
            return True
        return False

    def clear(self):
        self.data.clear()


# ============================================================
# SECTION 1: Basic Fixture
# ============================================================

@pytest.fixture
def database():
    """Fixture that creates and tears down database."""
    db = SimpleDatabase()
    print("Setup: Creating database")

    yield db  # Test uses this value

    print("Teardown: Clearing database")
    db.clear()


def test_add_user(database):
    database.add_user(1, {"name": "Alice", "email": "alice@example.com"})
    assert database.get_user(1) is not None

def test_get_nonexistent_user(database):
    assert database.get_user(999) is None

def test_delete_user(database):
    database.add_user(1, {"name": "Alice"})
    deleted = database.delete_user(1)
    assert deleted is True
    assert database.get_user(1) is None


# ============================================================
# SECTION 2: Fixture with Initial Data
# ============================================================

@pytest.fixture
def populated_database():
    """Fixture that creates database with sample data."""
    db = SimpleDatabase()
    db.add_user(1, {"name": "Alice", "email": "alice@example.com"})
    db.add_user(2, {"name": "Bob", "email": "bob@example.com"})
    db.add_user(3, {"name": "Charlie", "email": "charlie@example.com"})

    yield db

    db.clear()


def test_database_has_three_users(populated_database):
    assert populated_database.get_user(1)["name"] == "Alice"
    assert populated_database.get_user(2)["name"] == "Bob"
    assert populated_database.get_user(3)["name"] == "Charlie"

def test_database_user_count(populated_database):
    users = [populated_database.get_user(i) for i in range(1, 4)]
    assert len(users) == 3


# ============================================================
# SECTION 3: Fixture Dependencies
# ============================================================

@pytest.fixture
def user_data():
    """Basic user data."""
    return {"name": "TestUser", "email": "test@example.com"}

@pytest.fixture
def database_with_user(database, user_data):
    """Database fixture that depends on user_data."""
    database.add_user(1, user_data)
    return database

def test_user_exists_in_database(database_with_user):
    assert database_with_user.get_user(1) is not None

def test_user_has_correct_name(database_with_user, user_data):
    retrieved_user = database_with_user.get_user(1)
    assert retrieved_user["name"] == user_data["name"]


# ============================================================
# SECTION 4: Fixture Scopes
# ============================================================

@pytest.fixture(scope="module")
def shared_database():
    """Database shared across all tests in module."""
    db = SimpleDatabase()
    db.add_user(1, {"name": "Shared", "email": "shared@example.com"})
    print("Setup shared database once")

    yield db

    print("Teardown shared database once")
    db.clear()


def test_shared_db_first(shared_database):
    assert shared_database.get_user(1)["name"] == "Shared"

def test_shared_db_second(shared_database):
    # Same database instance as previous test
    assert shared_database.get_user(1)["name"] == "Shared"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
