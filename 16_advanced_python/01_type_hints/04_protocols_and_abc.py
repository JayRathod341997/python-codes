"""
============================================================
TOPIC: 04_protocols_and_abc.py
Real-world context: Payment processing system with different
payment methods (card, wallet, crypto) using protocols.
============================================================
"""

from typing import Protocol, List
from abc import ABC, abstractmethod

# ============================================================
# SECTION 1: What are Protocols? (Structural Typing)
# ============================================================
print("=" * 60)
print("SECTION 1: Protocols - Structural Typing")
print("=" * 60)

# Protocol: define what methods an object MUST have
# No inheritance needed - just implement the methods

class PaymentProcessor(Protocol):
    """Any object that can process payments must have these methods."""

    def pay(self, amount: float) -> bool:
        """Process a payment."""
        ...

    def refund(self, amount: float) -> bool:
        """Refund a payment."""
        ...


# Now implement different payment methods
# NO inheritance from PaymentProcessor - just matching methods!

class CreditCardPayment:
    """Process payments via credit card."""

    def __init__(self, card_number: str) -> None:
        self.card_number = card_number

    def pay(self, amount: float) -> bool:
        print(f"  -> Processing card payment of Rs{amount}")
        return True

    def refund(self, amount: float) -> bool:
        print(f"  -> Refunding card payment of Rs{amount}")
        return True


class WalletPayment:
    """Process payments via digital wallet."""

    def __init__(self, wallet_id: str) -> None:
        self.wallet_id = wallet_id

    def pay(self, amount: float) -> bool:
        print(f"  -> Processing wallet payment of Rs{amount}")
        return True

    def refund(self, amount: float) -> bool:
        print(f"  -> Refunding wallet payment of Rs{amount}")
        return True


class CryptoPayment:
    """Process payments via cryptocurrency."""

    def __init__(self, wallet_address: str) -> None:
        self.wallet_address = wallet_address

    def pay(self, amount: float) -> bool:
        print(f"  -> Processing crypto payment of {amount} tokens")
        return True

    def refund(self, amount: float) -> bool:
        print(f"  -> Refunding crypto payment of {amount} tokens")
        return True


# Function that accepts ANY PaymentProcessor
# Doesn't care about class inheritance - only cares about methods
def process_order(processor: PaymentProcessor, amount: float) -> None:
    """Process an order with any payment processor."""
    if processor.pay(amount):
        print(f"  Checkmark Payment successful")
    else:
        print(f"  Cross Payment failed")


print("\nUsing different payment methods with same function:")
print("\n1. Credit Card:")
card = CreditCardPayment("1234-5678-9012-3456")
process_order(card, 500)

print("\n2. Wallet:")
wallet = WalletPayment("user_wallet_123")
process_order(wallet, 300)

print("\n3. Cryptocurrency:")
crypto = CryptoPayment("0x123abc...")
process_order(crypto, 0.05)


# ============================================================
# SECTION 2: Protocol vs Inheritance (ABC)
# ============================================================
print("\n" + "=" * 60)
print("SECTION 2: Protocol vs Abstract Base Class (ABC)")
print("=" * 60)

# Abstract Base Class approach (inheritance-based)
class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def make_sound(self) -> str:
        """Make a sound."""
        pass

    @abstractmethod
    def move(self) -> str:
        """Move around."""
        pass


class Dog(Animal):
    """Dog must inherit from Animal and implement methods."""

    def make_sound(self) -> str:
        return "Woof!"

    def move(self) -> str:
        return "Running on four legs"


class Bird(Animal):
    """Bird must inherit from Animal."""

    def make_sound(self) -> str:
        return "Tweet!"

    def move(self) -> str:
        return "Flying with wings"


# Function using ABC
def describe_animal(animal: Animal) -> None:
    """Works only with Animal subclasses."""
    print(f"  Sound: {animal.make_sound()}")
    print(f"  Movement: {animal.move()}")


print("\nUsing ABC:")
dog = Dog()
describe_animal(dog)

print()
bird = Bird()
describe_animal(bird)


# ============================================================
# SECTION 3: Protocol Advantage - No Inheritance Needed
# ============================================================
print("\n" + "=" * 60)
print("SECTION 3: Protocol Advantage - Duck Typing Made Formal")
print("=" * 60)

