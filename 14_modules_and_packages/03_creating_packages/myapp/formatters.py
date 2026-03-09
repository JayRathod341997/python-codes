# ─────────────────────────────────────────────
# myapp/formatters.py
# ─────────────────────────────────────────────
"""Output formatting helpers."""

def format_currency(amount: float, symbol: str = "₹") -> str:
    """Format a number as currency string with Indian comma separators."""
    return f"{symbol}{amount:,.2f}"

def mask_card(number: str) -> str:
    """Mask all but last 4 digits of a card number."""
    cleaned = number.replace(" ", "").replace("-", "")
    return "**** **** **** " + cleaned[-4:]

def truncate(text: str, max_len: int, suffix: str = "...") -> str:
    """Truncate text to max_len characters, appending suffix if cut."""
    return text if len(text) <= max_len else text[:max_len] + suffix
