# Project 13 — Async Patient Data Aggregation

## The Real-Life Problem

A healthcare platform needs to fetch patient data from 5 APIs concurrently:
- Lab results, prescriptions, imaging, vitals, insurance

Fetching serially (one at a time) takes 5+ seconds. With async/await, we can fetch all 5 concurrently in ~1 second.

This teaches async/await, asyncio.gather, dataclasses, type hints.

## Domain Context

**Industry**: Healthcare / Telemedicine / EHR
**Tools**: healthcare APIs, electronic health records, patient portals
**Why Python**: async is essential for high-concurrency backend services

## Concepts

async/await, asyncio.gather, dataclasses, type hints, @dataclass, Optional types
