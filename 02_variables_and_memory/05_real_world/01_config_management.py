# ============================================================
# Real World Example 1: Configuration Management
# ============================================================
# Demonstrates: constants, naming conventions, immutability,
# shallow vs deep copy for safe config overrides.
# ============================================================

import copy

# --- App-wide constants (UPPER_SNAKE_CASE) ---
DEFAULT_HOST = "localhost"
DEFAULT_PORT = 5432
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3

# --- Base config (dict — mutable) ---
BASE_CONFIG = {
    "host": DEFAULT_HOST,
    "port": DEFAULT_PORT,
    "timeout": DEFAULT_TIMEOUT,
    "retries": MAX_RETRIES,
    "db": {
        "name": "app_db",
        "pool_size": 5,
    },
}

def get_environment_config(env: str) -> dict:
    """Return a fully independent config for a given environment."""
    config = copy.deepcopy(BASE_CONFIG)     # deep copy — no shared state

    if env == "production":
        config["host"] = "prod.db.example.com"
        config["port"] = 5433
        config["db"]["pool_size"] = 20
    elif env == "staging":
        config["host"] = "staging.db.example.com"
        config["db"]["pool_size"] = 10
    # "development" uses BASE_CONFIG values as-is

    return config

# --- Build configs ---
dev_config = get_environment_config("development")
staging_config = get_environment_config("staging")
prod_config = get_environment_config("production")

# --- Modifying one does NOT affect others (deep copy) ---
prod_config["timeout"] = 60

print("=== Environment Configs ===")
for name, cfg in [("dev", dev_config), ("staging", staging_config), ("prod", prod_config)]:
    print(f"\n[{name.upper()}]")
    print(f"  host:      {cfg['host']}")
    print(f"  port:      {cfg['port']}")
    print(f"  timeout:   {cfg['timeout']}")
    print(f"  pool_size: {cfg['db']['pool_size']}")

# --- Variable reassignment for environment switching ---
current_env = "development"
active_config = get_environment_config(current_env)
print(f"\nActive env: {current_env} → {active_config['host']}")

current_env = "production"
active_config = get_environment_config(current_env)
print(f"Active env: {current_env} → {active_config['host']}")

# --- Type hints in real configs ---
def connect(host: str, port: int, timeout: int = DEFAULT_TIMEOUT) -> str:
    return f"Connected to {host}:{port} (timeout={timeout}s)"

print("\n" + connect(**{k: active_config[k] for k in ("host", "port", "timeout")}))
