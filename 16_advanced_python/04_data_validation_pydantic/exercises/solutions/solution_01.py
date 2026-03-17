"""
============================================================
SOLUTION 01 — User Registration with Validation
============================================================
Complete working solution for Exercise 01.
Demonstrates model definition, validation, and error handling.
============================================================
"""

from pydantic import BaseModel, field_validator, ValidationError
from typing import Optional
from datetime import datetime


class Address(BaseModel):
    """Address model for user."""
    street: str
    city: str
    zipcode: str


class User(BaseModel):
    """User model with comprehensive validation."""
    name: str
    email: str
    age: int
    password: str
    address: Optional[Address] = None

    @field_validator('name')
    @classmethod
    def name_must_be_valid(cls, v):
        """Validate name: not empty, minimum 2 characters."""
        if not v or not v.strip():
            raise ValueError('Name cannot be empty')
        if len(v.strip()) < 2:
            raise ValueError('Name must be at least 2 characters')
        return v.strip()

    @field_validator('email')
    @classmethod
    def email_must_be_valid(cls, v):
        """Validate email: must contain @ and valid domain."""
        if '@' not in v:
            raise ValueError('Email must contain @')

        local, domain = v.split('@', 1)

        if not local or not domain:
            raise ValueError('Invalid email format')

        if '.' not in domain:
            raise ValueError('Email domain must contain .')

        return v.lower()

    @field_validator('age')
    @classmethod
    def age_must_be_valid(cls, v):
        """Validate age: between 18 and 100."""
        if not (18 <= v <= 100):
            raise ValueError('Age must be between 18 and 100')
        return v

    @field_validator('password')
    @classmethod
    def password_must_be_strong(cls, v):
        """Validate password: minimum 8 chars, uppercase, digit."""
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')

        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain at least one uppercase letter')

        if not any(c.isdigit() for c in v):
            raise ValueError('Password must contain at least one digit')

        return v


def create_user_from_dict(user_data: dict) -> Optional[User]:
    """
    Create user from dictionary with error handling.

    Args:
        user_data: Dictionary with user information

    Returns:
        User object if valid, None if validation fails
    """
    try:
        return User(**user_data)
    except ValidationError as e:
        print(f"Failed to create user due to {e.error_count()} validation error(s)")
        return None


def display_validation_errors(e: ValidationError) -> None:
    """
    Display validation errors in user-friendly format.

    Args:
        e: ValidationError exception
    """
    print(f"Validation failed ({e.error_count()} error(s)):")
    for error in e.errors():
        field = error['loc'][0]
        msg = error['msg']
        print(f"  {field}: {msg}")


if __name__ == "__main__":
    print("=" * 60)
    print("SOLUTION 01 - User Registration with Validation")
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

    user = create_user_from_dict(user_data_valid)
    if user:
        print(f"Success! User created:")
        print(f"  Name: {user.name}")
        print(f"  Email: {user.email}")
        print(f"  Age: {user.age}")
        print(f"  Address: {user.address.street}, {user.address.city}")
    print()

    # Test case 2: Invalid name
    print("Test 2: Invalid name (too short)")
    user_data_invalid_name = {
        "name": "B",
        "email": "bob@example.com",
        "age": 30,
        "password": "SecurePass123"
    }

    try:
        user = User(**user_data_invalid_name)
    except ValidationError as e:
        display_validation_errors(e)
    print()

    # Test case 3: Invalid email
    print("Test 3: Invalid email")
    user_data_invalid_email = {
        "name": "Charlie",
        "email": "invalid_email",
        "age": 25,
        "password": "SecurePass123"
    }

    try:
        user = User(**user_data_invalid_email)
    except ValidationError as e:
        display_validation_errors(e)
    print()

    # Test case 4: Invalid password
    print("Test 4: Invalid password (weak)")
    user_data_invalid_password = {
        "name": "Diana",
        "email": "diana@example.com",
        "age": 32,
        "password": "weak"
    }

    try:
        user = User(**user_data_invalid_password)
    except ValidationError as e:
        display_validation_errors(e)
    print()

    # Test case 5: Multiple validation errors
    print("Test 5: Multiple validation errors")
    user_data_multiple_errors = {
        "name": "X",
        "email": "bad_email",
        "age": 150,
        "password": "short"
    }

    try:
        user = User(**user_data_multiple_errors)
    except ValidationError as e:
        display_validation_errors(e)
    print()

    # Test case 6: Valid user without address
    print("Test 6: Valid user without address (optional)")
    user_data_no_address = {
        "name": "Eve",
        "email": "eve@example.com",
        "age": 26,
        "password": "ValidPass123"
    }

    user = create_user_from_dict(user_data_no_address)
    if user:
        print(f"Success! User created without address:")
        print(f"  Name: {user.name}")
        print(f"  Email: {user.email}")
        print(f"  Address: {user.address}")
    print()

    # Test case 7: Serialization
    print("Test 7: User serialization")
    user_data = {
        "name": "Frank",
        "email": "frank@example.com",
        "age": 35,
        "password": "SecurePass456",
        "address": {
            "street": "456 Oak Ave",
            "city": "Boston",
            "zipcode": "02101"
        }
    }

    user = create_user_from_dict(user_data)
    if user:
        print(f"User as dict:")
        print(f"  {user.model_dump()}")
        print(f"\nUser as JSON:")
        print(f"  {user.model_dump_json()}")

    print("\n" + "=" * 60)
    print("KEY LEARNINGS")
    print("=" * 60)
    print("""
1. @field_validator runs validation on individual fields
2. ValidationError contains all validation errors
3. error.errors() returns list of error dictionaries
4. Each error has: loc (field), msg (message), type
5. Raise ValueError with clear message in validators
6. Optional fields can be None (don't require input)
7. Nested models are validated automatically
8. Use model_dump() to convert to dict
9. Use model_dump_json() to convert to JSON string
10. Always handle ValidationError in production code
""")
