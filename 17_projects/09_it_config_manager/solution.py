# ─────────────────────────────────────────────────────────────────
# Project 09 — IT — Config Manager
# Concepts  : JSON I/O, OOP, dot-notation access, datetime logging
# Difficulty: Intermediate
# ─────────────────────────────────────────────────────────────────

import json
from pathlib import Path
from datetime import datetime

# ── Section 1: ConfigManager Class ────────────────────────────────
class ConfigManager:
    """Manage application configuration with JSON I/O and logging."""

    def __init__(self, config_file):
        self.config_file = Path(config_file)
        self.config_dir = self.config_file.parent
        self.config_dir.mkdir(exist_ok=True)
        self.data = {}
        self.changelog_file = self.config_dir / "changelog.txt"

    def load(self):
        """Load configuration from JSON file."""
        if self.config_file.exists():
            with open(self.config_file, "r") as f:
                self.data = json.load(f)
                print(f"✓ Loaded config from {self.config_file}")
        else:
            print(f"⚠ Config file not found: {self.config_file}")

    def save(self):
        """Save configuration to JSON file."""
        with open(self.config_file, "w") as f:
            json.dump(self.data, f, indent=2)
        print(f"✓ Saved config to {self.config_file}")

    def get(self, key, default=None):
        """Get config value using dot notation (e.g., 'db.host')."""
        keys = key.split(".")
        value = self.data
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value

    def set(self, key, value):
        """Set config value using dot notation."""
        keys = key.split(".")
        config = self.data
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        config[keys[-1]] = value
        self._log_change(f"SET {key} = {value}")
        print(f"✓ Set {key} = {value}")

    def _log_change(self, message):
        """Log configuration change with timestamp."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.changelog_file, "a") as f:
            f.write(f"[{timestamp}] {message}\n")

# ── Section 2: Demo Usage ──────────────────────────────────────────
print("\n" + "="*70)
print("CONFIG MANAGER DEMO")
print("="*70)

config_mgr = ConfigManager("configs/app_config.json")

# Create initial config
config_mgr.data = {
    "database": {"host": "localhost", "port": 5432, "name": "myapp"},
    "cache": {"host": "redis-server", "port": 6379},
    "api": {"timeout": 30, "retries": 3},
}
config_mgr.save()

# Load and modify
config_mgr.load()
print("\nInitial config:")
print(f"  DB Host: {config_mgr.get('database.host')}")
print(f"  Cache Host: {config_mgr.get('cache.host')}")

print("\nModifying config...")
config_mgr.set("database.host", "prod-db.example.com")
config_mgr.set("database.port", 3306)
config_mgr.set("api.timeout", 60)

config_mgr.save()

print("\n" + "="*70 + "\n")
