#!/bin/bash
# ─────────────────────────────────────────────
# Running Python from Terminal
# ─────────────────────────────────────────────

# ── Basic execution ──────────────────────────
python script.py                    # run a script
python3 script.py                   # Linux/macOS explicit
py script.py                        # Windows py launcher

# ── Pass command-line arguments ───────────────
python script.py arg1 arg2
python script.py --name Jay --age 25

# ── Run a module directly ─────────────────────
python -m http.server 8000          # built-in web server
python -m json.tool data.json       # pretty-print JSON
python -m venv venv                 # create virtual env
python -m pip install requests      # run pip as module

# ── One-liner execution (-c flag) ─────────────
python -c "print('Hello from terminal')"
python -c "import sys; print(sys.version)"
python -c "print(sum(range(101)))"         # sum 1..100

# ── Interactive mode after script (-i flag) ───
python -i script.py                 # run script, then stay in REPL

# ── Check syntax without running ─────────────
python -m py_compile script.py

# ── Measure execution time ────────────────────
python -m timeit "sum(range(1000))"

# ── Run with optimizations ────────────────────
python -O script.py                 # remove assert statements

# ── Environment variables ─────────────────────
PYTHONPATH=/my/modules python script.py
PYTHONDONTWRITEBYTECODE=1 python script.py   # no .pyc files
