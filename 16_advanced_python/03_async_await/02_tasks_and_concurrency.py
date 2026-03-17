"""
============================================================
TOPIC: 02_tasks_and_concurrency.py
Real-world context: Building a web crawler that fetches
multiple URLs concurrently without using threading.
============================================================
"""

import asyncio
import time
import random
from datetime import datetime
from typing import List

print("=" * 60)
print("SECTION 1: Creating Tasks with create_task()")
print("=" * 60)

async def fetch_page(url: str) -> dict:
    """Simulate fetching a web page."""
    fetch_time = random.uniform(0.5, 2.0)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Fetching {url}... (simulated {fetch_time:.1f}s)")
    await asyncio.sleep(fetch_time)
    return {
        "url": url,
        "status": 200,
        "content_length": random.randint(1000, 10000)
    }

async def web_crawler_with_tasks():
    """
    Crawl multiple URLs using tasks.
    Tasks run concurrently; we don't wait for each one before starting the next.
    """
    start = time.time()

    urls = [
        "https://example.com",
        "https://python.org",
        "https://stackoverflow.com",
        "https://github.com"
    ]

    # Create tasks (they start running immediately)
    tasks = [asyncio.create_task(fetch_page(url)) for url in urls]

    print(f"Created {len(tasks)} tasks. All running concurrently.")
    print(f"(Without tasks, this would take {sum([2, 1, 1.5, 0.8]):.1f}s sequential)")

    # Wait for all tasks to complete
    results = await asyncio.gather(*tasks)

    elapsed = time.time() - start
    print(f"\nAll pages fetched in {elapsed:.1f}s (concurrent)")
    print(f"Results:")
    for result in results:
        print(f"  {result['url']}: {result['content_length']} bytes")

asyncio.run(web_crawler_with_tasks())
print()


# ============================================================
# SECTION 2: Task Monitoring and Status
# ============================================================
print("=" * 60)
print("SECTION 2: Monitoring Task Status")
print("=" * 60)

async def monitored_fetch(task_id: int, delay: float) -> str:
    """A task that takes specific delay."""
    print(f"Task {task_id} started")
    await asyncio.sleep(delay)
    print(f"Task {task_id} completed")
    return f"Result {task_id}"

async def monitor_tasks():
    """Create tasks and monitor their status."""

    # Create multiple tasks with different delays
    tasks = [
        asyncio.create_task(monitored_fetch(1, 1.0)),
        asyncio.create_task(monitored_fetch(2, 2.0)),
        asyncio.create_task(monitored_fetch(3, 0.5)),
    ]

    print(f"Created {len(tasks)} tasks")
    print(f"Task statuses before awaiting:")
    for i, task in enumerate(tasks):
        print(f"  Task {i}: done={task.done()}, cancelled={task.cancelled()}")

    # Wait a moment
    await asyncio.sleep(0.7)

    print(f"\nTask statuses after 0.7 seconds:")
    for i, task in enumerate(tasks):
        print(f"  Task {i}: done={task.done()}, cancelled={task.cancelled()}")

    # Wait for all to complete
    results = await asyncio.gather(*tasks)

    print(f"\nTask statuses after all completed:")
    for i, task in enumerate(tasks):
        print(f"  Task {i}: done={task.done()}, cancelled={task.cancelled()}")

asyncio.run(monitor_tasks())
print()


# ============================================================
# SECTION 3: Using asyncio.wait() for Partial Completion
# ============================================================
print("=" * 60)
print("SECTION 3: asyncio.wait() - Wait for Partial Completion")
print("=" * 60)

async def process_data(item_id: int) -> dict:
    """Process a data item with variable processing time."""
    process_time = random.uniform(0.5, 2.5)
    await asyncio.sleep(process_time)
    return {
        "item_id": item_id,
        "processed_at": datetime.now().isoformat(),
        "duration": process_time
    }

async def wait_for_first_completion():
    """
    Wait for FIRST task to complete, then process others.
    This is useful when you want to start handling results as they come.
    """
    print("Creating 5 processing tasks...")

    tasks = {
        asyncio.create_task(process_data(i))
        for i in range(5)
    }

    # Wait for first task to complete
    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_COMPLETED
    )

    print(f"\nFirst completed:")
    for task in done:
        print(f"  {task.result()}")

    print(f"\nStill pending: {len(pending)} tasks")

    # Wait for next one
    done, pending = await asyncio.wait(
        pending,
        return_when=asyncio.FIRST_COMPLETED
    )

    print(f"\nNext completed:")
    for task in done:
        print(f"  {task.result()}")

    print(f"\nRemaining pending: {len(pending)} tasks")

    # Wait for all remaining
    if pending:
        done, _ = await asyncio.wait(pending)
        print(f"\nAll remaining completed: {len(done)} tasks")

asyncio.run(wait_for_first_completion())
print()


# ============================================================
# SECTION 4: Task Cancellation
# ============================================================
print("=" * 60)
print("SECTION 4: Cancelling Tasks")
print("=" * 60)

async def long_running_task(task_id: int) -> str:
    """A task that runs for a long time."""
    try:
        for i in range(10):
            print(f"Task {task_id}: step {i+1}/10")
            await asyncio.sleep(0.5)
        return f"Task {task_id} completed"
    except asyncio.CancelledError:
        print(f"Task {task_id}: Received cancellation request")
        raise  # IMPORTANT: Must re-raise to signal cancellation

