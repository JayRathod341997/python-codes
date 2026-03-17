"""
============================================================
TOPIC: 03_async_context_managers.py
Real-world context: Managing database connections, HTTP
clients, file handles asynchronously with proper cleanup.
============================================================
"""

import asyncio
from datetime import datetime

print("=" * 60)
print("SECTION 1: Async Context Managers Basics")
print("=" * 60)

class AsyncDatabaseConnection:
    """
    Simulates an async database connection.
    Implements async context manager protocol.
    """

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.is_connected = False

    async def __aenter__(self):
        """
        Called when entering 'async with' block.
        Async setup (e.g., connecting to database).
        """
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Connecting to {self.db_name}...")
        await asyncio.sleep(0.5)  # Simulate connection time
        self.is_connected = True
        print(f"Connected to {self.db_name}")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Called when exiting 'async with' block.
        Async cleanup (e.g., closing connection).
        """
        print(f"Disconnecting from {self.db_name}...")
        await asyncio.sleep(0.3)  # Simulate disconnect time
        self.is_connected = False
        print(f"Disconnected from {self.db_name}")

        # Return False to propagate exceptions
        # Return True to suppress exceptions
        return False

    async def execute_query(self, query: str) -> list:
        """Execute a database query."""
        if not self.is_connected:
            raise RuntimeError("Database not connected")

        print(f"Executing: {query}")
        await asyncio.sleep(0.3)  # Simulate query execution
        return ["row1", "row2", "row3"]


async def basic_async_context_manager():
    """Use async context manager to manage database connection."""

    async with AsyncDatabaseConnection("mydb") as db:
        # Connection is automatically established
        results = await db.execute_query("SELECT * FROM users")
        print(f"Results: {results}")
        # Connection is automatically closed when exiting block

    print(f"Connection closed. is_connected={db.is_connected}")

asyncio.run(basic_async_context_manager())
print()


# ============================================================
# SECTION 2: Exception Handling in Async Context Managers
# ============================================================
print("=" * 60)
print("SECTION 2: Exception Handling")
print("=" * 60)

class RobustAsyncConnection:
    """Database connection that handles exceptions gracefully."""

    def __init__(self, db_name: str):
        self.db_name = db_name

    async def __aenter__(self):
        print(f"Connecting to {self.db_name}...")
        await asyncio.sleep(0.2)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Handle exceptions in context."""
        print(f"Cleaning up {self.db_name}...")
        await asyncio.sleep(0.1)

        if exc_type is not None:
            print(f"Exception occurred: {exc_type.__name__}: {exc_val}")
            # Return True to suppress exception, False to propagate
            return False  # Propagate exception
        return False

    async def query(self, sql: str):
        await asyncio.sleep(0.2)
        return f"Result of {sql}"


async def exception_handling_demo():
    """Demonstrate exception handling in async context manager."""

    # Example 1: No exception
    print("Example 1: Normal operation")
    async with RobustAsyncConnection("db1") as db:
        result = await db.query("SELECT 1")
        print(f"Query result: {result}")

    print()

    # Example 2: Exception inside context
    print("Example 2: Exception handling")
    try:
        async with RobustAsyncConnection("db2") as db:
            result = await db.query("SELECT 1")
            raise ValueError("Query validation failed!")
    except ValueError as e:
        print(f"Caught exception: {e}")

asyncio.run(exception_handling_demo())
print()


# ============================================================
# SECTION 3: Multiple Async Context Managers
# ============================================================
print("=" * 60)
print("SECTION 3: Multiple Async Context Managers")
print("=" * 60)

class AsyncService:
    """Generic async service that requires setup/cleanup."""

    def __init__(self, service_name: str):
        self.service_name = service_name

    async def __aenter__(self):
        print(f"Initializing {self.service_name}...")
        await asyncio.sleep(0.2)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"Cleaning up {self.service_name}...")
        await asyncio.sleep(0.1)
        return False

    async def call(self):
        return f"Result from {self.service_name}"


async def multiple_context_managers():
    """
    Use multiple async context managers in sequence.
    Each is entered/exited in order.
    """

    # Multiple context managers: both opened/closed in order
    async with AsyncService("database") as db, \
               AsyncService("cache") as cache, \
               AsyncService("logger") as logger:

        result = await db.call()
        cached = await cache.call()
        logged = await logger.call()

        print(f"Results: {result}, {cached}, {logged}")

    # All cleaned up in reverse order

asyncio.run(multiple_context_managers())
print()


# ============================================================
# SECTION 4: Custom Async Context Manager with asynccontextmanager
# ============================================================
print("=" * 60)
print("SECTION 4: Using contextlib.asynccontextmanager")
print("=" * 60)

from contextlib import asynccontextmanager
from typing import AsyncGenerator

@asynccontextmanager
async def async_resource(resource_id: int) -> AsyncGenerator:
    """
    Create async context manager using decorator.
    Code before yield: setup
    Code after yield: cleanup
    """
    print(f"Setting up resource {resource_id}...")
    await asyncio.sleep(0.2)

    try:
        yield f"Resource{resource_id}"  # This is what 'as' variable gets
    finally:
        print(f"Cleaning up resource {resource_id}...")
        await asyncio.sleep(0.1)


