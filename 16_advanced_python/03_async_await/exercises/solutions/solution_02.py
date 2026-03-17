"""
============================================================
SOLUTION 02 — Async Context Managers and Resource Management
============================================================
Complete working solution for Exercise 02.
Demonstrates async context manager protocol and cleanup.
============================================================
"""

import asyncio
from typing import List, Optional
from datetime import datetime


class AsyncDatabase:
    """
    Async database connection manager.

    Implements async context manager protocol:
    - __aenter__: Establish connection
    - __aexit__: Close connection and cleanup
    """

    def __init__(self, db_name: str):
        """Initialize database with name and state."""
        self.db_name = db_name
        self.is_connected = False
        self.query_count = 0

    async def __aenter__(self):
        """
        Async entry: establish connection when entering 'async with' block.

        Simulates connection setup that requires I/O (network, authentication).
        """
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Connecting to {self.db_name}...")
        await asyncio.sleep(0.5)  # Simulate connection time

        self.is_connected = True
        print(f"Connected to {self.db_name}")

        return self  # This is what 'as' variable refers to

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Async exit: cleanup connection when exiting 'async with' block.

        Called even if exception occurred (cleanup is guaranteed).
        """
        print(f"Disconnecting from {self.db_name}...")
        await asyncio.sleep(0.2)  # Simulate disconnect time

        self.is_connected = False
        print(f"Disconnected from {self.db_name} "
              f"(executed {self.query_count} queries)")

        # exc_type will be None if no exception
        if exc_type is not None:
            print(f"Exception occurred during context: {exc_type.__name__}: {exc_val}")

        # Return False to propagate exceptions (don't suppress)
        return False

    async def execute_query(self, query: str) -> List[str]:
        """
        Execute a single database query asynchronously.

        Args:
            query: SQL query string

        Returns:
            List of result rows
        """
        if not self.is_connected:
            raise RuntimeError("Database not connected")

        self.query_count += 1
        print(f"Executing query {self.query_count}: {query}")

        # Simulate query execution time
        await asyncio.sleep(0.1)

        # Return simulated results
        return [f"row_{i}" for i in range(1, 4)]

    async def execute_multiple_queries(self, queries: List[str]) -> List[List[str]]:
        """
        Execute multiple queries concurrently.

        All queries run at the same time (not sequentially).

        Args:
            queries: List of SQL query strings

        Returns:
            List of result lists (one per query)
        """
        if not self.is_connected:
            raise RuntimeError("Database not connected")

        # Create tasks for all queries (will run concurrently)
        tasks = [
            asyncio.create_task(self.execute_query(query))
            for query in queries
        ]

        # Wait for all queries to complete
        results = await asyncio.gather(*tasks)
        return results


async def test_basic_context_manager() -> None:
    """
    Test 1: Basic context manager functionality.

    Demonstrates automatic connection/disconnection.
    """
    print("=" * 60)
    print("TEST 1: Basic Context Manager")
    print("=" * 60)

    async with AsyncDatabase("production_db") as db:
        # Connection is now active
        assert db.is_connected, "Should be connected"

        # Execute a query
        results = await db.execute_query("SELECT * FROM users")
        print(f"Results: {results}\n")

    # Connection is now closed (automatically)
    assert not db.is_connected, "Should be disconnected after context"
    print()


async def test_exception_handling() -> None:
    """
    Test 2: Exception handling and guaranteed cleanup.

    Even when an exception occurs, __aexit__ is called.
    This ensures connection is always closed.
    """
    print("=" * 60)
    print("TEST 2: Exception Handling")
    print("=" * 60)

    try:
        async with AsyncDatabase("test_db") as db:
            results = await db.execute_query("SELECT * FROM products")
            print(f"Results: {results}\n")

            # Deliberately raise an exception
            print("Simulating query error...")
            raise ValueError("Invalid query syntax!")

    except ValueError as e:
        print(f"Caught exception: {e}\n")

    # Even though exception occurred, db is still disconnected
    assert not db.is_connected, "Connection should be closed despite exception"
    print("Connection was properly closed despite exception!\n")


async def test_multiple_queries() -> None:
    """
    Test 3: Executing multiple queries concurrently.

    Demonstrates that multiple queries run in parallel,
    not sequentially. Time should be ~0.1s (not 0.3s for 3 queries).
    """
    print("=" * 60)
    print("TEST 3: Concurrent Query Execution")
    print("=" * 60)

    import time

    async with AsyncDatabase("analytics_db") as db:
        queries = [
            "SELECT COUNT(*) FROM users",
            "SELECT SUM(amount) FROM orders",
            "SELECT AVG(rating) FROM reviews",
        ]

        start = time.time()

        # Execute all queries concurrently
        all_results = await db.execute_multiple_queries(queries)

        elapsed = time.time() - start

        print(f"\nResults from {len(queries)} concurrent queries:")
        for i, results in enumerate(all_results, 1):
            print(f"  Query {i}: {results}")

        print(f"\nTotal time: {elapsed:.2f}s")
        print(f"(If sequential, would take ~0.3s; concurrent takes ~0.1s)\n")


async def test_context_manager_ensures_cleanup() -> None:
    """
    Test 4: Verify context manager cleanup order.

    Demonstrates that connection closes in correct order,
    and database state is properly updated.
    """
    print("=" * 60)
    print("TEST 4: Cleanup Order")
    print("=" * 60)

    db = AsyncDatabase("cleanup_test_db")

    print(f"Before context: is_connected={db.is_connected}, query_count={db.query_count}")

    async with db:
        print(f"Inside context: is_connected={db.is_connected}, query_count={db.query_count}")

        await db.execute_query("SELECT 1")
        await db.execute_query("SELECT 2")

        print(f"After queries: is_connected={db.is_connected}, query_count={db.query_count}")

    print(f"After context: is_connected={db.is_connected}, query_count={db.query_count}\n")


async def main() -> None:
    """Run all tests."""
    await test_basic_context_manager()
    await test_exception_handling()
    await test_multiple_queries()
    await test_context_manager_ensures_cleanup()


if __name__ == "__main__":
    print("=" * 60)
    print("SOLUTION 02 - Async Context Managers")
    print("=" * 60)
    print()

    asyncio.run(main())

    print("=" * 60)
    print("KEY LEARNINGS")
    print("=" * 60)
    print("""
1. Async context managers implement __aenter__ and __aexit__
2. __aenter__ runs when entering 'async with' block
3. __aexit__ runs when exiting (even if exception occurs)
4. Return value from __aenter__ is assigned to 'as' variable
5. __aexit__ receives exception info if one occurred
6. Returning False from __aexit__ propagates exceptions
7. Returning True from __aexit__ suppresses exceptions
8. Use for resource management (connections, files, sessions)
9. Guarantees cleanup even if errors occur
10. Can execute multiple async operations concurrently
""")
