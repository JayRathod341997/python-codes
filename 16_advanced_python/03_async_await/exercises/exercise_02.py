"""
============================================================
EXERCISE 02 — Async Context Managers and Resource Management
============================================================
Problem: Build an async database connection manager that
properly handles connection setup, cleanup, and errors.

Requirements:
  1. Create AsyncDatabase class with async context manager
  2. Implement __aenter__ to simulate connection (0.5 sec)
  3. Implement __aexit__ to simulate disconnection (0.2 sec)
  4. Create method to execute queries asynchronously
  5. Test context manager with multiple database operations
  6. Ensure connection is closed even if exception occurs
  7. Count total queries executed

Challenge: What happens if an exception occurs inside
the context manager? Is cleanup still called?

Hints: Use async def __aenter__ and async def __aexit__
       Use asyncio.sleep() to simulate connection time
       Wrap the context in try/except to test error handling
       Return value from __aenter__ is assigned to 'as' variable
============================================================
"""

import asyncio
from typing import List, Optional

# TODO: Implement your solution below

class AsyncDatabase:
    """
    Async database connection manager.

    Should implement async context manager protocol:
    - __aenter__: Establish connection
    - __aexit__: Close connection and cleanup
    """

    def __init__(self, db_name: str):
        # TODO: Initialize database name and state
        pass

    async def __aenter__(self):
        # TODO: Implement async entry
        # - Simulate connection time with asyncio.sleep(0.5)
        # - Print "Connecting to {db_name}"
        # - Return self
        pass

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # TODO: Implement async exit
        # - Simulate disconnect time with asyncio.sleep(0.2)
        # - Print "Disconnected from {db_name}"
        # - Handle exception info if needed
        # - Return False (don't suppress exceptions)
        pass

    async def execute_query(self, query: str) -> List[str]:
        """Execute a database query."""
        # TODO: Implement query execution
        # - Simulate query execution with asyncio.sleep(0.1)
        # - Return list of results (e.g., ["row1", "row2", "row3"])
        pass

    async def execute_multiple_queries(self, queries: List[str]) -> List[List[str]]:
        """Execute multiple queries concurrently."""
        # TODO: Implement concurrent query execution
        # - Use asyncio.gather() to run queries concurrently
        # - Return list of all results
        pass


async def test_basic_context_manager() -> None:
    """Test basic context manager functionality."""
    # TODO: Implement test
    # - Create AsyncDatabase instance
    # - Use 'async with' to connect
    # - Execute one query
    # - Verify disconnection happens
    pass


async def test_exception_handling() -> None:
    """Test that cleanup happens even when exception occurs."""
    # TODO: Implement test
    # - Create AsyncDatabase instance
    # - Use try/except around 'async with'
    # - Raise an exception inside the context
    # - Verify that __aexit__ was still called
    pass


async def test_multiple_queries() -> None:
    """Test executing multiple queries concurrently."""
    # TODO: Implement test
    # - Create AsyncDatabase instance
    # - Execute 3 queries concurrently using execute_multiple_queries
    # - Collect and display results
    pass


async def main() -> None:
    """Run all tests."""
    # TODO: Uncomment to run tests
    # await test_basic_context_manager()
    # await test_exception_handling()
    # await test_multiple_queries()
    pass


if __name__ == "__main__":
    print("=" * 60)
    print("EXERCISE 02 - Async Context Managers")
    print("=" * 60)

    # asyncio.run(main())

    print("\nImplementation pending...")
    print("\nExpected behavior:")
    print("- Database connects and disconnects automatically")
    print("- Cleanup happens even if exception occurs")
    print("- Multiple queries execute concurrently")
    print("- Total query time should be ~0.1s (not 0.3s for 3 queries)")
