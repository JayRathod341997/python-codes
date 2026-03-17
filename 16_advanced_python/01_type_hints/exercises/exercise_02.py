"""
============================================================
EXERCISE 02 — Type Hints: Collections & Advanced Types
============================================================
Problem: Build an inventory management system with proper typing.

Requirements:
  1. Define a Product type (id: int, name: str, price: float, in_stock: bool)
  2. Create function to get all products of a certain category
  3. Create function to calculate total inventory value
  4. Create function to find cheapest and most expensive product
  5. Use List, Dict, Tuple, Optional, and Union types appropriately

Hint: Use TypedDict or dataclass for Product structure
      Dict[str, List[Product]] for categories -> products
      Tuple[str, float] for returning (product_name, price)
============================================================
"""

from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass

# TODO: Define your Product structure (using dataclass or TypedDict)
# Example with dataclass:
# @dataclass
# class Product:
#     id: int
#     name: str
#     price: float
#     in_stock: bool

# Step 1: Create inventory dictionary
# Structure: category_name -> list of products
# Example: {"Electronics": [Product(...), Product(...)], "Books": [...]}

# Step 2: Write function to add product to inventory
# def add_product(inventory: Dict[str, List[Product]], category: str, product: Product) -> None:
#     """Add a product to a specific category."""
#     pass

# Step 3: Write function to get products by category
# def get_by_category(inventory: Dict[str, List[Product]], category: str) -> List[Product]:
#     """Get all products in a category."""
#     pass

# Step 4: Calculate total inventory value
# def total_value(products: List[Product]) -> float:
#     """Calculate total value of all products in stock."""
#     pass

# Step 5: Find price range
# def price_range(products: List[Product]) -> Tuple[str, float, str, float]:
#     """Return (cheapest_name, cheapest_price, expensive_name, expensive_price)."""
#     pass

# Step 6: Find product by name
# def find_by_name(products: List[Product], name: str) -> Optional[Product]:
#     """Find a product by name. Return None if not found."""
#     pass

if __name__ == "__main__":
    print("=" * 60)
    print("EXERCISE 02 - Inventory Management")
    print("=" * 60)

    # Create inventory and test your functions
    # TODO: Implement and test

    # Example structure:
    # inventory = {
    #     "Electronics": [...],
    #     "Books": [...],
    #     "Home": [...]
    # }

    # Test cases (implement after creating functions):
    # 1. Add products to different categories
    # 2. Get all products in a category
    # 3. Calculate total value
    # 4. Find price range
    # 5. Search for a specific product

    print("\nImplementation pending...")
