# Interview Q&A — Data Validation with Pydantic

## Q1. What's the difference between Pydantic v1 and v2?

**A:** Pydantic v2 (2023+) has major improvements: faster validation (using Rust), different import paths, ConfigDict instead of Config class, and @field_validator decorator (not @validator). Most code is similar, but v2 is recommended for new projects.

```python
# v1
from pydantic import validator

# v2
from pydantic import field_validator
```

---

## Q2. How does Pydantic handle type coercion?

**A:** Pydantic intelligently converts types before validation. It converts "123" to 123, "true" to True, etc. If coercion fails, it raises ValidationError. The conversion rules follow Python's built-in type conversion behavior.

```python
from pydantic import BaseModel

class Item(BaseModel):
    quantity: int
    price: float
    active: bool

item = Item(quantity="10", price="9.99", active="yes")
# quantity=10 (int), price=9.99 (float), active=True (bool)
```

---

## Q3. When should I use @field_validator vs @model_validator?

**A:** Use `@field_validator` for single-field validation (check email format, length, etc). Use `@model_validator` for cross-field validation (quantity <= max_quantity). Field validators run on individual fields; model validators on entire model.

```python
from pydantic import BaseModel, field_validator, model_validator

class Order(BaseModel):
    quantity: int
    max_quantity: int

    @field_validator('quantity')
    @classmethod
    def qty_must_be_positive(cls, v):
        if v <= 0: raise ValueError('Must be positive')
        return v

    @model_validator(mode='after')
    def qty_not_exceed_max(self):
        if self.quantity > self.max_quantity:
            raise ValueError('Exceeds max')
        return self
```

---

## Q4. How do I make a field required vs optional?

**A:** Use `Optional[Type]` or `Type | None` for optional fields. A field without a default is required. Optional fields should have defaults (usually None).

```python
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    name: str  # Required
    email: str  # Required
    phone: Optional[str] = None  # Optional
    age: int = 0  # Has default, optional
```

---

## Q5. What happens if validation fails?

**A:** Pydantic raises `ValidationError` with detailed information about what failed. The error includes field name, expected type, value provided, and explanation. Always catch it when handling untrusted input.

```python
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    age: int

try:
    user = User(age="not_a_number")
except ValidationError as e:
    print(e)
    # Shows: value is not a valid integer (type=type_error.integer)
```

---

## Q6. How do I validate related fields together?

**A:** Use `@model_validator(mode='after')` to access other fields. This runs after all fields are validated individually, so you have access to the entire model.

```python
from pydantic import BaseModel, model_validator

class DateRange(BaseModel):
    start_date: str
    end_date: str

    @model_validator(mode='after')
    def end_after_start(self):
        if self.end_date < self.start_date:
            raise ValueError('end_date must be after start_date')
        return self
```

---

## Q7. Can I use Pydantic with FastAPI?

**A:** Yes, perfectly. FastAPI uses Pydantic models for request/response validation. Define your model, use it as a route parameter, and FastAPI automatically validates requests and generates OpenAPI docs.

```python
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item  # FastAPI validates the request body
```

---

## Q8. How do I serialize a Pydantic model to JSON?

**A:** Use `.model_dump_json()` for JSON string, `.model_dump()` for dict. You can exclude fields, include computed fields, and control serialization.

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    password: str

user = User(name="Alice", age=30, password="secret")

# As JSON string
json_str = user.model_dump_json()

# As dict
data = user.model_dump()

# Exclude sensitive fields
data = user.model_dump(exclude={'password'})
```

---

## Q9. What's the difference between validate_assignment and runtime validation?

**A:** `validate_assignment=True` validates fields when you assign them after creation. Without it, you can assign any value. Runtime validation happens during __init__. Use it for immutable-like models.

```python
from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    age: int

user = User(age=25)
user.age = "invalid"  # ✗ ValidationError (assignment validated)

# Without validate_assignment:
class User2(BaseModel):
    age: int

user2 = User2(age=25)
user2.age = "invalid"  # OK (no validation on assignment)
print(user2.age)  # "invalid" (wrong type, but allowed)
```

---

## Q10. How do I handle validation of complex nested structures?

**A:** Define separate model classes for each nested structure. Pydantic automatically validates nested models recursively.

```python
from pydantic import BaseModel
from typing import List

class Address(BaseModel):
    street: str
    city: str
    zipcode: str

class User(BaseModel):
    name: str
    addresses: List[Address]  # Nested, automatically validated

user = User(
    name="Alice",
    addresses=[
        {"street": "123 Main", "city": "NYC", "zipcode": "10001"},
        {"street": "456 Oak", "city": "LA", "zipcode": "90001"}
    ]
)
# All nested addresses are validated automatically
```

---

## Q11. Can I make a model immutable?

**A:** Yes, use `frozen=True` in ConfigDict. Once created, you cannot modify fields.

```python
from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(frozen=True)
    name: str
    age: int

user = User(name="Alice", age=30)
user.name = "Bob"  # ✗ ValidationError: Model is frozen
```

---

## Q12. How do I load configuration from environment variables?

**A:** Use `BaseSettings` from `pydantic_settings`. It automatically loads from environment variables and .env files.

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    api_key: str
    debug: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
# Automatically loads from environment or .env file
```
