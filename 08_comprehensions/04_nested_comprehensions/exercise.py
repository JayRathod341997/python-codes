# ─────────────────────────────────────────────
# Exercises — Nested Comprehensions
# ─────────────────────────────────────────────

# ── Exercise 1: Flatten Weekly Attendance ─────
# Real-life: HR system
# Each sublist represents a week's daily attendance counts.
# Flatten into one list.

weekly = [[45, 47, 50, 48, 46], [40, 42, 44, 43, 41], [50, 52, 51, 53, 49]]

# --- your code here ---


# ── Exercise 2: Ticket IDs ────────────────────
# Real-life: Support desk — generate ticket IDs like "ZONE-A-001", "ZONE-A-002" …
# Zones: ["A", "B"], Ticket numbers: 1–3

zones   = ["A", "B"]
numbers = [1, 2, 3]

# --- your code here ---
# Expected format: "ZONE-A-1", "ZONE-A-2", "ZONE-A-3", "ZONE-B-1", ...


# ── Exercise 3: Extract All Permissions ───────
# Real-life: RBAC (Role-Based Access Control) system
# Each role has a list of permissions.
# Flatten all permissions into one list.

roles = [
    {"role": "admin",   "permissions": ["read", "write", "delete", "manage"]},
    {"role": "editor",  "permissions": ["read", "write"]},
    {"role": "viewer",  "permissions": ["read"]},
]

# --- your code here ---


# ── Exercise 4: Identity Matrix ───────────────
# Real-life: Linear algebra / ML preprocessing
# Build an n×n identity matrix as a list of lists.
# identity[i][j] = 1 if i==j else 0

n = 4

# --- your code here ---
# Hint: [[1 if i==j else 0 for j in range(n)] for i in range(n)]


# ── Exercise 5: Batch Order Items ─────────────
# Real-life: Warehouse pick list
# Each order has items with quantities as (item, qty) tuples.
# Create a flat list of individual item strings repeated by quantity.
# e.g. ("Pen", 3) → ["Pen", "Pen", "Pen"]

orders = [
    {"id": "O1", "items": [("Pen", 3), ("Notebook", 1)]},
    {"id": "O2", "items": [("Eraser", 2), ("Marker", 4)]},
]

# --- your code here ---
# Hint: nested for — one for each order, one for each (item, qty),
#       one for each repeat using range(qty)


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: [45, 47, 50, 48, 46, 40, 42, 44, 43, 41, 50, 52, 51, 53, 49]
# Ex2: ['ZONE-A-1', 'ZONE-A-2', 'ZONE-A-3', 'ZONE-B-1', 'ZONE-B-2', 'ZONE-B-3']
# Ex3: ['read', 'write', 'delete', 'manage', 'read', 'write', 'read']
# Ex4: [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
# Ex5: ['Pen', 'Pen', 'Pen', 'Notebook', 'Eraser', 'Eraser', 'Marker', 'Marker', 'Marker', 'Marker']
# ─────────────────────────────────────────────
