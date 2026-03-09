# ─────────────────────────────────────────────
# tests/test_utils.py
# Run with: pytest
# ─────────────────────────────────────────────

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))

from utils import add, greet

def test_add_integers():
    assert add(2, 3) == 5

def test_add_floats():
    assert add(1.5, 2.5) == 4.0

def test_greet():
    assert greet("Jay") == "Hello, Jay!"
