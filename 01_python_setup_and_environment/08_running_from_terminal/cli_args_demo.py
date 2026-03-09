# ─────────────────────────────────────────────
# Accepting command-line arguments
# Run: python cli_args_demo.py Jay 25
# Run: python cli_args_demo.py --name Jay --age 25
# ─────────────────────────────────────────────

import sys
import argparse

# ── Method 1: sys.argv (basic) ────────────────
print("=== sys.argv ===")
print("All args:", sys.argv)
# sys.argv[0] = script name
# sys.argv[1], [2]... = user arguments

if len(sys.argv) >= 3:
    name = sys.argv[1]
    age  = sys.argv[2]
    print(f"Name: {name}, Age: {age}")
else:
    print("Usage: python cli_args_demo.py <name> <age>")

print()

# ── Method 2: argparse (recommended) ─────────
print("=== argparse ===")
parser = argparse.ArgumentParser(description="Greet a user")
parser.add_argument("--name", type=str, default="World", help="Your name")
parser.add_argument("--age",  type=int, default=0,       help="Your age")
parser.add_argument("--verbose", action="store_true",     help="Verbose output")

args = parser.parse_args()

print(f"Hello, {args.name}!")
if args.age:
    print(f"You are {args.age} years old.")
if args.verbose:
    print("Verbose mode ON")
