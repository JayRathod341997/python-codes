# Data Validation with Pydantic: Building Robust Data Models

## What is it?

Pydantic is a Python library for data validation and parsing using type hints. It automatically validates data at runtime, converts types, and provides clear error messages. It's the standard for building reliable APIs, CLI applications, and data pipelines.

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

user = User(name="Alice", age=30, email="alice@example.com")
print(user)  # name='Alice' age=30 email='alice@example.com'

# Automatic validation and type conversion
user = User(name="Bob", age="25", email="bob@example.com")  # "25" converted to int
print(user.age)  # 25 (now int, not string)

# Validation errors
try:
    user = User(name="Charlie", age="invalid", email="charlie@example.com")
except Exception as e:
    print(f"Validation error: {e}")
```

---

## Why Use Pydantic?

| Benefit | Example |
|---------|---------|
| **Automatic validation** | Type mismatches caught immediately |
| **Type coercion** | "123" auto-converts to int |
| **Clear error messages** | Tells exactly what's wrong and where |
| **Self-documenting code** | Model definition = documentation |
| **JSON serialization** | .model_dump_json() for API responses |
| **Nested models** | Complex nested structures naturally |
| **Custom validators** | Business logic validation |
| **Settings management** | Load config from env files |
| **Works with FastAPI** | Perfect for building APIs |

---

## Core Concepts

### 1. Basic Model Definition

```python
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
    quantity: int
    in_stock: bool = True  # Optional with default

# Create instance
product = Product(
    name="Laptop",
    price=999.99,
    quantity=10
)

print(product)
# Product(name='Laptop', price=999.99, quantity=10, in_stock=True)
```

### 2. Type Annotations and Coercion

Pydantic coerces types intelligently:

```python
from pydantic import BaseModel

class Item(BaseModel):
    count: int
    total: float
    active: bool

# Type coercion
item = Item(count="50", total="99.99", active="yes")
print(item.count)     # 50 (int)
print(item.total)     # 99.99 (float)
print(item.active)    # True (bool, "yes" converts to True)
```

### 3. Optional Fields and Defaults

```python
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None  # Optional, defaults to None
    age: int = 0  # Has default value
    verified: bool = False  # Boolean with default

# Missing optional fields are OK
user = User(name="Alice", email="alice@example.com")
print(user.phone)  # None
print(user.verified)  # False
```

### 4. Nested Models

```python
from pydantic import BaseModel
from typing import List

class Address(BaseModel):
    street: str
    city: str
    zipcode: str

class Person(BaseModel):
    name: str
    address: Address
    tags: List[str] = []

# Create with nested data
person = Person(
    name="Alice",
    address={"street": "123 Main St", "city": "NYC", "zipcode": "10001"},
    tags=["developer", "python"]
)

print(person.address.city)  # "NYC"
print(person.tags)  # ["developer", "python"]
```

### 5. Field Validation with Validators

```python
from pydantic import BaseModel, field_validator

class Product(BaseModel):
    name: str
    price: float
    quantity: int

    @field_validator('name')
    @classmethod
    def name_must_not_be_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Name cannot be empty')
        return v.strip()

    @field_validator('price')
    @classmethod
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Price must be positive')
        return v

    @field_validator('quantity')
    @classmethod
    def quantity_must_be_non_negative(cls, v):
        if v < 0:
            raise ValueError('Quantity cannot be negative')
        return v

# Validation happens automatically
product = Product(name="Laptop", price=999.99, quantity=5)
print(product)  # OK

# Triggers validation error
try:
    product = Product(name="", price=999.99, quantity=5)
except Exception as e:
    print(f"Error: {e}")
```

### 6. Root Validators (Cross-field validation)

```python
from pydantic import BaseModel, model_validator

class Order(BaseModel):
    product: str
    quantity: int
    max_quantity: int

    @model_validator(mode='after')
    def validate_quantity_not_exceed_max(self):
        if self.quantity > self.max_quantity:
            raise ValueError(
                f'Quantity {self.quantity} exceeds max {self.max_quantity}'
            )
        return self

# Validation checks across fields
order = Order(product="Phone", quantity=5, max_quantity=10)  # OK
order = Order(product="Phone", quantity=15, max_quantity=10)  # Error!
```

### 7. Model Configuration

```python
from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,  # Validate on field assignment
        str_strip_whitespace=True,  # Strip whitespace from strings
        frozen=False,  # Allow modification (True = immutable)
        json_schema_extra={
            "example": {"name": "John", "age": 30}
        }
    )

    name: str
    age: int

user = User(name="  Alice  ", age=25)
print(user.name)  # "Alice" (whitespace stripped)
```

### 8. JSON Serialization and Deserialization

```python
from pydantic import BaseModel
from datetime import datetime

class Event(BaseModel):
    title: str
    timestamp: datetime
    description: str

# Deserialize from JSON/dict
event_data = {
    "title": "Meeting",
    "timestamp": "2024-01-15T10:30:00",
    "description": "Team sync"
}
event = Event(**event_data)

# Serialize to JSON
json_str = event.model_dump_json()
print(json_str)
# {"title":"Meeting","timestamp":"2024-01-15T10:30:00","description":"Team sync"}

