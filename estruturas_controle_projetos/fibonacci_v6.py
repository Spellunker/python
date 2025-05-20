#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

def fibonacci(quantity):
    result = [0, 1]
    while True:
        result.append(sum(result[-2:]))
        if len(result) == quantity:
            break
    return result


if __name__ == "__main__":
    # Listar os 20 primeiros números da sequência
    for fib in fibonacci(20):
        print(fib, end=", ")
    print()
