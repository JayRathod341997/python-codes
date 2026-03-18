# Project 06 — Retail Inventory Management with OOP

## The Real-Life Problem

Anand manages a Supermarket. He stocks thousands of SKUs (stock-keeping units) across different categories. He needs to:
- Track product details (SKU, name, category, price, stock quantity)
- Add/remove stock when items are sold or restocked
- Validate that stock doesn't go negative
- Generate reorder reports when stock falls below threshold
- Manage a warehouse of products efficiently

Without OOP, this is 100s of parallel lists. With classes, he models Product and Warehouse as cohesive objects.

## Domain Context

**Industry**: Retail / Inventory Management
**Role**: Store Manager / Inventory Controller
**Tools in the real world**: SAP Inventory, WMS systems, Shopify inventory
**Why Python is used here**: Backend systems use OOP to model real-world entities (Product, Warehouse).

## The Python Solution Approach

We create two classes:
1. **Product**: Encapsulates product data (sku, name, category, price, stock). Uses @property with setter for stock validation.
2. **Warehouse**: Holds a dict of products. Methods: restock, sell, reorder_report.

We use @property to allow `product.stock` syntax while hiding validation logic. We use raise ValueError for invalid operations. This teaches the fundamentals of OOP: encapsulation, properties, validation.

## Python Concepts You Will Practice

| Concept | Where It Appears |
|---|---|
| Class definition | Section 1: Product, Warehouse |
| __init__ constructor | Sections 1–2: Initializing objects |
| Instance attributes | Sections 1–2: product.stock, warehouse.products |
| @property decorator | Section 1: Computed/validated attributes |
| @property setter | Section 1: Custom logic when setting stock |
| @classmethod | Section 2: Factory methods (optional) |
| Instance methods | Sections 2–3: warehouse.sell, warehouse.restock |
| Exception handling (raise) | Sections 1–3: Raising ValueError for invalid operations |
| Dictionary iteration | Section 3: Iterating through warehouse products |
| f-string formatting | Section 4: Formatted reports |

## How to Use This Project

1. Read this file to understand inventory management
2. Run `solution.py` and observe object creation and method calls
3. Notice how @property makes validation transparent
4. Understand how classes avoid parallel lists
5. Attempt exercises without looking at the solution
6. Compare your approach with `exercises/solutions/solution_ex.py`

## Extension Ideas

- **Expiry date tracking**: Add expiry dates and flag expired products
- **Multi-warehouse**: Model multiple warehouses with transfer logic
- **Supplier integration**: Track which supplier provides each product
- **Seasonal adjustments**: Adjust reorder thresholds by season

## Real-World Equivalent

This project mimics:
- **Inventory management systems** (SAP, Oracle): product tracking
- **E-commerce backends**: stock management
- **Supply chain platforms**: warehouse operations
- **Point of Sale systems**: real-time inventory updates
