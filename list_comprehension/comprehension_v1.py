#!/usr/bin/python3

# [ expressão for item in list ]
doubles = [i * 2 for i in range(10)]
print(doubles)

# Versão "normal"
doubles = []
for i in range(10):
    doubles.append(i * 2)
print(doubles)
