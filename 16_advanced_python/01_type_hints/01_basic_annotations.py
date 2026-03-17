"""
============================================================
TOPIC: 01_basic_annotations.py
Real-world context: User registration system where we need
to validate and store user information with clear types.
============================================================
"""

# ============================================================
# SECTION 1: Variable Annotations (Basic Types)
# ============================================================
# Real-world context: Declaring user profile fields

print("=" * 60)
print("SECTION 1: Variable Annotations")
print("=" * 60)

# String type annotation
username: str = "alice_smith"
print(f"Username: {username}, Type: {type(username).__name__}")

# Integer type annotation
user_age: int = 28
print(f"Age: {user_age}, Type: {type(user_age).__name__}")

# Float type annotation (for ratings, scores, prices)
rating: float = 4.85
print(f"Rating: {rating}, Type: {type(rating).__name__}")

# Boolean type annotation
is_premium: bool = True
print(f"Is Premium: {is_premium}, Type: {type(is_premium).__name__}")

# Note: Type hints don't enforce types at runtime
# Python will NOT raise an error even if you assign wrong type
username_wrong: str = 123  # ✗ Type checker would complain, but Python allows it
print(f"Wrong type assigned: {username_wrong} (Python allows this)")


# ============================================================
# SECTION 2: Function Type Hints (Parameters & Return)
# ============================================================
print("\n" + "=" * 60)
print("SECTION 2: Function Type Hints")
print("=" * 60)

def calculate_age(birth_year: int) -> int:
    """
    Calculate user age from birth year.

    Args:
        birth_year: The year person was born (int)

    Returns:
        int: The calculated age
    """
    current_year = 2024
    return current_year - birth_year

age = calculate_age(1995)
print(f"Age calculated: {age}, Type: {type(age).__name__}")


def greet_user(first_name: str, last_name: str) -> str:
    """Greet a user by full name."""
    return f"Hello, {first_name} {last_name}!"

greeting = greet_user("Alice", "Smith")
print(f"Greeting: {greeting}")


def create_user_profile(name: str, age: int, is_active: bool) -> None:
    """
    Create and display user profile.
    Return type is None (function doesn't return anything).
    """
    print(f"  -> Creating profile for {name}, age {age}, active={is_active}")

create_user_profile("Bob", 30, True)


# ============================================================
# SECTION 3: Complex Return Types
# ============================================================
print("\n" + "=" * 60)
print("SECTION 3: Complex Return Types")
print("=" * 60)

def process_payment(amount: float) -> bool:
    """Process payment and return success status."""
    is_success = amount > 0
    print(f"  -> Processing Rs{amount}... Success: {is_success}")
    return is_success

result = process_payment(500)
print(f"Payment result: {result}, Type: {type(result).__name__}")


def calculate_discount(price: float, discount_percent: int) -> float:
    """Calculate discounted price."""
    discount_amount = price * (discount_percent / 100)
    return price - discount_amount

final_price = calculate_discount(1000, 20)
print(f"Original: Rs1000, Discount: 20%, Final: Rs{final_price}")


# ============================================================
# SECTION 4: Optional Type Annotations
# ============================================================
print("\n" + "=" * 60)
print("SECTION 4: Optional Type Annotations")
print("=" * 60)

from typing import Optional

def find_user_by_id(user_id: int) -> Optional[str]:
    """
    Find user by ID. Returns name if found, None otherwise.
    Optional[str] means: str or None
    """
    users = {1: "Alice", 2: "Bob", 3: "Charlie"}
    return users.get(user_id)  # Returns None if not found

found_user = find_user_by_id(1)
print(f"Found user: {found_user}, Type: {type(found_user).__name__}")

not_found = find_user_by_id(999)
print(f"Not found: {not_found}, Type: {type(not_found).__name__}")


def get_user_email(user_id: int) -> Optional[str]:
    """Return email or None if user doesn't exist."""
    emails = {1: "alice@example.com", 2: "bob@example.com"}
    return emails.get(user_id)

email = get_user_email(2)
print(f"Email: {email if email else 'Not available'}")


# ============================================================
# SECTION 5: Union Types (Multiple Possible Types)
# ============================================================
print("\n" + "=" * 60)
print("SECTION 5: Union Types")
print("=" * 60)

from typing import Union

def convert_to_int(value: Union[str, int]) -> int:
    """
    Convert value to int. Accepts string or int.
    Union[str, int] means: either str or int
    """
    if isinstance(value, str):
        return int(value)
    return value

result1 = convert_to_int("42")
result2 = convert_to_int(42)
print(f"Converted '42': {result1}, Type: {type(result1).__name__}")
print(f"Converted 42: {result2}, Type: {type(result2).__name__}")


def format_user_id(user_id: Union[int, str]) -> str:
    """Format user ID regardless of input type."""
    return f"USER_{str(user_id).upper()}"

print(f"Formatted ID (int): {format_user_id(123)}")
print(f"Formatted ID (str): {format_user_id('abc')}")


# ============================================================
# SECTION 6: Python 3.10+ Union Syntax (X | Y)
# ============================================================
print("\n" + "=" * 60)
print("SECTION 6: Modern Union Syntax (Python 3.10+)")
print("=" * 60)

# This is cleaner alternative to Union[str, int]
def modern_union_example(value: str | int) -> str:
    """Same as Union[str, int], but cleaner syntax."""
    return f"Value: {value}, Type: {type(value).__name__}"

print(modern_union_example("hello"))
print(modern_union_example(42))

# And for Optional[X] -> X | None
def modern_optional_example(user_id: int) -> str | None:
    """Same as Optional[str], but cleaner syntax."""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

print(f"Modern Optional: {modern_optional_example(1)}")
print(f"Modern Optional (None): {modern_optional_example(999)}")


# ============================================================
# KEY POINTS
# ============================================================
print("\n" + "=" * 60)
print("KEY POINTS")
print("=" * 60)
print("""
1. Type hints are DOCUMENTATION, not enforcement
   - Python allows wrong types at runtime
   - Use type checkers (mypy) to catch errors

2. Basic types: str, int, float, bool, None

3. Function hints: param_name: Type -> ReturnType

4. Optional[Type] = Type or None (for nullable values)

5. Union[Type1, Type2] = Type1 or Type2

6. Python 3.10+: Use 'Type1 | Type2' instead of Union

7. Always document return type with -> Type

8. Type hints improve code clarity and IDE autocompletion
""")
