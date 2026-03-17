"""
============================================================
TOPIC: 01_coroutines_basics.py
Real-world context: Building an order processing system
that handles multiple customer requests concurrently
without blocking.
============================================================
"""

import asyncio
import time
from datetime import datetime

print("=" * 60)
print("SECTION 1: Defining and Running Coroutines")
print("=" * 60)

# Define a coroutine function (async def)
async def process_order(order_id: int) -> str:
    """
    Simulate processing a customer order asynchronously.
    In real-world: could be database query, payment processing, etc.
    """
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Processing order {order_id}...")
    await asyncio.sleep(1)  # Simulate I/O wait (network, database)
    return f"Order {order_id} completed"


# Key point: Calling a coroutine doesn't execute it
order_coro = process_order(1)
print(f"Type of result: {type(order_coro)}")
print(f"Coroutine: {order_coro}")

# You must use asyncio.run() to execute the coroutine
result = asyncio.run(process_order(101))
print(f"Result: {result}\n")


# ============================================================
# SECTION 2: Multiple Sequential Coroutines (Slow)
# ============================================================
print("=" * 60)
print("SECTION 2: Sequential Execution (Awaiting one-by-one)")
print("=" * 60)

async def sequential_orders():
    """
    Process orders one at a time.
    Each order waits for the previous to complete.
    Total time: sum of all wait times.
    """
    start = time.time()

    result1 = await process_order(1)
    result2 = await process_order(2)
    result3 = await process_order(3)

    elapsed = time.time() - start
    print(f"Sequential execution took: {elapsed:.1f}s")

asyncio.run(sequential_orders())
print()


# ============================================================
# SECTION 3: Concurrent Execution with gather()
# ============================================================
print("=" * 60)
print("SECTION 3: Concurrent Execution with gather()")
print("=" * 60)

async def concurrent_orders():
    """
    Process multiple orders concurrently.
    All orders run at the same time.
    Total time: duration of longest order, not sum.
    """
    start = time.time()

    # gather() creates tasks and waits for all to complete
    results = await asyncio.gather(
        process_order(1),
        process_order(2),
        process_order(3)
    )

    elapsed = time.time() - start
    print(f"Concurrent execution took: {elapsed:.1f}s")
    print(f"Results: {results}")

asyncio.run(concurrent_orders())
print()


# ============================================================
# SECTION 4: Creating and Managing Tasks
# ============================================================
print("=" * 60)
print("SECTION 4: Creating Tasks Explicitly")
print("=" * 60)

async def task_management_example():
    """
    Demonstrate creating tasks explicitly with create_task().
    Tasks are scheduled immediately; awaiting later.
    """
    print("Creating tasks without waiting immediately...")

    # Create tasks (scheduled, not awaited yet)
    task1 = asyncio.create_task(process_order(10))
    task2 = asyncio.create_task(process_order(11))
    task3 = asyncio.create_task(process_order(12))

    print("All tasks created. They're running concurrently now.")

    # Await all tasks
    results = await asyncio.gather(task1, task2, task3)
    print(f"All tasks completed: {results}")

asyncio.run(task_management_example())
print()


# ============================================================
# SECTION 5: Returning Different Data Types from Coroutines
# ============================================================
print("=" * 60)
print("SECTION 5: Different Return Types")
print("=" * 60)

async def get_user_info(user_id: int) -> dict:
    """Return structured data from coroutine."""
    await asyncio.sleep(0.5)
    return {
        "user_id": user_id,
        "name": f"User{user_id}",
        "email": f"user{user_id}@example.com"
    }

async def get_product_price(product_id: int) -> float:
    """Return numeric data from coroutine."""
    await asyncio.sleep(0.5)
    return 99.99 * product_id

async def fetch_all_data():
    """Fetch different types of data concurrently."""
    user, price = await asyncio.gather(
        get_user_info(1),
        get_product_price(5)
    )

    print(f"User info: {user}")
    print(f"Product price: ${price:.2f}")

asyncio.run(fetch_all_data())
print()


# ============================================================
# SECTION 6: Exception Handling in Coroutines
# ============================================================
print("=" * 60)
print("SECTION 6: Exception Handling")
print("=" * 60)

async def risky_operation(should_fail: bool) -> str:
    """Simulate operation that might fail."""
    await asyncio.sleep(0.5)
    if should_fail:
        raise ValueError("Operation failed!")
    return "Operation succeeded"

async def handle_exceptions():
    """Handle exceptions in concurrent operations."""
    print("Handling exceptions in gather()...")

    # Option 1: Stop on first exception (raises)
    try:
        results = await asyncio.gather(
            risky_operation(False),
            risky_operation(True),
            risky_operation(False),
            return_exceptions=False  # Default: raise on first error
        )
    except ValueError as e:
        print(f"Caught exception: {e}")

    print()

    # Option 2: Collect all results/exceptions
    results = await asyncio.gather(
        risky_operation(False),
        risky_operation(True),
        risky_operation(False),
        return_exceptions=True  # Return exceptions as values
    )

    print(f"Results with return_exceptions=True:")
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"  [{i}] Error: {result}")
        else:
            print(f"  [{i}] Success: {result}")

asyncio.run(handle_exceptions())
print()


# ============================================================
# SECTION 7: Async Functions Can Call Other Async Functions
# ============================================================
print("=" * 60)
print("SECTION 7: Nested Async Calls")
print("=" * 60)

async def verify_payment(order_id: int) -> bool:
    """Verify payment for an order."""
    await asyncio.sleep(0.3)
    print(f"  Payment verified for order {order_id}")
    return True

async def ship_order(order_id: int) -> str:
    """Ship an order after verification."""
    verified = await verify_payment(order_id)  # Nested async call
    if verified:
        await asyncio.sleep(0.3)
        return f"Order {order_id} shipped"
    return "Shipping failed"

async def process_complete_order(order_id: int):
    """Complete order pipeline."""
    result = await ship_order(order_id)
    print(f"Result: {result}")

asyncio.run(process_complete_order(99))
print()


# ============================================================
# SECTION 8: await vs asyncio.run()
# ============================================================
print("=" * 60)
print("SECTION 8: When to Use await vs asyncio.run()")
print("=" * 60)

async def main():
    """
    Main entry point for async program.
    Use 'await' inside async functions.
    Use 'asyncio.run()' to start from sync code.
    """

    # Inside async function, use 'await'
    result = await process_order(200)
    print(f"Result inside main: {result}")

    # You CANNOT use asyncio.run() inside an async function
    # result = asyncio.run(process_order(201))  # ✗ Error!

# At module level or in sync code, use asyncio.run()
if __name__ == "__main__":
    asyncio.run(main())

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
Key points:
1. Define async functions with 'async def'
2. Call async functions to get coroutine objects (don't execute yet)
3. Use 'await' inside async functions to execute coroutines
4. Use 'asyncio.run()' at top level to start async program
5. Use 'asyncio.gather()' to run multiple coroutines concurrently
6. Tasks created with create_task() run in background
7. Exceptions can be caught or collected with return_exceptions=True
8. Concurrent execution significantly faster than sequential for I/O-bound work
""")
