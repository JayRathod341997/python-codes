# ───────────────────────────────────────────────────────────────
# Exercises — Project 09: Config Manager
# ───────────────────────────────────────────────────────────────

# ── Exercise 1: Load and Validate Configuration ─────────────────────
# Task: Load app_config.json. Validate that required keys exist:
#       - database.host (must be non-empty string)
#       - api.timeout (must be > 0)
#       Report validation results.
#
# Requirements:
#   - Load config from JSON
#   - Check existence and type of config keys
#   - Print validation pass/fail for each key
#
# Hint: Use try/except and isinstance() for type checking.

# --- your code here ---




# ── Exercise 2: Update Configuration and Log Changes ──────────────
# Task: Update config values and verify changelog.txt is created.
#
# Requirements:
#   - Update 3 config values using set()
#   - Save to JSON
#   - Read changelog.txt and print all entries
#   - Each entry should have timestamp
#
# Hint: Changelog is appended to, not overwritten.

# --- your code here ---




# ── Exercise 3: Export Config to Environment Variables ──────────────
# Task: Convert config to .env format and save.
#       Example: database_host=localhost, api_timeout=30
#
# Requirements:
#   - Read config.json
#   - Flatten nested dict to env vars (db.host → DB_HOST)
#   - Write to .env file
#   - Print the generated .env content
#
# Hint: Recursively flatten the dict, convert keys to uppercase with _.

# --- your code here ---




# ───────────────────────────────────────────────────────────────
# Expected outputs (for self-check):
#
# Ex1: Validation report
#      ✓ database.host exists
#      ✓ api.timeout is valid (> 0)
#      etc.
#
# Ex2: Changelog entries
#      [timestamp] SET key = value
#      [timestamp] SET key = value
#      etc.
#
# Ex3: .env file content
#      DATABASE_HOST=localhost
#      DATABASE_PORT=5432
#      CACHE_HOST=redis-server
#      API_TIMEOUT=30
#      etc.
# ───────────────────────────────────────────────────────────────
