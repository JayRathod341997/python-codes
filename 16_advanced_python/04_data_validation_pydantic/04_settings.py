"""
============================================================
TOPIC: 04_settings.py
Real-world context: Loading application configuration from
environment variables, .env files, and defaults.
============================================================
"""

from pydantic import BaseModel, Field, field_validator
from typing import Optional
import os

print("=" * 60)
print("SECTION 1: Environment Variable Basics")
print("=" * 60)

# Set some environment variables for demo
os.environ['DATABASE_URL'] = 'postgresql://localhost/mydb'
os.environ['API_KEY'] = 'secret_key_123'
os.environ['DEBUG'] = 'true'
os.environ['MAX_CONNECTIONS'] = '100'

# Simulate pydantic_settings behavior (BaseSettings equivalent)
class Settings(BaseModel):
    """Application settings from environment."""
    database_url: str = Field(default='sqlite:///db.sqlite3')
    api_key: str = Field(default='')
    debug: bool = Field(default=False)
    max_connections: int = Field(default=10)

    class Config:
        # Configuration for loading from env
        env_file = ".env"
        case_sensitive = False

    def __init__(self, **data):
        # Override with environment variables
        env_data = {}
        if 'database_url' not in data and os.getenv('DATABASE_URL'):
            env_data['database_url'] = os.getenv('DATABASE_URL')
        if 'api_key' not in data and os.getenv('API_KEY'):
            env_data['api_key'] = os.getenv('API_KEY')
        if 'debug' not in data and os.getenv('DEBUG'):
            env_data['debug'] = os.getenv('DEBUG').lower() in ['true', '1', 'yes']
        if 'max_connections' not in data and os.getenv('MAX_CONNECTIONS'):
            env_data['max_connections'] = int(os.getenv('MAX_CONNECTIONS'))

        merged = {**env_data, **data}
        super().__init__(**merged)

# Load settings (picks up environment variables)
settings = Settings()
print(f"Settings from environment:")
print(f"  Database: {settings.database_url}")
print(f"  API Key: {settings.api_key}")
print(f"  Debug: {settings.debug}")
print(f"  Max Connections: {settings.max_connections}")
print()


print("=" * 60)
print("SECTION 2: Settings with Validation")
print("=" * 60)

class DatabaseSettings(BaseModel):
    """Database configuration with validation."""
    host: str = Field(default='localhost')
    port: int = Field(default=5432, ge=1, le=65535)  # Validate range
    database: str
    username: str
    password: str
    pool_size: int = Field(default=5, ge=1, le=100)

    @field_validator('host')
    @classmethod
    def host_must_not_be_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Host cannot be empty')
        return v

    @field_validator('database')
    @classmethod
    def database_must_be_valid_name(cls, v):
        if not v.replace('_', '').isalnum():
            raise ValueError('Database name must be alphanumeric (with underscores)')
        return v

# Create database settings
db_settings = DatabaseSettings(
    host='db.example.com',
    port=5432,
    database='production_db',
    username='dbuser',
    password='secure_password'
)

print(f"Database settings:")
print(f"  Host: {db_settings.host}:{db_settings.port}")
print(f"  Database: {db_settings.database}")
print(f"  Username: {db_settings.username}")
print(f"  Pool size: {db_settings.pool_size}")
print()


print("=" * 60)
print("SECTION 3: Hierarchical Settings")
print("=" * 60)

class CORSSettings(BaseModel):
    """CORS configuration."""
    allow_origins: list = ['http://localhost:3000']
    allow_credentials: bool = True
    allow_methods: list = ['GET', 'POST', 'PUT', 'DELETE']
    allow_headers: list = ['*']

class LoggingSettings(BaseModel):
    """Logging configuration."""
    level: str = 'INFO'
    format: str = '%(asctime)s - %(levelname)s - %(message)s'
    file: Optional[str] = None

class AppSettings(BaseModel):
    """Complete application settings."""
    app_name: str = 'MyAPI'
    app_version: str = '1.0.0'
    debug: bool = Field(default=False)
    database: DatabaseSettings
    cors: CORSSettings = CORSSettings()
    logging: LoggingSettings = LoggingSettings()

