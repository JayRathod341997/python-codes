"""
============================================================
TOPIC: 03_nested_models_config.py
Real-world context: Building complex API request/response
models with nested data and configuration options.
============================================================
"""

from pydantic import BaseModel, ConfigDict, field_validator, computed_field
from typing import List, Optional
from datetime import datetime, timedelta

print("=" * 60)
print("SECTION 1: Nested Models")
print("=" * 60)

class Address(BaseModel):
    """Address model (nested)."""
    street: str
    city: str
    state: str
    zipcode: str
    country: str = "USA"

class Contact(BaseModel):
    """Contact model (nested)."""
    email: str
    phone: Optional[str] = None
    website: Optional[str] = None

class Company(BaseModel):
    """Company model with nested models."""
    name: str
    industry: str
    founded_year: int
    headquarters: Address  # Nested model
    contact: Contact  # Nested model
    employees_count: int

# Create with nested data
company_data = {
    "name": "TechCorp",
    "industry": "Software",
    "founded_year": 2010,
    "headquarters": {
        "street": "123 Tech Boulevard",
        "city": "San Francisco",
        "state": "CA",
        "zipcode": "94105"
    },
    "contact": {
        "email": "info@techcorp.com",
        "phone": "555-1234"
    },
    "employees_count": 500
}

company = Company(**company_data)
print(f"Company: {company.name}")
print(f"  Address: {company.headquarters.street}, {company.headquarters.city}")
print(f"  Email: {company.contact.email}")
print(f"  Phone: {company.contact.phone}")
print()


print("=" * 60)
print("SECTION 2: Lists of Nested Models")
print("=" * 60)

class Person(BaseModel):
    """Person model."""
    name: str
    age: int
    title: str

class Department(BaseModel):
    """Department with list of employees."""
    name: str
    budget: float
    manager: Person  # Single nested
    employees: List[Person]  # List of nested

# Create department with multiple employees
dept_data = {
    "name": "Engineering",
    "budget": 500000,
    "manager": {
        "name": "Alice Johnson",
        "age": 40,
        "title": "VP Engineering"
    },
    "employees": [
        {"name": "Bob Smith", "age": 30, "title": "Senior Engineer"},
        {"name": "Charlie Brown", "age": 28, "title": "Engineer"},
        {"name": "Diana Prince", "age": 29, "title": "Engineer"},
    ]
}

dept = Department(**dept_data)
print(f"Department: {dept.name}")
print(f"Manager: {dept.manager.name} ({dept.manager.title})")
print(f"Employees ({len(dept.employees)}):")
for emp in dept.employees:
    print(f"  - {emp.name}, {emp.age}, {emp.title}")
print()


print("=" * 60)
print("SECTION 3: Model Configuration (ConfigDict)")
print("=" * 60)

class User(BaseModel):
    """User with specific configuration."""
    model_config = ConfigDict(
        validate_assignment=True,  # Validate on field assignment
        str_strip_whitespace=True,  # Strip leading/trailing whitespace
        use_enum_values=True,  # Use enum values in serialization
    )

    name: str
    email: str
    age: int

# String whitespace is automatically stripped
user = User(name="  Alice Smith  ", email="alice@example.com", age=30)
print(f"Name (whitespace stripped): '{user.name}'")

# Validation on assignment
user.age = 31  # OK
print(f"Age after assignment: {user.age}")

try:
    user.age = "invalid"  # Error due to validate_assignment=True
except Exception as e:
    print(f"Assignment validation error: Invalid type for age")
print()


print("=" * 60)
print("SECTION 4: Immutable Models (frozen=True)")
print("=" * 60)

class ImmutableUser(BaseModel):
    """Immutable user model."""
    model_config = ConfigDict(frozen=True)

    user_id: int
    username: str
    email: str

user = ImmutableUser(user_id=1, username="alice", email="alice@example.com")
print(f"Immutable user: {user.username}")

try:
    user.email = "newemail@example.com"  # Error
except Exception as e:
    print(f"Cannot modify frozen model: {type(e).__name__}")
print()


print("=" * 60)
print("SECTION 5: Computed Fields")
print("=" * 60)

