# ─────────────────────────────────────────────
# myapp/validators.py
# ─────────────────────────────────────────────
"""Input validation helpers for user data."""

import re

def validate_email(email: str) -> bool:
    """Return True if email has basic valid format."""
    return bool(re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email))

def validate_phone(phone: str) -> bool:
    """Return True if phone is a 10-digit Indian number (optional +91)."""
    cleaned = phone.replace(" ", "").replace("-", "")
    return bool(re.match(r"^(\+91)?[6-9]\d{9}$", cleaned))

def validate_pincode(code: str) -> bool:
    """Return True if code is a 6-digit Indian pincode."""
    return bool(re.match(r"^[1-9]\d{5}$", code))
