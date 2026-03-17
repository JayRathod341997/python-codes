"""
============================================================
SOLUTION 02 — Type Hints: Collections & Advanced Types
============================================================
Complete inventory management system with proper typing.
============================================================
"""

from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass


@dataclass
class Product:
    """Product in inventory."""
    id: int
    name: str
    price: float
    in_stock: bool

    def __repr__(self) -> str:
        status = "[In]" if self.in_stock else "[Out]"
        return f"{self.name} (Rs{self.price}) [{status}]"


# Inventory structure: category -> list of products
inventory: Dict[str, List[Product]] = {}


def add_product(category: str, product: Product) -> None:
    """
    Add a product to inventory.

    Args:
        category: Product category name
        product: Product object to add
    """
    if category not in inventory:
        inventory[category] = []
    inventory[category].append(product)
    print(f"[OK] Added {product.name} to {category}")


def get_by_category(category: str) -> List[Product]:
    """
    Get all products in a category.

    Args:
        category: Category name

    Returns:
        List of products in category (empty list if not found)
    """
    return inventory.get(category, [])


def total_value(products: List[Product]) -> float:
    """
    Calculate total value of products in stock.

    Args:
        products: List of products

    Returns:
        Total value in rupees
    """
    return sum(p.price for p in products if p.in_stock)


def price_range(products: List[Product]) -> Tuple[str, float, str, float]:
    """
    Find cheapest and most expensive product.

    Args:
        products: List of products

    Returns:
        Tuple of (cheapest_name, cheapest_price, expensive_name, expensive_price)
    """
    if not products:
        return ("", 0.0, "", 0.0)

    cheapest = min(products, key=lambda p: p.price)
    expensive = max(products, key=lambda p: p.price)

    return (cheapest.name, cheapest.price, expensive.name, expensive.price)


def find_by_name(category: str, name: str) -> Optional[Product]:
    """
    Find a product by name in a category.

    Args:
        category: Category to search in
        name: Product name

    Returns:
        Product if found, None otherwise
    """
    products = get_by_category(category)
    for product in products:
        if product.name.lower() == name.lower():
            return product
    return None


def inventory_summary() -> None:
    """Print summary of entire inventory."""
    total_value_all = 0.0
    total_items = 0

    for category, products in inventory.items():
        value = total_value(products)
        total_value_all += value
        total_items += len(products)
        print(f"\n{category}:")
        for product in products:
            print(f"  • {product}")
        print(f"  Total value: Rs{value:.2f}")

    print(f"\n{'=' * 50}")
    print(f"Total items: {total_items}")
    print(f"Total inventory value: Rs{total_value_all:.2f}")


if __name__ == "__main__":
    print("=" * 60)
    print("SOLUTION 02 - Inventory Management System")
    print("=" * 60)

    # Add products
    print("\n1. Adding products:")
    add_product("Electronics", Product(101, "Laptop", 50000, True))
    add_product("Electronics", Product(102, "Mouse", 500, True))
    add_product("Electronics", Product(103, "Monitor", 12000, False))

    add_product("Books", Product(201, "Python Guide", 499, True))
    add_product("Books", Product(202, "Data Science", 799, True))

    add_product("Home", Product(301, "Pillow", 250, True))
    add_product("Home", Product(302, "Blanket", 1500, True))

    # Get products by category
    print("\n2. Products in Electronics:")
    electronics = get_by_category("Electronics")
    for product in electronics:
        print(f"  • {product}")

    # Calculate total value
    print("\n3. Total value:")
    books_value = total_value(get_by_category("Books"))
    print(f"Books inventory value: Rs{books_value:.2f}")

    home_value = total_value(get_by_category("Home"))
    print(f"Home inventory value: Rs{home_value:.2f}")

    electronics_value = total_value(get_by_category("Electronics"))
    print(f"Electronics inventory value: Rs{electronics_value:.2f}")

    # Find price range
    print("\n4. Price range in Electronics:")
    cheap, cheap_price, expensive, expensive_price = price_range(electronics)
    print(f"Cheapest: {cheap} (Rs{cheap_price})")
    print(f"Most expensive: {expensive} (Rs{expensive_price})")

    # Find by name
    print("\n5. Searching for products:")
    found = find_by_name("Electronics", "Laptop")
    if found:
        print(f"[OK] Found: {found}")
    else:
        print("✗ Not found")

    found = find_by_name("Books", "Python Guide")
    if found:
        print(f"[OK] Found: {found}")

    # Full inventory summary
    print("\n6. Complete inventory summary:")
    inventory_summary()

    # Type safety demonstration
    print(f"\n{'=' * 50}")
    print("Type Safety Features:")
    print("[OK] Product is a typed dataclass")
    print("[OK] Functions have clear parameter types")
    print("[OK] Return types are explicit (List, Tuple, Optional)")
    print("[OK] Type checker catches errors before runtime")
