"""
============================================================
TOPIC: 02_validation_and_errors.py
Real-world context: API endpoint that validates payment
and user registration data with custom business logic.
============================================================
"""

from pydantic import BaseModel, field_validator, model_validator, ValidationError
from typing import Optional
from datetime import datetime

print("=" * 60)
print("SECTION 1: Field Validators")
print("=" * 60)

class User(BaseModel):
    """User model with field validators."""
    username: str
    email: str
    age: int
    password: str

    @field_validator('username')
    @classmethod
    def username_must_be_alphanumeric(cls, v):
        if not v.replace('_', '').isalnum():
            raise ValueError('Username must contain only letters, numbers, underscore')
        return v

    @field_validator('email')
    @classmethod
    def email_must_be_valid(cls, v):
        if '@' not in v or '.' not in v.split('@')[-1]:
            raise ValueError('Invalid email format')
        return v

    @field_validator('age')
    @classmethod
    def age_must_be_in_range(cls, v):
        if not (13 <= v <= 120):
            raise ValueError('Age must be between 13 and 120')
        return v

    @field_validator('password')
    @classmethod
    def password_must_be_strong(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain at least one uppercase letter')
        return v

# Valid user
user = User(
    username="alice_123",
    email="alice@example.com",
    age=25,
    password="SecurePass123"
)
print(f"Valid user created: {user.username}\n")

# Invalid email
try:
    user = User(
        username="bob",
        email="invalid_email",
        age=30,
        password="SecurePass123"
    )
except ValidationError as e:
    print(f"Email validation error:")
    for error in e.errors():
        print(f"  {error['loc'][0]}: {error['msg']}")
    print()

# Invalid password
try:
    user = User(
        username="charlie",
        email="charlie@example.com",
        age=28,
        password="weak"
    )
except ValidationError as e:
    print(f"Password validation error:")
    for error in e.errors():
        print(f"  {error['loc'][0]}: {error['msg']}")
    print()


print("=" * 60)
print("SECTION 2: Model Validators (Cross-field)")
print("=" * 60)

class DateRange(BaseModel):
    """Model that validates relationship between fields."""
    event_name: str
    start_date: datetime
    end_date: datetime
    description: str

    @model_validator(mode='after')
    def end_after_start(self):
        if self.end_date <= self.start_date:
            raise ValueError('End date must be after start date')
        return self

# Valid date range
event = DateRange(
    event_name="Conference",
    start_date=datetime(2024, 6, 1),
    end_date=datetime(2024, 6, 3),
    description="Annual tech conference"
)
print(f"Valid event: {event.event_name}")
print(f"  {event.start_date.date()} to {event.end_date.date()}\n")

# Invalid date range
try:
    event = DateRange(
        event_name="Workshop",
        start_date=datetime(2024, 6, 10),
        end_date=datetime(2024, 6, 5),
        description="Python workshop"
    )
except ValidationError as e:
    print(f"Date range validation error:")
    print(f"  {e.errors()[0]['msg']}\n")


print("=" * 60)
print("SECTION 3: Payment Validation")
print("=" * 60)

class Payment(BaseModel):
    """Payment model with complex validation."""
    amount: float
    currency: str
    card_number: str
    cvv: str
    cardholder_name: str

    @field_validator('amount')
    @classmethod
    def amount_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Amount must be greater than 0')
        if v > 1000000:
            raise ValueError('Amount exceeds maximum limit')
        return v

    @field_validator('currency')
    @classmethod
    def currency_must_be_valid(cls, v):
        valid_currencies = ['USD', 'EUR', 'GBP', 'JPY']
        if v.upper() not in valid_currencies:
            raise ValueError(f'Currency must be one of {valid_currencies}')
        return v.upper()

    @field_validator('card_number')
    @classmethod
    def card_number_must_be_valid(cls, v):
        # Remove spaces
        v = v.replace(' ', '')
        if not v.isdigit() or len(v) not in [15, 16]:
            raise ValueError('Invalid card number (must be 15-16 digits)')
        return v

    @field_validator('cvv')
    @classmethod
    def cvv_must_be_valid(cls, v):
        if not v.isdigit() or len(v) not in [3, 4]:
            raise ValueError('CVV must be 3-4 digits')
        return v

    @model_validator(mode='after')
    def validate_card_holder(self):
        if len(self.cardholder_name) < 3:
            raise ValueError('Cardholder name must be at least 3 characters')
        return self

# Valid payment
payment = Payment(
    amount=99.99,
    currency="usd",
    card_number="4111 1111 1111 1111",
    cvv="123",
    cardholder_name="John Doe"
)
print(f"Valid payment: ${payment.amount} {payment.currency}")
print(f"  Card: {payment.card_number}")
print(f"  Cardholder: {payment.cardholder_name}\n")

# Multiple validation errors
try:
    payment = Payment(
        amount=-50,
        currency="xxx",
        card_number="invalid",
        cvv="12",
        cardholder_name="Jo"
    )
except ValidationError as e:
    print(f"Payment validation errors ({e.error_count()} total):")
    for error in e.errors():
        field = error['loc'][0]
        msg = error['msg']
        print(f"  {field}: {msg}")
    print()


print("=" * 60)
print("SECTION 4: Custom Error Messages")
print("=" * 60)

class Product(BaseModel):
    """Product with custom error messages."""
    sku: str
    price: float
    stock: int

    @field_validator('sku')
    @classmethod
    def sku_must_match_format(cls, v):
        if not (len(v) == 10 and v[:3].isalpha() and v[3:].isdigit()):
            raise ValueError(
                'SKU must be in format: 3 letters + 7 digits (e.g., ABC1234567)'
            )
        return v

    @field_validator('price')
    @classmethod
    def price_must_be_reasonable(cls, v):
        if v < 0.01:
            raise ValueError('Price must be at least $0.01')
        if v > 99999:
            raise ValueError('Price seems unreasonably high (max $99,999)')
        return v

    @field_validator('stock')
    @classmethod
    def stock_must_be_non_negative(cls, v):
        if v < 0:
            raise ValueError('Stock cannot be negative')
        if v > 1000000:
            raise ValueError('Stock exceeds warehouse capacity')
        return v

# Valid product
product = Product(sku="ABC1234567", price=29.99, stock=100)
print(f"Valid product: {product.sku} at ${product.price}\n")

# Display custom error message
try:
    product = Product(sku="INVALID", price=-10, stock=1000000000)
except ValidationError as e:
    print(f"Product validation with custom messages:")
    for error in e.errors():
        field = error['loc'][0]
        msg = error['msg']
        print(f"  {field}: {msg}")
    print()


print("=" * 60)
print("SECTION 5: Exception Handling Patterns")
print("=" * 60)

def create_user_safely(user_data: dict) -> Optional[User]:
    """Create user with error handling."""
    try:
        return User(**user_data)
    except ValidationError as e:
        print(f"Failed to create user:")
        print(f"  Total errors: {e.error_count()}")
        for error in e.errors():
            field = error['loc'][0]
            msg = error['msg']
            print(f"  {field}: {msg}")
        return None

# Test with valid data
user_data = {
    "username": "alice_smith",
    "email": "alice@example.com",
    "age": 28,
    "password": "SecurePass123"
}
user = create_user_safely(user_data)
if user:
    print(f"User created: {user.username}\n")

# Test with invalid data
user_data = {
    "username": "bob@invalid",
    "email": "invalid",
    "age": 5,
    "password": "weak"
}
user = create_user_safely(user_data)
print()


print("=" * 60)
print("SECTION 6: Handling Multiple Validation Errors")
print("=" * 60)

def format_validation_errors(e: ValidationError) -> dict:
    """Format validation errors for API response."""
    errors = {}
    for error in e.errors():
        field = error['loc'][0]
        msg = error['msg']
        if field not in errors:
            errors[field] = []
        errors[field].append(msg)
    return errors

# Create invalid payment
try:
    payment = Payment(
        amount=-10,
        currency="INVALID",
        card_number="1234",
        cvv="1",
        cardholder_name="X"
    )
except ValidationError as e:
    errors = format_validation_errors(e)
    print(f"Formatted API error response:")
    for field, messages in errors.items():
        print(f"  {field}:")
        for msg in messages:
            print(f"    - {msg}")
    print()

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
Validation techniques:
1. @field_validator: Validate individual fields
2. @model_validator: Validate relationships between fields
3. mode='before': Validate before type coercion
4. mode='after': Validate after type coercion
5. ValidationError contains all validation errors
6. error.errors() returns list of error dicts
7. Each error has: loc (field), msg (message), type
8. Custom error messages for clarity
9. Handle validation errors gracefully in APIs
10. Format errors for user-friendly responses
""")
