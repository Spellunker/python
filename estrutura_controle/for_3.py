#!/usr/bin/python3
# -*- coding: utf-8 -*-

product = {"name": "Expensive pen", "price": 14.99, "imported": True, "stock": 793}

for key in product:
    print(key)

print(key)

for value in product.values():
    print(value)

print(value)

for key, value in product.items():
    print(key, "=", value)

print(key, value)