# Serialize to dict
dict_data = event.model_dump()
print(dict_data)
# {'title': 'Meeting', 'timestamp': datetime(...), 'description': 'Team sync'}
```

### 9. Settings/Environment Variables

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Load configuration from environment variables.
    """
    database_url: str = "postgresql://localhost/mydb"
    api_key: str
    debug: bool = False
    max_connections: int = 10

    class Config:
        env_file = ".env"  # Load from .env file
        case_sensitive = False

# Environment variables override defaults
import os
os.environ['API_KEY'] = 'secret123'
os.environ['DEBUG'] = 'true'

settings = Settings()
print(settings.api_key)  # "secret123"
print(settings.debug)  # True
print(settings.max_connections)  # 10 (default)
```

### 10. Computed Fields

```python
from pydantic import BaseModel, computed_field

class Rectangle(BaseModel):
    width: float
    height: float

    @computed_field
    @property
    def area(self) -> float:
        return self.width * self.height

    @computed_field
    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

rect = Rectangle(width=5, height=3)
print(rect.area)  # 15.0
print(rect.perimeter)  # 16.0
print(rect.model_dump())
# {'width': 5, 'height': 3, 'area': 15.0, 'perimeter': 16.0}
```

---

## Common Pitfalls

### Pitfall 1: Forgetting validation errors are exceptions

```python
from pydantic import BaseModel

class User(BaseModel):
    age: int

# Wrong: Assuming it won't raise
user = User(age="not a number")  # ✗ Raises ValidationError

# Right: Catch ValidationError
from pydantic import ValidationError

try:
    user = User(age="not a number")
except ValidationError as e:
    print(f"Validation failed: {e}")
```

### Pitfall 2: Not handling nested validation errors

```python
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    zipcode: int  # Expects integer

class Person(BaseModel):
    name: str
    address: Address

# Wrong: Invalid nested data without error handling
person = Person(
    name="Alice",
    address={"street": "Main St", "zipcode": "invalid"}
)  # ✗ Raises ValidationError

# Right: Handle nested validation
try:
    person = Person(
        name="Alice",
        address={"street": "Main St", "zipcode": "12345"}
    )
except ValidationError as e:
    print(f"Error in nested model: {e}")
```

### Pitfall 3: Field validators modifying other fields

```python
from pydantic import BaseModel, field_validator

class Payment(BaseModel):
    amount: float
    fee: float

    @field_validator('amount')
    @classmethod
    def deduct_fee(cls, v):
        # Wrong: Can't modify other fields in field_validator
        # cls.fee -= v * 0.02  # ✗ Error

        # Right: Use model_validator for cross-field logic
        return v

# Use model_validator instead for complex logic
```

### Pitfall 4: Not using validation_mode correctly

```python
from pydantic import BaseModel, field_validator

class Product(BaseModel):
    price: float

    @field_validator('price', mode='before')
    @classmethod
    def parse_price(cls, v):
        # 'before': Runs before Pydantic type coercion
        if isinstance(v, str):
            return float(v.replace('$', ''))
        return v

# Parsing custom formats
product = Product(price="$99.99")
print(product.price)  # 99.99
```

---

## Best Practices

1. **Use typed fields for clear intent**
   ```python
   class User(BaseModel):
       name: str
       age: int
       email: str
   ```

2. **Provide meaningful defaults**
   ```python
   class Config(BaseModel):
       timeout: int = 30
       retries: int = 3
       debug: bool = False
   ```

3. **Use validators for business logic**
   ```python
   @field_validator('email')
   @classmethod
   def email_must_be_valid(cls, v):
       if '@' not in v:
           raise ValueError('Invalid email')
       return v
   ```

4. **Separate nested models for clarity**
   ```python
   class Address(BaseModel):
       street: str
       city: str

   class User(BaseModel):
       name: str
       address: Address
   ```

5. **Use ConfigDict for model-wide settings**
   ```python
   model_config = ConfigDict(
       validate_assignment=True,
       str_strip_whitespace=True
   )
   ```

6. **Handle ValidationError explicitly**
   ```python
   try:
       user = User(**data)
   except ValidationError as e:
       return {"error": str(e)}
   ```

7. **Use computed fields for derived data**
   ```python
   @computed_field
   @property
   def display_name(self) -> str:
       return f"{self.first_name} {self.last_name}"
   ```

8. **Load settings from environment variables**
   ```python
   class Settings(BaseSettings):
       database_url: str
       api_key: str
   ```

9. **Use schema export for documentation**
   ```python
   schema = User.model_json_schema()
   print(schema)  # JSON Schema for API documentation
   ```

10. **Validate immediately on creation**
    ```python
    user = User(**request_data)  # Raises if invalid
    # If we reach here, user is guaranteed valid
    ```

---

## Performance Considerations

### Validation Overhead

Pydantic adds validation overhead, but it's minimal:

```python
# Simple model: ~50 microseconds per validation
class Item(BaseModel):
    name: str
    price: float

item = Item(name="Widget", price=9.99)
```

### Complex Models

For complex nested models with many validators, validation time increases. Profile in production:

```python
import timeit

class Product(BaseModel):
    name: str
    price: float
    # ... many fields and validators

# Measure validation time
time = timeit.timeit(
    lambda: Product(name="Item", price=99.99),
    number=10000
)
print(f"Average: {time/10000*1000:.2f}ms per validation")
```

---

## Summary

Pydantic provides:
- Automatic runtime data validation
- Type coercion and conversion
- Clear error messages
- Self-documenting code
- Integration with FastAPI and other frameworks
- Settings management from environment variables
- JSON serialization/deserialization
- Custom validation logic
- Nested model support
- Computed fields for derived data

Master Pydantic to build robust, maintainable Python applications with confidence in your data integrity.
