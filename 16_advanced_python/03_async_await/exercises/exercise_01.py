"""
============================================================
EXERCISE 01 — Async/Await: Concurrent Task Execution
============================================================
Problem: Build an order processing system that processes
multiple customer orders concurrently.

Requirements:
  1. Create async function to simulate processing an order
     (should take 1-2 seconds, simulating I/O)
  2. Process 5 different orders concurrently (not sequentially)
  3. Measure and display total time taken
  4. Collect results from all orders
  5. Display which order completed and when
  6. Handle potential errors gracefully

Challenge: What would be the difference if you awaited
each order sequentially vs using gather()?

Hints: Use asyncio.gather() for concurrent execution
       Use asyncio.sleep() to simulate I/O
       Use time.time() to measure execution time
       Use asyncio.create_task() for explicit task creation
============================================================
"""

import asyncio
import time
from datetime import datetime
from typing import List, Dict

# TODO: Implement your solution below

async def process_order(order_id: int, processing_time: float = None) -> Dict:
    """
    Simulate processing a customer order asynchronously.

    Args:
        order_id: The order ID to process
        processing_time: Time to simulate (1-2 seconds typical)

    Returns:
        Dict with order status, completion time, order_id
    """
    # TODO: Implement this function
    # Step 1: Print order processing started with timestamp
    # Step 2: Simulate I/O with asyncio.sleep()
    # Step 3: Return dict with order_id, status, timestamp
    pass


async def main() -> None:
    """
    Main function to demonstrate concurrent order processing.

    TODO: Implement this function
    Step 1: Record start time
    Step 2: Create tasks for 5 different orders using asyncio.gather()
    Step 3: Wait for all orders to complete
    Step 4: Calculate total time elapsed
    Step 5: Display results
    """
    pass


if __name__ == "__main__":
    print("=" * 60)
    print("EXERCISE 01 - Concurrent Order Processing")
    print("=" * 60)

    # Run the async main function
    # asyncio.run(main())

    # TODO: Uncomment above to test your implementation

    print("\nImplementation pending...")
    print("\nExpected behavior:")
    print("- Process 5 orders concurrently")
    print("- Total time should be ~1-2 seconds (not 5-10)")
    print("- All orders complete roughly at the same time")
