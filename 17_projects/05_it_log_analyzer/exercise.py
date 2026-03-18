# ───────────────────────────────────────────────────────────────
# Exercises — Project 05: IT Log Analyzer
# ───────────────────────────────────────────────────────────────

# Use the logs from solution.py.

# ── Exercise 1: Parse Logs and Display First 5 Errors ────────────
# Task: Parse all logs. Extract only ERROR-level logs. Display first 5.
#
# Requirements:
#   - Use parse_log_line() or create your own parser
#   - Filter for level == "ERROR"
#   - Collect into a list
#   - Print first 5 with timestamp, IP, and message
#
# Hint: Use a for loop to parse and filter.

# --- your code here ---




# ── Exercise 2: Count Errors by IP Address ─────────────────────────
# Task: Build a dict mapping IP → error_count.
#       Print IPs sorted by error frequency (highest first).
#
# Requirements:
#   - Iterate through logs
#   - Filter for ERROR level
#   - Count errors per IP using a dict
#   - Sort by count (use sorted + lambda)
#   - Print top 3 IPs
#
# Hint: Similar to suspicious_ips logic, but display all ranked.

# --- your code here ---




# ── Exercise 3: Warning Message Analysis ───────────────────────────
# Task: Extract all WARNING messages. Count occurrences of each message type.
#       Show which warning is most common.
#
# Requirements:
#   - Filter for level == "WARNING"
#   - Use a dict to count each unique warning message
#   - Find the most common one
#   - Print count and the message
#
# Hint: Use similar logic to top_error_messages.

# --- your code here ---




# ───────────────────────────────────────────────────────────────
# Expected outputs (for self-check):
#
# Ex1: First 5 ERROR logs
#      2024-01-15 10:23:45 192.168.1.101 Database connection failed
#      ... (4 more)
#
# Ex2: Errors by IP (top 3)
#      192.168.1.101: 5 errors
#      192.168.1.104: 2 errors
#      192.168.1.106: 1 error
#
# Ex3: Most common warning
#      "High memory usage detected" or similar: 1 occurrence
#      (There are multiple warnings with 1 occurrence each)
# ───────────────────────────────────────────────────────────────
