# Topic 04: Data Validation with Pydantic v2

## Overview

Build robust data models with automatic validation using Pydantic v2.

## Quick Start

```bash
python 01_basic_models.py
python 02_validation_and_errors.py
python 03_nested_models_config.py
python 04_settings.py
python exercises/solutions/solution_01.py
python exercises/solutions/solution_02.py
```

## Files

| File | Lines | What You'll Learn |
|------|-------|-------------------|
| notes.md | 400+ | Theory, examples, config |
| interview.md | 300+ | 12 Q&A |
| 01_basic_models.py | 200+ | BaseModel, field types |
| 02_validation_and_errors.py | 250+ | Validators, error handling |
| 03_nested_models_config.py | 250+ | Nested models, config |
| 04_settings.py | 200+ | BaseSettings, env vars |
| exercises/solution_01.py | 200+ | User validation |
| exercises/solution_02.py | 200+ | API request validation |

## Learning Path

1. **Read notes.md** (30 min)
2. **Run 01_basic_models.py** (10 min)
3. **Run 02_validation_and_errors.py** (10 min)
4. **Run 03_nested_models_config.py** (10 min)
5. **Run 04_settings.py** (10 min)
6. **Review interview.md** (10 min)
7. **Solve exercises** (30 min)

## Key Concepts

### BaseModel
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: int

user = User(name="Alice", email="alice@example.com", age=25)
```

### Field Types
```python
from pydantic import Field

class Product(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    quantity: int = Field(default=1, ge=0)
```

### Validators
```python
from pydantic import field_validator

class User(BaseModel):
    email: str

    @field_validator('email')
    @classmethod
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email')
        return v
```

### Nested Models
```python
class Address(BaseModel):
    street: str
    city: str

class User(BaseModel):
    name: str
    address: Address
```

### Model Config
```python
from pydantic import ConfigDict

class User(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_default=True
    )
```

### Settings
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    api_key: str
    debug: bool = False

    class Config:
        env_file = ".env"
```

## Real-World Example

### API Request Validation
```python
from datetime import datetime
from pydantic import BaseModel, EmailStr

class CreateUserRequest(BaseModel):
    name: str
    email: EmailStr
    age: int
    created_at: datetime = None

# Usage
user_data = {
    "name": "Alice",
    "email": "alice@example.com",
    "age": 25
}
user = CreateUserRequest(**user_data)
```

### Database Model
```python
class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool

    model_config = ConfigDict(from_attributes=True)

# From ORM object
product = Product.from_orm(orm_object)
```

## Exercises

### Exercise 01: User Registration
Create validator for:
- Email format
- Password strength
- Age validation
- Phone number

### Exercise 02: API Request Validation
Create validators for:
- Request body format
- Required fields
- Data type conversion
- Error messages

## Common Patterns

| Pattern | Use |
|---------|-----|
| BaseModel | All data validation |
| Field() | Custom field config |
| @field_validator | Custom validation |
| @model_validator | Cross-field validation |
| BaseSettings | Config from env |
| Nested models | Related data |

## Validation Features

1. **Type checking** - str, int, float, bool, datetime
2. **Constraints** - min, max, min_length, max_length
3. **Custom validators** - @field_validator
4. **Default values** - field defaults
5. **Optional fields** - Optional[T]
6. **Aliases** - field(alias="api_name")
7. **Error messages** - custom error text
8. **JSON schema** - auto schema generation

## Error Handling

```python
from pydantic import ValidationError

try:
    user = User(name="", email="invalid")
except ValidationError as e:
    print(e.errors())  # List of errors
    print(e.json())    # JSON format
```

## JSON Schema Generation

```python
# Get JSON Schema
schema = User.model_json_schema()
print(schema)

# Generate OpenAPI docs
from fastapi import FastAPI
app = FastAPI()
# Automatically uses Pydantic models
```

## FastAPI Integration

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
async def create_item(item: Item):
    return item
# Pydantic auto-validates request body
```

## Key Takeaways

1. Use BaseModel for all data validation
2. Define types explicitly
3. Use Field() for constraints
4. Create custom validators
5. Nest models for related data
6. Use BaseSettings for config
7. Let Pydantic auto-validate
8. Handle ValidationError

## Interview Questions

See interview.md for Q1-Q12:
- What is BaseModel?
- How to validate fields?
- Custom validators
- Nested models
- Configuration
- FastAPI integration

## Performance Tips

1. Reuse models (don't recreate)
2. Use validators wisely (can be slow)
3. Lazy validation available
4. Pre-compute if possible
5. Cache validation errors

## Next Topic

→ [05_testing_pytest](../05_testing_pytest/README.md)

---

**Estimated Time:** 2 hours

**Prerequisites:** Type hints (Topic 01)

**Difficulty:** Beginner-Intermediate

**Required Packages:** pydantic, pydantic-settings
