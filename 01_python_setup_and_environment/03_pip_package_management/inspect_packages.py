# ─────────────────────────────────────────────
# Inspect installed packages from Python code
# ─────────────────────────────────────────────

import importlib.metadata as meta
import sys

# List all installed packages
installed = sorted(meta.packages_distributions().keys())
print(f"Total packages: {len(installed)}\n")

# Show details for a specific package
package = "pip"
try:
    dist = meta.distribution(package)
    print(f"Name    : {dist.metadata['Name']}")
    print(f"Version : {dist.metadata['Version']}")
    print(f"Summary : {dist.metadata.get('Summary', 'N/A')}")
except meta.PackageNotFoundError:
    print(f"'{package}' is not installed")

# Check if a package is importable
def is_installed(pkg_name):
    try:
        meta.version(pkg_name)
        return True
    except meta.PackageNotFoundError:
        return False

packages_to_check = ["requests", "numpy", "flask", "pip"]
for pkg in packages_to_check:
    status = "installed" if is_installed(pkg) else "NOT installed"
    print(f"  {pkg:12} -> {status}")
