# ─────────────────────────────────────────────
# Python Project Folder Structure
# ─────────────────────────────────────────────

structure = """
my_project/                   ← root folder
│
├── src/                      ← source code (or use package name directly)
│   └── my_project/
│       ├── __init__.py       ← makes it a Python package
│       ├── main.py           ← entry point
│       ├── config.py         ← configuration / constants
│       └── utils.py          ← helper functions
│
├── tests/                    ← all test files
│   ├── __init__.py
│   ├── test_main.py
│   └── test_utils.py
│
├── data/                     ← data files (csv, json, etc.)
├── docs/                     ← documentation
├── scripts/                  ← one-off utility scripts
│
├── .venv/                    ← virtual environment (not in git)
├── .gitignore                ← files git should ignore
├── pyproject.toml            ← modern project config (uv / poetry)
├── requirements.txt          ← pip dependencies
├── requirements-dev.txt      ← dev-only pip dependencies
└── README.md                 ← project description
"""

print(structure)

# ── Minimal structure (small scripts / learning) ──
minimal = """
my_script/
├── main.py
├── utils.py
├── requirements.txt
└── .venv/
"""

print("Minimal structure for small projects:")
print(minimal)
