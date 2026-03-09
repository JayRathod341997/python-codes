# ============================================================
# Real World Example 2: Shopping Cart
# ============================================================
# Demonstrates: mutability, references, copy safety,
# multiple assignment, dynamic typing, id() inspection.
# ============================================================

import copy

class Product:
    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        return f"Product({self.name!r}, ${self.price:.2f})"


class ShoppingCart:
    def __init__(self, owner: str):
        self.owner = owner
        self._items: list[dict] = []    # mutable — modified in place

    def add_item(self, product: Product, quantity: int = 1):
        # Check if product already in cart
        for item in self._items:
            if item["product"].name == product.name:
                item["quantity"] += quantity    # mutate dict in place
                return
        self._items.append({"product": product, "quantity": quantity})

    def remove_item(self, product_name: str):
        self._items = [i for i in self._items if i["product"].name != product_name]

    @property
    def total(self) -> float:
        return sum(i["product"].price * i["quantity"] for i in self._items)

    def snapshot(self) -> list:
        """Return a deep copy — safe to inspect without side effects."""
        return copy.deepcopy(self._items)

    def __repr__(self):
        lines = [f"Cart ({self.owner}):"]
        for item in self._items:
            p = item["product"]
            q = item["quantity"]
            lines.append(f"  {p.name:20s} x{q}  ${p.price * q:.2f}")
        lines.append(f"  {'TOTAL':20s}     ${self.total:.2f}")
        return "\n".join(lines)


# --- Create products ---
laptop = Product("Laptop", 999.99, "electronics")
mouse  = Product("Mouse",   29.99, "electronics")
book   = Product("Python Book", 49.99, "books")
cable  = Product("USB Cable",    9.99, "accessories")

# --- User carts (mutable, independent) ---
cart_jay  = ShoppingCart("Jay")
cart_sara = ShoppingCart("Sara")

cart_jay.add_item(laptop)
cart_jay.add_item(mouse, quantity=2)
cart_jay.add_item(book)

cart_sara.add_item(book)
cart_sara.add_item(cable, quantity=3)

print(cart_jay)
print()
print(cart_sara)

# --- snapshot: deep copy lets us "save state" ---
saved = cart_jay.snapshot()
cart_jay.remove_item("Mouse")
cart_jay.add_item(cable)

print("\n=== After modifications ===")
print(cart_jay)

print("\n=== Saved snapshot (unchanged) ===")
for item in saved:
    p, q = item["product"], item["quantity"]
    print(f"  {p.name} x{q}")

# --- Multiple assignment: unpack totals ---
jay_total, sara_total = cart_jay.total, cart_sara.total
print(f"\nJay total:  ${jay_total:.2f}")
print(f"Sara total: ${sara_total:.2f}")
grand_total = jay_total + sara_total
print(f"Grand total: ${grand_total:.2f}")

# --- Dynamic typing: discount can be int or float ---
discount = 10           # int — 10%
discount = discount / 100  # now float
print(f"\nDiscount ({type(discount).__name__}): {discount}")
print(f"Jay's discounted total: ${jay_total * (1 - discount):.2f}")
