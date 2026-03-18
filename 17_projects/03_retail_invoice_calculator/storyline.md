# Project 03 — Retail GST Invoice Calculator

## The Real-Life Problem

Pradeep runs a small electronics store in Delhi. When customers buy multiple items, he manually calculates GST (Goods and Services Tax) for each product and creates invoices. Different products have different GST rates (electronics 18%, clothing 5%, food 12%, luxury goods 28%), and he needs to apply bulk discounts if the total crosses ₹10,000.

Without automation, creating an invoice takes 15 minutes and is error-prone. With Python, he can instantly compute totals, apply GST by category, apply bulk discounts, and generate a clean invoice.

## Domain Context

**Industry**: Retail / Point of Sale (POS)
**Role**: Store Owner / Billing Clerk
**Tools in the real world**: POS software (Shopify, Square, Tally, SAP), billing systems
**Why Python is used here**: Every e-commerce platform and retail system uses Python backends to compute taxes and discounts. This script mimics the tax calculation module in any POS system.

## The Python Solution Approach

We store a shopping cart as hardcoded items (product name, quantity, price per unit, GST category). We loop through each item with a while loop (to practice loop control). We apply GST based on product category: 5% for food, 12% for clothing, 18% for electronics, 28% for luxury. We format invoice output using f-strings with alignment. We check if the subtotal crosses ₹10,000 and apply a 5% bulk discount if it does. Finally, we compute the grand total with GST + discount applied.

## Python Concepts You Will Practice

| Concept | Where It Appears |
|---|---|
| Variables and operators | Section 1: Price, quantity, GST rates |
| while loop | Section 2: Iterating through shopping cart items |
| if/elif for category matching | Section 2: Determining GST rate by product category |
| Ternary operator (x if condition else y) | Section 3: Applying discount conditionally |
| List of dicts (data structure) | Section 1: Shopping cart as list of product dicts |
| Arithmetic (+, -, *, /) | Sections 2–4: Computing totals, taxes, discounts |
| f-string formatting with alignment | Sections 3–4: Formatted invoice output with alignment and thousands separator |

## How to Use This Project

1. Read this file to understand GST structure and invoice flow
2. Run `solution.py` and observe how invoice is computed step-by-step
3. Pay attention to the while loop — it iterates safely through cart items
4. Notice GST category matching and ternary operators for discount logic
5. Attempt exercises without looking at the solution
6. Compare your approach with `exercises/solutions/solution_ex.py`

## Extension Ideas

- **Multiple discounts**: Apply flat discount + percentage discount + category-specific discounts
- **GST crediting**: Track input GST (paid on purchases) vs output GST (collected from customers)
- **Seasonal offers**: Add a season parameter and adjust discount thresholds
- **Multi-cart processing**: Read multiple invoices and compute daily revenue, highest discount, etc.

## Real-World Equivalent

This project mimics:
- **Retail POS systems** (Square, Shopify): where items are scanned and invoice is generated
- **E-commerce checkout** (Amazon, Flipkart): where cart totals, taxes, and discounts are computed in real-time
- **Accounting software** (Tally, Busy): where GST compliance is a core feature
- **Invoice generators** (ERPNext): where business rules (discounts, taxes) are applied automatically