class Order(BaseModel):
    """Order with computed fields."""
    order_id: int
    items: List[str]
    item_prices: List[float]
    tax_rate: float = 0.08

    @computed_field
    @property
    def subtotal(self) -> float:
        """Computed: sum of all prices."""
        return sum(self.item_prices)

    @computed_field
    @property
    def tax(self) -> float:
        """Computed: tax based on subtotal."""
        return self.subtotal * self.tax_rate

    @computed_field
    @property
    def total(self) -> float:
        """Computed: subtotal + tax."""
        return self.subtotal + self.tax

    @computed_field
    @property
    def item_count(self) -> int:
        """Computed: number of items."""
        return len(self.items)

# Create order
order = Order(
    order_id=1001,
    items=["Laptop", "Mouse", "Keyboard"],
    item_prices=[999.99, 29.99, 79.99],
    tax_rate=0.10
)

print(f"Order {order.order_id}:")
print(f"  Items: {order.item_count}")
for item, price in zip(order.items, order.item_prices):
    print(f"    - {item}: ${price:.2f}")
print(f"  Subtotal: ${order.subtotal:.2f}")
print(f"  Tax (10%): ${order.tax:.2f}")
print(f"  Total: ${order.total:.2f}")
print()

# Computed fields included in serialization
order_dict = order.model_dump()
print(f"Serialized order includes computed fields:")
print(f"  subtotal: {order_dict['subtotal']}")
print(f"  tax: {order_dict['tax']}")
print(f"  total: {order_dict['total']}")
print()


print("=" * 60)
print("SECTION 6: Field Aliases")
print("=" * 60)

from pydantic import Field

class Product(BaseModel):
    """Product with field aliases for external data."""
    product_id: int = Field(alias='id')
    product_name: str = Field(alias='name')
    unit_price: float = Field(alias='price')
    available_stock: int = Field(alias='stock', default=0)

# Create from data with aliased field names
external_data = {
    'id': 123,
    'name': 'Laptop',
    'price': 999.99,
    'stock': 10
}

product = Product(**external_data)
print(f"Product created from external data:")
print(f"  ID: {product.product_id}")
print(f"  Name: {product.product_name}")
print(f"  Price: ${product.unit_price}")
print(f"  Stock: {product.available_stock}")

# Serialize with aliases
product_dict = product.model_dump(by_alias=True)
print(f"\nSerialized with aliases: {product_dict}")
print()


print("=" * 60)
print("SECTION 7: Custom Validation with Nested Models")
print("=" * 60)

class Location(BaseModel):
    """Location model."""
    latitude: float
    longitude: float

    @field_validator('latitude')
    @classmethod
    def latitude_in_range(cls, v):
        if not (-90 <= v <= 90):
            raise ValueError('Latitude must be between -90 and 90')
        return v

    @field_validator('longitude')
    @classmethod
    def longitude_in_range(cls, v):
        if not (-180 <= v <= 180):
            raise ValueError('Longitude must be between -180 and 180')
        return v

class Event(BaseModel):
    """Event with location."""
    name: str
    location: Location
    event_date: datetime

# Valid event
event = Event(
    name="Conference",
    location={"latitude": 37.7749, "longitude": -122.4194},
    event_date=datetime(2024, 6, 15, 9, 0)
)
print(f"Event: {event.name}")
print(f"  Location: {event.location.latitude}, {event.location.longitude}")
print(f"  Date: {event.event_date}")
print()


print("=" * 60)
print("SECTION 8: Serialization Control")
print("=" * 60)

class SensitiveData(BaseModel):
    """Model with sensitive fields to exclude."""
    username: str
    email: str
    password_hash: str
    api_key: str
    public_profile: str

user = SensitiveData(
    username="alice",
    email="alice@example.com",
    password_hash="hashed_password_123",
    api_key="sk_live_secret_key",
    public_profile="Software Engineer"
)

# Include all fields
print("Full serialization:")
print(user.model_dump())

# Exclude sensitive fields
print("\nPublic serialization (excluded sensitive fields):")
print(user.model_dump(exclude={'password_hash', 'api_key'}))

# Include only specific fields
print("\nPublic profile only:")
print(user.model_dump(include={'username', 'public_profile'}))
print()

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
Nested models and configuration:
1. Nest BaseModel within BaseModel for complex structures
2. Use List[Model] for arrays of nested objects
3. ConfigDict controls model behavior
4. validate_assignment=True: Validate on field assignment
5. str_strip_whitespace=True: Auto-strip string whitespace
6. frozen=True: Makes model immutable
7. Computed fields for derived data
8. Field aliases for external data mapping
9. Custom validators work with nested models
10. Control serialization with exclude/include
""")
