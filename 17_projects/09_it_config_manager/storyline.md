# Project 09 — App Configuration Manager with JSON

## The Real-Life Problem

A microservice needs multiple config files (database connection, cache settings, API keys). The app needs to:
- Load config from JSON with dot-notation access (config.db.host)
- Validate config values
- Log changes to a changelog file
- Persist config back to JSON

This teaches JSON I/O, OOP with file operations, datetime logging.

## Domain Context

**Industry**: DevOps / Cloud / Microservices
**Tools**: Docker configs, Kubernetes ConfigMaps, environment files
**Why Python**: Configuration management is a core DevOps task

## Concepts

JSON I/O, classes, __getattr__/__setattr__, pathlib, datetime, logging
