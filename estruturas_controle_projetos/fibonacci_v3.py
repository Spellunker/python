#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

def fibonacci(limit):
    second_to_last = 0
    last = 1
    print(f"{second_to_last}, {last}", end=", ")
    while last < limit:
        second_to_last, last = last, second_to_last + last
        print(last, end=", ")


if __name__ == "__main__":
    fibonacci(20000)
