# ───────────────────────────────────────────────────────────────
# Exercises — Project 13: Async/Await
# ───────────────────────────────────────────────────────────────

# ── Exercise 1: Create PatientRecord and Fetch Single Patient ──────
# Task: Using @dataclass PatientRecord, create and populate one manually.
#       Then use async fetch_patient to populate concurrently.
#
# Requirements:
#   - Define PatientRecord with fields (patient_id, name, etc.)
#   - Create instance manually with mock data
#   - Create async function that fetches all 5 data types
#   - Run with asyncio.run()
#   - Print the populated record
#
# Hint: @dataclass removes __init__ boilerplate. asyncio.run() runs async main.

# --- your code here ---




# ── Exercise 2: Fetch Multiple Patients Concurrently ───────────────
# Task: Fetch data for 5 patients concurrently. Compare time vs serial.
#
# Requirements:
#   - Create async function to fetch single patient
#   - Create async function to fetch multiple patients using asyncio.gather
#   - Time both approaches
#   - Print time comparison
#   - Show speedup factor
#
# Hint: asyncio.gather(*tasks) runs all concurrently. time.time() for timing.

# --- your code here ---




# ── Exercise 3: Error Handling in Async Pipeline ───────────────────
# Task: Add error handling to async fetch functions.
#       If one API fails, others still complete.
#
# Requirements:
#   - Modify one fetch function to randomly fail
#   - Use try/except or return_exceptions=True in gather
#   - Handle partial failures gracefully
#   - Print which APIs succeeded/failed
#   - Continue fetching other patients
#
# Hint: asyncio.gather(..., return_exceptions=True) returns exceptions instead of raising.

# --- your code here ---




# ───────────────────────────────────────────────────────────────
# Expected outputs (for self-check):
#
# Ex1: Single patient with @dataclass
#      PatientRecord(patient_id=101, name='Alice', lab_results=[...], ...)
#
# Ex2: Multiple patients timing
#      Concurrent: 1.05s (5 * 1s in parallel ≈ 1s total)
#      Serial: 5.10s (5 * 1s sequentially)
#      Speedup: 4.9x faster
#
# Ex3: Error handling in pipeline
#      Patient 1: ✓ All APIs succeeded
#      Patient 2: ⚠ Lab API failed, others OK
#      Patient 3: ✓ All APIs succeeded
#      Graceful degradation shown
# ───────────────────────────────────────────────────────────────