async def cancel_tasks_demo():
    """Demonstrate task cancellation."""

    task1 = asyncio.create_task(long_running_task(1))
    task2 = asyncio.create_task(long_running_task(2))
    task3 = asyncio.create_task(long_running_task(3))

    # Let tasks run for a bit
    await asyncio.sleep(1.5)

    print("\nCancelling task2...")
    task2.cancel()

    # Try to await all tasks
    results = await asyncio.gather(
        task1, task2, task3,
        return_exceptions=True  # Capture CancelledError
    )

    print("\nResults:")
    for i, result in enumerate(results, 1):
        if isinstance(result, asyncio.CancelledError):
            print(f"  Task {i}: Cancelled")
        else:
            print(f"  Task {i}: {result}")

asyncio.run(cancel_tasks_demo())
print()


# ============================================================
# SECTION 5: Task Groups (Python 3.11+)
# ============================================================
print("=" * 60)
print("SECTION 5: Structured Concurrency (Python 3.11+ TaskGroup)")
print("=" * 60)

async def modern_concurrent_example():
    """
    TaskGroup is modern structured concurrency (Python 3.11+).
    Automatically waits for all tasks and handles exceptions.
    """
    # Check Python version
    import sys
    if sys.version_info >= (3, 11):
        async def task(n: int):
            await asyncio.sleep(0.5)
            return f"Task {n} done"

        try:
            async with asyncio.TaskGroup() as tg:
                task1 = tg.create_task(task(1))
                task2 = tg.create_task(task(2))
                task3 = tg.create_task(task(3))

            # All tasks completed successfully
            print(f"TaskGroup example:")
            print(f"  task1.result() = {task1.result()}")
            print(f"  task2.result() = {task2.result()}")
            print(f"  task3.result() = {task3.result()}")
        except Exception as e:
            print(f"TaskGroup caught exception: {e}")
    else:
        print(f"Python {sys.version_info.major}.{sys.version_info.minor}")
        print("TaskGroup requires Python 3.11+")
        print("Use asyncio.gather() for older versions")

asyncio.run(modern_concurrent_example())
print()


# ============================================================
# SECTION 6: Timeout with Tasks
# ============================================================
print("=" * 60)
print("SECTION 6: Timeout Handling")
print("=" * 60)

async def slow_api(api_name: str, duration: float) -> str:
    """Simulate API call with specific duration."""
    try:
        await asyncio.sleep(duration)
        return f"{api_name} completed"
    except asyncio.TimeoutError:
        return f"{api_name} timed out"

async def timeout_example():
    """Handle timeouts on individual tasks."""

    api1 = asyncio.create_task(slow_api("API1", 1.0))
    api2 = asyncio.create_task(slow_api("API2", 3.0))
    api3 = asyncio.create_task(slow_api("API3", 0.5))

    # Apply timeout to individual tasks
    try:
        result1 = await asyncio.wait_for(api1, timeout=2.0)
        print(f"Result 1: {result1}")
    except asyncio.TimeoutError:
        print("API1 timed out")

    # You can also timeout groups of tasks
    try:
        results = await asyncio.wait_for(
            asyncio.gather(api2, api3),
            timeout=2.0
        )
        print(f"Results 2,3: {results}")
    except asyncio.TimeoutError:
        print("API2/API3 group timed out")

asyncio.run(timeout_example())
print()


# ============================================================
# SECTION 7: Combining Concurrent Tasks with Results Processing
# ============================================================
print("=" * 60)
print("SECTION 7: Processing Results from Concurrent Tasks")
print("=" * 60)

async def data_processing_pipeline():
    """
    Real-world example: Fetch data from multiple sources concurrently,
    then process results.
    """
    async def fetch_source(source_name: str) -> dict:
        await asyncio.sleep(random.uniform(0.5, 1.5))
        return {
            "source": source_name,
            "data": [1, 2, 3, 4, 5],
            "timestamp": datetime.now().isoformat()
        }

    # Fetch from multiple sources concurrently
    sources = ["database", "api", "cache"]
    tasks = [asyncio.create_task(fetch_source(s)) for s in sources]
    results = await asyncio.gather(*tasks)

    # Process results
    print("Collected results from all sources:")
    total_items = 0
    for result in results:
        item_count = len(result["data"])
        total_items += item_count
        print(f"  {result['source']}: {item_count} items at {result['timestamp']}")

    print(f"Total items collected: {total_items}")

asyncio.run(data_processing_pipeline())
print()

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
Key points about tasks:
1. create_task() schedules coroutine to run concurrently
2. Tasks run in background; you control when to await them
3. gather() awaits multiple tasks and returns results as list
4. wait() provides more control: can wait for FIRST_COMPLETED
5. Tasks can be cancelled with task.cancel()
6. CancelledError must be caught and re-raised
7. Task status can be checked with task.done(), task.cancelled()
8. wait_for() applies timeout to tasks
9. TaskGroup (Python 3.11+) is modern structured concurrency
10. Proper task management enables highly concurrent applications
""")
