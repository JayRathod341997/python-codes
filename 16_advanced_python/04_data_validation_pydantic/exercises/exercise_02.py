"""
============================================================
EXERCISE 02 — Pydantic: Product Inventory System
============================================================
Problem: Build a product inventory system with validation,
nested models, and computed fields.

Requirements:
  1. Create Category model (name, description)
  2. Create Product model with:
     - product_id, name, price, quantity
     - category (nested)
     - validation for price > 0 and quantity >= 0
  3. Create Inventory model containing:
     - List of products
     - Computed field for total_value
     - Computed field for product_count
  4. Add configuration with validate_assignment
  5. Create inventory from external data (JSON/dict)
  6. Calculate and display totals using computed fields

Hints: Use BaseModel for nested models
       Use ConfigDict(validate_assignment=True)
       Use @computed_field for derived values
       List[Product] for multiple products
       model_dump() for serialization
============================================================
"""

from pydantic import BaseModel, field_validator, computed_field
from typing import List, Optional

# TODO: Implement your solution below

# Step 1: Create Category model
class Category(BaseModel):
    """Product category."""
    # TODO: Add fields: name, description
    pass


# Step 2: Create Product model
class Product(BaseModel):
    """Product with validation."""
    # TODO: Add fields:
    # - product_id: int
    # - name: str
    # - description: str
    # - price: float (must be > 0)
    # - quantity: int (must be >= 0)
    # - category: Category (nested)

    # TODO: Add @field_validator for price
    # Validate: must be greater than 0

    # TODO: Add @field_validator for quantity
    # Validate: cannot be negative

    pass


# Step 3: Create Inventory model
class Inventory(BaseModel):
    """Inventory containing multiple products."""
    # TODO: Add ConfigDict with validate_assignment=True
    # model_config = ConfigDict(...)

    # TODO: Add field: products: List[Product]

    # TODO: Add @computed_field for total_value
    # Calculate: sum of (price * quantity) for all products

    # TODO: Add @computed_field for product_count
    # Calculate: number of products

    # TODO: Add method to add product to inventory
    def add_product(self, product: Product) -> None:
        """Add product to inventory."""
        pass

    # TODO: Add method to get product by ID
    def get_product(self, product_id: int) -> Optional[Product]:
        """Get product by ID."""
        pass

    pass


# Step 4: Function to create inventory from data
def create_inventory_from_data(inventory_data: dict) -> Inventory:
    """
    TODO: Create inventory from dictionary.

    Args:
        inventory_data: Dictionary containing products

    Returns:
        Inventory object
    """
    pass


if __name__ == "__main__":
    print("=" * 60)
    print("EXERCISE 02 - Product Inventory System")
    print("=" * 60)

    # Create inventory with sample products
    inventory_data = {
        "products": [
            {
                "product_id": 1,
                "name": "Laptop",
                "description": "High-performance laptop",
                "price": 999.99,
                "quantity": 5,
                "category": {
                    "name": "Electronics",
                    "description": "Electronic devices"
                }
            },
            {
                "product_id": 2,
                "name": "Mouse",
                "description": "Wireless mouse",
                "price": 29.99,
                "quantity": 50,
                "category": {
                    "name": "Accessories",
                    "description": "Computer accessories"
                }
            },
            {
                "product_id": 3,
                "name": "Keyboard",
                "description": "Mechanical keyboard",
                "price": 79.99,
                "quantity": 25,
                "category": {
                    "name": "Accessories",
                    "description": "Computer accessories"
                }
            }
        ]
    }

    # TODO: Create inventory from data
    # inventory = create_inventory_from_data(inventory_data)

    # TODO: Display inventory information
    # - Product count (from computed field)
    # - Total inventory value (from computed field)
    # - List each product with category

    # TODO: Test validation
    # - Try to add product with invalid price
    # - Try to add product with invalid quantity

    # TODO: Test validation_assignment
    # - Try to modify product quantity to negative

    print("\n" + "=" * 60)
    print("Expected behavior:")
    print("- Inventory displays product count and total value")
    print("- Computed fields auto-calculate totals")
    print("- Validation prevents invalid data")
    print("- Assignment validation catches bad modifications")
