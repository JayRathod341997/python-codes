"""
============================================================
TOPIC: 01_basic_models.py
Real-world context: Building an e-commerce API with
product and order models that validate all input.
============================================================
"""

from pydantic import BaseModel, ValidationError
from typing import Optional, List
from decimal import Decimal

print("=" * 60)
print("SECTION 1: Basic Model Definition")
print("=" * 60)

class Product(BaseModel):
    """Product model for e-commerce system."""
    name: str
    description: str
    price: float
    quantity: int
    in_stock: bool = True

# Create product instance
product = Product(
    name="Laptop",
    description="High-performance laptop",
    price=999.99,
    quantity=5
)

print(f"Product: {product}")
print(f"Name: {product.name}")
print(f"Price: ${product.price}")
print(f"In Stock: {product.in_stock}\n")


print("=" * 60)
print("SECTION 2: Type Coercion")
print("=" * 60)

# Pydantic automatically converts types
product = Product(
    name="Mouse",
    description="Wireless mouse",
    price="49.99",  # String, will convert to float
    quantity="10",  # String, will convert to int
    in_stock="yes"  # String, will convert to bool (truthy value)
)

print(f"Product: {product}")
print(f"Price type: {type(product.price)} = {product.price}")
print(f"Quantity type: {type(product.quantity)} = {product.quantity}")
print(f"In Stock type: {type(product.in_stock)} = {product.in_stock}\n")


print("=" * 60)
print("SECTION 3: Validation and Error Handling")
print("=" * 60)

# Invalid data triggers ValidationError
test_cases = [
    {
        "name": "Keyboard",
        "description": "Mechanical keyboard",
        "price": "invalid_price",  # Invalid float
        "quantity": 5
    },
    {
        "name": "Monitor",
        "description": "4K Monitor",
        "price": 299.99,
        "quantity": "not_a_number"  # Invalid int
    },
]

for test_data in test_cases:
    try:
        product = Product(**test_data)
    except ValidationError as e:
        print(f"Validation error for {test_data.get('name', 'unknown')}:")
        print(f"  {e.error_count()} error(s) found")
        for error in e.errors():
            print(f"  - {error['loc'][0]}: {error['msg']}")
        print()


print("=" * 60)
print("SECTION 4: Optional Fields and Defaults")
print("=" * 60)

class Order(BaseModel):
    """Order model with optional and default fields."""
    order_id: int
    customer_name: str
    email: str
    phone: Optional[str] = None  # Optional, defaults to None
    shipping_address: str
    notes: str = ""  # Default empty string
    priority: bool = False  # Default False
    discount_percent: float = 0.0  # Default 0

# Create with minimal required fields
order = Order(
    order_id=1001,
    customer_name="Alice",
    email="alice@example.com",
    shipping_address="123 Main St"
)

print(f"Order: {order}")
print(f"Phone: {order.phone} (None because not provided)")
print(f"Notes: '{order.notes}' (empty string default)")
print(f"Priority: {order.priority} (False by default)")
print()

# Override defaults
order = Order(
    order_id=1002,
    customer_name="Bob",
    email="bob@example.com",
    phone="555-1234",
    shipping_address="456 Oak Ave",
    notes="Fragile - handle with care",
    priority=True,
    discount_percent=10.0
)

print(f"Order with all fields: {order}\n")


print("=" * 60)
print("SECTION 5: Accessing Model Data")
print("=" * 60)

# Access fields as attributes
print(f"Customer: {order.customer_name}")
print(f"Email: {order.email}")
print(f"Discount: {order.discount_percent}%")

# Convert to dictionary
order_dict = order.model_dump()
print(f"\nAs dictionary: {order_dict}")

# Convert to JSON string
order_json = order.model_dump_json()
print(f"As JSON: {order_json}")

# Convert with exclusions
order_dict_no_notes = order.model_dump(exclude={'notes'})
print(f"Without notes: {order_dict_no_notes}\n")


print("=" * 60)
print("SECTION 6: Model Schema and Documentation")
print("=" * 60)

# Get JSON schema for documentation
schema = Product.model_json_schema()
print(f"Product schema fields:")
for field_name, field_info in schema.get('properties', {}).items():
    field_type = field_info.get('type', 'unknown')
    print(f"  {field_name}: {field_type}")
print()


print("=" * 60)
print("SECTION 7: Creating from External Data")
print("=" * 60)

# From API request (JSON)
api_response = {
    "name": "Headphones",
    "description": "Noise-cancelling headphones",
    "price": 199.99,
    "quantity": 15,
    "in_stock": True
}

product = Product(**api_response)
print(f"Product from API: {product}")

# From database query
db_row = ("Phone", "Smartphone", 799.99, 20, True)
product = Product(
    name=db_row[0],
    description=db_row[1],
    price=db_row[2],
    quantity=db_row[3],
    in_stock=db_row[4]
)
print(f"Product from database: {product}\n")


print("=" * 60)
print("SECTION 8: Mutability and Field Assignment")
print("=" * 60)

# By default, you can modify fields after creation
product = Product(
    name="Tablet",
    description="10-inch tablet",
    price=399.99,
    quantity=8
)

print(f"Original quantity: {product.quantity}")
product.quantity = 5  # Modify field
print(f"Modified quantity: {product.quantity}")

# Note: No validation on assignment by default
product.price = "invalid"  # No error!
print(f"Price after invalid assignment: {product.price} (type: {type(product.price)})")
print("(Without validate_assignment=True, invalid types are allowed)\n")


print("=" * 60)
print("SECTION 9: Model Representation")
print("=" * 60)

product = Product(
    name="Monitor",
    description="27-inch 4K monitor",
    price=599.99,
    quantity=3
)

# Default string representation
print(f"repr: {repr(product)}")
print(f"str: {str(product)}")

# Pretty print
print(f"\nFormatted output:")
print(f"  Name: {product.name}")
print(f"  Description: {product.description}")
print(f"  Price: ${product.price:.2f}")
print(f"  Quantity: {product.quantity} units")
print(f"  In Stock: {'Yes' if product.in_stock else 'No'}\n")


print("=" * 60)
print("SECTION 10: Type Hints Documentation")
print("=" * 60)

# Pydantic uses type hints for self-documentation
class Customer(BaseModel):
    """Customer model with various field types."""
    customer_id: int  # Customer ID
    name: str  # Customer name
    email: str  # Email address
    age: int  # Customer age
    is_premium: bool  # Premium member?
    tags: List[str] = []  # Customer tags
    phone: Optional[str] = None  # Phone number

# Type hints are visible in IDE autocomplete and documentation
customer = Customer(
    customer_id=1,
    name="Charlie",
    email="charlie@example.com",
    age=35,
    is_premium=True,
    tags=["vip", "frequent-buyer"]
)

print(f"Customer: {customer}")
print(f"Fields with type hints are self-documenting!")
print(f"IDEs can show autocomplete for all fields.\n")

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
Key points:
1. Define models with type hints using BaseModel
2. Pydantic validates and coerces types automatically
3. Optional fields use Optional[Type] with default None
4. Fields without defaults are required
5. ValidationError contains detailed error information
6. Use model_dump() for dict, model_dump_json() for JSON
7. Access fields as attributes: model.field_name
8. Models are mutable by default (can modify fields)
9. Type hints serve as documentation
10. Pydantic makes APIs robust and self-documenting
""")
