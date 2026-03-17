"""
============================================================
TOPIC: 04_real_world_httpx.py
Real-world context: Building a scalable web scraper/API
client that fetches data from multiple sources concurrently.
This demonstrates real-world async patterns without
requiring httpx (using simulated async operations).
============================================================
"""

import asyncio
import random
from datetime import datetime
from typing import List, Optional, Dict, Any
from dataclasses import dataclass

print("=" * 60)
print("SECTION 1: Simulated Async HTTP Client")
print("=" * 60)

@dataclass
class HTTPResponse:
    """Represents an HTTP response."""
    status_code: int
    body: Any
    headers: Dict[str, str]
    url: str

    def json(self) -> Any:
        """Parse response as JSON."""
        return self.body


class AsyncHTTPClient:
    """
    Simulated async HTTP client (mimics httpx.AsyncClient).
    In production, you'd use: async with httpx.AsyncClient() as client:
    """

    def __init__(self, base_url: str = "", timeout: float = 10.0):
        self.base_url = base_url
        self.timeout = timeout
        self.request_count = 0
        self.is_connected = False

    async def __aenter__(self):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Opening HTTP session...")
        self.is_connected = True
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing HTTP session (made {self.request_count} requests)")
        self.is_connected = False
        return False

    async def get(self, endpoint: str) -> HTTPResponse:
        """Make async GET request."""
        if not self.is_connected:
            raise RuntimeError("Session not connected")

        url = f"{self.base_url}{endpoint}"
        self.request_count += 1

        # Simulate network latency
        latency = random.uniform(0.5, 2.0)
        print(f"GET {url} (simulated {latency:.1f}s)")
        await asyncio.sleep(latency)

        return HTTPResponse(
            status_code=200,
            body={"url": url, "data": f"Data from {endpoint}"},
            headers={"Content-Type": "application/json"},
            url=url
        )

    async def post(self, endpoint: str, json: dict) -> HTTPResponse:
        """Make async POST request."""
        if not self.is_connected:
            raise RuntimeError("Session not connected")

        url = f"{self.base_url}{endpoint}"
        self.request_count += 1

        latency = random.uniform(0.3, 1.5)
        print(f"POST {url} with {json} (simulated {latency:.1f}s)")
        await asyncio.sleep(latency)

        return HTTPResponse(
            status_code=201,
            body={"id": random.randint(1, 10000), "created": True},
            headers={"Content-Type": "application/json"},
            url=url
        )


# ============================================================
# SECTION 2: Fetching Multiple URLs Concurrently
# ============================================================
print("=" * 60)
print("SECTION 2: Concurrent API Requests")
print("=" * 60)

async def fetch_user_data(client: AsyncHTTPClient, user_id: int) -> dict:
    """Fetch a single user's data."""
    response = await client.get(f"/users/{user_id}")
    return response.json()

async def fetch_multiple_users():
    """Fetch data for multiple users concurrently."""
    start = datetime.now()

    async with AsyncHTTPClient(base_url="https://api.example.com") as client:
        # Create tasks for multiple users
        user_ids = [1, 2, 3, 4, 5]
        tasks = [
            asyncio.create_task(fetch_user_data(client, uid))
            for uid in user_ids
        ]

        # Wait for all to complete
        results = await asyncio.gather(*tasks)

        # Process results
        for user_data in results:
            print(f"  {user_data}")

    elapsed = (datetime.now() - start).total_seconds()
    print(f"Fetched {len(user_ids)} users in {elapsed:.1f}s (concurrent)")

asyncio.run(fetch_multiple_users())
print()


# ============================================================
# SECTION 3: Error Handling with Retries
# ============================================================
print("=" * 60)
print("SECTION 3: Retry Logic with Exponential Backoff")
print("=" * 60)

