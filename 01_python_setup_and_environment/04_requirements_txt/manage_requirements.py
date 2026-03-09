# ─────────────────────────────────────────────
# Working with requirements.txt in Python code
# ─────────────────────────────────────────────

import subprocess
import sys

REQ_FILE = "requirements.txt"

def read_requirements(filepath=REQ_FILE):
    """Read and parse a requirements.txt file."""
    with open(filepath) as f:
        lines = f.readlines()

    packages = []
    for line in lines:
        line = line.strip()
        # skip comments and empty lines
        if line and not line.startswith("#") and not line.startswith("-r"):
            packages.append(line)
    return packages

def install_requirements(filepath=REQ_FILE):
    """Install packages from a requirements file."""
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", "-r", filepath],
        capture_output=True, text=True
    )
    print(result.stdout)
    if result.returncode != 0:
        print("Error:", result.stderr)

def freeze_requirements(output_file=REQ_FILE):
    """Save currently installed packages to a file."""
    result = subprocess.run(
        [sys.executable, "-m", "pip", "freeze"],
        capture_output=True, text=True
    )
    with open(output_file, "w") as f:
        f.write(result.stdout)
    print(f"Saved to {output_file}")

# ── Demo ─────────────────────────────────────
if __name__ == "__main__":
    pkgs = read_requirements()
    print("Packages in requirements.txt:")
    for p in pkgs:
        print(f"  {p}")
