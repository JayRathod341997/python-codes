"""
============================================================
TOPIC: 05_advanced_patterns.py
Real-world context: Advanced type patterns used in modern
Python libraries (Pydantic, FastAPI, etc.)
============================================================
"""

from typing import Literal, TypedDict, Final, overload, Any
from dataclasses import dataclass

# ============================================================
# SECTION 1: Literal Types (Restrict to Specific Values)
# ============================================================
print("=" * 60)
print("SECTION 1: Literal Types")
print("=" * 60)

# Literal restricts a value to specific constants
def set_log_level(level: Literal["DEBUG", "INFO", "WARNING", "ERROR"]) -> None:
    """
    Set log level. Only accepts these exact strings.
    Much better than just str!
    """
    print(f"  -> Setting log level to {level}")


print("Valid log levels:")
set_log_level("DEBUG")
set_log_level("INFO")
set_log_level("ERROR")

# set_log_level("VERBOSE")  # Error from type checker!


# Literal with multiple types
def process_status(status: Literal[200, 404, 500]) -> str:
    """Process HTTP status code. Only accepts these specific codes."""
    messages = {
        200: "Success",
        404: "Not Found",
        500: "Internal Server Error"
    }
    return messages[status]


print("\nHTTP status processing:")
print(f"Status 200: {process_status(200)}")
print(f"Status 404: {process_status(404)}")


# Real-world: Configuration modes
def start_app(mode: Literal["development", "staging", "production"]) -> None:
    """Start app in specific mode."""
    configs = {
        "development": "Debug=True, Database=localhost",
        "staging": "Debug=False, Database=staging.db",
        "production": "Debug=False, Database=prod.db"
    }
    print(f"  -> Starting app in {mode} mode")
    print(f"  -> Config: {configs[mode]}")


print("\nApp startup:")
start_app("development")


# ============================================================
# SECTION 2: TypedDict (Typed Dictionaries)
# ============================================================
print("\n" + "=" * 60)
print("SECTION 2: TypedDict - Dictionary with Known Keys")
print("=" * 60)

# Define structure of a dictionary
class UserData(TypedDict):
    """User information dictionary."""
    name: str
    email: str
    age: int
    is_active: bool


# Now you can use it as a type hint
def create_user(user: UserData) -> None:
    """Create a user from UserData."""
    print(f"  -> Creating user {user['name']} ({user['email']})")
    print(f"  -> Age: {user['age']}, Active: {user['is_active']}")


user: UserData = {
    "name": "Alice",
    "email": "alice@example.com",
    "age": 28,
    "is_active": True
}
create_user(user)


# Real-world: API response
class APIResponse(TypedDict):
    """Standard API response format."""
    status: Literal["success", "error"]
    data: Any
    message: str


def handle_response(response: APIResponse) -> None:
    """Process API response."""
    if response["status"] == "success":
        print(f"  OK {response['message']}")
    else:
        print(f"  Error {response['message']}")


api_response: APIResponse = {
    "status": "success",
    "data": {"user_id": 123},
    "message": "User created successfully"
}
handle_response(api_response)


# TypedDict with optional fields (total=False)
class OptionalUserData(TypedDict, total=False):
    """User data where some fields are optional."""
    name: str  # Required
    email: str  # Required
    phone: str  # Optional
    address: str  # Optional


optional_user: OptionalUserData = {
    "name": "Bob",
    "email": "bob@example.com"
    # phone and address are optional
}
print(f"\nOptional user: {optional_user}")


# ============================================================
# SECTION 3: Final (Prevent Reassignment)
# ============================================================
print("\n" + "=" * 60)
print("SECTION 3: Final - Immutable/Constant Values")
print("=" * 60)

# Final prevents reassignment
MAX_RETRIES: Final[int] = 3
print(f"Max retries: {MAX_RETRIES}")

# MAX_RETRIES = 5  # Error from type checker!


# Final in classes
class Configuration:
    """Application configuration."""

    VERSION: Final = "1.2.0"
    MAX_CONNECTIONS: Final[int] = 100
    DEFAULT_TIMEOUT: Final[float] = 30.0

    # VERSION = "2.0"  # Error from type checker!


print(f"\nConfiguration:")
print(f"  Version: {Configuration.VERSION}")
print(f"  Max connections: {Configuration.MAX_CONNECTIONS}")
print(f"  Default timeout: {Configuration.DEFAULT_TIMEOUT}s")


# Final with methods (can't be overridden)
class Base:
    """Base class with final method."""

    def core_logic(self) -> None:
        """This method should not be overridden."""
        print("  -> Core logic executed")


# If you try to override, type checker will complain
# (But Python doesn't prevent it at runtime)


# ============================================================
# SECTION 4: @overload (Multiple Signatures)
# ============================================================
print("\n" + "=" * 60)
print("SECTION 4: @overload - Multiple Function Signatures")
print("=" * 60)

