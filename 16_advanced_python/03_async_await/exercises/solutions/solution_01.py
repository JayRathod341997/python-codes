"""
============================================================
SOLUTION 01 — Concurrent Order Processing
============================================================
Complete working solution for Exercise 01.
Demonstrates asyncio.gather() for concurrent task execution.
============================================================
"""

import asyncio
import time
import random
from datetime import datetime
from typing import List, Dict


async def process_order(order_id: int, processing_time: float = None) -> Dict:
    """
    Simulate processing a customer order asynchronously.

    In real world: would call payment gateway, update inventory,
    send confirmation email, etc.

    Args:
        order_id: The order ID to process
        processing_time: Time to simulate (1-2 seconds typical)

    Returns:
        Dict with order_id, status, completion timestamp
    """
    # Use provided time or random between 1-2 seconds
    if processing_time is None:
        processing_time = random.uniform(1.0, 2.0)

    start_time = datetime.now().strftime("%H:%M:%S")
    print(f"[{start_time}] Processing order {order_id}... (will take {processing_time:.1f}s)")

    # Simulate I/O operation (network, database, etc.)
    await asyncio.sleep(processing_time)

    completion_time = datetime.now().strftime("%H:%M:%S")
    return {
        "order_id": order_id,
        "status": "completed",
        "started_at": start_time,
        "completed_at": completion_time,
        "processing_time": processing_time
    }


async def main() -> None:
    """
    Main function to demonstrate concurrent order processing.

    Key insight: gather() runs all coroutines concurrently.
    Total time is approximately the longest individual order,
    not the sum of all orders.
    """
    print("Starting concurrent order processing...\n")

    # Record start time
    start = time.time()

    # Create tasks for 5 different orders
    # These will run concurrently, not sequentially
    results = await asyncio.gather(
        process_order(101),
        process_order(102),
        process_order(103),
        process_order(104),
        process_order(105),
    )

    # Calculate total time elapsed
    elapsed = time.time() - start

    # Display results
    print(f"\n{'=' * 60}")
    print(f"ORDER PROCESSING SUMMARY")
    print(f"{'=' * 60}")

    for result in results:
        print(
            f"Order {result['order_id']}: "
            f"{result['status'].upper()} "
            f"({result['processing_time']:.1f}s) "
            f"[{result['started_at']} -> {result['completed_at']}]"
        )

    print(f"\nTotal time elapsed: {elapsed:.1f}s")
    print(f"Number of orders: {len(results)}")
    print(f"Average processing time per order: {sum(r['processing_time'] for r in results) / len(results):.1f}s")
    print(f"\nNote: Total time ({elapsed:.1f}s) is much less than sum of individual times")
    print(f"({sum(r['processing_time'] for r in results):.1f}s) due to concurrency!")


async def sequential_example() -> None:
    """
    Compare with sequential processing to show the benefit.
    This is much slower because each order must complete
    before the next one starts.
    """
    print("\n" + "=" * 60)
    print("SEQUENTIAL PROCESSING (for comparison)")
    print("=" * 60)
    print("Processing orders one at a time...\n")

    start = time.time()

    # Await each order sequentially (one after another)
    results = []
    for order_id in range(101, 106):
        result = await process_order(order_id)
        results.append(result)

    elapsed = time.time() - start

    print(f"\nSequential processing took: {elapsed:.1f}s")
    print(f"This is much slower than concurrent processing!")


if __name__ == "__main__":
    print("=" * 60)
    print("SOLUTION 01 - Concurrent Order Processing")
    print("=" * 60)
    print()

    # Run concurrent version
    asyncio.run(main())

    # Show sequential version for comparison
    asyncio.run(sequential_example())

    print("\n" + "=" * 60)
    print("KEY LEARNINGS")
    print("=" * 60)
    print("""
1. asyncio.gather() runs all coroutines concurrently
2. Concurrent execution time = longest individual task
3. Sequential execution time = sum of all tasks
4. For I/O-bound work, async is much faster
5. Use asyncio.gather() when order doesn't matter
6. Use tasks when you need more control
7. Each coroutine must be awaited eventually
8. random.uniform() simulates variable operation time
""")