async def fetch_with_retry(
    client: AsyncHTTPClient,
    endpoint: str,
    max_retries: int = 3,
    backoff_factor: float = 1.0
) -> Optional[HTTPResponse]:
    """
    Fetch with automatic retry on failure.
    Uses exponential backoff between retries.
    """

    for attempt in range(max_retries):
        try:
            # Simulate occasional failures
            if random.random() < 0.3:  # 30% failure rate
                raise Exception(f"Network error on attempt {attempt + 1}")

            response = await client.get(endpoint)
            return response
        except Exception as e:
            if attempt == max_retries - 1:
                print(f"Failed after {max_retries} attempts: {e}")
                return None

            # Exponential backoff
            wait_time = backoff_factor * (2 ** attempt)
            print(f"Attempt {attempt + 1} failed, retrying in {wait_time:.1f}s...")
            await asyncio.sleep(wait_time)

    return None


async def retry_example():
    """Demonstrate retry logic."""
    async with AsyncHTTPClient(base_url="https://api.example.com") as client:
        print("Attempting to fetch with retries...")

        response = await fetch_with_retry(
            client,
            "/unreliable-endpoint",
            max_retries=3,
            backoff_factor=0.5
        )

        if response:
            print(f"Success: {response.json()}")
        else:
            print("Failed to fetch after retries")

asyncio.run(retry_example())
print()


# ============================================================
# SECTION 4: Parallel Batch Processing
# ============================================================
print("=" * 60)
print("SECTION 4: Processing Data in Parallel Batches")
print("=" * 60)

async def process_api_batch(client: AsyncHTTPClient, batch_ids: List[int]) -> List[dict]:
    """Process a batch of items from API."""
    tasks = [
        asyncio.create_task(client.get(f"/items/{item_id}"))
        for item_id in batch_ids
    ]

    responses = await asyncio.gather(*tasks)
    return [r.json() for r in responses]


async def batch_processing_example():
    """
    Process items in batches.
    Useful for rate limiting: process 10 at a time, then next 10.
    """
    async with AsyncHTTPClient(base_url="https://api.example.com") as client:
        item_ids = list(range(1, 26))  # 25 items

        # Process in batches of 5
        batch_size = 5
        all_results = []

        for i in range(0, len(item_ids), batch_size):
            batch = item_ids[i:i + batch_size]
            print(f"\nProcessing batch {i // batch_size + 1}: items {batch}")

            results = await process_api_batch(client, batch)
            all_results.extend(results)

            # Add delay between batches (rate limiting)
            if i + batch_size < len(item_ids):
                print("Waiting before next batch...")
                await asyncio.sleep(0.5)

        print(f"\nProcessed total {len(all_results)} items")

asyncio.run(batch_processing_example())
print()


# ============================================================
# SECTION 5: Timeout Management
# ============================================================
print("=" * 60)
print("SECTION 5: Timeout Handling")
print("=" * 60)

async def fetch_with_timeout(
    client: AsyncHTTPClient,
    endpoint: str,
    timeout: float
) -> Optional[HTTPResponse]:
    """Fetch with timeout."""
    try:
        response = await asyncio.wait_for(
            client.get(endpoint),
            timeout=timeout
        )
        return response
    except asyncio.TimeoutError:
        print(f"Request timed out after {timeout}s")
        return None


async def timeout_example():
    """Demonstrate timeout handling."""
    async with AsyncHTTPClient(base_url="https://api.example.com") as client:
        # Fast request with tight timeout
        response = await fetch_with_timeout(client, "/users/1", timeout=3.0)
        if response:
            print(f"Got response: {response.json()}")

        print()

        # Potentially slow request with generous timeout
        response = await fetch_with_timeout(client, "/slow-endpoint", timeout=5.0)

asyncio.run(timeout_example())
print()


# ============================================================
# SECTION 6: Rate Limiting
# ============================================================
print("=" * 60)
print("SECTION 6: Rate Limiting Concurrent Requests")
print("=" * 60)

class RateLimiter:
    """Limit concurrent requests using a semaphore."""

    def __init__(self, max_concurrent: int):
        self.semaphore = asyncio.Semaphore(max_concurrent)

    async def acquire(self):
        """Acquire a slot."""
        async with self.semaphore:
            yield