async def decorator_context_manager():
    """Use decorator-based async context manager."""

    async with async_resource(1) as res:
        print(f"Using {res}")

    async with async_resource(2) as res:
        print(f"Using {res}")

asyncio.run(decorator_context_manager())
print()


# ============================================================
# SECTION 5: Real-World: HTTP Client Context Manager
# ============================================================
print("=" * 60)
print("SECTION 5: Real-World: HTTP Client Simulation")
print("=" * 60)

class AsyncHTTPClient:
    """
    Simulates an async HTTP client (like httpx.AsyncClient).
    Manages connection pooling and resource cleanup.
    """

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session_active = False
        self.requests_made = 0

    async def __aenter__(self):
        """Initialize HTTP session."""
        print(f"Creating HTTP session for {self.base_url}...")
        await asyncio.sleep(0.2)
        self.session_active = True
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Close HTTP session and cleanup."""
        print(f"Closing HTTP session (made {self.requests_made} requests)...")
        await asyncio.sleep(0.1)
        self.session_active = False
        return False

    async def get(self, endpoint: str) -> dict:
        """Make GET request."""
        if not self.session_active:
            raise RuntimeError("Session not active")

        self.requests_made += 1
        await asyncio.sleep(0.3)  # Simulate network request
        return {
            "status": 200,
            "data": f"Response from {endpoint}"
        }

    async def post(self, endpoint: str, data: dict) -> dict:
        """Make POST request."""
        if not self.session_active:
            raise RuntimeError("Session not active")

        self.requests_made += 1
        await asyncio.sleep(0.3)  # Simulate network request
        return {
            "status": 201,
            "data": f"Created via {endpoint}"
        }


async def http_client_example():
    """
    Demonstrate HTTP client context manager.
    Without context manager, you'd need to manually close the session.
    """

    async with AsyncHTTPClient("https://api.example.com") as client:
        # Make multiple requests
        user = await client.get("/users/1")
        print(f"User: {user}")

        new_post = await client.post("/posts", {"title": "New"})
        print(f"Created: {new_post}")

        comments = await client.get("/posts/1/comments")
        print(f"Comments: {comments}")

    # Session automatically closed
    # No need to call client.close()

asyncio.run(http_client_example())
print()


# ============================================================
# SECTION 6: Nested Async Context Managers
# ============================================================
print("=" * 60)
print("SECTION 6: Nested Context Managers")
print("=" * 60)

@asynccontextmanager
async def nested_resource(level: int, parent: str = "root"):
    """Context manager that can be nested."""
    indent = "  " * level
    print(f"{indent}Entering level {level} (parent: {parent})")
    await asyncio.sleep(0.1)

    try:
        yield f"resource_{level}"
    finally:
        print(f"{indent}Exiting level {level}")
        await asyncio.sleep(0.1)


async def nested_context_demo():
    """Demonstrate nested async context managers."""

    async with nested_resource(0) as res0:
        print(f"Using {res0}")

        async with nested_resource(1, res0) as res1:
            print(f"Using {res1}")

            async with nested_resource(2, res1) as res2:
                print(f"Using {res2}")

asyncio.run(nested_context_demo())
print()


# ============================================================
# SECTION 7: Context Manager for Transaction-like Operations
# ============================================================
print("=" * 60)
print("SECTION 7: Transaction-like Operations")
print("=" * 60)

@asynccontextmanager
async def async_transaction(transaction_id: int):
    """Context manager for database transactions."""
    print(f"BEGIN TRANSACTION {transaction_id}")
    await asyncio.sleep(0.1)

    try:
        yield transaction_id
        # If no exception, commit
        print(f"COMMIT TRANSACTION {transaction_id}")
        await asyncio.sleep(0.1)
    except Exception as e:
        # On exception, rollback
        print(f"ROLLBACK TRANSACTION {transaction_id} (error: {e})")
        await asyncio.sleep(0.1)
        raise


async def transaction_example():
    """Demonstrate transaction context manager."""

    # Successful transaction
    print("Example 1: Successful transaction")
    async with async_transaction(1) as tx_id:
        print(f"Executing operations in transaction {tx_id}")

    print()

    # Failed transaction
    print("Example 2: Failed transaction")
    try:
        async with async_transaction(2) as tx_id:
            print(f"Executing operations in transaction {tx_id}")
            raise ValueError("Operation failed!")
    except ValueError:
        print("Exception caught and handled")

asyncio.run(transaction_example())
print()

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
Async context managers:
1. Implement __aenter__ (async setup) and __aexit__ (async cleanup)
2. Used with 'async with' statement
3. Automatically cleanup resources even if exceptions occur
4. Can manage connections, sessions, transactions, file handles
5. Multiple managers can be chained with commas
6. @asynccontextmanager decorator simplifies implementation
7. Perfect for resource management in async code
8. Exception info available in __aexit__ parameters
9. Return True from __aexit__ to suppress exceptions
10. Always cleanup in __aexit__, even on exceptions
""")
