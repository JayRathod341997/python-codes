"""
============================================================
SOLUTION 02 — Product Inventory System
============================================================
Complete working solution for Exercise 02.
Demonstrates nested models, computed fields, and configuration.
============================================================
"""

from pydantic import BaseModel, field_validator, computed_field, ConfigDict
from typing import List, Optional


class Category(BaseModel):
    """Product category."""
    name: str
    description: str


class Product(BaseModel):
    """Product with validation."""
    product_id: int
    name: str
    description: str
    price: float
    quantity: int
    category: Category

    @field_validator('price')
    @classmethod
    def price_must_be_positive(cls, v):
        """Price must be greater than 0."""
        if v <= 0:
            raise ValueError('Price must be greater than 0')
        return v

    @field_validator('quantity')
    @classmethod
    def quantity_must_be_non_negative(cls, v):
        """Quantity cannot be negative."""
        if v < 0:
            raise ValueError('Quantity cannot be negative')
        return v


class Inventory(BaseModel):
    """Inventory containing multiple products."""
    model_config = ConfigDict(validate_assignment=True)

    products: List[Product] = []

    @computed_field
    @property
    def total_value(self) -> float:
        """Calculate total inventory value."""
        return sum(p.price * p.quantity for p in self.products)

    @computed_field
    @property
    def product_count(self) -> int:
        """Calculate number of unique products."""
        return len(self.products)

    def add_product(self, product: Product) -> None:
        """Add product to inventory."""
        # Check if product already exists
        existing = None
        for p in self.products:
            if p.product_id == product.product_id:
                existing = p
                break

        if existing:
            # Update quantity if product exists
            existing.quantity += product.quantity
        else:
            # Add new product
            self.products.append(product)

    def get_product(self, product_id: int) -> Optional[Product]:
        """Get product by ID."""
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def remove_product(self, product_id: int) -> bool:
        """Remove product by ID."""
        for i, product in enumerate(self.products):
            if product.product_id == product_id:
                self.products.pop(i)
                return True
        return False

    def get_value_by_category(self, category_name: str) -> float:
        """Get total value of products in a category."""
        return sum(
            p.price * p.quantity
            for p in self.products
            if p.category.name.lower() == category_name.lower()
        )

    def display_summary(self) -> None:
        """Display inventory summary."""
        print(f"\nInventory Summary:")
        print(f"  Total products: {self.product_count}")
        print(f"  Total value: ${self.total_value:,.2f}")
        print(f"  Average product value: ${self.total_value / self.product_count:,.2f}" if self.product_count > 0 else "")


if __name__ == "__main__":
    print("=" * 60)
    print("SOLUTION 02 - Product Inventory System")
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

    # Create inventory from data
    inventory = Inventory(**inventory_data)

    # Display inventory information
    inventory.display_summary()

    print(f"\nProducts in inventory:")
    for product in inventory.products:
        value = product.price * product.quantity
        print(f"  {product.product_id}. {product.name}")
        print(f"     Category: {product.category.name}")
        print(f"     Price: ${product.price:.2f} x {product.quantity} = ${value:,.2f}")

    # Show value by category
    print(f"\nValue by category:")
    electronics_value = inventory.get_value_by_category("Electronics")
    accessories_value = inventory.get_value_by_category("Accessories")
    print(f"  Electronics: ${electronics_value:,.2f}")
    print(f"  Accessories: ${accessories_value:,.2f}")

    # Test adding a new product
    print(f"\nAdding new product...")
    new_product = Product(
        product_id=4,
        name="Monitor",
        description="27-inch 4K Monitor",
        price=399.99,
        quantity=8,
        category=Category(name="Electronics", description="Electronic devices")
    )
    inventory.add_product(new_product)
    inventory.display_summary()

    # Test validation on assignment
    print(f"\nTesting validation on field assignment...")
    print(f"Before: {inventory.products[0].quantity} units of {inventory.products[0].name}")

    try:
        # Try to set negative quantity (should fail due to validate_assignment)
        inventory.products[0].quantity = -5
    except Exception as e:
        print(f"Error: Cannot set negative quantity (validation blocked it)")

    print(f"After: {inventory.products[0].quantity} units (unchanged)")

    # Test invalid product creation
    print(f"\nTesting invalid product creation...")
    try:
        invalid_product = Product(
            product_id=5,
            name="Invalid Product",
            description="This will fail",
            price=-10,  # Invalid!
            quantity=5,
            category=Category(name="Test", description="Test category")
        )
    except Exception as e:
        print(f"Error: Cannot create product with negative price")

    # Serialization
    print(f"\nInventory serialization:")
    inv_dict = inventory.model_dump()
    print(f"  Product count in dict: {inv_dict['product_count']}")
    print(f"  Total value in dict: {inv_dict['total_value']}")

    print("\n" + "=" * 60)
    print("KEY LEARNINGS")
    print("=" * 60)
    print("""
1. Nested BaseModel classes validate recursively
2. List[Model] validates each item in the list
3. @computed_field calculates values on access
4. ConfigDict(validate_assignment=True) validates field changes
5. Custom methods can access computed field values
6. Validators work with nested models
7. model_dump() includes computed fields
8. Can query and filter products efficiently
9. Add business logic methods to models
10. Pydantic makes data integrity automatic
""")