async def fetch_with_rate_limit(
    client: AsyncHTTPClient,
    endpoint: str,
    rate_limiter: RateLimiter
) -> dict:
    """Fetch with rate limiting."""
    async with rate_limiter.semaphore:
        response = await client.get(endpoint)
        return response.json()


async def rate_limiting_example():
    """Demonstrate rate limiting."""
    async with AsyncHTTPClient(base_url="https://api.example.com") as client:
        # Limit to 3 concurrent requests
        rate_limiter = RateLimiter(max_concurrent=3)

        endpoints = [f"/items/{i}" for i in range(10)]

        tasks = [
            asyncio.create_task(
                fetch_with_rate_limit(client, endpoint, rate_limiter)
            )
            for endpoint in endpoints
        ]

        results = await asyncio.gather(*tasks)
        print(f"Fetched {len(results)} items with rate limiting")

asyncio.run(rate_limiting_example())
print()


# ============================================================
# SECTION 7: Pipeline Pattern - Chain Async Operations
# ============================================================
print("=" * 60)
print("SECTION 7: Async Pipeline Pattern")
print("=" * 60)

async def fetch_user_pipeline(client: AsyncHTTPClient, user_id: int):
    """
    Pipeline: Fetch user -> Fetch their posts -> Fetch comments on first post
    Sequential operations where each depends on previous result.
    """

    # Step 1: Fetch user
    user_response = await client.get(f"/users/{user_id}")
    user_data = user_response.json()
    print(f"User: {user_data}")

    # Step 2: Fetch user's posts
    posts_response = await client.get(f"/users/{user_id}/posts")
    posts = posts_response.json()
    print(f"Posts: {posts}")

    # Step 3: Fetch comments on first post (if exists)
    if isinstance(posts, dict):
        post_id = posts.get("data", {}).get("id", 1)
        comments_response = await client.get(f"/posts/{post_id}/comments")
        comments = comments_response.json()
        print(f"Comments: {comments}")

    return {"user": user_data, "posts": posts}


async def pipeline_example():
    """Demonstrate async pipeline."""
    async with AsyncHTTPClient(base_url="https://api.example.com") as client:
        result = await fetch_user_pipeline(client, user_id=1)
        print(f"Pipeline complete: {len(str(result))} chars of data")

asyncio.run(pipeline_example())
print()


# ============================================================
# SECTION 8: Fan-Out Pattern - One Source, Many Destinations
# ============================================================
print("=" * 60)
print("SECTION 8: Fan-Out Pattern")
print("=" * 60)

async def fan_out_example():
    """
    Fan-out: Fetch one piece of data, then use it to fetch many related items.
    Example: Get featured product, then fetch reviews, inventory, recommendations.
    """

    async with AsyncHTTPClient(base_url="https://api.example.com") as client:
        # Fetch featured product
        product_response = await client.get("/featured-product")
        product = product_response.json()
        product_id = 1

        print(f"Featured product: {product}")
        print(f"\nFanning out to fetch related data...")

        # Fan out: fetch multiple related items concurrently
        tasks = [
            asyncio.create_task(client.get(f"/products/{product_id}/reviews")),
            asyncio.create_task(client.get(f"/products/{product_id}/inventory")),
            asyncio.create_task(client.get(f"/products/{product_id}/recommendations")),
            asyncio.create_task(client.get(f"/products/{product_id}/ratings")),
        ]

        results = await asyncio.gather(*tasks)

        print("\nResults from fan-out:")
        for i, response in enumerate(results, 1):
            print(f"  Result {i}: {response.json()}")

asyncio.run(fan_out_example())
print()

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
Real-world async HTTP patterns:
1. Use context managers (async with) for resource cleanup
2. Create tasks for concurrent requests
3. Implement retry logic with exponential backoff
4. Use batch processing for rate limiting
5. Set timeouts on long-running requests
6. Use Semaphore for concurrent request limits
7. Chain operations in pipelines (sequential when needed)
8. Use fan-out pattern (one -> many)
9. Gather results and handle exceptions
10. Always close sessions properly
11. In production, use httpx or aiohttp instead of simulated client
12. Monitor request counts and performance metrics
""")