# @overload defines what types are accepted (for type checkers)
# The actual implementation comes after

@overload
def convert(value: int) -> str:
    ...  # Type signature only


@overload
def convert(value: str) -> int:
    ...  # Type signature only


# Actual implementation
def convert(value):
    """Convert between int and str."""
    if isinstance(value, int):
        return str(value)
    elif isinstance(value, str):
        return int(value)
    else:
        raise TypeError(f"Cannot convert {type(value)}")


print("Overload examples:")
result1 = convert(42)  # Type checker knows this returns str
print(f"convert(42) = {result1}, Type: {type(result1).__name__}")

result2 = convert("123")  # Type checker knows this returns int
print(f"convert('123') = {result2}, Type: {type(result2).__name__}")


# Real-world: fetch function
@overload
def fetch(url: str) -> str:
    ...  # Returns text


@overload
def fetch(url: str, json: bool) -> dict:
    ...  # Returns JSON


def fetch(url, json=False):
    """Fetch data from URL."""
    print(f"  -> Fetching {url}")
    if json:
        return {"status": "success", "data": []}
    return "<html>...</html>"


print("\nFetch examples:")
text = fetch("https://example.com")
print(f"Text result: {text[:20]}...")

json_data = fetch("https://api.example.com", json=True)
print(f"JSON result: {json_data}")


# ============================================================
# SECTION 5: Type Narrowing
# ============================================================
print("\n" + "=" * 60)
print("SECTION 5: Type Narrowing")
print("=" * 60)

from typing import Union

def process_input(value: Union[int, str]) -> None:
    """
    Process input that could be int or str.
    Type narrowing: after isinstance check, type checker knows the type.
    """
    if isinstance(value, int):
        # Type checker knows value is int here
        print(f"  -> Processing integer: {value * 2}")
    elif isinstance(value, str):
        # Type checker knows value is str here
        print(f"  -> Processing string: {value.upper()}")


process_input(42)
process_input("hello")


# Type narrowing with Optional
def get_user_name(user_id: int) -> str | None:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)


user_name = get_user_name(1)
if user_name is not None:
    # Type checker knows user_name is str here (not None)
    print(f"User name: {user_name.upper()}")
else:
    print("User not found")


# ============================================================
# SECTION 6: Type Aliases
# ============================================================
print("\n" + "=" * 60)
print("SECTION 6: Type Aliases")
print("=" * 60)

# Create a meaningful alias for complex types
UserID = int
Email = str
Score = float

def create_user_record(user_id: UserID, email: Email, score: Score) -> None:
    """Create a user record with type aliases."""
    print(f"  -> User {user_id}: {email} (Score: {score})")


create_user_record(1, "alice@example.com", 95.5)


# Alias for complex types
from typing import Dict, List
UserScores = Dict[str, List[float]]

def calculate_average(scores: UserScores) -> None:
    """Calculate average score for each user."""
    for name, score_list in scores.items():
        avg = sum(score_list) / len(score_list) if score_list else 0
        print(f"  {name}: {avg:.2f}")


data: UserScores = {
    "Alice": [95, 92, 88],
    "Bob": [87, 90, 85]
}
calculate_average(data)


# ============================================================
# SECTION 7: Using Any (Type Escape Hatch)
# ============================================================
print("\n" + "=" * 60)
print("SECTION 7: Using Any (Last Resort)")
print("=" * 60)

# Any means "any type" - disables type checking
def process_any(data: Any) -> Any:
    """
    Accept any type, return any type.
    Use Any only when absolutely necessary!
    """
    return data


print(f"Process any: {process_any(42)}")
print(f"Process any: {process_any('hello')}")
print(f"Process any: {process_any([1, 2, 3])}")


# Better: be specific when possible
from typing import Union, List

def process_specific(data: Union[int, str, List]) -> Union[int, str, List]:
    """More specific than Any."""
    return data


print(f"\nProcess specific: {process_specific(42)}")


# ============================================================
# KEY POINTS
# ============================================================
print("\n" + "=" * 60)
print("KEY POINTS")
print("=" * 60)
print("""
1. Literal[T1, T2, ...]: Restrict to specific values
   Example: Literal["success", "error"]

2. TypedDict: Define dictionary structure with keys and types
   class User(TypedDict):
       name: str
       age: int

3. Final: Mark as immutable (can't be reassigned)
   MAX_RETRIES: Final[int] = 3

4. @overload: Define multiple function signatures
   @overload
   def convert(x: int) -> str: ...
   @overload
   def convert(x: str) -> int: ...

5. Type narrowing: isinstance() helps type checker understand types
   if isinstance(value, int):
       # Type checker knows it's int here

6. Type aliases: Create meaningful names for complex types
   UserID = int
   Scores = Dict[str, List[float]]

7. Avoid Any: Only use when truly necessary
   Any disables type checking

8. These patterns make code self-documenting and catch errors early
""")
