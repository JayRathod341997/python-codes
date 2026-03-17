"""
============================================================
SOLUTION 01 — Context Managers: File Logger
============================================================
Complete implementation of FileLogger context manager.
============================================================
"""

from datetime import datetime
from contextlib import contextmanager


# Solution 1: Class-based FileLogger
class FileLogger:
    """Context manager for file-based logging."""

    def __init__(self, filename: str, timestamp: bool = True) -> None:
        self.filename = filename
        self.file = None
        self.timestamp = timestamp

    def __enter__(self):
        print(f"[LOG] Opening {self.filename}")
        self.file = open(self.filename, "a")
        self._write("[LOG] Session started")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self._write(f"[ERROR] {exc_type.__name__}: {exc_val}")
        self._write("[LOG] Session ended")
        if self.file:
            self.file.close()
        print(f"[LOG] Closed {self.filename}")
        return False

    def log(self, message: str) -> None:
        """Log a message."""
        self._write(f"[INFO] {message}")

    def error(self, message: str) -> None:
        """Log an error."""
        self._write(f"[ERROR] {message}")

    def _write(self, message: str) -> None:
        """Internal write method with optional timestamp."""
        if self.timestamp:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"{timestamp} {message}"
        if self.file:
            self.file.write(message + "\n")
            self.file.flush()


# Solution 2: Decorator-based FileLogger
@contextmanager
def file_logger(filename: str, timestamp: bool = True):
    """Context manager for file logging using decorator."""
    print(f"[LOG] Opening {filename}")
    f = None
    try:
        f = open(filename, "a")
        yield f
    except Exception as e:
        if f:
            f.write(f"[ERROR] {type(e).__name__}: {e}\n")
        raise
    finally:
        if f:
            f.close()
        print(f"[LOG] Closed {filename}")


if __name__ == "__main__":
    print("=" * 60)
    print("SOLUTION 01 - File Logger Context Manager")
    print("=" * 60)

    # Test 1: Class-based logger
    print("\n1. Class-based FileLogger:")
    with FileLogger("app.log") as logger:
        logger.log("Application started")
        logger.log("Processing user data")
        logger.log("Database sync completed")

    # Test 2: Exception handling
    print("\n2. Error handling (file closes automatically):")
    try:
        with FileLogger("error.log") as logger:
            logger.log("Starting payment process")
            logger.error("Payment gateway timeout")
            raise ConnectionError("Network unreachable")
    except ConnectionError as e:
        print(f"Exception caught outside context: {e}")
        print("But file was closed properly!")

    # Test 3: Multiple loggers
    print("\n3. Multiple loggers:")
    with FileLogger("debug.log") as debug_log, \
         FileLogger("info.log") as info_log:
        debug_log.log("Debug: Variable x = 42")
        info_log.log("Info: Process completed")

    # Read and display logs
    print("\n4. Log contents:")
    for log_file in ["app.log", "error.log", "debug.log", "info.log"]:
        try:
            with open(log_file, "r") as f:
                print(f"\n--- {log_file} ---")
                print(f.read())
        except FileNotFoundError:
            pass

    # Cleanup
    import os
    for f in ["app.log", "error.log", "debug.log", "info.log"]:
        if os.path.exists(f):
            os.remove(f)
    print("\n[CLEANUP] Test log files removed.")
