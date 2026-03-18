# Project 12 — API Monitoring with Decorators

## The Real-Life Problem

An API monitoring system needs to:
- Measure execution time of each endpoint
- Log all function calls with args and return values
- Retry failed requests up to 3 times
- Cache results to avoid redundant calls
- Rate-limit to 10 calls/second

Instead of duplicating logic in each function, we use decorators to wrap functions with these behaviors.

## Domain Context

**Industry**: DevOps / Cloud / Microservices
**Tools**: API gateways, APM tools, middleware
**Why Python**: Decorators are Python's elegant way to add cross-cutting concerns

## Concepts

Decorators, @functools.wraps, decorator factories, stacking decorators, closures
