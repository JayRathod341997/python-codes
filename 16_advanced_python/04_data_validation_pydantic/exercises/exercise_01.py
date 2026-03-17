"""
============================================================
EXERCISE 01 — Pydantic: Building a Validated User Model
============================================================
Problem: Create a complete user registration system with
proper data validation and error handling.

Requirements:
  1. Create User model with name, email, age, password
  2. Add field validators for:
     - name: not empty, minimum 2 characters
     - email: must contain @ and valid domain
     - age: between 18 and 100
     - password: minimum 8 chars, needs uppercase, number
  3. Create Address model (street, city, zipcode)
  4. Add address to User as nested model
  5. Handle ValidationError and show error messages
  6. Create users from JSON/dict data
  7. Serialize user to dict/JSON

Hints: Use BaseModel, @field_validator decorator
       Raise ValueError in validators with clear messages
       Use ValidationError for error handling
       Nested models validate recursively
============================================================
"""

from pydantic import BaseModel, field_validator, ValidationError
from typing import Optional

# TODO: Implement your solution below

# Step 1: Create Address model
class Address(BaseModel):
    """Address model for user."""
    # TODO: Add fields: street, city, zipcode
    pass


# Step 2: Create User model with validators
class User(BaseModel):
    """User model with validation."""
    # TODO: Add fields with type hints
    # - name: str
    # - email: str
    # - age: int
    # - password: str
    # - address: Optional[Address] = None

    # TODO: Add @field_validator for name
    # Validate: not empty, minimum 2 characters

    # TODO: Add @field_validator for email
    # Validate: must contain @ and . in domain part

    # TODO: Add @field_validator for age
    # Validate: between 18 and 100

    # TODO: Add @field_validator for password
    # Validate: minimum 8 chars, at least one uppercase, one digit

    pass


# Step 3: Function to create user from dict data
def create_user_from_dict(user_data: dict) -> Optional[User]:
    """
    TODO: Create user from dictionary with error handling.

    Args:
        user_data: Dictionary with user information

    Returns:
        User object if valid, None if validation fails
    """
    pass


# Step 4: Function to display validation errors
def display_validation_errors(e: ValidationError) -> None:
    """
    TODO: Display validation errors in user-friendly format.

    Args:
        e: ValidationError exception
    """
    pass


if __name__ == "__main__":
    print("=" * 60)
    print("EXERCISE 01 - User Registration with Validation")
    print("=" * 60)

    # Test case 1: Valid user
    print("\nTest 1: Valid user")
    user_data_valid = {
        "name": "Alice Smith",
        "email": "alice@example.com",
        "age": 28,
        "password": "SecurePass123",
        "address": {
            "street": "123 Main St",
            "city": "New York",
            "zipcode": "10001"
        }
    }
    # TODO: Create and display user

    # Test case 2: Invalid name
    print("\nTest 2: Invalid name (too short)")
    user_data_invalid_name = {
        "name": "B",
        "email": "bob@example.com",
        "age": 30,
        "password": "SecurePass123"
    }
    # TODO: Try to create user and handle error

    # Test case 3: Invalid email
    print("\nTest 3: Invalid email")
    user_data_invalid_email = {
        "name": "Charlie",
        "email": "invalid_email",
        "age": 25,
        "password": "SecurePass123"
    }
    # TODO: Try to create user and handle error

    # Test case 4: Invalid password
    print("\nTest 4: Invalid password (weak)")
    user_data_invalid_password = {
        "name": "Diana",
        "email": "diana@example.com",
        "age": 32,
        "password": "weak"
    }
    # TODO: Try to create user and handle error

    print("\n" + "=" * 60)
    print("Expected behavior:")
    print("- Valid user is created successfully")
    print("- Invalid data shows clear error messages")
    print("- Errors show field name and what's wrong")
    print("- Nested address is validated automatically")
