#!/usr/bin/python3

# [ expressão for item in list if condicional ]
evens_doubles = [i * 2 for i in range(10) if i % 2 == 0]
print(evens_doubles)

# Versão "normal"
evens_doubles = []
for i in range(10):
    if i % 2 == 0:
        evens_doubles.append(i * 2)
print(evens_doubles)
