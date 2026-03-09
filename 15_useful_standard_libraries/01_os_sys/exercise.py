# ─────────────────────────────────────────────
# Exercises — os & sys
# ─────────────────────────────────────────────

import os, sys

# ── Exercise 1: Project Directory Scanner ────
# Real-life: Code review tool
# Write a function scan_project(directory) that walks the given
# directory tree and returns a dict:
# {
#   "total_files": int,
#   "total_dirs" : int,
#   "by_extension": {".py": 5, ".txt": 2, ...},
#   "largest_file": {"name": "...", "size_kb": ...}
# }
# Print a formatted summary report.
# Test with os.getcwd() (current folder or its parent).

# --- your code here ---


# ── Exercise 2: Environment Config Reader ─────
# Real-life: 12-factor app — read config from environment
# Write a function get_config() that returns a dict of app settings:
#   DB_HOST   → os.environ or default "localhost"
#   DB_PORT   → os.environ or default "5432"  (convert to int)
#   DEBUG     → os.environ or default "False" (convert to bool)
#   SECRET_KEY→ os.environ or raise RuntimeError if missing
#                (simulate: set it first with os.environ["SECRET_KEY"]="dev-key-123")
#
# Print the full config dict.
# Also: temporarily set DEBUG=True via os.environ, then reload and print again.

# --- your code here ---


# ── Exercise 3: Safe File Organiser ──────────
# Real-life: Download folder cleaner
# Write a function categorise_files(source_dir) that:
#   - Lists all files in source_dir
#   - Groups them by extension into categories:
#       images: .jpg .jpeg .png .gif .bmp .webp
#       docs  : .pdf .doc .docx .txt .md
#       code  : .py .js .ts .java .cpp .go
#       data  : .csv .json .xml .yaml .yml
#       other : everything else
#   - Prints a table:
#       Category    Count   Files
#       ─────────────────────────
#       code        3       notes.py, exercise.py, ...
#       other       1       README
#
# Use the current directory as source_dir.

# --- your code here ---


# ── Exercise 4: sys introspection tool ────────
# Real-life: Compatibility checker / diagnostic script
# Write a function system_report() that prints:
#
#   ══════════════════════════════
#   System Diagnostic Report
#   ══════════════════════════════
#   Python   : 3.11.4 (main, ...)
#   Platform : win32 / linux / darwin
#   Executable: /usr/bin/python3
#   Prefix   : /usr
#   Path entries: 6
#   Loaded modules: 42
#   stdin  encoding: utf-8
#   stdout encoding: utf-8
#   ══════════════════════════════
#
# Hint: sys.version, sys.platform, sys.executable, sys.prefix,
#       len(sys.path), len(sys.modules), sys.stdin.encoding

# --- your code here ---


# ── Exercise 5: CLI argument parser ──────────
# Real-life: Simple CLI tool (like a mini argparse)
# Write a script section (under __name__ == "__main__") that parses
# sys.argv manually to support:
#
#   python exercise.py greet --name Jay --times 3
#   → Hello, Jay!
#   → Hello, Jay!
#   → Hello, Jay!
#
#   python exercise.py add --a 10 --b 25
#   → 10 + 25 = 35
#
#   python exercise.py   (no args)
#   → Usage: exercise.py <command> [--name X] [--times N] [--a X] [--b Y]
#
# Parse sys.argv[1:] to extract the command and --key value pairs.

if __name__ == "__main__":
    # --- your code here ---
    pass


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: Summary with file counts, extension breakdown, largest file
# Ex2: Config dict with defaults; updated after setting DEBUG env var
# Ex3: Table of files grouped by category
# Ex4: Formatted system report
# Ex5: greet / add commands work; no-args shows usage
# ─────────────────────────────────────────────
