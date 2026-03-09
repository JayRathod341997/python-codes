# ─────────────────────────────────────────────
# Set Comprehension
# ─────────────────────────────────────────────

# ── Syntax ───────────────────────────────────
# {expression  for  item  in  iterable}
# Looks like dict comprehension but has NO colon — produces a SET.
# Short for:
#   result = set()
#   for item in iterable:
#       result.add(expression)

# ── Basic example ─────────────────────────────
unique_squares = {x ** 2 for x in [-3, -2, -1, 0, 1, 2, 3]}
print(unique_squares)   # {0, 1, 4, 9}  — duplicates auto-removed, unordered

# ── Real-life 1: Unique visitor IPs ──────────
# Web analytics — find distinct IP addresses from access log
access_log = [
    "192.168.1.1", "10.0.0.5", "192.168.1.1",
    "172.16.0.3",  "10.0.0.5", "192.168.1.2",
]
unique_ips = {ip for ip in access_log}
print(unique_ips)   # {'192.168.1.1', '10.0.0.5', '172.16.0.3', '192.168.1.2'}
print(f"Distinct visitors: {len(unique_ips)}")      # 4

# ── Real-life 2: Unique tags in a blog ───────
# CMS — gather all tags across posts (no duplicates)
posts = [
    {"title": "Python Basics",    "tags": ["python", "beginner", "tutorial"]},
    {"title": "Web Scraping",     "tags": ["python", "scraping", "tutorial"]},
    {"title": "Data Science 101", "tags": ["python", "data", "beginner"]},
]
all_tags = {tag for post in posts for tag in post["tags"]}
print(all_tags)     # {'python', 'beginner', 'tutorial', 'scraping', 'data'}

# ── Real-life 3: Allowed file extensions ─────
# File upload validator — extract unique extensions from filenames
uploads = ["photo.jpg", "doc.pdf", "scan.jpg", "report.docx", "image.PNG"]
extensions = {f.split(".")[-1].lower() for f in uploads}
print(extensions)   # {'jpg', 'pdf', 'docx', 'png'}

# ── Real-life 4: Deduplicate order IDs ───────
# Order management — raw data may have duplicate order entries
raw_orders = [1021, 1034, 1021, 1056, 1034, 1078, 1056, 1099]
unique_orders = {oid for oid in raw_orders}
print(sorted(unique_orders))    # [1021, 1034, 1056, 1078, 1099]

# ── Set operations after comprehension ───────
# Real-life: Find common skills between two candidates
alice_skills = {"python", "sql", "docker", "git"}
bob_skills   = {"java",   "sql", "docker", "aws"}

# Who has skills neither candidate has?  (symmetric difference)
unique_to_each = alice_skills ^ bob_skills
print(unique_to_each)   # {'python', 'git', 'java', 'aws'}

# Common skills (intersection)
common = alice_skills & bob_skills
print(common)           # {'sql', 'docker'}

# ── Key points ───────────────────────────────
# • Use {} — no colon — to get a set, not a dict
# • Sets are unordered — don't rely on iteration order
# • Sets automatically deduplicate — perfect for uniqueness checks
# • Elements must be hashable (same rule as dict keys)
# • Use sorted() to print in a predictable order
# • Empty set comprehension: set() — not {} (that creates an empty dict!)
