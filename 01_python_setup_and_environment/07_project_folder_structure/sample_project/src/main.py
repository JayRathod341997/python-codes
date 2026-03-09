# ─────────────────────────────────────────────
# main.py — Entry point of the project
# Run: python src/main.py
# ─────────────────────────────────────────────

from utils import add, greet

if __name__ == "__main__":
    print(greet("Jay"))
    print("3 + 7 =", add(3, 7))
