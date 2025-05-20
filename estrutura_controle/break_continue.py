#!/usr/bin/python3
# -*- coding: utf-8 -*-

for x in range(1,11):
    if x % 2 == 0:
        continue  # Interrompe a repetição e vai para a próxima
    print(x)

for x in range(1,11):
    if x == 5:
        break  # Interrompe o laço e vai para o que estiver fora da repetição
    print(x)

print("Fim!")
