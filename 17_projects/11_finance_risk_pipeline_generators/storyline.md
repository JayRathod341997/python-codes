# Project 11 — Risk Pipeline with Generators

## The Real-Life Problem

A financial institution screens 10,000 transactions for fraud risk. Loading all 10,000 into memory is inefficient. Using generators, we can process them lazily:
1. Generate transactions on-the-fly
2. Filter large amounts
3. Flag suspicious patterns (round numbers)
4. Compute risk score
5. Materialize only top 50 high-risk

This teaches generators, yield, generator chaining, itertools.

## Domain Context

**Industry**: FinTech / AML (Anti-Money Laundering)
**Tools**: risk engines, fraud detection systems
**Why Python**: Generators handle large datasets efficiently

## Concepts

Generator functions, yield, generator chaining, itertools.islice, lazy evaluation
