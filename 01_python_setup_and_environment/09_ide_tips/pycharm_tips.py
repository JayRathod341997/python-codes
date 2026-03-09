# ─────────────────────────────────────────────
# PyCharm Tips for Python
# ─────────────────────────────────────────────

# ── Setup ────────────────────────────────────
# Community Edition is FREE at jetbrains.com/pycharm
# File → Settings → Project → Python Interpreter
# → Add Interpreter → Virtualenv → Existing → select venv

# ── Keyboard Shortcuts ────────────────────────
SHORTCUTS = {
    "Run current file"      : "Shift+F10",
    "Run with config"       : "Shift+F10 (after setup)",
    "Debug"                 : "Shift+F9",
    "Search everywhere"     : "Double Shift",
    "Find in files"         : "Ctrl+Shift+F",
    "Go to definition"      : "Ctrl+B or Ctrl+Click",
    "Rename refactor"       : "Shift+F6",
    "Format code"           : "Ctrl+Alt+L",
    "Optimize imports"      : "Ctrl+Alt+O",
    "Toggle comment"        : "Ctrl+/",
    "Open terminal"         : "Alt+F12",
    "Quick documentation"   : "Ctrl+Q",
    "Auto-complete"         : "Ctrl+Space",
}

for action, shortcut in SHORTCUTS.items():
    print(f"  {action:<25} {shortcut}")

# ── Key features ─────────────────────────────
features = [
    "Built-in debugger with breakpoints",
    "Database tool window",
    "Scientific mode (Jupyter integration)",
    "Django / Flask support",
    "Git integration built-in",
    "Code inspections & quick-fixes",
    "Refactoring tools (rename, extract method)",
]

print("\nPyCharm Key Features:")
for f in features:
    print(f"  - {f}")
