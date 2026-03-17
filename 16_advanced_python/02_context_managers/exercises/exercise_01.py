"""
============================================================
EXERCISE 01 — Context Managers
============================================================
Problem: Create a custom context manager for file logging.

Requirements:
  1. Create a FileLogger context manager (class-based)
  2. __enter__ opens a log file, __exit__ closes it
  3. Provide a log() method to write messages
  4. Ensure file closes even if exception occurs
  5. Optionally add timestamps to log messages

Bonus:
  - Use @contextmanager decorator for decorator-based version
  - Handle file open errors gracefully
============================================================
"""

# Step 1: Create FileLogger class-based context manager
# class FileLogger:
#     def __init__(self, filename: str):
#         self.filename = filename
#         self.file = None
#
#     def __enter__(self):
#         # Open log file
#         pass
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         # Close log file
#         pass
#
#     def log(self, message: str) -> None:
#         # Write to file
#         pass

# Step 2: Test your implementation
if __name__ == "__main__":
    print("=" * 60)
    print("EXERCISE 01 - File Logger Context Manager")
    print("=" * 60)

    # Test case 1: Normal logging
    # with FileLogger("app.log") as logger:
    #     logger.log("Application started")
    #     logger.log("Processing data...")
    #     logger.log("Done")

    # Test case 2: Exception handling
    # try:
    #     with FileLogger("error.log") as logger:
    #         logger.log("Starting risky operation")
    #         raise ValueError("Invalid data")
    #         logger.log("This won't execute")
    # except ValueError:
    #     print("Exception caught, file closed properly")

    print("\nImplementation pending...")