# Define what we need
class Drawable(Protocol):
    """Anything with a draw() method can be drawable."""

    def draw(self) -> None:
        """Draw the object."""
        ...


# Implement WITHOUT inheriting from Drawable
class Circle:
    def __init__(self, radius: int) -> None:
        self.radius = radius

    def draw(self) -> None:
        print(f"  -> Drawing circle with radius {self.radius}")


class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def draw(self) -> None:
        print(f"  -> Drawing {self.width}x{self.height} rectangle")


class Triangle:
    def __init__(self, base: int, height: int) -> None:
        self.base = base
        self.height = height

    def draw(self) -> None:
        print(f"  -> Drawing triangle {self.base}x{self.height}")


# Function that works with anything drawable (doesn't care about inheritance)
def render_shapes(shapes: List[Drawable]) -> None:
    """Render a list of drawable objects."""
    for shape in shapes:
        shape.draw()


print("\nRendering different shapes (no inheritance needed):")
shapes: List[Drawable] = [
    Circle(5),
    Rectangle(10, 20),
    Triangle(6, 8)
]
render_shapes(shapes)


# ============================================================
# SECTION 4: Protocol with Properties
# ============================================================
print("\n" + "=" * 60)
print("SECTION 4: Protocol with Properties")
print("=" * 60)

# Protocol requiring both methods AND properties
class Vehicle(Protocol):
    """Anything that acts like a vehicle."""

    @property
    def speed(self) -> float:
        """Current speed of vehicle."""
        ...

    def accelerate(self, amount: float) -> None:
        """Increase speed."""
        ...


class Car:
    def __init__(self) -> None:
        self._speed: float = 0

    @property
    def speed(self) -> float:
        return self._speed

    def accelerate(self, amount: float) -> None:
        self._speed += amount
        print(f"  -> Car accelerated to {self._speed} km/h")


class Motorcycle:
    def __init__(self) -> None:
        self._speed: float = 0

    @property
    def speed(self) -> float:
        return self._speed

    def accelerate(self, amount: float) -> None:
        self._speed += amount
        print(f"  -> Motorcycle accelerated to {self._speed} km/h")


def test_vehicle(vehicle: Vehicle) -> None:
    """Test any vehicle."""
    vehicle.accelerate(50)
    print(f"  Current speed: {vehicle.speed} km/h")


print("\nTesting vehicles:")
print("\n1. Car:")
car = Car()
test_vehicle(car)

print("\n2. Motorcycle:")
motorcycle = Motorcycle()
test_vehicle(motorcycle)


# ============================================================
# SECTION 5: When to Use Protocol vs ABC
# ============================================================
print("\n" + "=" * 60)
print("SECTION 5: When to Use Protocol vs ABC")
print("=" * 60)

print("""
USE PROTOCOL when:
  * You want "duck typing" formalized
  * Multiple unrelated classes should implement the interface
  * You're working with external libraries (they don't need to inherit)
  * Flexibility is more important than strict hierarchy

USE ABC (Abstract Base Class) when:
  * You want to enforce inheritance (MUST inherit from this class)
  * You want to share common code between subclasses
  * You want a strict type hierarchy
  * You need runtime checks (isinstance() works with ABC)
  * You're building a framework or library

REAL-WORLD EXAMPLE:
  Protocol: "We need anything that can serialize to JSON"
    - Pydantic models, dataclasses, custom classes
    - They don't inherit, just implement the interface

  ABC: "All database models inherit from Model"
    - Enforces common structure
    - Shares query(), save(), delete() implementations
""")


# ============================================================
# KEY POINTS
# ============================================================
print("\n" + "=" * 60)
print("KEY POINTS")
print("=" * 60)
print("""
1. Protocol: Define what methods an object must have
   from typing import Protocol

2. Protocol is structural typing:
   - No inheritance needed
   - If it has the methods, it matches the protocol
   - "Duck typing" made explicit for type checkers

3. ABC (Abstract Base Class): Define what subclasses must do
   from abc import ABC, abstractmethod
   - REQUIRES inheritance
   - Can share code
   - Stricter but more explicit

4. Protocol is better for:
   - Integrating external code
   - Flexible duck typing
   - Multiple unrelated implementations

5. ABC is better for:
   - Building frameworks
   - Sharing code between subclasses
   - Enforcing a type hierarchy

6. Both help type checkers understand your intentions
   - Use them to make code more self-documenting
""")
