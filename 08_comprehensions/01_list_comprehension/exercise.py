# ─────────────────────────────────────────────
# Exercises — List Comprehension
# ─────────────────────────────────────────────

# ── Exercise 1: Invoice Total ─────────────────
# Real-life: Billing system
# Each item is (unit_price, quantity).
# Create a list of line totals (price × qty).

items = [(50, 3), (120, 2), (999, 1), (15, 10)]

# --- your code here ---


# ── Exercise 2: Normalize Filenames ───────────
# Real-life: File upload handler
# Convert every filename to lowercase and replace spaces with underscores.

filenames = ["Profile Photo.JPG", "Resume Final.PDF", "cover letter.docx"]

# --- your code here ---


# ── Exercise 3: Word Lengths ──────────────────
# Real-life: SEO tool — get character count of each keyword
# Return a list of (word, length) tuples.

keywords = ["python", "comprehension", "list", "real-world", "tutorial"]

# --- your code here ---


# ── Exercise 4: Email Domain Extractor ────────
# Real-life: Marketing segmentation
# Given a list of email addresses, extract only the domain part
# (everything after "@").

emails = [
    "alice@gmail.com",
    "bob@company.org",
    "carol@outlook.com",
    "dave@gmail.com",
]

# --- your code here ---


# ── Exercise 5: Inventory Reorder List ────────
# Real-life: Warehouse management
# A product dict has "name" and "stock".
# Build a list of names where stock < 10 (items to reorder).

products = [
    {"name": "Pen",      "stock": 5},
    {"name": "Notebook", "stock": 120},
    {"name": "Stapler",  "stock": 3},
    {"name": "Tape",     "stock": 50},
    {"name": "Eraser",   "stock": 8},
]

# --- your code here ---


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: [150, 240, 999, 150]
# Ex2: ['profile_photo.jpg', 'resume_final.pdf', 'cover_letter.docx']
# Ex3: [('python', 6), ('comprehension', 13), ('list', 4), ('real-world', 10), ('tutorial', 8)]
# Ex4: ['gmail.com', 'company.org', 'outlook.com', 'gmail.com']
# Ex5: ['Pen', 'Stapler', 'Eraser']
# ─────────────────────────────────────────────
