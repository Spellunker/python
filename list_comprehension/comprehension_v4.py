#!/usr/bin/python3

generator = (i**2 for i in range(10) if i % 2 == 0)

for number in generator:
    print(number)
