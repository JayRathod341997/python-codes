# Solutions — Project 09: Config Manager

import json
from pathlib import Path
from datetime import datetime

class ConfigManager:
    def __init__(self, config_file):
        self.config_file = Path(config_file)
        self.config_dir = self.config_file.parent
        self.config_dir.mkdir(exist_ok=True)
        self.data = {}
        self.changelog = self.config_dir / "changelog.txt"

    def load(self):
        if self.config_file.exists():
            with open(self.config_file) as f:
                self.data = json.load(f)

    def save(self):
        with open(self.config_file, "w") as f:
            json.dump(self.data, f, indent=2)

    def get(self, key, default=None):
        keys = key.split(".")
        val = self.data
        for k in keys:
            val = val.get(k, default) if isinstance(val, dict) else default
        return val

    def set(self, key, value):
        keys = key.split(".")
        cfg = self.data
        for k in keys[:-1]:
            if k not in cfg:
                cfg[k] = {}
            cfg = cfg[k]
        cfg[keys[-1]] = value
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.changelog, "a") as f:
            f.write(f"[{ts}] SET {key}={value}\n")

print("\n" + "="*70)
print("EXERCISE 1 SOLUTION: Config Validation")
print("="*70 + "\n")

mgr = ConfigManager("configs/app_config.json")
mgr.data = {"database": {"host": "localhost", "port": 5432}, "api": {"timeout": 30}}
mgr.save()
mgr.load()

print("Validation Results:")
try:
    host = mgr.get("database.host")
    print(f"  ✓ database.host exists: '{host}'")
except:
    print(f"  ✗ database.host missing")

try:
    timeout = mgr.get("api.timeout")
    if timeout > 0:
        print(f"  ✓ api.timeout is valid: {timeout}")
except:
    print(f"  ✗ api.timeout invalid")

print("\n" + "="*70)
print("EXERCISE 2 SOLUTION: Update and Log")
print("="*70 + "\n")

mgr.set("database.host", "prod-db.example.com")
mgr.set("api.timeout", 60)
mgr.save()

print("Changelog entries:")
with open(mgr.changelog) as f:
    for line in f:
        print(f"  {line.strip()}")

print("\n" + "="*70 + "\n")
