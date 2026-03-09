# ─────────────────────────────────────────────
# VS Code Tips for Python
# ─────────────────────────────────────────────

# ── Essential Extensions ──────────────────────
# 1. Python          (ms-python.python)       — core support
# 2. Pylance         (ms-python.vscode-pylance) — IntelliSense
# 3. Ruff            (charliermarsh.ruff)      — fast linter
# 4. Black Formatter (ms-python.black-formatter)

# ── Select Python Interpreter ─────────────────
# Ctrl+Shift+P → "Python: Select Interpreter"
# Choose your venv's Python (e.g. .venv/bin/python)

# ── Keyboard Shortcuts ────────────────────────
SHORTCUTS = {
    "Run file"              : "F5 or Ctrl+F5",
    "Run line/selection"    : "Shift+Enter",
    "Open terminal"         : "Ctrl+`",
    "Command palette"       : "Ctrl+Shift+P",
    "Go to definition"      : "F12",
    "Find all references"   : "Shift+F12",
    "Format document"       : "Shift+Alt+F",
    "Toggle comment"        : "Ctrl+/",
    "Multi-cursor"          : "Alt+Click",
    "Rename symbol"         : "F2",
}

for action, shortcut in SHORTCUTS.items():
    print(f"  {action:<25} {shortcut}")

# ── Useful settings.json snippets ─────────────
settings = '''
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
    "editor.formatOnSave": true,
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter"
    },
    "ruff.enable": true,
    "python.terminal.activateEnvironment": true
}
'''
print("\nRecommended settings.json:")
print(settings)