# Create complete settings from nested data
app_settings = AppSettings(
    app_name='ProductAPI',
    app_version='2.1.0',
    debug=True,
    database={
        'host': 'prod-db.internal',
        'port': 5432,
        'database': 'products',
        'username': 'api_user',
        'password': 'api_password'
    },
    cors={
        'allow_origins': ['https://app.example.com'],
        'allow_methods': ['GET', 'POST'],
        'allow_credentials': True
    },
    logging={
        'level': 'DEBUG',
        'file': '/var/log/app.log'
    }
)

print(f"Application: {app_settings.app_name} v{app_settings.app_version}")
print(f"Database: {app_settings.database.host}:{app_settings.database.port}/{app_settings.database.database}")
print(f"CORS allowed origins: {app_settings.cors.allow_origins}")
print(f"Logging level: {app_settings.logging.level}")
if app_settings.logging.file:
    print(f"Log file: {app_settings.logging.file}")
print()


print("=" * 60)
print("SECTION 4: Environment-Specific Settings")
print("=" * 60)

class EnvironmentSettings:
    """Load settings based on environment."""

    @staticmethod
    def get_settings(env: str = 'development') -> DatabaseSettings:
        """Get settings for specific environment."""

        environments = {
            'development': {
                'host': 'localhost',
                'port': 5432,
                'database': 'dev_db',
                'username': 'dev_user',
                'password': 'dev_password',
                'pool_size': 5
            },
            'testing': {
                'host': 'test-db',
                'port': 5432,
                'database': 'test_db',
                'username': 'test_user',
                'password': 'test_password',
                'pool_size': 3
            },
            'production': {
                'host': 'prod-db.internal',
                'port': 5432,
                'database': 'prod_db',
                'username': os.getenv('DB_USER', 'prod_user'),
                'password': os.getenv('DB_PASSWORD', 'secure_prod_password'),
                'pool_size': 20
            }
        }

        config = environments.get(env, environments['development'])
        return DatabaseSettings(**config)

# Get settings for different environments
for env in ['development', 'testing', 'production']:
    settings = EnvironmentSettings.get_settings(env)
    print(f"{env.upper()}: {settings.host} - {settings.database}")
print()


print("=" * 60)
print("SECTION 5: Settings from Dictionary")
print("=" * 60)

# Configuration from external source (file, API, etc.)
config_dict = {
    'app_name': 'ConfigAPI',
    'app_version': '1.5.0',
    'debug': False,
    'database': {
        'host': 'config-db',
        'port': 5432,
        'database': 'config_db',
        'username': 'config_user',
        'password': 'config_password'
    }
}

settings = AppSettings(**config_dict)
print(f"Settings loaded from dictionary:")
print(f"  App: {settings.app_name}")
print(f"  Database: {settings.database.database}")
print()


print("=" * 60)
print("SECTION 6: Override Settings")
print("=" * 60)

# Base settings
base_settings = AppSettings(
    app_name='BaseAPI',
    database={
        'host': 'localhost',
        'port': 5432,
        'database': 'base_db',
        'username': 'base_user',
        'password': 'base_password'
    }
)

print(f"Base settings: {base_settings.app_name}")
print(f"  Database: {base_settings.database.host}")

# Override specific settings
override_data = base_settings.model_dump()
override_data['app_name'] = 'OverriddenAPI'
override_data['database']['host'] = 'override-db'

overridden_settings = AppSettings(**override_data)
print(f"\nOverridden settings: {overridden_settings.app_name}")
print(f"  Database: {overridden_settings.database.host}")
print()


print("=" * 60)
print("SECTION 7: Settings Serialization")
print("=" * 60)

settings = AppSettings(
    app_name='ExportAPI',
    debug=True,
    database={
        'host': 'export-db',
        'port': 5432,
        'database': 'export_db',
        'username': 'export_user',
        'password': 'export_password'
    }
)

# Export to dictionary
settings_dict = settings.model_dump()
print(f"Settings as dict (partial):")
print(f"  app_name: {settings_dict['app_name']}")
print(f"  debug: {settings_dict['debug']}")

# Export to JSON
settings_json = settings.model_dump_json(indent=2)
print(f"\nSettings as JSON (partial):")
for line in settings_json.split('\n')[:5]:
    print(f"  {line}")
print()

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
Settings management:
1. Use BaseModel (or BaseSettings) for configuration
2. Load from environment variables automatically
3. Use Field() for defaults and validation
4. Validate settings with @field_validator
5. Support hierarchical nested settings
6. Different configs per environment
7. Load from .env files for local development
8. Override settings programmatically
9. Export settings to dict/JSON for logging
10. Keep sensitive data in environment variables
""")
